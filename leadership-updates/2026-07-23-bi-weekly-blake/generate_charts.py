#!/usr/bin/env python3
"""Generate PNG charts for bi-weekly Blake/Dhanashree leadership update."""

from __future__ import annotations

from pathlib import Path
import textwrap

import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).resolve().parent / "_assets"
NAVY = "#003057"
TEAL = "#007A8C"
GREEN = "#2E7D32"
AMBER = "#E65100"
RED = "#C62828"
V2_COLOR = "#4CAF50"
V3_COLOR = "#E53935"
AI_COLOR = "#007A8C"
TRAD_COLOR = "#90A4AE"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Calibri", "Arial"],
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.labelsize": 10,
})


def save(fig, name: str) -> Path:
    ASSETS.mkdir(parents=True, exist_ok=True)
    path = ASSETS / name
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def chart_cumulative_growth() -> Path:
    months = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr"]
    v2 = [250, 280, 320, 350, 381, 454, 500]
    v3 = [180, 200, 220, 240, 255, 325, 373]
    x = np.arange(len(months))
    width = 0.38
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.bar(x - width / 2, v2, width, label="V2 nightly TCs", color=V2_COLOR)
    ax.bar(x + width / 2, v3, width, label="V3 nightly TCs", color=V3_COLOR)
    ax.set_xticks(x)
    ax.set_xticklabels(months)
    ax.set_ylabel("Cumulative test cases")
    ax.set_title("V2 & V3 Nightly Regression Growth (verified through Apr 2026)")
    ax.legend(loc="upper left")
    ax.grid(axis="y", alpha=0.25)
    for i, (a, b) in enumerate(zip(v2, v3)):
        ax.text(i - width / 2, a + 8, str(a), ha="center", fontsize=8)
        ax.text(i + width / 2, b + 8, str(b), ha="center", fontsize=8)
    fig.text(0.01, 0.01, "Source: Demand Planning Reports 03/04 and 04/02", fontsize=8, color="#666")
    return save(fig, "chart_v2_v3_cumulative.png")


def chart_q2_monthly_adds() -> Path:
    months = ["April", "May", "June"]
    v2_adds = [46, 25, 15]
    v3_adds = [48, 18, 12]
    x = np.arange(len(months))
    width = 0.35
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(x - width / 2, v2_adds, width, label="V2 TCs added", color=V2_COLOR)
    ax.bar(x + width / 2, v3_adds, width, label="V3 TCs added", color=V3_COLOR)
    ax.set_xticks(x)
    ax.set_xticklabels(months)
    ax.set_ylabel("Test cases added (incremental)")
    ax.set_title("Q2 2026 — V2/V3 Test Cases Added by Month")
    ax.legend()
    ax.grid(axis="y", alpha=0.25)
    for bars in ax.containers:
        ax.bar_label(bars, padding=2, fontsize=9)
    fig.text(
        0.01, 0.01,
        "April: verified (Demand Planning 04/02). May/June: program estimate — monthly snapshot not in KB.",
        fontsize=8, color="#666",
    )
    return save(fig, "chart_q2_monthly_adds.png")


def chart_mobile_msc() -> Path:
    labels = ["Mobile 2\n(endpoints)", "Mobile 1\n(endpoints)"]
    implemented = [24, 6]
    total = [25, 27]
    x = np.arange(len(labels))
    width = 0.3
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - width / 2, implemented, width, label="Implemented", color=TEAL)
    ax.bar(x + width / 2, total, width, label="Documented scope", color="#B0BEC5")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Business endpoints")
    ax.set_title("Unite MSC Mobile API Automation (Jul 2026)")
    ax.legend()
    ax.set_ylim(0, 30)
    for i, (impl, tot) in enumerate(zip(implemented, total)):
        pct = impl / tot * 100
        ax.text(i, impl + 0.8, f"{impl}/{tot} ({pct:.0f}%)", ha="center", fontsize=10, fontweight="bold")
    fig.text(0.01, 0.01, "Source: leadership-updates/unite-msc/2026-07-17; api-test-automation @ cee0de9", fontsize=8, color="#666")
    return save(fig, "chart_mobile_msc_coverage.png")


def chart_ai_productivity() -> Path:
    # M2: typical 6 wks manual; actual 4 wks (2 sprints) → 1 sprint saved.
    tracks = [
        "Mobile 2\n(framework + 24 endpoints)\nCOMPLETE",
        "Mobile 1\n(auth foundation)\nIN PROGRESS",
    ]
    typical = [6, 3]
    with_ai = [4, 2]
    saved_labels = ["1 sprint saved", "1 wk saved"]
    x = np.arange(len(tracks))
    width = 0.3
    fig, ax = plt.subplots(figsize=(9, 6))
    bars_trad = ax.bar(x - width / 2, typical, width, label="Typical without AI (weeks)", color=TRAD_COLOR)
    bars_ai = ax.bar(x + width / 2, with_ai, width, label="Actual with agentic AI (weeks)", color=AI_COLOR)
    ax.set_xticks(x)
    ax.set_xticklabels(tracks, fontsize=9)
    ax.set_ylabel("Elapsed weeks")
    ax.set_title("Agentic AI — Time Saved on Unite MSC API Work")
    ax.set_ylim(0, 8.5)
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(axis="y", alpha=0.25)
    for bar in bars_trad:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 0.1, f"{int(h)} wks", ha="center", fontsize=9, color="#455A64")
    for bar in bars_ai:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 0.1, f"{int(h)} wks", ha="center", fontsize=9, color=NAVY, fontweight="bold")
    for i, label in enumerate(saved_labels):
        ymax = max(typical[i], with_ai[i])
        ax.annotate(
            label,
            xy=(i, ymax + 0.45),
            ha="center",
            fontsize=10,
            fontweight="bold",
            color=GREEN,
        )
    footnote = textwrap.fill(
        "Mobile 2 completed in 2 sprints (~4 weeks), including canonical TestNG framework build, "
        "dashboard automation, and custom reporting design. Typical manual delivery for the same scope "
        "is ~6 weeks (inventory, scaffolding, and ~2-3 days per endpoint without AI-assisted tooling).",
        width=105,
    )
    fig.subplots_adjust(bottom=0.30)
    fig.text(0.5, 0.04, footnote, ha="center", va="bottom", fontsize=7.5, color="#555", multialignment="center")
    return save(fig, "chart_ai_productivity.png")


def main() -> None:
    paths = [
        chart_cumulative_growth(),
        chart_q2_monthly_adds(),
        chart_mobile_msc(),
        chart_ai_productivity(),
    ]
    for p in paths:
        print(f"Wrote {p}")


if __name__ == "__main__":
    main()
