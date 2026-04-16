"""Stage G: assemble digest.md from section files + non-trending bullets. No LLM."""
from __future__ import annotations

import json
from pathlib import Path

from jinja2 import Template

TEMPLATE = Template(
    """# {{ topic_title }} digest — {{ run_date }}

{% if tldr -%}
## TL;DR

{% for bullet in tldr -%}
- {{ bullet }}
{% endfor %}
{% endif -%}

{% if sections -%}
## Trending

{% for section in sections %}
{{ section }}

---
{% endfor %}
{% endif -%}

{% if also_noted -%}
## Also noted

{% for item in also_noted -%}
- [{{ item.title }}]({{ item.url }}) — *{{ item.source }}*
{% endfor %}
{% endif -%}
"""
)


def _read_sections(run_dir: Path) -> tuple[list[str], list[str]]:
    sections_dir = run_dir / "sections"
    bodies: list[str] = []
    headlines: list[str] = []
    if not sections_dir.exists():
        return bodies, headlines
    for path in sorted(sections_dir.glob("*.md")):
        body = path.read_text(encoding="utf-8").strip()
        if not body:
            continue
        bodies.append(body)
        # First line = "## Headline"
        first = body.splitlines()[0].lstrip("# ").strip()
        if first:
            headlines.append(first)
    return bodies, headlines


def _load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def _also_noted(run_dir: Path) -> list[dict]:
    triage_path = run_dir / "triage.json"
    items_path = run_dir / "items.jsonl"
    if not triage_path.exists() or not items_path.exists():
        return []

    triage = json.loads(triage_path.read_text(encoding="utf-8"))
    trending_ids = set(triage.get("trending", []))
    clusters = triage.get("clusters", [])

    also_item_ids: list[str] = []
    for cluster in clusters:
        cid = cluster.get("id") or cluster.get("cluster_id")
        if cid in trending_ids:
            continue
        also_item_ids.extend(cluster.get("item_ids", []))
    also_item_ids.extend(triage.get("standalone", []))

    seen: set[str] = set()
    ordered: list[str] = []
    for iid in also_item_ids:
        if iid not in seen:
            seen.add(iid)
            ordered.append(iid)

    items_by_id = {it["id"]: it for it in _load_jsonl(items_path)}
    out = []
    for iid in ordered:
        it = items_by_id.get(iid)
        if it:
            out.append(
                {
                    "title": it["title"],
                    "url": it["url"],
                    "source": it["source"],
                }
            )
    return out


def assemble(run_dir: Path, *, topic: str, run_date: str) -> Path:
    bodies, headlines = _read_sections(run_dir)
    also_noted = _also_noted(run_dir)
    rendered = TEMPLATE.render(
        topic_title=topic.upper() if len(topic) <= 3 else topic.capitalize(),
        run_date=run_date,
        tldr=headlines[:3],
        sections=bodies,
        also_noted=also_noted,
    )
    out_path = run_dir / "digest.md"
    out_path.write_text(rendered, encoding="utf-8")
    print(f"[assemble] wrote {out_path} ({len(bodies)} trending, {len(also_noted)} also noted)")
    return out_path
