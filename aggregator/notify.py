"""Email dispatch via Resend."""
from __future__ import annotations

import os
from pathlib import Path

import markdown as md_lib
import resend


def send_digest(
    digest_path: Path,
    *,
    config: dict,
    run_date: str,
    topic: str,
    dry_run: bool = False,
) -> bool:
    email_cfg = config.get("output", {}).get("email", {})
    if not email_cfg.get("enabled", False):
        print("[notify] email disabled in config")
        return False

    api_key = os.environ.get("RESEND_API_KEY")
    if not api_key and not dry_run:
        print("[notify] RESEND_API_KEY missing — skipping send")
        return False

    to_env = email_cfg.get("to_env", "DIGEST_EMAIL_TO")
    to_addr = os.environ.get(to_env) or email_cfg.get("fallback_to")
    if not to_addr:
        print("[notify] no recipient (env DIGEST_EMAIL_TO or fallback_to)")
        return False

    subject = email_cfg.get("subject_template", "Digest — {date}").format(
        date=run_date, topic=topic
    )
    from_addr = email_cfg.get("from", "digest@resend.dev")

    md_text = digest_path.read_text(encoding="utf-8")
    html = md_lib.markdown(md_text, extensions=["extra", "sane_lists"])

    if dry_run:
        print(f"[notify] DRY RUN — would send to {to_addr}")
        print(f"  from:    {from_addr}")
        print(f"  subject: {subject}")
        print(f"  body:    {len(md_text)} chars markdown / {len(html)} chars html")
        return True

    resend.api_key = api_key
    resp = resend.Emails.send(
        {
            "from": from_addr,
            "to": [to_addr],
            "subject": subject,
            "html": html,
            "text": md_text,
        }
    )
    print(f"[notify] sent via Resend, id={resp.get('id', '?')}")
    return True
