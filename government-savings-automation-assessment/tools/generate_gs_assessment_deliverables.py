#!/usr/bin/env python3
"""Generate GS Automation Assessment XLSX and leadership DOCX from CSV sources."""

from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.chart import BarChart, Reference
except ImportError:
    raise SystemExit("Install openpyxl: pip install openpyxl")

try:
    from docx import Document
    from docx.enum.section import WD_ORIENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor, Cm
except ImportError:
    raise SystemExit("Install python-docx: pip install python-docx")

ROOT = Path(__file__).resolve().parent.parent
MATRIX_CSV = ROOT / "03-analysis" / "government-savings-coverage-matrix.csv"
XLSX_OUT = ROOT / "03-analysis" / "government-savings-coverage-matrix.xlsx"
DOCX_OUT = ROOT / "04-leadership" / "Government-Savings-Automation-Coverage-Assessment.docx"
REPORT_DATE = "July 20, 2026"

NAVY = "003057"
TEAL = "007A8C"
WHITE = "FFFFFF"
LIGHT_BG = "E8EEF4"
GREEN_BG = "E8F5E9"
AMBER_BG = "FFF3E0"


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return reader.fieldnames or [], rows


def style_header_row(ws, row_idx: int = 1) -> None:
    fill = PatternFill("solid", fgColor=NAVY)
    font = Font(bold=True, color=WHITE, name="Calibri", size=10)
    for cell in ws[row_idx]:
        cell.fill = fill
        cell.font = font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)


def auto_width(ws, max_width: int = 45) -> None:
    for col in ws.columns:
        letter = get_column_letter(col[0].column)
        length = max(len(str(c.value or "")) for c in col)
        ws.column_dimensions[letter].width = min(max(length + 2, 10), max_width)


def build_xlsx() -> None:
    wb = Workbook()

    # --- Summary sheet ---
    ws_sum = wb.active
    ws_sum.title = "Executive Summary"
    ws_sum["A1"] = "Government Savings — Automation Coverage Summary"
    ws_sum["A1"].font = Font(bold=True, size=14, color=NAVY, name="Calibri")
    ws_sum["A2"] = f"Assessment date: {REPORT_DATE}"
    ws_sum.merge_cells("A1:F1")

    summary_headers = ["GS Area", "Verified Metric", "Percentage / Count", "Denominator Basis", "CI Scheduled", "Confidence"]
    summary_data = [
        ["V3 / Universal Experience UI", "Scoped TestNG methods", "86.9%", "379 of 436 nightly methods", "Yes — GitLab", "High"],
        ["V2 UI (UP-scoped)", "qTest cases mapped", "36.0%", "268 of 744 qTest population", "Jenkins/Ant — TBD", "High"],
        ["Mobile 2 MSC API", "Documented endpoints", "100%", "24 of 24 in-scope endpoints", "No — QA-1405 pending", "High"],
        ["Mobile 1 MSC API", "Documented endpoints", "22.2%", "6 of 27 endpoints", "No", "High"],
        ["UP API operations", "HTTP operations", "11 ops", "UP operation catalog", "Partial — metadataweb", "High"],
        ["UP performance", "Business journeys", "15 journeys", "UP perf ledger", "IDP scheduled", "Medium"],
        ["V2 full UI corpus", "Cucumber scenarios", "2,176 scenarios", "TBD business scope", "TBD", "Medium"],
        ["ASTRO UI", "Cucumber scenarios", "1,236 scenarios", "TBD", "Not verified", "Medium"],
        ["COPACS", "—", "TBD", "Not identified", "No", "Low"],
    ]
    start = 4
    for c, h in enumerate(summary_headers, 1):
        ws_sum.cell(row=start, column=c, value=h)
    style_header_row(ws_sum, start)
    for r, row in enumerate(summary_data, start + 1):
        for c, val in enumerate(row, 1):
            cell = ws_sum.cell(row=r, column=c, value=val)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            if c == 3 and "%" in str(val):
                cell.fill = PatternFill("solid", fgColor=GREEN_BG if float(val.strip("%")) >= 80 else AMBER_BG)

    # Chart
    chart_row = start + len(summary_data) + 3
    ws_sum.cell(row=chart_row, column=1, value="Verified % (where applicable)")
    pct_rows = [
        ("V3 UI inventory", 86.9),
        ("V2 UP inventory", 36.0),
        ("Mobile 2 API", 100.0),
        ("Mobile 1 API", 22.2),
    ]
    for i, (label, pct) in enumerate(pct_rows, chart_row + 1):
        ws_sum.cell(row=i, column=1, value=label)
        ws_sum.cell(row=i, column=2, value=pct)

    chart = BarChart()
    chart.type = "col"
    chart.title = "Verified Coverage Metrics (%)"
    chart.y_axis.title = "Percent"
    chart.x_axis.title = "Area"
    data = Reference(ws_sum, min_col=2, min_row=chart_row + 1, max_row=chart_row + len(pct_rows))
    cats = Reference(ws_sum, min_col=1, min_row=chart_row + 1, max_row=chart_row + len(pct_rows))
    chart.add_data(data, titles_from_data=False)
    chart.set_categories(cats)
    chart.height = 10
    chart.width = 18
    ws_sum.add_chart(chart, f"D{chart_row}")

    auto_width(ws_sum)

    # --- Full matrix sheet ---
    headers, rows = load_csv(MATRIX_CSV)
    ws = wb.create_sheet("Coverage Matrix")
    for c, h in enumerate(headers, 1):
        ws.cell(row=1, column=c, value=h)
    style_header_row(ws, 1)
    thin = Side(style="thin", color="CCCCCC")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for r, row in enumerate(rows, 2):
        for c, h in enumerate(headers, 1):
            cell = ws.cell(row=r, column=c, value=row.get(h, ""))
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = border
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(rows)+1}"
    auto_width(ws)

    # --- CI Gates sheet ---
    pipe_csv = ROOT / "01-inventory" / "pipeline-job-inventory.csv"
    ph, pr = load_csv(pipe_csv)
    ws_ci = wb.create_sheet("CI Pipeline Jobs")
    for c, h in enumerate(ph, 1):
        ws_ci.cell(row=1, column=c, value=h)
    style_header_row(ws_ci, 1)
    for r, row in enumerate(pr, 2):
        for c, h in enumerate(ph, 1):
            ws_ci.cell(row=r, column=c, value=row.get(h, "")).alignment = Alignment(wrap_text=True)
    auto_width(ws_ci)

    # --- Categories pivot ---
    ws_cat = wb.create_sheet("By Category")
    ws_cat.append(["Automation Type", "Areas Count", "Avg Verified % (where numeric)"])
    style_header_row(ws_cat, 1)
    type_counts: dict[str, list[float]] = {}
    for row in rows:
        at = row.get("automation_type", "Unknown")
        pct = row.get("verified_pct", "")
        type_counts.setdefault(at, [])
        if pct and pct.endswith("%"):
            try:
                type_counts[at].append(float(pct.replace("%", "")))
            except ValueError:
                pass
    for at, pcts in sorted(type_counts.items()):
        avg = round(sum(pcts) / len(pcts), 1) if pcts else "TBD"
        ws_cat.append([at, len([r for r in rows if r.get("automation_type") == at]), f"{avg}%" if isinstance(avg, float) else avg])
    auto_width(ws_cat)

    wb.save(XLSX_OUT)
    print(f"Wrote {XLSX_OUT}")


def set_docx_header_footer(doc: Document) -> None:
    section = doc.sections[0]
    section.orientation = WD_ORIENT.PORTRAIT
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    header = section.header
    hp = header.paragraphs[0]
    hp.text = "Ascensus Government Savings  |  Automation Coverage Assessment"
    hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for run in hp.runs:
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0x00, 0x30, 0x57)

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = fp.add_run(f"Confidential — Internal Use  |  {REPORT_DATE}  |  Page ")
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x61, 0x61, 0x61)
    # page number field
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    run._r.addnext(fld)


def add_table(doc: Document, headers: list[str], data: list[list[str]]) -> None:
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        for p in hdr[i].paragraphs:
            for r in p.runs:
                r.bold = True
    for row_data in data:
        row = table.add_row().cells
        for i, val in enumerate(row_data):
            row[i].text = str(val)
    doc.add_paragraph()


def build_docx() -> None:
    doc = Document()
    set_docx_header_footer(doc)

    title = doc.add_heading("Government Savings", level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub = doc.add_paragraph("Automation Coverage & CI Integration Assessment")
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.runs[0].bold = True
    sub.runs[0].font.size = Pt(14)
    meta = doc.add_paragraph(f"Assessment Date: {REPORT_DATE}\nPrepared for: Ascensus Leadership")
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_heading("Executive Summary", level=1)
    doc.add_paragraph(
        "Government Savings has meaningful automated coverage across Universal Platform V3 UI (GitLab nightly), "
        "legacy V2 UI (large Jenkins/Ant corpus), MSC Mobile APIs (100% in-scope endpoint automation in code), "
        "metadataweb API (GitLab nightly), and performance assets. A single GS-wide coverage percentage is not "
        "defensible without a unified business denominator. Verified metrics: V3 UI 86.9% inventory share; "
        "V2 UP-scoped 36.0%; Mobile 2 API 100% (24/24 endpoints); Mobile 1 API 22.2% (6/27 endpoints)."
    )

    doc.add_heading("Verified Coverage Snapshot", level=1)
    add_table(
        doc,
        ["Area", "Metric", "Result", "CI Scheduled"],
        [
            ["V3 / UE UI", "TestNG inventory share", "86.9% (379/436)", "Yes — GitLab"],
            ["V2 UI (UP)", "qTest inventory share", "36.0% (268/744)", "Jenkins — TBD"],
            ["Mobile 2 API", "Endpoint automation", "100% (24/24)", "No — QA-1405"],
            ["Mobile 1 API", "Endpoint automation", "22.2% (6/27)", "No"],
            ["UP API", "Operations", "11 automated", "Partial"],
            ["Performance", "Journeys", "15 in-scope", "IDP scheduled"],
        ],
    )

    doc.add_heading("CI/CD Integration", level=1)
    doc.add_paragraph(
        "GitLab: V3 scheduled_regression_job (hard gate) and api-test-automation metadataweb Stage1 nightly. "
        "GitHub Actions: Mobile 2 workflow documented but not in repository. "
        "Jenkins: IDP performance scheduled weekdays; MSC endurance manual; V2/Ant targets exist."
    )

    doc.add_heading("Key Gaps", level=1)
    gaps = [
        "Mobile 2 GitLab nightly not implemented (QA-1405)",
        "Mobile 1 — 21 of 27 endpoints not automated",
        "ASTRO and full V2 backoffice not on V3 GitLab schedule",
        "COPACS — no automation identified",
        "No unified GS denominator for one headline %",
    ]
    for g in gaps:
        doc.add_paragraph(g, style="List Bullet")

    doc.add_heading("Leadership Decisions Required", level=1)
    decisions = [
        "Prioritize Mobile 2 GitLab nightly as MSC API gate",
        "Confirm Mobile 1 sprint scope and target endpoints",
        "Clarify code coverage vs test automation coverage terminology",
        "V2/Jenkins vs V3/GitLab consolidation strategy",
        "COPACS and ASTRO scope ownership",
    ]
    for d in decisions:
        doc.add_paragraph(d, style="List Number")

    doc.add_heading("Roadmap Horizons", level=1)
    add_table(
        doc,
        ["Horizon", "Focus"],
        [
            ["0–30 days", "M2 CI nightly, evidence refresh, M1 sprint, CI inventory"],
            ["30–90 days", "M1 IDP, perf schedule, ASTRO/COPACS scope, qTest mapping"],
            ["90+ days", "Enrollment API, microservice gates, quarterly GS roadmap"],
        ],
    )

    doc.add_paragraph()
    p = doc.add_paragraph(
        "Full detail: qa-automation-kb/government-savings-automation-assessment/ "
        "including Excel matrix and CSV inventories."
    )
    p.runs[0].italic = True

    doc.save(DOCX_OUT)
    print(f"Wrote {DOCX_OUT}")


def main() -> None:
    build_xlsx()
    build_docx()


if __name__ == "__main__":
    main()
