"""YouTube transcript fetching."""
from __future__ import annotations

import re

VIDEO_ID_RE = re.compile(
    r"(?:v=|/videos/|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})"
)


def extract_video_id(url: str) -> str | None:
    m = VIDEO_ID_RE.search(url)
    return m.group(1) if m else None


def fetch_transcript(url: str) -> str:
    """Return concatenated transcript text, empty string on failure."""
    video_id = extract_video_id(url)
    if not video_id:
        return ""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        from youtube_transcript_api._errors import (
            NoTranscriptFound,
            TranscriptsDisabled,
            VideoUnavailable,
        )
    except ImportError:
        return ""

    try:
        chunks = YouTubeTranscriptApi.get_transcript(video_id)
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable):
        return ""
    except Exception:
        return ""

    return " ".join(c.get("text", "") for c in chunks).strip()
