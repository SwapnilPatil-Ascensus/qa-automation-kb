#!/usr/bin/env python3
"""Count monthly TC additions from git history for Dhanashree dashboard."""
from __future__ import annotations

import re
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path

MONTHS = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]


def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout


def month_key(iso_date: str) -> str:
    return iso_date[:7]


def count_scenarios(text: str) -> int:
    # Cucumber Scenario / Scenario Outline + Examples table rows (data rows after header)
    scenarios = len(re.findall(r"^\s*Scenario(?: Outline)?:", text, re.M))
    # Count example data rows (lines starting with | that aren't header-only heuristics)
    example_rows = 0
    in_examples = False
    header_seen = False
    for line in text.splitlines():
        if re.match(r"^\s*Examples:\s*$", line):
            in_examples = True
            header_seen = False
            continue
        if in_examples:
            if re.match(r"^\s*\|", line):
                if not header_seen:
                    header_seen = True
                    continue
                if re.search(r"\|\s*\S", line):
                    example_rows += 1
            elif line.strip() == "" or line.strip().startswith("#"):
                continue
            else:
                in_examples = False
                header_seen = False
    # Prefer examples when present (each data row = 1 TC); else scenarios
    return example_rows if example_rows else scenarios


def count_java_tests(text: str) -> int:
    return len(re.findall(r"@Test\b", text))


def count_jmx_samplers(text: str) -> int:
    # HTTPSamplerProxy + TransactionController as rough case proxies
    return len(re.findall(r'testclass="HTTPSamplerProxy"', text)) + len(
        re.findall(r'testclass="TransactionController"', text)
    )


def file_at(repo, rev, path):
    return run(["git", "show", f"{rev}:{path}"], repo)


def list_paths_at(repo, rev, globs):
    out = run(["git", "ls-tree", "-r", "--name-only", rev], repo)
    paths = []
    for line in out.splitlines():
        for g in globs:
            if re.search(g, line.replace("\\", "/"), re.I):
                paths.append(line)
                break
    return paths


def first_commit_on_or_before(repo, end_date):
    # tip as of end of month
    out = run(["git", "rev-list", "-1", f"--before={end_date} 23:59:59", "origin/main"], repo)
    tip = out.strip().splitlines()[0] if out.strip() else ""
    return tip


def inventory_at(repo, rev, globs, counter):
    if not rev:
        return 0, {}
    total = 0
    by_path = {}
    for path in list_paths_at(repo, rev, globs):
        try:
            text = file_at(repo, rev, path)
        except Exception:
            continue
        n = counter(text)
        if n:
            by_path[path] = n
            total += n
    return total, by_path


def monthly_deltas(repo, globs, counter, label):
    """Cumulative inventory at month-end, then delta vs prior month."""
    ends = {
        "2026-04": "2026-04-30",
        "2026-05": "2026-05-31",
        "2026-06": "2026-06-30",
        "2026-07": "2026-07-31",
        "2026-08": "2026-08-31",
        "2026-09": "2026-09-29",
    }
    tips = {}
    totals = {}
    for m, d in ends.items():
        tips[m] = first_commit_on_or_before(repo, d)
        totals[m], _ = inventory_at(repo, tips[m], globs, counter)
        print(f"  {label} {m}: tip={tips[m][:8] if tips[m] else 'NONE'} total={totals[m]}")

    # baseline before Apr = Mar 31
    base_tip = first_commit_on_or_before(repo, "2026-03-31")
    base_total, _ = inventory_at(repo, base_tip, globs, counter)
    print(f"  {label} baseline 2026-03-31: {base_total}")

    deltas = {}
    prev = base_total
    for m in MONTHS:
        cur = totals[m]
        deltas[m] = max(0, cur - prev)  # additions only (ignore net removals for dashboard)
        # Also track raw delta
        print(f"  {label} delta {m}: +{deltas[m]} (raw {cur - prev})")
        prev = cur
    return deltas, totals


def main():
    v2 = Path(r"C:\Workspace\GitLab\Automation")
    # confirm unite path
    if (v2 / "unite-test-automation").exists():
        v2_repo = v2  # monorepo?
    else:
        v2_repo = v2

    # Find actual V2 features root via git
    print("=== V2 repo structure ===")
    print(run(["git", "ls-tree", "-d", "--name-only", "HEAD"], v2_repo)[:500])

    v3 = Path(r"C:\Workspace\GitLab\prime-test-automation")
    api = Path(r"C:\Workspace\GitLab\api-test-automation")

    print("\n=== Fetching remotes ===")
    for r in (v2_repo, v3, api):
        print(r, run(["git", "fetch", "origin", "main"], r)[:200])

    # V2 feature files
    print("\n=== V2 feature scenarios ===")
    v2_globs = [r"\.feature$"]
    # exclude archive if possible
    v2_deltas, v2_totals = monthly_deltas(
        v2_repo,
        [r"(?i)feature.*\.feature$|\.feature$"],
        count_scenarios,
        "V2",
    )

    print("\n=== V3 feature scenarios ===")
    v3_deltas, v3_totals = monthly_deltas(
        v3,
        [r"\.feature$"],
        count_scenarios,
        "V3",
    )

    print("\n=== Stage5 features (V2+V3) ===")
    s5_v2, s5_v2_tot = monthly_deltas(
        v2_repo,
        [r"(?i)stage.?5.*\.feature$|(?i)smoke.*stage.?5|(?i)bin/.*stage5"],
        count_scenarios,
        "S5-V2",
    )
    s5_v3, s5_v3_tot = monthly_deltas(
        v3,
        [r"(?i)stage.?5|stage5"],
        count_scenarios,
        "S5-V3",
    )

    print("\n=== Perf JMX ===")
    perf_path = v2_repo / "performance-test-automation"
    perf_repo = v2_repo if perf_path.exists() else v2_repo
    perf_deltas, perf_totals = monthly_deltas(
        perf_repo,
        [r"(?i)performance.*\.jmx$|\.jmx$"],
        count_jmx_samplers,
        "PERF",
    )

    print("\n=== API TestNG @Test ===")
    api_deltas, api_totals = monthly_deltas(
        api,
        [r"(?i)mobile.*/.*Test\.java$|(?i)mobile/.*/src/.*\.java$"],
        count_java_tests,
        "API",
    )

    print("\n=== SUMMARY TABLE ===")
    print("Month,V2_added,V3_added,Stage5_V2,Stage5_V3,Perf_samplers,API_tests")
    for m in MONTHS:
        print(
            f"{m},{v2_deltas.get(m,0)},{v3_deltas.get(m,0)},"
            f"{s5_v2.get(m,0)},{s5_v3.get(m,0)},{perf_deltas.get(m,0)},{api_deltas.get(m,0)}"
        )

    print("\n=== CUMULATIVE TOTALS (month-end) ===")
    print("Month,V2_total,V3_total,Perf_total,API_total")
    for m in MONTHS:
        print(f"{m},{v2_totals.get(m,0)},{v3_totals.get(m,0)},{perf_totals.get(m,0)},{api_totals.get(m,0)}")


if __name__ == "__main__":
    main()
