#!/usr/bin/env python3
"""Generate VP-grade leadership briefing DOCX + PPTX — no local repo references."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor
from pptx import Presentation
from pptx.dml.color import RGBColor as PptRGB
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches as PptInches
from pptx.util import Pt as PptPt

ROOT = Path(__file__).resolve().parents[1] / "2026-08-am-squad-leadership-update"
METRICS = ROOT / "data" / "leadership-metrics.json"
CHARTS = ROOT / "assets" / "charts"
DELIVERABLES = ROOT / "deliverables"
DOCX_OUT = DELIVERABLES / "AM-Squad-Leadership-Briefing-Aug2026.docx"
PPTX_OUT = DELIVERABLES / "AM-Squad-Leadership-Update-Aug2026.pptx"

TITLE = "QA Automation — AM Squad Leadership Update"
SUBTITLE = "April – August 2026"
VERSION = "August 2026"

NAVY = RGBColor(0x00, 0x32, 0x41)
TEAL = RGBColor(0x02, 0x6B, 0x84)
PEAK = RGBColor(0x00, 0x9E, 0x86)
GRAY = RGBColor(0x47, 0x55, 0x69)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

PPT_NAVY = PptRGB(0x00, 0x32, 0x41)
PPT_TEAL = PptRGB(0x05, 0xA2, 0xC6)
PPT_PEAK = PptRGB(0x00, 0x9E, 0x86)
PPT_WHITE = PptRGB(0xFF, 0xFF, 0xFF)
PPT_TEXT = PptRGB(0x1E, 0x29, 0x3B)
PPT_MUTED = PptRGB(0x64, 0x74, 0x8B)

REFS = [
    ("Jira — QA Automation project", "https://ascensuscollegesavings.atlassian.net/jira/software/projects/QA"),
    ("GitLab — api-test-automation", "https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation"),
    ("GitLab — unite-test-automation (V2)", "https://gitlab.com/ascensus-gs/products/depot/qa-automation/automation"),
    ("GitLab — prime-test-automation (V3)", "https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation"),
    ("qTest — Automation Unite", "https://ascensus.qtestnet.com"),
    ("Jenkins — QA performance & nightly regression", "jenkinsqant1 (internal QA Jenkins)"),
]


def load_metrics() -> dict:
    with METRICS.open(encoding="utf-8") as f:
        return json.load(f)


# ── DOCX helpers ──────────────────────────────────────────────────────────────

def set_cell_shading(cell, fill_hex: str) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill_hex)
    shd.set(qn("w:val"), "clear")
    tc_pr.append(shd)


def add_toc(doc: Document) -> None:
    doc.add_heading("Table of Contents", 1)
    p = doc.add_paragraph()
    run = p.add_run()
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = 'TOC \\o "1-3" \\h \\z \\u'
    fld_sep = OxmlElement("w:fldChar")
    fld_sep.set(qn("w:fldCharType"), "separate")
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_begin)
    run._r.append(instr)
    run._r.append(fld_sep)
    run._r.append(fld_end)
    note = doc.add_paragraph("Right-click Table of Contents → Update Field in Word to refresh page numbers.")
    note.runs[0].italic = True
    note.runs[0].font.size = Pt(9)
    note.runs[0].font.color.rgb = GRAY
    doc.add_page_break()


def add_header_footer(doc: Document) -> None:
    for section in doc.sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.2)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)
        header = section.header
        hp = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
        hp.text = f"{TITLE}  |  {VERSION}"
        hp.runs[0].font.size = Pt(8)
        hp.runs[0].font.color.rgb = GRAY
        footer = section.footer
        fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = fp.add_run(f"QA Automation AM Squad  ·  {SUBTITLE}  ·  Page ")
        run.font.size = Pt(8)
        run.font.color.rgb = GRAY
        fld = OxmlElement("w:fldChar")
        fld.set(qn("w:fldCharType"), "begin")
        instr = OxmlElement("w:instrText")
        instr.text = "PAGE"
        fld2 = OxmlElement("w:fldChar")
        fld2.set(qn("w:fldCharType"), "end")
        run2 = fp.add_run()
        run2._r.append(fld)
        run2._r.append(instr)
        run2._r.append(fld2)


def add_scorecard_table(doc: Document, m: dict) -> None:
    sc = m["scorecard"]
    j = m["jira"]["totals"]
    rows = [
        ("GitLab merges to main", str(sc["gitlab_merges"]), "GitLab MR export Apr–Aug 2026"),
        ("Jira story points delivered", str(j["story_points"]), "Sprints 26.04–26.12"),
        ("Jira work items closed", str(j["work_items_in_sprints"]), "Stories, tasks, spikes"),
        ("Automation bugs found", str(j["automation_bugs_logged"]), "Logged via automation triage"),
        ("V2 nightly test methods", str(sc["v2_nightly_methods"]), "Stage1 Jenkins nightly"),
        ("V3 nightly test methods", str(sc["v3_nightly_methods"]), "GitLab nightly Aug 4 snapshot"),
        ("Performance test cases", str(sc["perf_test_cases"]), "Transaction labels × plan permutations"),
        ("MSC Mobile 2 endpoints", sc["msc_m2_endpoints"], "100% business scope"),
        ("MSC Mobile 1 core endpoints", sc["msc_m1_core"], "Excludes optional health/docs"),
        ("Release automation", f"~{sc['release_automation_pct']}%", "Was 17 FTE → 2 FTE equivalent"),
        ("Perf regression scenarios", str(sc["perf_test_cases"]), "Transaction labels × plans"),
    ]
    table = doc.add_table(rows=1, cols=3)
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    for i, label in enumerate(["Metric", "Value", "Notes"]):
        hdr[i].text = label
        set_cell_shading(hdr[i], "003241")
        hdr[i].paragraphs[0].runs[0].font.color.rgb = WHITE
        hdr[i].paragraphs[0].runs[0].bold = True
    for metric, value, note in rows:
        row = table.add_row().cells
        row[0].text = metric
        row[1].text = value
        row[2].text = note


def add_chart(doc: Document, title: str, chart_name: str) -> None:
    doc.add_heading(title, 2)
    path = CHARTS / chart_name
    if path.exists():
        doc.add_picture(str(path), width=Inches(6.2))
    else:
        doc.add_paragraph(f"[Chart: {chart_name}]")


def build_docx(m: dict) -> None:
    DELIVERABLES.mkdir(parents=True, exist_ok=True)
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Segoe UI"
    style.font.size = Pt(11)

    # Cover
    for _ in range(6):
        doc.add_paragraph()
    cover = doc.add_paragraph(TITLE)
    cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover.runs[0].font.size = Pt(28)
    cover.runs[0].font.bold = True
    cover.runs[0].font.color.rgb = NAVY
    sub = doc.add_paragraph(SUBTITLE)
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.runs[0].font.size = Pt(16)
    sub.runs[0].font.color.rgb = TEAL
    org = doc.add_paragraph("QA Automation — AM Squad")
    org.alignment = WD_ALIGN_PARAGRAPH.CENTER
    org.runs[0].font.size = Pt(12)
    org.runs[0].font.color.rgb = GRAY
    doc.add_page_break()

    add_header_footer(doc)
    add_toc(doc)

    # 1 Executive summary
    doc.add_heading("1. Executive Summary", 1)
    doc.add_paragraph(
        "The QA Automation AM Squad operates across six parallel channels — V2 Legacy UI, V3 Universal "
        "Platform, API/Unite MSC, performance testing, pipeline/CI integration, and department-wide standards. "
        "Delivery metrics alone understate impact: framework architecture, AI-accelerated migration, "
        "cross-team emergency support, and release-cycle transformation represent the majority of business value."
    )
    add_scorecard_table(doc, m)

    # 2 Delivery velocity
    doc.add_heading("2. Delivery Velocity", 1)
    doc.add_paragraph(
        "GitLab merge activity peaked in June–July 2026 during the Unite MSC API sprint."
    )
    add_chart(doc, "GitLab merges by repository", "01-gitlab-mrs-by-month.png")
    add_chart(doc, "Monthly automation test cases added", "08-monthly-automation-test-cases-added.png")

    # 3 Jira
    doc.add_heading("3. Jira Sprint Delivery", 1)
    j = m["jira"]
    doc.add_paragraph(
        f"Across AMSQUAD Sprints 26.04 through 26.12, the squad closed {j['totals']['work_items_in_sprints']} "
        f"work items totaling {j['totals']['story_points']:.0f} story points. "
        f"{j['totals']['automation_bugs_logged']} automation-discovered defects were logged for triage."
    )
    add_chart(doc, "Story points by sprint", "09-jira-story-points-by-sprint.png")
    add_chart(doc, "Automation bugs by sprint", "10-jira-automation-bugs-by-sprint.png")

    sprint_table = doc.add_table(rows=1, cols=6)
    sprint_table.style = "Table Grid"
    hdr = ["Sprint", "Work Items", "Stories", "Spikes", "Bugs", "Story Points"]
    for i, h in enumerate(hdr):
        sprint_table.rows[0].cells[i].text = h
        set_cell_shading(sprint_table.rows[0].cells[i], "026B84")
        sprint_table.rows[0].cells[i].paragraphs[0].runs[0].font.color.rgb = WHITE
    for s in j["sprints"]:
        row = sprint_table.add_row().cells
        row[0].text = s["sprint"].replace("AMSQUAD Sprint ", "")
        row[1].text = str(s["work_items"])
        row[2].text = str(s["stories"])
        row[3].text = str(s["spikes"])
        row[4].text = str(s["bugs"])
        row[5].text = f"{s['story_points']:.0f}"

    # 4 V2
    doc.add_heading("4. V2 Legacy UI Automation", 1)
    doc.add_paragraph(
        "V2 runs on Jenkins Stage1 nightly (Mon–Fri). The Aug 4 snapshot shows 592 test methods across "
        "12 modules. CSR maintenance modules (fee entry, contributions, authorize agent) were added Apr–Jul. "
        "CSR Actions suite adds 33 additional scenarios in the next nightly expansion."
    )
    add_chart(doc, "V2 module snapshot", "04-v2-regression-by-module.png")

    # 5 V3
    doc.add_heading("5. V3 Universal Platform", 1)
    v3 = m["v3_snapshot"]
    doc.add_paragraph(
        f"V3 GitLab nightly regression runs {v3['total_methods']} test methods across "
        f"{len(v3['modules'])} modules (Aug 4 snapshot). Universal Enrollment (303), "
        f"IDP Login (56), Contributions (36), Withdrawals (20), and more."
    )
    add_chart(doc, "V3 module snapshot", "11-v3-regression-by-module.png")

    # 6 API MSC
    doc.add_heading("6. API / Unite MSC", 1)
    doc.add_paragraph(
        "Mobile 2 API automation is complete at 25/25 endpoints. "
        "Mobile 1 is at ~25/29 core endpoints. The project was rescued using AI-assisted migration delivering "
        "~50% schedule compression versus the original ETA."
    )
    add_chart(doc, "MSC endpoint coverage", "05-unite-msc-coverage.png")
    add_chart(doc, "API module snapshot", "13-api-regression-by-module.png")

    # 7 Performance
    doc.add_heading("7. Performance Testing", 1)
    doc.add_paragraph(
        f"Performance automation inventory: {m['perf_inventory']['total_test_cases']} test cases "
        "(business transaction labels × plan permutations). Covers IDP login, auth delay, "
        "forgot username/password, legacy login, MSC endurance, barcode, and pipeline API profiles."
    )
    add_chart(doc, "Performance test case inventory", "12-perf-test-case-inventory.png")

    # 8 Beyond metrics
    doc.add_heading("8. Value Beyond Tracked Metrics", 1)
    beyond = [
        "Framework architecture and canonical repo structure (API, perf, UI)",
        "AI-accelerated documentation, Postman collections, and TestNG boilerplate",
        "qTest master suite design and department-wide enforcement",
        "Automation bug lifecycle standard (triage → JIRA → leadership notification)",
        "Pipeline/DevOps co-design (hub workflow, module switches, GHA/Nexus)",
        "Cross-team emergency support (Empower, barcode, JEA proxy validation)",
        "Release support and regression triage (V2 + V3 + perf daily)",
        "Technical debt cleanup and standards documentation",
    ]
    for item in beyond:
        doc.add_paragraph(item, style="List Bullet")
    add_chart(doc, "Investment allocation", "06-work-allocation-index.png")
    add_chart(doc, "Release automation impact", "07-release-automation-impact.png")

    # 9 Roadmap & asks
    doc.add_heading("9. Roadmap & Leadership Asks", 1)
    doc.add_paragraph("Q3–Q4 priorities:", style="List Bullet")
    priorities = [
        "Mobile 2 GitLab nightly scheduling (QA-1405)",
        "Mobile 1 master suite completion",
        "MSC enrollment API automation",
        "CSR Actions Jenkins nightly expansion",
        "Automated monthly leadership dashboard",
    ]
    for p in priorities:
        doc.add_paragraph(p, style="List Bullet 2")
    doc.add_paragraph(
        "Leadership asks: (1) involve AM Squad at SDLC start for roadmap visibility, not end-of-sprint "
        "emergency; (2) administrative capacity to free technical lead for architecture and AI tooling."
    )

    # 10 References
    doc.add_heading("10. References & Evidence Sources", 1)
    for label, url in REFS:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(f"{label}: ")
        r.bold = True
        p.add_run(url)

    doc.add_paragraph(
        f"\nDocument generated {datetime.now().strftime('%B %d, %Y')}. "
        "Metrics sourced from GitLab MR export, Jira AMSQUAD sprint export, qTest execution export, "
        "and Jenkins nightly regression snapshots."
    )
    doc.save(DOCX_OUT)
    print(f"Wrote {DOCX_OUT}")


# ── PPTX helpers ──────────────────────────────────────────────────────────────

def slide_title(prs: Presentation, title: str, subtitle: str = "") -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.shapes.add_shape(1, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = PPT_NAVY
    bg.line.fill.background()
    tb = slide.shapes.add_textbox(PptInches(0.55), PptInches(2.4), PptInches(9), PptInches(1.2))
    p = tb.text_frame.paragraphs[0]
    p.text = title
    p.font.size = PptPt(32)
    p.font.bold = True
    p.font.color.rgb = PPT_WHITE
    if subtitle:
        sb = slide.shapes.add_textbox(PptInches(0.55), PptInches(3.6), PptInches(9), PptInches(0.8))
        sp = sb.text_frame.paragraphs[0]
        sp.text = subtitle
        sp.font.size = PptPt(16)
        sp.font.color.rgb = PPT_TEAL


def slide_section(prs: Presentation, title: str) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect = slide.shapes.add_shape(1, 0, 0, PptInches(0.35), prs.slide_height)
    rect.fill.solid()
    rect.fill.fore_color.rgb = PPT_PEAK
    rect.line.fill.background()
    tb = slide.shapes.add_textbox(PptInches(0.7), PptInches(3.0), PptInches(8.5), PptInches(1))
    p = tb.text_frame.paragraphs[0]
    p.text = title
    p.font.size = PptPt(36)
    p.font.bold = True
    p.font.color.rgb = PPT_NAVY


def slide_bullets(prs: Presentation, title: str, bullets: list[str], note: str = "") -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    tb = slide.shapes.add_textbox(PptInches(0.45), PptInches(0.3), PptInches(9.1), PptInches(0.75))
    tp = tb.text_frame.paragraphs[0]
    tp.text = title
    tp.font.size = PptPt(26)
    tp.font.bold = True
    tp.font.color.rgb = PPT_NAVY
    bar = slide.shapes.add_shape(1, PptInches(0.45), PptInches(1.05), PptInches(1.2), PptInches(0.06))
    bar.fill.solid()
    bar.fill.fore_color.rgb = PPT_PEAK
    bar.line.fill.background()
    body = slide.shapes.add_textbox(PptInches(0.55), PptInches(1.25), PptInches(8.9), PptInches(5.5))
    tf = body.text_frame
    tf.word_wrap = True
    for i, bullet in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = bullet
        p.font.size = PptPt(15)
        p.font.color.rgb = PPT_TEXT
        p.space_after = PptPt(6)
    if note:
        nb = slide.shapes.add_textbox(PptInches(0.45), PptInches(6.6), PptInches(9), PptInches(0.5))
        np = nb.text_frame.paragraphs[0]
        np.text = note
        np.font.size = PptPt(10)
        np.font.italic = True
        np.font.color.rgb = PPT_MUTED


def slide_chart(prs: Presentation, title: str, chart: str) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    tb = slide.shapes.add_textbox(PptInches(0.45), PptInches(0.25), PptInches(9), PptInches(0.65))
    tp = tb.text_frame.paragraphs[0]
    tp.text = title
    tp.font.size = PptPt(22)
    tp.font.bold = True
    tp.font.color.rgb = PPT_NAVY
    path = CHARTS / chart
    if path.exists():
        slide.shapes.add_picture(str(path), PptInches(0.35), PptInches(0.95), width=PptInches(9.3))


def build_pptx(m: dict) -> None:
    sc = m["scorecard"]
    j = m["jira"]["totals"]
    prs = Presentation()
    prs.slide_width = PptInches(10)
    prs.slide_height = PptInches(7.5)

    slide_title(prs, "QA Automation — AM Squad", f"Leadership Update · {SUBTITLE}")

    slide_bullets(prs, "Executive headline", [
        f"{sc['gitlab_merges']} merged changes to main across 3 automation repositories",
        f"{j['story_points']:.0f} Jira story points · {j['work_items_in_sprints']} work items · {j['automation_bugs_logged']} bugs found",
        f"~{sc['release_automation_pct']}% of monthly release validations automated (17 FTE → 2 FTE)",
        "Unite MSC rescued — Mobile 2 at 25/25 endpoints, ~50% ETA savings",
        "Six parallel tracks: V2 · V3 · API/MSC · Perf · Pipeline · Standards",
    ])

    slide_bullets(prs, "Scorecard", [
        f"V2 Legacy UI: {sc['v2_nightly_methods']} nightly test methods (Stage1)",
        f"V3 Universal Platform: {sc['v3_nightly_methods']} nightly test methods",
        f"API / Unite MSC: M2 {sc['msc_m2_endpoints']} · M1 {sc['msc_m1_core']}",
        f"Performance: {sc['perf_test_cases']} test cases in inventory",
        "Pipeline: enrollment + metadata in hub; MSC GHA vertical slice",
    ])

    slide_chart(prs, "GitLab merges by repository", "01-gitlab-mrs-by-month.png")
    slide_chart(prs, "Monthly automation test cases added", "08-monthly-automation-test-cases-added.png")

    slide_bullets(prs, "Beyond the metrics — additional value delivered", [
        "Framework architecture & canonical repo design",
        "AI-accelerated docs, Postman, TestNG boilerplate",
        "qTest master suite & automation bug lifecycle standard",
        "Pipeline/DevOps co-design & module switches",
        "Cross-team emergency support & release triage",
        "Technical debt cleanup & department standards",
    ], note="These investments are not fully captured in merge or test-count metrics.")

    slide_chart(prs, "Jira sprint delivery — story points", "09-jira-story-points-by-sprint.png")
    slide_chart(prs, "Automation defects discovered", "10-jira-automation-bugs-by-sprint.png")

    # V2 section
    slide_section(prs, "V2 Legacy UI Automation")
    slide_bullets(prs, "V2 — Overview", [
        "Jenkins Stage1 nightly: Mon–Fri regression",
        f"{sc['v2_nightly_methods']} test methods across 12 modules (Aug 4 snapshot)",
        "CSR modules added: fee entry, contributions, authorize agent, security questions",
        "+33 CSR Actions scenarios ready for next nightly expansion",
    ])
    slide_chart(prs, "V2 — Module pass/fail snapshot", "04-v2-regression-by-module.png")
    slide_bullets(prs, "V2 — Business value", [
        "Core member journeys covered nightly before release",
        "CSR maintenance gaps closed — high-risk flows now automated",
        "Enrollments/login triage active — separates env vs product defects",
    ])

    # V3 section
    slide_section(prs, "V3 Universal Platform")
    slide_bullets(prs, "V3 — Overview", [
        f"{sc['v3_nightly_methods']} test methods in GitLab nightly (Aug 4 snapshot)",
        "Modules: Universal Enrollment (303), IDP Login (56), Contributions (36), Withdrawals (20)",
        "Entity platform suites expanding on separate track",
        "GitLab CI scheduled regression operational",
    ])
    slide_chart(prs, "V3 — Module pass/fail snapshot", "11-v3-regression-by-module.png")
    slide_bullets(prs, "V3 — Delivery highlights", [
        "Entity registration/login suites expanded",
        "IDP open-account (MIB) and member withdrawal regression",
        "Flaky-test stabilization and web registration flows",
        "Stage 5 smoke suites for UE + IDP",
    ])
    slide_bullets(prs, "V3 — Next steps", [
        "Entity platform nightly expansion",
        "Additional universal API modules in GitLab schedule",
    ])

    # API section
    slide_section(prs, "API / Unite MSC")
    slide_bullets(prs, "MSC — Problem & solution", [
        "Legacy Cucumber tied to monolith, no Postman baseline, past ETA",
        "Canonical TestNG framework in api-test-automation/mobile/",
        "AI agents for docs, Postman, data utils, migration stubs",
        "Delivered in ~50% of original ETA",
    ])
    slide_chart(prs, "MSC — Endpoint coverage", "05-unite-msc-coverage.png")
    slide_chart(prs, "API — Module coverage snapshot", "13-api-regression-by-module.png")
    slide_bullets(prs, "MSC — Status", [
        "M2: 25/25 endpoints (100%) — sign-off ready",
        "M1: ~25/29 core (~86%) — master suite in progress",
        "Branding: OKD (non-IDP) · NYD/NMD (IDP)",
        "P0: GitLab nightly scheduling (QA-1405)",
    ])

    # Perf section
    slide_section(prs, "Performance Testing")
    slide_bullets(prs, "Performance — Regression suite", [
        f"{sc['perf_test_cases']} performance test cases in inventory",
        "IDP login: 15 transaction labels × 7 plans",
        "Auth delay, forgot username/password, legacy login",
        "MSC non-IDP + IDP login endurance profiles",
    ])
    slide_chart(prs, "Performance — Test case inventory", "12-perf-test-case-inventory.png")
    slide_bullets(prs, "Performance — Emergency delivery", [
        "Barcode SYN-443: full perf cycle in ~1 week",
        "JEA/Jahia proxy patch validation scripts",
        "Department perf DoD and BlazeMeter reporting standard",
    ])
    slide_bullets(prs, "Performance — Value", [
        "Repeatable baselines — no manual re-run each release",
        "Evidence for platform team pre/post patch comparison",
    ])

    slide_chart(prs, "Investment allocation", "06-work-allocation-index.png")
    slide_chart(prs, "Release automation impact", "07-release-automation-impact.png")

    slide_bullets(prs, "AI acceleration", [
        "MSC migration agents — Postman, docs, TestNG boilerplate",
        "Automation bug lifecycle — Cursor skill + standardized reporting",
        "Chart & metrics generators — reproducible leadership packs",
        "Coverage intelligence foundation for monthly dashboard",
    ])

    slide_bullets(prs, "Roadmap Q3–Q4 2026", [
        "P0: MSC GitLab nightly · M1 master suite",
        "P1: MSC enrollment API · CSR Actions nightly expansion",
        "P2: Entity V3 nightly · automated monthly dashboard",
        "Engage squad at SDLC start → proven ETA track record",
    ])

    slide_bullets(prs, "Leadership asks", [
        "Roadmap visibility — AM Squad at SDLC start, not sign-off deadline",
        "Administrative capacity — free lead for architecture & AI tooling",
        "Recommended: 30-minute live walkthrough (framework + pipeline + qTest)",
    ])

    slide_bullets(prs, "References", [f"{label}: {url}" for label, url in REFS])

    slide_title(prs, "QA Automation AM Squad", "Delivering across six automation channels")

    prs.save(PPTX_OUT)
    print(f"Wrote {PPTX_OUT}")


def main() -> None:
    for old in (DOCX_OUT, PPTX_OUT):
        if old.exists():
            old.unlink()
    m = load_metrics()
    build_pptx(m)
    build_docx(m)


if __name__ == "__main__":
    main()
