#!/usr/bin/env python3
"""Analyze AM Squad GitLab MR exports for leadership metrics."""
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parents[1] / (
    "2026-08-am-squad-leadership-update/evidence/gitlab/"
    "AM-Squad-Merge-to-main-20260401-20260804.csv"
)
# Fallback to legacy location if not yet moved
LEGACY_CSV = Path(__file__).resolve().parents[2] / (
    "leadership-updates-legacy/AMSquad_OverallUpdate/Gitlab Details/"
    "AM Squad Merge to main - 04012026-0804-2026.csv"
)


def load_rows(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_date(s: str) -> datetime:
    return datetime.strptime(s.strip('"'), "%m/%d/%Y %H:%M:%S")


def repo_from_url(url: str) -> str:
    if "/qa-automation/" not in url:
        return "unknown"
    part = url.split("/qa-automation/")[1].split("/-/")[0]
    return part.split("/")[-1] if "/" in part else part


def analyze(rows, start_month=4, end_month=8, year=2026):
    filtered = []
    for r in rows:
        d = parse_date(r["Merged At"])
        if d.year == year and start_month <= d.month <= end_month:
            filtered.append(r)

    by_month = defaultdict(int)
    by_author = defaultdict(int)
    by_repo = defaultdict(int)
    by_month_author = defaultdict(lambda: defaultdict(int))
    by_month_repo = defaultdict(lambda: defaultdict(int))
    by_area = defaultdict(int)

    area_map = {
        "api-test-automation": "API / Unite MSC",
        "prime-test-automation": "V3 Universal Platform",
        "automation": "V2 Legacy UI + Performance",
    }

    for r in filtered:
        d = parse_date(r["Merged At"])
        m = d.strftime("%Y-%m")
        repo = repo_from_url(r["URL"])
        by_month[m] += 1
        by_author[r["Author"]] += 1
        by_repo[repo] += 1
        by_month_author[m][r["Author"]] += 1
        by_month_repo[m][repo] += 1
        by_area[area_map.get(repo, repo)] += 1

    return {
        "total_mrs": len(filtered),
        "by_month": dict(sorted(by_month.items())),
        "by_author": dict(sorted(by_author.items(), key=lambda x: -x[1])),
        "by_repo": dict(sorted(by_repo.items(), key=lambda x: -x[1])),
        "by_area": dict(sorted(by_area.items(), key=lambda x: -x[1])),
        "by_month_author": {m: dict(v) for m, v in sorted(by_month_author.items())},
        "by_month_repo": {m: dict(v) for m, v in sorted(by_month_repo.items())},
    }


def main():
    path = CSV_PATH if CSV_PATH.exists() else LEGACY_CSV
    rows = load_rows(path)
    result = analyze(rows)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
