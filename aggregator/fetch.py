"""Feed ingestion.

Metadata-only. No LLM, no full-text, no transcripts. Deepening happens in
article.py / youtube.py during the deepen stage.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import feedparser
import yaml
from dateutil import parser as dateparser

from . import store


YT_FEED_TEMPLATE = "https://www.youtube.com/feeds/videos.xml?channel_id={cid}"


@dataclass
class Item:
    id: str
    topic: str
    source: str
    source_type: str  # rss | youtube | podcast | news
    title: str
    url: str
    published: str  # ISO-8601 UTC
    author: str = ""
    summary_text: str = ""  # plain, stripped, truncated to 600 chars
    duration_sec: int | None = None
    extra: dict[str, Any] = field(default_factory=dict)


def load_sources(root: Path, topic: str) -> dict[str, list[dict]]:
    raw = yaml.safe_load((root / "sources.yaml").read_text())
    topic_cfg = raw.get("topics", {}).get(topic)
    if not topic_cfg:
        raise ValueError(f"Topic {topic!r} not defined in sources.yaml")
    return topic_cfg


def load_config(root: Path) -> dict[str, Any]:
    return yaml.safe_load((root / "config.yaml").read_text())


_HTML_TAG_RE = re.compile(r"<[^>]+>")
_WHITESPACE_RE = re.compile(r"\s+")


def _strip_html(text: str, limit: int = 600) -> str:
    clean = _HTML_TAG_RE.sub(" ", text or "")
    clean = _WHITESPACE_RE.sub(" ", clean).strip()
    if len(clean) > limit:
        clean = clean[: limit - 1].rstrip() + "…"
    return clean


def _iso(entry_time: Any) -> str:
    if not entry_time:
        return ""
    try:
        if isinstance(entry_time, str):
            dt = dateparser.parse(entry_time)
        else:
            # time.struct_time from feedparser
            dt = datetime(*entry_time[:6], tzinfo=timezone.utc)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()
    except (ValueError, TypeError):
        return ""


def _stable_id(source: str, url: str, entry_id: str | None) -> str:
    basis = entry_id or url or ""
    h = hashlib.sha1(f"{source}|{basis}".encode("utf-8")).hexdigest()[:16]
    return h


def _parse_duration(entry: Any) -> int | None:
    # iTunes podcast duration: HH:MM:SS or seconds
    dur = getattr(entry, "itunes_duration", None)
    if not dur:
        return None
    if ":" in dur:
        parts = [int(p) for p in dur.split(":")]
        if len(parts) == 3:
            h, m, s = parts
            return h * 3600 + m * 60 + s
        if len(parts) == 2:
            m, s = parts
            return m * 60 + s
    try:
        return int(dur)
    except ValueError:
        return None


def _entry_to_item(
    entry: Any, *, topic: str, source_name: str, source_type: str
) -> Item | None:
    url = getattr(entry, "link", "") or ""
    title = getattr(entry, "title", "").strip()
    if not url or not title:
        return None
    published = _iso(getattr(entry, "published_parsed", None)) or _iso(
        getattr(entry, "updated", None)
    )
    author = getattr(entry, "author", "")
    summary = getattr(entry, "summary", "") or getattr(entry, "description", "")
    item_id = _stable_id(source_name, url, getattr(entry, "id", None))
    return Item(
        id=item_id,
        topic=topic,
        source=source_name,
        source_type=source_type,
        title=title,
        url=url,
        published=published,
        author=author,
        summary_text=_strip_html(summary),
        duration_sec=_parse_duration(entry),
    )


def _fetch_one_feed(
    feed_url: str,
    *,
    topic: str,
    source_name: str,
    source_type: str,
    cutoff: datetime,
    max_items: int,
) -> list[Item]:
    parsed = feedparser.parse(feed_url)
    items: list[Item] = []
    for entry in parsed.entries[: max_items * 2]:  # extra slack for date filter
        item = _entry_to_item(
            entry, topic=topic, source_name=source_name, source_type=source_type
        )
        if item is None:
            continue
        if item.published:
            try:
                dt = datetime.fromisoformat(item.published)
                if dt < cutoff:
                    continue
            except ValueError:
                pass
        items.append(item)
        if len(items) >= max_items:
            break
    return items


def _iter_sources(topic_cfg: dict[str, list[dict]]) -> list[tuple[str, str, str]]:
    """Yield (source_type, name, feed_url) triples."""
    out: list[tuple[str, str, str]] = []
    for group, entries in topic_cfg.items():
        for entry in entries or []:
            name = entry["name"]
            if group == "youtube":
                url = YT_FEED_TEMPLATE.format(cid=entry["channel_id"])
            else:
                url = entry["url"]
            out.append((group, name, url))
    return out


def run_date_dir(root: Path, run_date: str) -> Path:
    d = root / "state" / "runs" / run_date
    d.mkdir(parents=True, exist_ok=True)
    return d


def fetch_topic(
    root: Path,
    *,
    topic: str,
    run_date: str,
    lookback_days: int | None = None,
    max_per_source: int | None = None,
) -> Path:
    config = load_config(root)
    topic_cfg = load_sources(root, topic)

    lookback_days = lookback_days or int(config.get("lookback_days", 14))
    max_per_source = max_per_source or int(config.get("max_items_per_source", 30))
    cutoff = datetime.now(timezone.utc) - timedelta(days=lookback_days)

    out_dir = run_date_dir(root, run_date)
    out_path = out_dir / "items.jsonl"

    count_new = 0
    count_total = 0
    with store.connect(root) as conn, out_path.open("w", encoding="utf-8") as fh:
        for source_type, source_name, feed_url in _iter_sources(topic_cfg):
            try:
                items = _fetch_one_feed(
                    feed_url,
                    topic=topic,
                    source_name=source_name,
                    source_type=source_type,
                    cutoff=cutoff,
                    max_items=max_per_source,
                )
            except Exception as e:  # feedparser is forgiving; guard anyway
                print(f"[fetch] {source_name}: ERROR {e}")
                continue
            count_total += len(items)
            for item in items:
                if store.is_seen(conn, item.id):
                    continue
                store.mark_seen(
                    conn,
                    item_id=item.id,
                    topic=topic,
                    url=item.url,
                    title=item.title,
                    source=item.source,
                    first_seen=run_date,
                )
                fh.write(json.dumps(asdict(item), ensure_ascii=False) + "\n")
                count_new += 1
            print(f"[fetch] {source_name}: {len(items)} in-window")

    print(
        f"[fetch] wrote {count_new} new items (of {count_total} in-window) → {out_path}"
    )
    return out_path
