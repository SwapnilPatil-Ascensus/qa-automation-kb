#!/usr/bin/env python3
"""Generate leadership update charts for AM Squad Q2-Q3 2026."""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

NAVY = "#003241"
TEAL = "#026B84"
PEAK = "#009E86"
ORANGE = "#F7941D"
PURPLE = "#5B4B9A"
GRAY = "#6D6E71"
LIGHT = "#E8EEF4"

ROOT = Path(__file__).resolve().parents[1] / "2026-08-am-squad-leadership-update"
OUT = ROOT / "assets" / "charts"
METRICS = ROOT / "data" / "leadership-metrics.json"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "Segoe UI",
    "font.size": 10,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
})


def load_metrics() -> dict:
    with METRICS.open(encoding="utf-8") as f:
        return json.load(f)


def save(fig, name: str) -> None:
    path = OUT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {path}")


def chart_gitlab_merges_stacked(m: dict) -> None:
    """GitLab merges by month — stacked by repository channel."""
    months = ["Apr", "May", "Jun", "Jul", "Aug"]
    keys = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08"]
    repo_data = m["gitlab"]["monthly_by_repo"]
    v2 = [repo_data[k]["V2 Legacy UI"] for k in keys]
    v3 = [repo_data[k]["V3 Universal Platform"] for k in keys]
    api = [repo_data[k]["API / Unite MSC"] for k in keys]
    x = np.arange(len(months))
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.bar(x, v2, 0.62, label="V2 (automation repo)", color=NAVY)
    ax.bar(x, v3, 0.62, bottom=v2, label="V3 (prime-test-automation)", color=TEAL)
    b2 = [a + b for a, b in zip(v2, v3)]
    ax.bar(x, api, 0.62, bottom=b2, label="API / MSC (api-test-automation)", color=PEAK)
    totals = [repo_data[k]["total"] for k in keys]
    for i, t in enumerate(totals):
        ax.text(i, t + 1.2, str(t), ha="center", fontweight="bold", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(months)
    ax.set_ylabel("GitLab merges to main")
    ax.set_title("GitLab Delivery Velocity by Repository (Apr–Aug 2026)")
    ax.legend(loc="upper left", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.2)
    save(fig, "01-gitlab-mrs-by-month.png")


def chart_monthly_test_cases_added(m: dict) -> None:
    """Automation test cases added per month — NOT merge count."""
    data = m["monthly_test_cases_added"]
    labels = [d["label"] for d in data]
    channels = ["V2 Legacy UI", "V3 Universal Platform", "Performance Testing", "API / Unite MSC", "Standards / Pipeline"]
    colors = [NAVY, TEAL, ORANGE, PEAK, PURPLE]
    x = np.arange(len(labels))
    bottom = np.zeros(len(labels))
    fig, ax = plt.subplots(figsize=(10, 5.2))
    for ch, color in zip(channels, colors):
        vals = [d.get(ch, 0) for d in data]
        ax.bar(x, vals, 0.62, bottom=bottom, label=ch, color=color)
        bottom = bottom + np.array(vals)
    for i, d in enumerate(data):
        ax.text(i, d["total"] + 3, str(d["total"]), ha="center", fontweight="bold", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Estimated test cases added (period)")
    ax.set_title("Monthly Automation Delivery — New Coverage Added (Apr–Aug 2026)")
    ax.legend(loc="upper left", fontsize=8)
    note = (
        "Period delivery estimate from Jira resolved stories — not cumulative inventory. "
        "Team formed Q2 2025; nightly totals (592 V2, 442 V3, 323 perf) reflect ~12 months of build-out."
    )
    ax.text(0.01, -0.14, note, transform=ax.transAxes, fontsize=8, color=GRAY)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.2)
    save(fig, "08-monthly-automation-test-cases-added.png")


def chart_jira_story_points(m: dict) -> None:
    sprints = m["jira"]["sprints"]
    labels = [s["sprint"].replace("AMSQUAD Sprint ", "S") for s in sprints]
    points = [s["story_points"] for s in sprints]
    items = [s["work_items"] for s in sprints]
    fig, ax1 = plt.subplots(figsize=(10, 4.8))
    bars = ax1.bar(labels, points, color=TEAL, alpha=0.9)
    ax1.set_ylabel("Story points delivered")
    ax1.set_title("Jira Sprint Delivery — Story Points & Work Items (Sprint 26.04–26.12)")
    ax2 = ax1.twinx()
    ax2.plot(labels, items, color=NAVY, marker="o", linewidth=2)
    ax2.set_ylabel("Work items closed")
    for b, v in zip(bars, points):
        ax1.text(b.get_x() + b.get_width() / 2, v + 1.5, f"{v:.0f}", ha="center", fontsize=8, fontweight="bold")
    ax1.spines[["top"]].set_visible(False)
    ax2.spines[["top"]].set_visible(False)
    ax1.grid(axis="y", alpha=0.2)
    save(fig, "09-jira-story-points-by-sprint.png")


def chart_jira_bugs(m: dict) -> None:
    sprints = m["jira"]["sprints"]
    labels = [s["sprint"].replace("AMSQUAD Sprint ", "S") for s in sprints]
    bugs = [s["bugs"] for s in sprints]
    fig, ax = plt.subplots(figsize=(10, 4.2))
    bars = ax.bar(labels, bugs, color=ORANGE, edgecolor="white")
    ax.set_ylabel("Automation bugs logged")
    ax.set_title(f"Defects Found via Automation — {m['jira']['totals']['automation_bugs_logged']} total")
    for b, v in zip(bars, bugs):
        if v:
            ax.text(b.get_x() + b.get_width() / 2, v + 0.15, str(v), ha="center", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.2)
    save(fig, "10-jira-automation-bugs-by-sprint.png")


def chart_module_totals(
    modules: list[str],
    totals: list[int],
    title: str,
    filename: str,
    bar_color: str = TEAL,
) -> None:
    """Bar chart of total test methods per module + share-of-suite line (no pass/fail)."""
    suite_total = sum(totals)
    shares = [100 * t / suite_total for t in totals]
    x = np.arange(len(modules))
    fig, ax1 = plt.subplots(figsize=(11, 5))
    bars = ax1.bar(x, totals, 0.62, color=bar_color, alpha=0.92)
    ax1.set_ylabel("Test methods (total)")
    ax1.set_title(title)
    ax1.set_xticks(x)
    ax1.set_xticklabels(modules, rotation=32, ha="right")
    ax2 = ax1.twinx()
    ax2.plot(x, shares, color=NAVY, marker="o", linewidth=2, label="% of suite")
    ax2.set_ylabel("% of nightly suite")
    ax2.set_ylim(0, max(shares) * 1.35 if shares else 10)
    for b, v in zip(bars, totals):
        ax1.text(b.get_x() + b.get_width() / 2, v + max(totals) * 0.02, str(v),
                 ha="center", fontsize=8, fontweight="bold")
    ax1.text(0.99, 0.97, f"Suite total: {suite_total} test methods",
             transform=ax1.transAxes, ha="right", va="top", fontsize=9, color=GRAY)
    ax1.spines[["top"]].set_visible(False)
    ax2.spines[["top"]].set_visible(False)
    ax1.grid(axis="y", alpha=0.2)
    save(fig, filename)


def chart_v2_regression_modules() -> None:
    modules = [
        "Enrollments", "Acct Maint", "Empower", "Withdrawals", "Contributions",
        "Ugift", "Web Reg", "Sardine", "Inv Options", "Transfers", "Web Login", "Balance",
    ]
    passed = [59, 67, 54, 63, 45, 29, 35, 24, 14, 7, 4, 7]
    failed = [88, 7, 21, 10, 3, 7, 6, 9, 10, 5, 15, 3]
    totals = [p + f for p, f in zip(passed, failed)]
    chart_module_totals(
        modules, totals,
        "V2 Stage1 Nightly — Test Methods by Module (Aug 4 snapshot; excludes smoke/Stage 2/5)",
        "04-v2-regression-by-module.png",
        bar_color=NAVY,
    )


def chart_v3_regression_modules(m: dict) -> None:
    modules = m["v3_snapshot"]["modules"]
    names = []
    for mod in modules:
        short = (
            mod["module"]
            .replace("Universal Enrollment Stage1 Environment", "Universal Enrollment")
            .replace(" Stage1 Environment", "")
        )
        names.append(short[:24])
    totals = [mod["methods"] for mod in modules]
    chart_module_totals(
        names, totals,
        "V3 GitLab Stage1 Nightly — Test Methods by Module (Aug 4 snapshot; excludes smoke/integrations)",
        "11-v3-regression-by-module.png",
        bar_color=TEAL,
    )


def chart_api_module_snapshot(m: dict) -> None:
    """API automation coverage by module/category — coverage only."""
    cats = m["api_module_snapshot"]["categories"]
    names = [c["name"][:20] for c in cats]
    automated = [c["automated"] for c in cats]
    remaining = [max(c["target"] - c["automated"], 0) for c in cats]
    x = np.arange(len(names))
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.bar(x, automated, 0.55, label="Automated", color=TEAL)
    ax.bar(x, remaining, 0.55, bottom=automated, label="Remaining", color=LIGHT, edgecolor=GRAY, linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=30, ha="right")
    ax.set_ylabel("Endpoints / categories")
    ax.set_title("API / Unite MSC — Automation Coverage by Module (Aug 2026)")
    ax.legend(loc="upper right")
    for i, c in enumerate(cats):
        pct = round(100 * c["automated"] / c["target"]) if c["target"] else 100
        ax.text(i, c["target"] + 0.3, f"{pct}%", ha="center", fontweight="bold", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "13-api-regression-by-module.png")


def chart_msc_coverage(m: dict) -> None:
    """Coverage only — no wired/target comparison."""
    cats = m["api_snapshot"]["categories"][:2]
    labels = [c["name"] for c in cats]
    pcts = [round(100 * c["count"] / c["denominator"]) for c in cats]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.bar(labels, pcts, color=[PEAK, TEAL], width=0.5)
    ax.set_ylim(0, 110)
    ax.set_ylabel("Coverage %")
    ax.set_title("Unite MSC — API Endpoint Coverage")
    for b, c, p in zip(bars, cats, pcts):
        ax.text(b.get_x() + b.get_width() / 2, p + 2, f"{c['count']}/{c['denominator']}\n({p}%)",
                ha="center", fontweight="bold", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.2)
    save(fig, "05-unite-msc-coverage.png")


def chart_perf_inventory(m: dict) -> None:
    areas = m["perf_inventory"]["areas"]
    names = [a["area"][:22] for a in areas]
    labels = [a["labels"] for a in areas]
    cases = [a["cases"] for a in areas]
    x = np.arange(len(names))
    fig, ax1 = plt.subplots(figsize=(11, 5.2))
    bars = ax1.bar(x, labels, 0.62, color=ORANGE, alpha=0.9, label="Transaction flows")
    ax1.set_ylabel("Base transaction flows")
    ax1.set_title("Performance Coverage — Flows vs Plan-Expanded Test Cases")
    ax1.set_xticks(x)
    ax1.set_xticklabels(names, rotation=32, ha="right")
    ax2 = ax1.twinx()
    ax2.plot(x, cases, color=NAVY, marker="o", linewidth=2, label="Expanded cases")
    ax2.set_ylabel("Test cases (× plan permutations)")
    for b, v in zip(bars, labels):
        ax1.text(b.get_x() + b.get_width() / 2, v + 0.4, str(v), ha="center", fontsize=7, fontweight="bold")
    total_cases = m["perf_inventory"]["total_test_cases"]
    base_flows = sum(labels)
    ax1.text(
        0.99, 0.97,
        f"{base_flows} base flows → {total_cases} test cases across plans\n"
        f"4 Jenkins scenarios schedule these permutations",
        transform=ax1.transAxes, ha="right", va="top", fontsize=8, color=GRAY,
    )
    ax1.spines[["top"]].set_visible(False)
    ax2.spines[["top"]].set_visible(False)
    ax1.grid(axis="y", alpha=0.2)
    save(fig, "12-perf-test-case-inventory.png")


def chart_mr_by_area(m: dict) -> None:
    labels = ["API / Unite MSC", "V2 Legacy UI +\nPerformance", "V3 Universal\nPlatform"]
    sizes = [48, 42, 26]
    colors = [PEAK, NAVY, TEAL]
    fig, ax = plt.subplots(figsize=(7, 5))
    _, _, autotexts = ax.pie(
        sizes, labels=labels, autopct="%1.0f%%", colors=colors,
        startangle=90, pctdistance=0.75, wedgeprops=dict(width=0.45, edgecolor="white"),
    )
    for t in autotexts:
        t.set_fontweight("bold")
        t.set_color("white")
    total = m["gitlab"]["total_mrs"]
    ax.set_title(f"{total} GitLab Merges by Automation Area")
    save(fig, "02-gitlab-mrs-by-area.png")


def chart_work_allocation() -> None:
    areas = ["Unite MSC API", "V2 UI Regression", "V3 UP UI", "Performance", "Pipeline/CI", "Standards", "Cross-team"]
    effort = [35, 20, 15, 12, 10, 8, 10]
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = plt.cm.Blues(np.linspace(0.45, 0.9, len(areas)))[::-1]
    ax.barh(areas[::-1], effort[::-1], color=colors[::-1], height=0.65)
    ax.set_xlabel("Relative effort index")
    ax.set_title("Investment Allocation — Multi-Track Delivery (Apr–Jul 2026)")
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "06-work-allocation-index.png")


def chart_release_automation_impact() -> None:
    fig, ax = plt.subplots(figsize=(5.5, 5))
    ax.pie([80, 20], labels=["Automated", "Manual queue"], autopct="%1.0f%%",
           colors=[PEAK, GRAY], startangle=90, wedgeprops=dict(edgecolor="white"))
    ax.set_title("Monthly Release Validation\n(17 FTE → 2 FTE equivalent)")
    save(fig, "07-release-automation-impact.png")


def main() -> None:
    m = load_metrics()
    chart_gitlab_merges_stacked(m)
    chart_monthly_test_cases_added(m)
    chart_jira_story_points(m)
    chart_jira_bugs(m)
    chart_v2_regression_modules()
    chart_v3_regression_modules(m)
    chart_api_module_snapshot(m)
    chart_msc_coverage(m)
    chart_perf_inventory(m)
    chart_mr_by_area(m)
    chart_work_allocation()
    chart_release_automation_impact()
    print("All charts generated.")


if __name__ == "__main__":
    main()
