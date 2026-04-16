"""Stage E: fetch transcripts / full articles per deepen_plan.json. No LLM."""
from __future__ import annotations

import json
from pathlib import Path

from . import article, fetch, youtube


def _load_items(items_path: Path) -> dict[str, dict]:
    by_id: dict[str, dict] = {}
    with items_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            it = json.loads(line)
            by_id[it["id"]] = it
    return by_id


def _truncate(text: str, cap: int) -> str:
    if len(text) <= cap:
        return text
    return text[: cap - 1].rstrip() + "…"


def run_deepen(root: Path, run_dir: Path) -> Path:
    plan_path = run_dir / "deepen_plan.json"
    items_path = run_dir / "items.jsonl"
    out_path = run_dir / "deepened.jsonl"

    config = fetch.load_config(root)
    cap = int(config.get("deepen", {}).get("transcript_char_cap", 16000))
    max_items = int(config.get("deepen", {}).get("max_deepened_items", 8))

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    items_by_id = _load_items(items_path)

    transcript_ids = list(dict.fromkeys(plan.get("needs_transcript", [])))
    article_ids = list(dict.fromkeys(plan.get("needs_full_article", [])))

    ordered = transcript_ids + [i for i in article_ids if i not in transcript_ids]
    ordered = ordered[:max_items]

    written = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for item_id in ordered:
            it = items_by_id.get(item_id)
            if not it:
                continue
            full_text = ""
            kind = ""
            url = it["url"]
            if item_id in transcript_ids and it.get("source_type") == "youtube":
                full_text = youtube.fetch_transcript(url)
                kind = "transcript"
            if not full_text and item_id in article_ids:
                full_text = article.extract(url)
                kind = "article"
            if not full_text:
                # Fallback: keep summary we already have
                full_text = it.get("summary_text", "")
                kind = "summary"
            record = {
                "id": item_id,
                "url": url,
                "title": it.get("title", ""),
                "source": it.get("source", ""),
                "kind": kind,
                "text": _truncate(full_text, cap),
            }
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1
            print(f"[deepen] {it.get('source','?')}: {kind} ({len(full_text)} ch) — {it.get('title','')[:60]}")

    print(f"[deepen] wrote {written} deepened items → {out_path}")
    return out_path
