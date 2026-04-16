# news-aggregator

AI-powered scheduled news digest. Fetches from RSS feeds, YouTube channels, podcasts, and conventional news, then uses a Claude Code routine to cluster, triage, and synthesize a biweekly digest. Delivered as a markdown file committed to this repo and optionally emailed.

## Quick start

```bash
# Install dependencies (Python 3.11+)
python3 -m venv .venv && source .venv/bin/activate
pip install -e .

# Fetch from all sources for topic "ai", last 3 days
aggregator fetch --topic ai --lookback-days 3

# Check what was fetched
cat state/runs/$(date +%F)/items.jsonl | head
```

The full pipeline (triage → deepen → synthesize → assemble → publish) runs inside a Claude Code routine — see [Routine setup](#routine-setup) below.

## Curating sources

All sources live in **`sources.yaml`**, organized by topic then source type.

### Structure

```yaml
topics:
  <topic-name>:           # e.g., "ai", "climate", "rust"
    rss:                   # blogs, newsletters with RSS/Atom feeds
      - name: Display Name
        url: https://example.com/feed.xml
    youtube:               # YouTube channels (no API key needed)
      - name: Channel Name
        channel_id: UC...  # 24-char ID from the channel URL
    podcasts:              # podcast RSS feeds
      - name: Show Name
        url: https://feeds.example.com/podcast.rss
    news:                  # conventional news aggregators
      - name: Google News — Topic
        url: https://news.google.com/rss/search?q=...
```

### Adding a source

1. Find the feed URL (see [Finding feed URLs](#finding-feed-urls) below).
2. Add an entry under the appropriate source type for your topic.
3. Test it: `aggregator fetch --topic <topic> --lookback-days 3`
4. Commit `sources.yaml`.

### Removing a source

Delete the entry from `sources.yaml`. Already-seen items stay in `state/seen.sqlite` (harmless; prevents re-processing if you re-add the source later).

### Adding a new topic

Add a new key under `topics:` with at least one source:

```yaml
topics:
  ai:
    # ... existing AI sources
  climate:
    rss:
      - name: Carbon Brief
        url: https://www.carbonbrief.org/feed/
    news:
      - name: Google News — Climate
        url: https://news.google.com/rss/search?q=climate+change+when%3A14d&hl=en-US&gl=US&ceid=US:en
```

Then run the pipeline with `--topic climate`.

### Finding feed URLs

| Source type | How to find the feed |
|---|---|
| **Blogs** | Look for an RSS/Atom icon, or try appending `/feed`, `/rss`, `/atom.xml`, or `/feed.xml` to the site URL. Browser extensions like "Get RSS Feed URL" help. |
| **Substack** | `https://<name>.substack.com/feed` |
| **YouTube** | Go to the channel page → view source → search for `channel_id`. Or use the channel URL: the ID is the `UC...` part after `/channel/`. Feed URL is auto-constructed from `channel_id`. |
| **Podcasts** | Search the show on [podcastindex.org](https://podcastindex.org/) or check Apple Podcasts listing for the RSS link. Substack podcasts: `https://api.substack.com/feed/podcast/<id>.rss`. |
| **Google News** | `https://news.google.com/rss/search?q=<query>&hl=en-US&gl=US&ceid=US:en` — use `+` for AND, `OR` for OR, `when%3A14d` for last 14 days. |
| **Hacker News** | [hnrss.org](https://hnrss.org/) — filter by keyword and minimum points, e.g., `https://hnrss.org/newest?q=AI+OR+LLM&points=100` |

### Tips

- **Quality over quantity.** The triage LLM clusters and ranks, but noisy sources burn fetch time and make clustering harder. 15–25 sources per topic is a good range.
- **Prefer RSS over scraping.** The pipeline only reads RSS/Atom — no HTML scraping at fetch time (that happens in the deepen stage for selected items only).
- **Google News is noisy.** It's useful as a catch-all but expect the triage stage to filter heavily. Keep the query specific.
- **YouTube channel IDs** are not the same as channel handles (`@name`). To find the ID: go to the channel → View Page Source → search `channelId`.

## Config reference

**`config.yaml`** controls pipeline behavior:

```yaml
cadence: biweekly              # informational label
lookback_days: 14              # how far back to fetch
max_items_per_source: 30       # cap per feed

triage:
  max_clusters: 12             # upper bound on clusters the LLM produces

trending:
  max_trending: 6              # how many clusters get full synthesis treatment

deepen:
  max_deepened_items: 8        # max items that get transcript/full-text extraction
  enable_whisper: false        # set true + install faster-whisper for podcast audio
  transcript_char_cap: 16000   # truncate transcripts before sending to LLM

output:
  digest_dir: digests          # where final markdown lands
  email:
    enabled: true
    to_env: DIGEST_EMAIL_TO    # env var checked first
    fallback_to: you@example.com
    from: "AI Digest <digest@resend.dev>"
    subject_template: "AI digest — {date}"
```

### Tuning token spend

- **`max_trending`** is the biggest lever — fewer trending clusters = fewer synthesis calls.
- **`max_deepened_items`** caps transcript/article fetches (each ~4k–16k chars sent to LLM).
- **`transcript_char_cap`** truncates long transcripts before they reach synthesis.
- Non-trending items always cost zero LLM tokens (rendered as raw title + link bullets).

## CLI commands

All commands run from the repo root via `aggregator <command>`.

| Command | Stage | LLM? | What it does |
|---|---|---|---|
| `fetch` | A | No | Pull feeds → `items.jsonl` |
| `expand-trending` | C | No | Hydrate trending clusters → `trending_expanded.jsonl` |
| `deepen` | E | No | Fetch transcripts/articles → `deepened.jsonl` |
| `assemble` | G | No | Stitch digest.md from sections + bullets |
| `publish` | H | No | Copy to `digests/`, git commit+push, email |

Stages B (triage), D (deepen-plan), and F (synthesize) are performed by the Claude routine agent itself — no CLI command needed.

Common flags: `--topic` (default: `ai`), `--date` (default: today), `--dry-run`, `--skip-git`, `--skip-email`.

## Routine setup

The digest is designed to run as a [Claude Code routine](https://claude.ai/code/routines) — a cloud-hosted Claude session on a cron schedule. Your laptop stays closed.

1. Push this repo to GitHub.
2. Go to **https://claude.ai/code/routines** → Create routine.
3. Configure:
   - **Name:** `ai-news-biweekly`
   - **Repository:** this repo
   - **Trigger:** Schedule → cron `0 9 * * 1` (Mondays 9am). The prompt checks ISO week parity to skip alternate weeks (biweekly).
   - **Network access:** allow outbound HTTP (for RSS feeds, youtube.com, api.resend.com).
   - **Environment variables:** `RESEND_API_KEY` (required for email), `DIGEST_EMAIL_TO` (optional override).
   - **Setup script:** `python3 -m venv .venv && source .venv/bin/activate && pip install -e .`
4. Paste the prompt body from [`.claude/routines/news-digest.md`](.claude/routines/news-digest.md).
5. Save.

### Manual test

Run the pipeline locally to verify before scheduling:

```bash
# Fetch
aggregator fetch --topic ai --lookback-days 3

# Stages B/D/F happen in the routine — for local testing,
# manually create triage.json + deepen_plan.json + sections/*.md
# or run the full routine interactively in Claude Code

# Assemble + dry-run publish
aggregator assemble --topic ai
aggregator publish --topic ai --dry-run
```

## Digests

Published digests live in `digests/YYYY-MM-DD-<topic>.md`, committed to the repo by the routine. Browse history via git.

## Project structure

```
├── sources.yaml           ← curate your feeds here
├── config.yaml            ← tune pipeline behavior
├── aggregator/            ← Python package (deterministic I/O)
│   ├── cli.py             ← typer CLI entry point
│   ├── fetch.py           ← RSS/Atom ingestion
│   ├── youtube.py         ← YT transcript extraction
│   ├── article.py         ← full-text via trafilatura
│   ├── expand.py          ← hydrate trending clusters
│   ├── deepen.py          ← orchestrate transcript/article fetch
│   ├── digest.py          ← Jinja assemble
│   ├── notify.py          ← Resend email
│   └── store.py           ← SQLite dedup
├── scripts/
│   └── routine-entry.sh   ← shell wrapper for routine stages
├── .claude/routines/
│   └── news-digest.md     ← routine prompt (paste into dashboard)
├── state/
│   ├── seen.sqlite        ← dedup DB (committed for cross-run persistence)
│   └── runs/              ← per-run artifacts (items, triage, sections, digest)
└── digests/               ← published digest history
```
