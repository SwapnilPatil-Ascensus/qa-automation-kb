#!/usr/bin/env python3
"""Test API connectivity for Jira, GitLab, qTest using .env credentials."""

from __future__ import annotations

import base64
import os
import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def load_env() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip())


def _open(req: urllib.request.Request, timeout: int = 20):
    last_err: Exception | None = None
    for verify in (True, False):
        ctx = ssl.create_default_context()
        if not verify:
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
        try:
            return urllib.request.urlopen(req, timeout=timeout, context=ctx)
        except Exception as e:
            last_err = e
    raise last_err  # type: ignore[misc]


def test_jira() -> tuple[bool, str]:
    base = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
    email = os.environ.get("JIRA_EMAIL", "")
    token = os.environ.get("JIRA_API_TOKEN", "")
    if not all([base, email, token]):
        return False, "Missing JIRA env vars"
    url = f"{base}/rest/api/3/myself"
    req = urllib.request.Request(url)
    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    req.add_header("Authorization", f"Basic {auth}")
    req.add_header("Accept", "application/json")
    try:
        with _open(req) as resp:
            return True, f"OK HTTP {resp.status}"
    except Exception as e:
        return False, str(e)


def test_gitlab() -> tuple[bool, str]:
    token = os.environ.get("GITLAB_PERSONAL_ACCESS_TOKEN", "")
    base = os.environ.get("GITLAB_API_URL", "https://gitlab.com/api/v4").rstrip("/")
    if not token:
        return False, "Missing GITLAB token"
    url = f"{base}/user"
    req = urllib.request.Request(url)
    req.add_header("PRIVATE-TOKEN", token)
    try:
        with _open(req) as resp:
            return True, f"OK HTTP {resp.status}"
    except Exception as e:
        return False, str(e)


def test_qtest() -> tuple[bool, str]:
    base = os.environ.get("QTEST_BASE_URL", "").rstrip("/")
    token = os.environ.get("QTEST_TOKEN", "")
    if not all([base, token]):
        return False, "Missing QTEST env vars"
    url = f"{base}/api/v3/projects"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/json")
    try:
        with _open(req) as resp:
            return True, f"OK HTTP {resp.status}"
    except Exception as e:
        return False, str(e)


def main() -> None:
    load_env()
    for name, fn in [("Jira", test_jira), ("GitLab", test_gitlab), ("qTest", test_qtest)]:
        ok, msg = fn()
        print(f"{name}: {'PASS' if ok else 'FAIL'} — {msg}")


if __name__ == "__main__":
    main()
