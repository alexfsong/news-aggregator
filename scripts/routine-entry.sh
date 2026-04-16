#!/usr/bin/env bash
# Thin wrapper the routine prompt invokes per stage.
# Keeps the prompt shell-free and makes local re-runs identical to routine runs.
set -euo pipefail

cd "$(dirname "$0")/.."

STAGE="${1:?usage: routine-entry.sh <stage> [args...]}"
shift || true

TOPIC="${TOPIC:-ai}"
RUN_DATE="${RUN_DATE:-$(date -u +%F)}"

case "$STAGE" in
  fetch)
    uv run aggregator fetch --topic "$TOPIC" --date "$RUN_DATE" "$@"
    ;;
  expand-trending)
    uv run aggregator expand-trending --date "$RUN_DATE" "$@"
    ;;
  deepen)
    uv run aggregator deepen --date "$RUN_DATE" "$@"
    ;;
  assemble)
    uv run aggregator assemble --topic "$TOPIC" --date "$RUN_DATE" "$@"
    ;;
  publish)
    uv run aggregator publish --topic "$TOPIC" --date "$RUN_DATE" "$@"
    ;;
  run-dir)
    echo "state/runs/$RUN_DATE"
    ;;
  *)
    echo "unknown stage: $STAGE" >&2
    exit 2
    ;;
esac
