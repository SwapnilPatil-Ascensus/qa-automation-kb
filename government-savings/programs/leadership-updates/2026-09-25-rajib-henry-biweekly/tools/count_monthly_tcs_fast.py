#!/usr/bin/env python3
"""Fast monthly TC add counts via git log patches (Scenario / Examples / @Test / JMX)."""
from __future__ import annotations

import re
import subprocess
from collections import defaultdict
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
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout


def patch_adds(repo, since, until, pathspecs, patterns):
    """Count lines matching patterns that were added (+) in patches."""
    cmd = [
        "git", "log", f"--since={since}", f"--until={until}",
        "-p", "--pretty=format:", "--", *pathspecs,
    ]
    out = run(cmd, repo)
    counts = {k: 0 for k in patterns}
    for line in out.splitlines():
        if not line.startswith("+") or line.startswith("+++"):
            continue
        body = line[1:]
        for name, pat in patterns.items():
            if pat.search(body):
                counts[name] += 1
    return counts


def count_current_suite_scenarios(repo, xml_glob_hint):
    """Parse feature refs from daily XMLs and count scenarios currently."""
    files = run(["git", "ls-files"], repo).splitlines()
    xmls = [f for f in files if "bin/regression/daily" in f.replace("\\", "/") and f.endswith(".xml") and "Archive" not in f]
    if xml_glob_hint:
        xmls = [f for f in xmls if xml_glob_hint in f or True]
    return len(xmls), xmls


SCENARIO_PATS = {
    "scenario": re.compile(r"^\s*Scenario(?: Outline)?:"),
    "example_row": re.compile(r"^\s*\|\s*(?!-+)(?!.*\bExamples\b).+\|"),  # rough
}
# Better example detection: after Examples: headers, data rows
TEST_PATS = {"test": re.compile(r"@Test\b")}
JMX_PATS = {"http": re.compile(r'testclass="HTTPSamplerProxy"')}


def month_feature_stats(repo, pathspecs):
    rows = {}
    for label, since, until in MONTHS:
        # Count +Scenario lines
        out = run(
            ["git", "log", f"--since={since}", f"--until={until}", "-p", "--pretty=format:", "--", *pathspecs],
            repo,
        )
        scen_add = scen_del = ex_add = ex_del = 0
        in_ex = False
        header = False
        for line in out.splitlines():
            if line.startswith("+++") or line.startswith("---"):
                continue
            sign = line[:1]
            body = line[1:] if sign in "+-" else line
            if re.match(r"^\s*Examples:\s*$", body):
                in_ex = True
                header = False
                continue
            if in_ex and re.match(r"^\s*\|", body):
                if not header:
                    header = True
                    continue
                if sign == "+":
                    ex_add += 1
                elif sign == "-":
                    ex_del += 1
                continue
            if in_ex and body.strip() and not body.strip().startswith("#") and not re.match(r"^\s*\|", body):
                in_ex = False
                header = False
            if re.match(r"^\s*Scenario(?: Outline)?:", body):
                if sign == "+":
                    scen_add += 1
                elif sign == "-":
                    scen_del += 1
        # Prefer example-row net adds when significant; else scenario net
        tc = ex_add if ex_add >= scen_add else scen_add
        rows[label] = {
            "scenario_add": scen_add,
            "scenario_del": scen_del,
            "example_add": ex_add,
            "example_del": ex_del,
            "tc_added": max(0, tc - (ex_del if ex_add >= scen_add else scen_del)),
            "tc_added_gross": tc,  # additions only (what dashboard usually wants)
        }
        print(f"{repo.name} {label}: scen +{scen_add}/-{scen_del}  ex +{ex_add}/-{ex_del}  report={rows[label]['tc_added_gross']}")
    return rows


def month_java_tests(repo, pathspecs):
    rows = {}
    for label, since, until in MONTHS:
        out = run(
            ["git", "log", f"--since={since}", f"--until={until}", "-p", "--pretty=format:", "--", *pathspecs],
            repo,
        )
        add = del_ = 0
        for line in out.splitlines():
            if line.startswith("+++") or line.startswith("---"):
                continue
            if "@Test" in line:
                if line.startswith("+"):
                    add += 1
                elif line.startswith("-"):
                    del_ += 1
        rows[label] = {"test_add": add, "test_del": del_, "tc_added_gross": add}
        print(f"{repo.name} JAVA {label}: @Test +{add}/-{del_}")
    return rows


def month_jmx(repo, pathspecs):
    rows = {}
    for label, since, until in MONTHS:
        out = run(
            ["git", "log", f"--since={since}", f"--until={until}", "-p", "--pretty=format:", "--", *pathspecs],
            repo,
        )
        add = 0
        for line in out.splitlines():
            if line.startswith("+") and not line.startswith("+++") and 'testclass="HTTPSamplerProxy"' in line:
                add += 1
        rows[label] = {"tc_added_gross": add}
        print(f"{repo.name} JMX {label}: HTTPSampler +{add}")
    return rows


def main():
    v2 = Path(r"C:\Workspace\GitLab\Automation")
    v3 = Path(r"C:\Workspace\GitLab\prime-test-automation")
    api = Path(r"C:\Workspace\GitLab\api-test-automation")

    print("=== V2 unite-test-automation features (exclude Archive) ===")
    v2_feat = month_feature_stats(
        v2,
        [
            "unite-test-automation/unite/**/*.feature",
            ":(exclude)unite-test-automation/unite/**/Archive/**",
            ":(exclude)**/archived/**",
        ],
    )

    print("\n=== V3 prime features ===")
    v3_feat = month_feature_stats(
        v3,
        ["unite/**/*.feature", ":(exclude)**/Archive/**"],
    )

    print("\n=== Stage5 V2 ===")
    s5_v2 = month_feature_stats(
        v2,
        [
            "unite-test-automation/**/*stage5*",
            "unite-test-automation/**/*Stage5*",
            "unite-test-automation/**/stage-5/**",
            "unite-test-automation/**/smoke/**/*.feature",
        ],
    )

    print("\n=== Stage5 V3 ===")
    s5_v3 = month_feature_stats(
        v3,
        ["**/*stage5*", "**/*Stage5*", "**/stage-5/**", "**/smoke/**/*.feature"],
    )

    print("\n=== Perf JMX ===")
    perf = month_jmx(v2, ["performance-test-automation/**/*.jmx"])

    print("\n=== API MSC TestNG ===")
    api_m1 = month_java_tests(api, ["mobile/mobile1/**/*.java"])
    api_m2 = month_java_tests(api, ["mobile/mobile2/**/*.java"])
    api_enr = month_java_tests(api, ["mobile/enrollment/**/*.java"])

    # Also count current daily regression XML cucumber tags / scenarios referenced
    print("\n=== Current daily XML file counts ===")
    for name, repo, hint in [
        ("V2 daily XMLs", v2, "unite-test-automation/unite/bin/regression/daily"),
        ("V3 daily XMLs", v3, "unite/"),
    ]:
        files = [f for f in run(["git", "ls-files"], repo).splitlines()
                 if "bin/regression/daily" in f and f.endswith(".xml") and "Archive" not in f]
        print(name, len(files))
        for f in files:
            print(" ", f)

    print("\n\n======= DASHBOARD TABLE (gross adds) =======")
    print("Month,V2,V3,Stage5_V2,Stage5_V3,Perf_JMX,MSC_M1,MSC_M2,MSC_Enroll,MSC_Total")
    for label, _, _ in MONTHS:
        m1 = api_m1[label]["tc_added_gross"]
        m2 = api_m2[label]["tc_added_gross"]
        en = api_enr[label]["tc_added_gross"]
        print(
            f"{label},"
            f"{v2_feat[label]['tc_added_gross']},"
            f"{v3_feat[label]['tc_added_gross']},"
            f"{s5_v2[label]['tc_added_gross']},"
            f"{s5_v3[label]['tc_added_gross']},"
            f"{perf[label]['tc_added_gross']},"
            f"{m1},{m2},{en},{m1+m2+en}"
        )


if __name__ == "__main__":
    main()
