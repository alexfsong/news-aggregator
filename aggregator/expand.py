"""Stage C: expand trending cluster items with full metadata. No LLM."""
from __future__ import annotations

import json
from pathlib import Path


def _load_items(items_path: Path) -> dict[str, dict]:
    by_id: dict[str, dict] = {}
    with items_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            by_id[item["id"]] = item
    return by_id


def expand_trending(run_dir: Path) -> Path:
    triage_path = run_dir / "triage.json"
    items_path = run_dir / "items.jsonl"
    out_path = run_dir / "trending_expanded.jsonl"

    triage = json.loads(triage_path.read_text(encoding="utf-8"))
    items_by_id = _load_items(items_path)

    trending_ids = set(triage.get("trending", []))
    clusters = triage.get("clusters", [])

    written = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for cluster in clusters:
            cid = cluster.get("id") or cluster.get("cluster_id")
            if cid not in trending_ids:
                continue
            hydrated_items = []
            for item_id in cluster.get("item_ids", []):
                it = items_by_id.get(item_id)
                if it:
                    hydrated_items.append(it)
            record = {
                "cluster_id": cid,
                "theme": cluster.get("theme", ""),
                "heat_score": cluster.get("heat_score"),
                "why": cluster.get("why", ""),
                "items": hydrated_items,
            }
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1

    print(f"[expand] wrote {written} trending clusters → {out_path}")
    return out_path
