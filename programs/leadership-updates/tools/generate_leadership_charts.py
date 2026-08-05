#!/usr/bin/env python3
"""Generate leadership update charts for AM Squad Q2-Q3 2026."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Ascensus-inspired palette
NAVY = "#003366"
TEAL = "#00A3AD"
ORANGE = "#F7941D"
GRAY = "#6D6E71"
LIGHT = "#E8EEF4"

OUT = Path(__file__).resolve().parents[1] / "2026-08-am-squad-leadership-update/assets/charts"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "Segoe UI",
    "font.size": 10,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
})


def save(fig, name: str):
    path = OUT / name
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {path}")


def chart_mr_by_month():
    months = ["Apr", "May", "Jun", "Jul", "Aug"]
    counts = [24, 22, 34, 33, 3]
    colors = [NAVY if c == max(counts) else TEAL for c in counts]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.bar(months, counts, color=colors, edgecolor="white", linewidth=0.8)
    ax.set_ylabel("Merged MRs to main")
    ax.set_title("AM Squad Delivery Velocity — GitLab Merges (Apr–Aug 2026)")
    ax.set_ylim(0, max(counts) + 8)
    for b, v in zip(bars, counts):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.6, str(v), ha="center", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.25)
    save(fig, "01-gitlab-mrs-by-month.png")


def chart_mr_by_area():
    labels = ["API / Unite MSC", "V2 Legacy UI +\nPerformance", "V3 Universal\nPlatform"]
    sizes = [48, 42, 26]
    colors = [NAVY, TEAL, ORANGE]
    fig, ax = plt.subplots(figsize=(7, 5))
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, autopct="%1.0f%%", colors=colors,
        startangle=90, pctdistance=0.75, wedgeprops=dict(width=0.45, edgecolor="white"),
    )
    for t in autotexts:
        t.set_fontweight("bold")
        t.set_color("white")
    ax.set_title("116 Merged MRs by Automation Area (Apr–Aug 2026)")
    save(fig, "02-gitlab-mrs-by-area.png")


def chart_mr_by_author():
    authors = ["Sunil", "Venkatesh", "Dinesh", "Swapnil", "Priti"]
    counts = [28, 27, 26, 25, 10]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    y = np.arange(len(authors))
    ax.barh(y, counts, color=TEAL, height=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(authors)
    ax.invert_yaxis()
    ax.set_xlabel("Merged MRs authored")
    ax.set_title("Team Contribution — GitLab Merge Requests (Apr–Aug 2026)")
    for i, v in enumerate(counts):
        ax.text(v + 0.4, i, str(v), va="center", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="x", alpha=0.25)
    save(fig, "03-gitlab-mrs-by-author.png")


def chart_v2_regression_modules():
    modules = [
        "Enrollments", "Acct Maint", "Empower", "Withdrawals",
        "Contributions", "Ugift", "Web Reg", "Sardine", "Inv Options",
        "Transfers", "Web Login", "Balance",
    ]
    passed = [59, 67, 54, 63, 45, 29, 35, 24, 14, 7, 4, 7]
    failed = [88, 7, 21, 10, 3, 7, 6, 9, 10, 5, 15, 3]
    x = np.arange(len(modules))
    w = 0.55
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(x, passed, w, label="Passed", color=TEAL)
    ax.bar(x, failed, w, bottom=passed, label="Failed", color=ORANGE)
    ax.set_xticks(x)
    ax.set_xticklabels(modules, rotation=35, ha="right")
    ax.set_ylabel("Test methods")
    ax.set_title("V2 Stage1 Nightly Regression — Module Snapshot (2026-08-04)")
    ax.legend(loc="upper right")
    totals = [p + f for p, f in zip(passed, failed)]
    ax.text(len(modules) - 0.5, max(totals) + 5,
            f"Total: {sum(totals)} methods | Pass rate: {100*sum(passed)/sum(totals):.0f}%",
            fontsize=9, color=GRAY)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "04-v2-regression-by-module.png")


def chart_unite_msc_coverage():
    categories = ["Mobile 2\nEndpoints", "Mobile 1\nEndpoints", "M2 Test\nClasses", "Perf\nScenarios"]
    current = [24, 18, 36, 6]
    target = [25, 27, 40, 12]
    x = np.arange(len(categories))
    w = 0.35
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(x - w / 2, current, w, label="Aug 2026", color=NAVY)
    ax.bar(x + w / 2, target, w, label="Target", color=LIGHT, edgecolor=NAVY)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylabel("Count")
    ax.set_title("Unite MSC — API & Performance Coverage Progress")
    ax.legend()
    for i, (c, t) in enumerate(zip(current, target)):
        pct = 100 * c / t
        ax.text(i, max(c, t) + 0.8, f"{pct:.0f}%", ha="center", fontweight="bold", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "05-unite-msc-coverage.png")


def chart_work_allocation():
    areas = [
        "Unite MSC API", "V2 UI Regression", "V3 UP UI", "Performance",
        "Pipeline/CI", "Standards &\nFramework", "Cross-team\nSupport",
    ]
    # Relative effort index (justified by MR mix + program priority)
    effort = [35, 20, 15, 12, 10, 8, 10]
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = plt.cm.Blues(np.linspace(0.45, 0.9, len(areas)))[::-1]
    ax.barh(areas[::-1], effort[::-1], color=colors[::-1], height=0.65)
    ax.set_xlabel("Relative effort index (Apr–Jul 2026)")
    ax.set_title("Where AM Squad Time Went — Multi-Track Delivery")
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "06-work-allocation-index.png")


def chart_release_automation_impact():
    labels = ["Automated\n(validations)", "Manual\n(queue)"]
    sizes = [80, 20]
    colors = [TEAL, GRAY]
    fig, ax = plt.subplots(figsize=(5.5, 5))
    ax.pie(sizes, labels=labels, autopct="%1.0f%%", colors=colors,
           startangle=90, wedgeprops=dict(edgecolor="white"))
    ax.set_title("Monthly Release Validation\n(17 FTE → 2 FTE + automation)")
    save(fig, "07-release-automation-impact.png")


def main():
    chart_mr_by_month()
    chart_mr_by_area()
    chart_mr_by_author()
    chart_v2_regression_modules()
    chart_unite_msc_coverage()
    chart_work_allocation()
    chart_release_automation_impact()
    print("All charts generated.")


if __name__ == "__main__":
    main()
