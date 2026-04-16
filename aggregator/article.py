"""Full-text article extraction via trafilatura."""
from __future__ import annotations

import httpx
import trafilatura


def extract(url: str, *, timeout: float = 20.0) -> str:
    """Return main-content text, empty string on failure."""
    try:
        resp = httpx.get(
            url,
            timeout=timeout,
            follow_redirects=True,
            headers={"User-Agent": "news-aggregator/0.1 (+github.com/alexfsong)"},
        )
        resp.raise_for_status()
    except (httpx.HTTPError, httpx.TimeoutException):
        return ""

    text = trafilatura.extract(
        resp.text,
        include_comments=False,
        include_tables=False,
        favor_precision=True,
    )
    return text or ""
