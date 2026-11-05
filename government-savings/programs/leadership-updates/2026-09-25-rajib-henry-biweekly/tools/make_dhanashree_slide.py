#!/usr/bin/env python3
"""Recreate Dhanashree's 3-panel QA AUTO slide format with Apr-Sep / Q3 numbers."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.gridspec import GridSpec
import numpy as np
from pathlib import Path

root = Path(
    r"c:\Workspace\GitLab\qa-automation-kb\programs\leadership-updates"
    r"\2026-09-25-rajib-henry-biweekly\dhanashree-monthly-tcs"
)

bg = "#D5E0E6"
header = "#2C5A66"
v2_c = "#2F7A6B"
v3_c = "#5C9A98"
text = "#243B42"


def panel_bg(ax):
    ax.set_facecolor(bg)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")


def bullets(ax, items, x0, y0, gap=7.2):
    y = y0
    for kind, line in items:
        if kind == "h":
            ax.text(x0, y, "•  " + line, fontsize=9.5, fontweight="bold", color=text, va="top")
        elif kind == "s":
            ax.text(x0 + 4, y, line, fontsize=8.3, color=text, va="top")
        elif kind == "t":
            ax.text(x0, y, line, fontsize=11, fontweight="bold", color=header, va="top")
        elif kind == "n":
            ax.text(x0 + 2, y, line, fontsize=8.5, color=text, va="top")
        y -= gap
    return y


LEFT = [
    ("h", "Expansion of Unite V2/V3 regression"),
    ("s", "(Total V2~451, V3~440 · nightly foundation;"),
    ("s", "CSR Actions + IDP / profile coverage expanded)"),
    ("h", "Unite MSC API / mobile automation"),
    ("s", "(M1 · M2 · Enrollment × 3 plans OKD/NYD/NMD)"),
    ("h", "Stage 5 / CAT smoke in active regression"),
    ("h", "Perf (JMeter) MSC / IDP / Mobile1 expansion"),
    ("t", "AI highlights"),
    ("n", "1. Cursor utils for Unite MSC automation"),
    ("n", "    (weeks saved on scaffold / MR flow)"),
    ("n", "2. Knowledge-base utils for dashboards"),
    ("n", "    & leadership docs / TC reporting"),
]

RIGHT = [
    ("h", "Jul–Sep capacity on MSC API + Perf +"),
    ("s", "Stage5/CAT — explains lower V2/V3"),
    ("s", "greenfield vs Apr–Jun; Sep uptick intentional"),
    ("h", "Roadmap / backlog visibility instead of"),
    ("s", "ad hoc task delivery"),
    ("h", "Dedicated ownership model for API and"),
    ("s", "Performance expansion (+ V2/V3 nightly,"),
    ("s", "CAT smoke)"),
    ("h", "Partial Scrum support for coordination,"),
    ("s", "backlog mgmt, reporting, and documentation"),
]


def draw_frame(fig):
    fig.patches.append(
        Rectangle(
            (0.015, 0.035),
            0.97,
            0.93,
            transform=fig.transFigure,
            fill=False,
            edgecolor="#7E97A2",
            linewidth=1.4,
            zorder=1000,
        )
    )
    for x in (0.345, 0.655):
        fig.patches.append(
            Rectangle(
                (x, 0.05),
                0.002,
                0.88,
                transform=fig.transFigure,
                facecolor="#9BB0B8",
                edgecolor="none",
                zorder=999,
            )
        )


def make_slide(months, v2, v3, title, outfile):
    fig = plt.figure(figsize=(15.2, 5.0), facecolor=bg)
    gs = GridSpec(
        1,
        3,
        width_ratios=[1.0, 1.25, 1.0],
        wspace=0.08,
        left=0.03,
        right=0.97,
        top=0.90,
        bottom=0.12,
    )

    axL = fig.add_subplot(gs[0])
    panel_bg(axL)
    axL.text(4, 94, "QA AUTO", fontsize=16, fontweight="bold", color=header, va="top")
    bullets(axL, LEFT, 4, 82, gap=6.0)

    axC = fig.add_subplot(gs[1])
    axC.set_facecolor("white")
    x = np.arange(len(months))
    w = 0.36 if len(months) <= 3 else 0.38
    b1 = axC.bar(x - w / 2, v2, w, label="V2 TCs added", color=v2_c, zorder=3)
    b2 = axC.bar(x + w / 2, v3, w, label="V3 TCs added", color=v3_c, zorder=3)
    for b in list(b1) + list(b2):
        h = b.get_height()
        axC.text(
            b.get_x() + b.get_width() / 2,
            h + 1.0,
            f"{int(h)}",
            ha="center",
            va="bottom",
            fontsize=8.5 if len(months) > 3 else 9.5,
            color=text,
            fontweight="bold",
        )
    axC.set_xticks(x, months, fontsize=9.5 if len(months) > 3 else 11, color=text)
    axC.set_ylim(0, 60)
    axC.set_yticks([0, 10, 20, 30, 40, 50, 60])
    axC.tick_params(axis="y", labelsize=8, colors=text)
    axC.set_title(title, fontsize=14, fontweight="bold", color=header, pad=10)
    leg = axC.legend(
        loc="upper right",
        fontsize=8.5,
        frameon=True,
        fancybox=False,
        edgecolor="#A8BCC4",
    )
    for t in leg.get_texts():
        t.set_color(text)
    axC.spines["top"].set_visible(False)
    axC.spines["right"].set_visible(False)
    axC.spines["left"].set_color("#8FA8B0")
    axC.spines["bottom"].set_color("#8FA8B0")
    axC.yaxis.grid(True, color="#C2D0D6", linewidth=0.9, zorder=0)
    axC.set_axisbelow(True)

    axR = fig.add_subplot(gs[2])
    panel_bg(axR)
    bullets(axR, RIGHT, 4, 90, gap=7.4)

    draw_frame(fig)
    out = root / outfile
    fig.savefig(out, dpi=220, facecolor=bg)
    plt.close()
    print(out)


make_slide(
    ["Apr", "May", "June", "Jul", "Aug", "Sep"],
    [46, 25, 15, 33, 8, 39],
    [48, 18, 12, 10, 8, 16],
    "TCs Added",
    "09-dhanashree-same-format-apr-sep.png",
)

make_slide(
    ["Jul", "Aug", "Sep"],
    [33, 8, 39],
    [10, 8, 16],
    "TCs Added in Q3",
    "09-dhanashree-same-format-q3.png",
)
