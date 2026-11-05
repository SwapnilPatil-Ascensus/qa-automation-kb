#!/usr/bin/env python3
"""Count dailyrun/regression TC adds + Stage5 smoke suite inventory."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

MONTHS = [
    ("2026-04", "2026-04-01", "2026-05-01"),
    ("2026-05", "2026-05-01", "2026-06-01"),
    ("2026-06", "2026-06-01", "2026-07-01"),
    ("2026-07", "2026-07-01", "2026-08-01"),
    ("2026-08", "2026-08-01", "2026-09-01"),
    ("2026-09", "2026-09-01", "2026-10-01"),
]


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout


def count_daily_examples_in_patch(repo, since, until, pathspecs):
    """Count added example rows that are under tags containing dailyrun or regression."""
    out = run(
        ["git", "log", f"--since={since}", f"--until={until}", "-p", "--pretty=format:", "--", *pathspecs],
        repo,
    )
    # Track tag context roughly: if recent lines had @dailyrun/@regression before Examples
    pending_tags = ""
    in_examples = False
    header = False
    daily_relevant = False
    add = 0
    scen_add = 0
    for line in out.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue
        sign = line[:1] if line[:1] in "+-" else " "
        body = line[1:] if sign in "+-" else line

        tag_m = re.findall(r"@[\w]+", body)
        if tag_m:
            pending_tags = " ".join(tag_m)
            daily_relevant = bool(re.search(r"dailyrun|regression|smoke", pending_tags, re.I))

        if re.match(r"^\s*Scenario(?: Outline)?:", body):
            if sign == "+" and daily_relevant:
                scen_add += 1
            continue

        if re.match(r"^\s*Examples:\s*$", body):
            in_examples = True
            header = False
            continue
        if in_examples and re.match(r"^\s*\|", body):
            if not header:
                header = True
                continue
            if sign == "+" and daily_relevant:
                add += 1
            continue
        if in_examples and body.strip() and not re.match(r"^\s*\|", body) and not body.strip().startswith("#"):
            in_examples = False
            header = False
    return {"daily_example_add": add, "daily_scenario_add": scen_add, "report": add if add else scen_add}


def parse_xml_cucumber_features(xml_text: str) -> list[str]:
    """Extract feature file paths from TestNG cucumber xml."""
    feats = re.findall(r"(?:features|cucumber\.features)[\"']?\s*[:=]\s*[\"']([^\"']+)[\"']", xml_text, re.I)
    feats += re.findall(r"<parameter\s+name=\"cucumber\.features\"\s+value=\"([^\"]+)\"", xml_text, re.I)
    feats += re.findall(r"features\s*=\s*\"([^\"]+)\"", xml_text)
    # Also glue from multiline
    return feats


def count_scenarios_in_features(repo, tip, feature_paths):
    total = 0
    for fp in feature_paths:
        fp = fp.strip()
        if not fp.endswith(".feature"):
            continue
        # try common roots
        candidates = [fp, fp.lstrip("./")]
        text = ""
        for c in candidates:
            text = run(["git", "show", f"{tip}:{c}"], repo)
            if text and not text.startswith("fatal"):
                break
        if not text or text.startswith("fatal"):
            continue
        ex = 0
        in_ex = False
        header = False
        scen = 0
        for line in text.splitlines():
            if re.match(r"^\s*Scenario(?: Outline)?:", line):
                scen += 1
            if re.match(r"^\s*Examples:\s*$", line):
                in_ex = True
                header = False
                continue
            if in_ex and re.match(r"^\s*\|", line):
                if not header:
                    header = True
                    continue
                ex += 1
            elif in_ex and line.strip() and not line.strip().startswith("#"):
                in_ex = False
        total += ex if ex else scen
    return total


def stage5_inventory(repo, xml_prefix):
    """Count scenarios currently wired in stage5 smoke XMLs."""
    files = [
        f
        for f in run(["git", "ls-files"], repo).splitlines()
        if "stage5" in f.lower() and f.endswith(".xml") and "Archive" not in f
    ]
    tip = run(["git", "rev-parse", "HEAD"], repo).strip()
    print(f"\n{repo.name} Stage5 XMLs ({len(files)}):")
    total = 0
    for f in files:
        xml = run(["git", "show", f"HEAD:{f}"], repo)
        # tags in cucumber.options
        tags = re.findall(r"tags\s*=\s*\"([^\"]+)\"", xml, re.I)
        tags += re.findall(r"cucumber\.filter\.tags[\"']?\s*[:=]\s*[\"']([^\"']+)", xml, re.I)
        # Count Feature: lines referenced via features= paths
        feat_paths = []
        for block in re.findall(r"features\s*=\s*\"([^\"]+)\"", xml, re.I):
            feat_paths.extend(re.split(r"[,;\s]+", block))
        # Many suites use package glue + tags only — count <test> blocks as proxy
        tests = len(re.findall(r"<test\b", xml, re.I))
        classes = len(re.findall(r"<class\b", xml, re.I))
        print(f"  {f}: <test>={tests} <class>={classes} tags={tags[:2]}")
        total += max(tests, classes)
    return total, files


def when_file_added(repo, path):
    out = run(["git", "log", "--diff-filter=A", "--follow", "--format=%ad", "--date=short", "--", path], repo)
    lines = [l for l in out.splitlines() if l.strip()]
    return lines[-1] if lines else ""


def main():
    v2 = Path(r"C:\Workspace\GitLab\Automation")
    v3 = Path(r"C:\Workspace\GitLab\prime-test-automation")
    api = Path(r"C:\Workspace\GitLab\api-test-automation")

    print("=== @dailyrun/@regression tagged adds ===")
    for label, since, until in MONTHS:
        v2c = count_daily_examples_in_patch(
            v2, since, until,
            ["unite-test-automation/unite/**/*.feature", ":(exclude)**/Archive/**"],
        )
        v3c = count_daily_examples_in_patch(
            v3, since, until,
            ["unite/**/*.feature", ":(exclude)**/Archive/**"],
        )
        print(f"{label}: V2 daily-ish={v2c} | V3 daily-ish={v3c}")

    print("\n=== Stage5 suite XML inventory (current) ===")
    s5v2, files_v2 = stage5_inventory(v2, "stage5")
    s5v3, files_v3 = stage5_inventory(v3, "stage5")
    print(f"V2 Stage5 XML test blocks total≈{s5v2}")
    print(f"V3 Stage5 XML test blocks total≈{s5v3}")

    print("\n=== Stage5 XML first-added dates ===")
    for repo, files in [(v2, files_v2), (v3, files_v3)]:
        for f in files:
            print(f"  {when_file_added(repo, f)}  {f}")

    # Count scenarios currently matching tags used by stage5 masters by scanning features with @smoke @stage5 if any
    print("\n=== Features mentioning stage5 or CAT ===")
    for repo in (v2, v3):
        out = run(["git", "grep", "-l", "-i", "stage5\\|@cat\\|CAT", "--", "*.feature"], repo)
        feats = [l for l in out.splitlines() if l.strip()]
        print(repo.name, "feature hits", len(feats))

    # API: net method inventory at month ends via simpler log --diff-filter
    print("\n=== API @Test adds by module (gross) — confirm ===")
    for mod in ["mobile/mobile1", "mobile/mobile2", "mobile/enrollment"]:
        for label, since, until in MONTHS:
            out = run(
                ["git", "log", f"--since={since}", f"--until={until}", "-p", "--pretty=format:", "--", f"{mod}/**/*.java"],
                api,
            )
            add = sum(1 for l in out.splitlines() if l.startswith("+") and not l.startswith("+++") and "@Test" in l)
            if add:
                print(f"  {label} {mod}: +{add}")


if __name__ == "__main__":
    main()
