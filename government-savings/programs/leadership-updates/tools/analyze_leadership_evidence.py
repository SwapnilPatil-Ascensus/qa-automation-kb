#!/usr/bin/env python3
"""Aggregate Jira, GitLab, qTest evidence into leadership metrics JSON."""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "2026-08-am-squad-leadership-update"
EVIDENCE = ROOT / "evidence"
OUT = ROOT / "data" / "leadership-metrics.json"


def parse_jira() -> dict:
    path = EVIDENCE / "Jira" / "JIRA - AMSQUAD Sprint 26.04 to 26.12 - All Fields.csv"
    by_sprint: dict[str, dict] = {}
    bugs_found = 0
    total_stories = 0
    total_points = 0.0
    by_type: dict[str, int] = defaultdict(int)
    sprint_re = re.compile(r"AMSQUAD Sprint ([\d.]+)", re.I)

    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    for r in rows:
        itype = (r.get("Issue Type") or "").strip()
        by_type[itype] += 1
        sp_raw = r.get("Custom field (Story Points)") or r.get("Custom field (Story point estimate)") or ""
        try:
            sp = float(sp_raw) if sp_raw else 0.0
        except ValueError:
            sp = 0.0

        # Sprint assignment in this export is primarily in Fix versions
        fix_versions = r.get("Fix versions") or ""
        sprint_match = sprint_re.search(fix_versions)
        if not sprint_match:
            # Fallback: Sprint columns (some exports)
            for key, val in r.items():
                if key.startswith("Sprint") and val and "AMSQUAD" in val:
                    sprint_match = sprint_re.search(val)
                    if sprint_match:
                        break
        if not sprint_match:
            continue

        sprint = f"AMSQUAD Sprint {sprint_match.group(1)}"
        if sprint not in by_sprint:
            by_sprint[sprint] = {
                "stories": 0,
                "tasks": 0,
                "spikes": 0,
                "bugs": 0,
                "story_points": 0.0,
                "work_items": 0,
            }
        bucket = by_sprint[sprint]
        bucket["work_items"] += 1
        if itype == "Bug":
            bucket["bugs"] += 1
            bugs_found += 1
        elif itype == "Spike":
            bucket["spikes"] += 1
            bucket["story_points"] += sp
            total_stories += 1
            total_points += sp
        elif itype == "Task":
            bucket["tasks"] += 1
            bucket["story_points"] += sp
            total_stories += 1
            total_points += sp
        elif itype in ("Story", "Sub-task"):
            bucket["stories"] += 1
            bucket["story_points"] += sp
            total_stories += 1
            total_points += sp

    ordered = []
    for key in sorted(by_sprint.keys(), key=lambda s: float(s.split()[-1])):
        ordered.append({"sprint": key, **by_sprint[key]})

    return {
        "sprints": ordered,
        "totals": {
            "work_items_in_sprints": sum(s["work_items"] for s in ordered),
            "stories_tasks_spikes": total_stories,
            "automation_bugs_logged": bugs_found,
            "story_points": round(total_points, 1),
            "total_issues_exported": len(rows),
        },
        "by_issue_type": dict(by_type),
    }


def parse_gitlab() -> dict:
    with (ROOT / "data" / "team-mr-summary.json").open(encoding="utf-8") as f:
        summary = json.load(f)

    repo_month = summary["by_month_repo"]
    monthly_area = {}
    for month, repos in repo_month.items():
        monthly_area[month] = {
            "V2 Legacy UI": repos.get("automation", 0),
            "V3 Universal Platform": repos.get("prime-test-automation", 0),
            "Performance Testing": 0,
            "API / Unite MSC": repos.get("api-test-automation", 0),
            "total": sum(repos.values()),
        }

    return {
        "total_mrs": summary["total_mrs"],
        "by_month": summary["by_month"],
        "by_area": summary["by_area"],
        "monthly_by_area": monthly_area,
        "source": "GitLab MR export (Apr 1 – Aug 4, 2026)",
    }


def parse_qtest() -> dict:
    path = EVIDENCE / "qTest" / "Table_9142.csv"
    by_month: dict[str, set[str]] = defaultdict(set)
    total_runs = 0
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_runs += 1
            tc_id = row.get("Test Case ID", "")
            exec_date = row.get("Execution End Date") or row.get("Execution Start Date") or ""
            if exec_date and tc_id:
                try:
                    dt = datetime.strptime(exec_date[:10], "%Y-%m-%d")
                    if dt.year == 2026 and dt.month >= 4:
                        by_month[dt.strftime("%Y-%m")].add(tc_id)
                except ValueError:
                    pass

    monthly_counts = {m: len(v) for m, v in sorted(by_month.items())}
    return {
        "note": "qTest reflects primarily V2/V3 UI automation runs — API and perf not fully reported",
        "total_execution_rows": total_runs,
        "unique_test_cases_by_month": monthly_counts,
        "project": "Automation Unite (90985)",
        "url": "https://ascensus.qtestnet.com",
    }


def delivery_work_units() -> dict:
    """Estimated monthly delivery units for stacked chart (MR-weighted + Jira SP)."""
    gitlab = parse_gitlab()
    jira = parse_jira()
    months = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08"]
    chart = []
    for m in months:
        area = gitlab["monthly_by_area"].get(m, {})
        chart.append({
            "month": m,
            "label": datetime.strptime(m, "%Y-%m").strftime("%b"),
            "V2 Legacy UI": area.get("V2 Legacy UI", 0),
            "V3 Universal Platform": area.get("V3 Universal Platform", 0),
            "Performance Testing": area.get("Performance Testing", 0),
            "API / Unite MSC": area.get("API / Unite MSC", 0),
            "total": area.get("total", 0),
        })
    return {"monthly_delivery_units": chart, "gitlab": gitlab, "jira": jira, "qtest": parse_qtest()}


def main() -> None:
    metrics = {
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "period": "April 1 – August 2026",
        "scorecard": {
            "gitlab_merges": 121,
            "v2_nightly_methods": 592,
            "v3_testng_cases": 379,
            "msc_m2_endpoints": "25/25",
            "msc_m1_core": "~25/29",
            "release_automation_pct": 80,
            "perf_regression_scenarios": 6,
        },
        **delivery_work_units(),
    }
    gitlab = metrics["gitlab"]
    metrics["scorecard"]["gitlab_merges"] = gitlab["total_mrs"]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    print(f"Wrote {OUT}")
    print(json.dumps(metrics["jira"]["totals"], indent=2))


if __name__ == "__main__":
    main()
