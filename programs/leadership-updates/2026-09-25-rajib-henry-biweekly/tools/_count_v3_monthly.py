#!/usr/bin/env python3
"""Count Gherkin Scenario/Example adds by month in prime-test-automation unite features."""
import re
import subprocess
from collections import defaultdict
from pathlib import Path

repo = Path(r"C:\Workspace\GitLab\prime-test-automation")
months = {
    "2026-07": ("2026-07-01", "2026-08-01"),
    "2026-08": ("2026-08-01", "2026-09-01"),
    "2026-09": ("2026-09-01", "2026-10-01"),
}

scenario_re = re.compile(r"^\+\s*(Scenario(?: Outline)?:)", re.M)
# examples rows roughly: | data | under Examples - count added | lines that look like data rows
example_row_re = re.compile(r"^\+\s*\|\s*(?!-|\s*[Ee]xamples)", re.M)


def month_diff_stats(since, until):
    r = subprocess.run(
        [
            "git",
            "log",
            f"--since={since}",
            f"--until={until}",
            "-p",
            "--",
            "unite/**/*.feature",
        ],
        cwd=repo,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore",
    )
    diff = r.stdout or ""
    scenarios = len(scenario_re.findall(diff))
    # Also count Scenario Outline examples carefully - user cares about TCs
    # Count files touched
    files = set(re.findall(r"^\+\+\+ b/(.+\.feature)$", diff, re.M))
    commits = subprocess.run(
        ["git", "log", f"--since={since}", f"--until={until}", "--oneline", "--", "unite/**/*.feature"],
        cwd=repo,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore",
    )
    n_commits = len([l for l in (commits.stdout or "").splitlines() if l.strip()])
    return scenarios, len(files), n_commits, files


for label, (a, b) in months.items():
    sc, nf, nc, files = month_diff_stats(a, b)
    print(f"{label}: +Scenario lines={sc}, files touched={nf}, commits={nc}")
    for f in sorted(files)[:25]:
        print(f"  {f}")
    if len(files) > 25:
        print(f"  ... +{len(files)-25} more")
