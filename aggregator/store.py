"""Persistence layer: dedup and run history via SQLite.

The SQLite file is committed to the repo so each routine invocation sees
all prior runs. Keep writes small and deterministic.
"""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

SCHEMA = """
CREATE TABLE IF NOT EXISTS seen (
    id TEXT PRIMARY KEY,
    topic TEXT NOT NULL,
    url TEXT NOT NULL,
    title TEXT,
    source TEXT,
    first_seen TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_seen_topic ON seen(topic);

CREATE TABLE IF NOT EXISTS runs (
    run_date TEXT PRIMARY KEY,
    topic TEXT NOT NULL,
    items_fetched INTEGER,
    clusters_trending INTEGER,
    items_deepened INTEGER,
    digest_path TEXT,
    notes TEXT
);
"""


def db_path(root: Path) -> Path:
    return root / "state" / "seen.sqlite"


@contextmanager
def connect(root: Path) -> Iterator[sqlite3.Connection]:
    path = db_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        conn.executescript(SCHEMA)
        yield conn
        conn.commit()
    finally:
        conn.close()


def is_seen(conn: sqlite3.Connection, item_id: str) -> bool:
    cur = conn.execute("SELECT 1 FROM seen WHERE id = ?", (item_id,))
    return cur.fetchone() is not None


def mark_seen(
    conn: sqlite3.Connection,
    *,
    item_id: str,
    topic: str,
    url: str,
    title: str,
    source: str,
    first_seen: str,
) -> None:
    conn.execute(
        "INSERT OR IGNORE INTO seen(id, topic, url, title, source, first_seen) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (item_id, topic, url, title, source, first_seen),
    )


def record_run(
    conn: sqlite3.Connection,
    *,
    run_date: str,
    topic: str,
    items_fetched: int,
    clusters_trending: int,
    items_deepened: int,
    digest_path: str,
    notes: str = "",
) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO runs("
        "run_date, topic, items_fetched, clusters_trending, items_deepened, digest_path, notes"
        ") VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            run_date,
            topic,
            items_fetched,
            clusters_trending,
            items_deepened,
            digest_path,
            notes,
        ),
    )
