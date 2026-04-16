"""Typer CLI: orchestration commands for each pipeline stage."""
from __future__ import annotations

import shutil
import subprocess
from datetime import date
from pathlib import Path

import typer

from . import deepen as deepen_mod
from . import digest as digest_mod
from . import expand as expand_mod
from . import fetch as fetch_mod
from . import notify as notify_mod
from . import store

app = typer.Typer(add_completion=False, help="News aggregator pipeline.")


def _root() -> Path:
    # Project root = cwd when invoked via `uv run aggregator ...` from repo root
    return Path.cwd()


def _today() -> str:
    return date.today().isoformat()


def _run_dir(run_date: str) -> Path:
    return fetch_mod.run_date_dir(_root(), run_date)


@app.command("fetch")
def fetch_cmd(
    topic: str = typer.Option("ai", "--topic"),
    run_date: str = typer.Option("", "--date"),
    lookback_days: int = typer.Option(0, "--lookback-days"),
    max_per_source: int = typer.Option(0, "--max-per-source"),
) -> None:
    """Stage A: pull RSS/Atom feeds → items.jsonl."""
    rd = run_date or _today()
    fetch_mod.fetch_topic(
        _root(),
        topic=topic,
        run_date=rd,
        lookback_days=lookback_days or None,
        max_per_source=max_per_source or None,
    )


@app.command("expand-trending")
def expand_cmd(run_date: str = typer.Option("", "--date")) -> None:
    """Stage C: hydrate trending clusters from triage.json → trending_expanded.jsonl."""
    rd = run_date or _today()
    expand_mod.expand_trending(_run_dir(rd))


@app.command("deepen")
def deepen_cmd(run_date: str = typer.Option("", "--date")) -> None:
    """Stage E: fetch transcripts / full articles per deepen_plan.json → deepened.jsonl."""
    rd = run_date or _today()
    deepen_mod.run_deepen(_root(), _run_dir(rd))


@app.command("assemble")
def assemble_cmd(
    topic: str = typer.Option("ai", "--topic"),
    run_date: str = typer.Option("", "--date"),
) -> None:
    """Stage G: stitch digest.md from sections/ + also-noted bullets."""
    rd = run_date or _today()
    digest_mod.assemble(_run_dir(rd), topic=topic, run_date=rd)


@app.command("publish")
def publish_cmd(
    topic: str = typer.Option("ai", "--topic"),
    run_date: str = typer.Option("", "--date"),
    dry_run: bool = typer.Option(False, "--dry-run"),
    skip_git: bool = typer.Option(False, "--skip-git"),
    skip_email: bool = typer.Option(False, "--skip-email"),
) -> None:
    """Stage H: copy digest → digests/, commit + push, email via Resend."""
    rd = run_date or _today()
    run_dir = _run_dir(rd)
    config = fetch_mod.load_config(_root())

    src = run_dir / "digest.md"
    if not src.exists():
        typer.echo(f"[publish] no digest at {src} — run assemble first", err=True)
        raise typer.Exit(1)

    digest_dir = _root() / config.get("output", {}).get("digest_dir", "digests")
    digest_dir.mkdir(parents=True, exist_ok=True)
    dest = digest_dir / f"{rd}-{topic}.md"
    if dry_run:
        typer.echo(f"[publish] DRY RUN: would copy → {dest}")
    else:
        shutil.copy2(src, dest)
        typer.echo(f"[publish] copied → {dest}")

    # Log run
    if not dry_run:
        with store.connect(_root()) as conn:
            store.record_run(
                conn,
                run_date=rd,
                topic=topic,
                items_fetched=_count_lines(run_dir / "items.jsonl"),
                clusters_trending=_count_lines(run_dir / "trending_expanded.jsonl"),
                items_deepened=_count_lines(run_dir / "deepened.jsonl"),
                digest_path=str(dest.relative_to(_root())),
            )

    if not skip_git:
        _git_commit_push(rd, topic, dry_run=dry_run)

    if not skip_email:
        notify_mod.send_digest(
            src, config=config, run_date=rd, topic=topic, dry_run=dry_run
        )


def _count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8") as fh:
        return sum(1 for line in fh if line.strip())


def _git_commit_push(run_date: str, topic: str, *, dry_run: bool) -> None:
    msg = f"digest({topic}): {run_date}"
    cmds = [
        ["git", "add", "digests/", "state/seen.sqlite"],
        ["git", "commit", "-m", msg],
        ["git", "push"],
    ]
    for cmd in cmds:
        if dry_run:
            typer.echo(f"[publish] DRY RUN git: {' '.join(cmd)}")
            continue
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            if cmd[1] == "commit":
                # Nothing to commit → not an error
                typer.echo(f"[publish] git commit: no changes ({e})")
                break
            typer.echo(f"[publish] git {' '.join(cmd)} failed: {e}", err=True)
            raise


if __name__ == "__main__":
    app()
