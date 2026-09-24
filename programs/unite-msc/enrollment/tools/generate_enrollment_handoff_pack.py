#!/usr/bin/env python3
"""Generate Enrollment QA-893 Word handover pack (KB only — not api-test-automation)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import matplotlib.pyplot as plt
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "deliverables"
ASSETS = ROOT / "deliverables" / "_assets"

SIGNOFF_DATE = date.today().strftime("%B %d, %Y")
NAVY = RGBColor(0x00, 0x30, 0x57)
TEAL = RGBColor(0x00, 0x7A, 0x8C)
GREEN = RGBColor(0x2E, 0x7D, 0x32)
GRAY = RGBColor(0x61, 0x61, 0x61)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_BG = "E8EEF4"
GREEN_BG = "E8F5E9"
AMBER_BG = "FFF3E0"
RED_BG = "FFEBEE"

ENDPOINTS = [
    ("ENR-01", "GET", "/enrollmentapi/health/liveness", "Smoke", "EnrollmentPingRequestTest", "Done", "okdirect"),
    ("ENR-02", "GET", "/enrollmentapi/v1/ping", "Smoke", "EnrollmentPingRequestTest", "Done", "okdirect"),
    ("ENR-03", "GET", "/enrollmentapi/v1/certificate", "Smoke", "EnrollmentCertificateRequestTest", "Done", "okdirect"),
    ("ENR-04", "GET", "/enrollmentapi/v1/usstates", "Smoke", "EnrollmentUsStatesRequestTest", "Done", "okdirect"),
    ("ENR-05", "GET", "/enrollmentapi/v1/country", "Smoke", "EnrollmentCountryRequestTest", "Done", "okdirect"),
    ("ENR-06", "GET", "/enrollmentapi/v1/plans", "Smoke", "EnrollmentPlansRequestTest", "Done", "okdirect"),
    ("ENR-07", "GET", "/enrollmentapi/v1/plans/{planId}", "Smoke", "EnrollmentPlansRequestTest", "Done", "okdirect"),
    ("ENR-08", "GET", "/enrollmentapi/v1/content", "Wizard", "EnrollmentContentRequestTest", "Done", "okdirect+newyork"),
    ("ENR-09", "POST", "/mobile1api/v1/mobilemembersession", "Optional", "MobileMemberSessionRequestTest", "Done (smoke group)", "okdirect"),
    ("ENR-10", "POST", ".../enrollmentstarted", "Wizard", "EnrollmentStartedRequestTest", "Done", "okdirect+newyork"),
    ("ENR-11", "POST", ".../prospects", "Wizard", "ProspectRequestTest", "Done", "okdirect+newyork"),
    ("ENR-12", "POST", ".../owner-entered", "Wizard", "OwnerEnteredTests", "Done", "okdirect+newyork"),
    ("ENR-13", "POST", ".../owner-address-entered", "Wizard", "OwnerAddressEnteredRequestTest", "Done", "okdirect+newyork"),
    ("ENR-14", "POST", ".../beneficiary-entered", "Wizard", "BeneficiaryEnteredTests", "Done", "okdirect+newyork"),
    ("ENR-15", "POST", ".../verify/routingnumber", "Wizard", "VerifyBankRoutingNumberRequestTest", "Done", "okdirect+newyork"),
    ("ENR-16", "POST", ".../bank-entered", "Wizard", "BankEnteredRequestTests", "Done", "okdirect+newyork"),
    ("ENR-17", "POST", ".../recurring-contribution-entered", "Wizard", "RecurringContributionEnteredRequestTest", "Done", "okdirect+newyork"),
    ("ENR-18", "POST", ".../enrollmentallocationfunds/get", "Wizard", "AllocationFundRequestTest", "Done", "okdirect+newyork"),
    ("ENR-19", "POST", ".../allocations-entered", "Wizard", "AllocationsEnteredRequestTests", "Done", "okdirect+newyork"),
    ("ENR-20", "POST", ".../review-confirm-entered", "Wizard", "ReviewConfirmEnteredRequestTest", "Done", "okdirect+newyork"),
    ("ENR-21", "GET", ".../subsequentenrollment/banks", "Subsequent", "SubsequentEnrollmentBanksRequestTest", "Done", "okdirect+newyork"),
    ("ENR-22", "POST", ".../subsequent.../beneficiary-entered", "Subsequent", "SubsequentBeneficiaryEnteredRequestTest", "Done", "okdirect+newyork"),
    ("ENR-23", "POST", ".../subsequent.../bank-entered", "Subsequent", "SubsequentEnrollmentBankEnteredRequestTest", "Done", "okdirect+newyork"),
    ("ENR-24", "POST", ".../subsequent.../recurring-contribution", "Subsequent", "SubsequentEnrollmentRecurringContributionRequestTest", "Done", "okdirect+newyork"),
    ("ENR-25", "POST", ".../subsequent.../review-confirm-entered", "Subsequent", "SubsequentEnrollmentReviewConfirmEnteredRequestTest", "Done", "okdirect+newyork"),
    ("ENR-26", "POST", ".../enrollments/submit", "Partner", "—", "Deferred QA-1808", "—"),
    ("ENR-27", "GET", ".../upromiseaccount", "Partner", "—", "Deferred QA-1807", "—"),
    ("ENR-28", "POST", ".../oauth/token", "Partner", "—", "Deferred", "—"),
]


def shade_cell(cell, hex_color: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tc_pr.append(shd)


def set_run_font(run, size=11, bold=False, color=None, name="Calibri"):
    run.font.size = Pt(size)
    run.bold = bold
    run.font.name = name
    if color:
        run.font.color.rgb = color


def set_cell_text(cell, text: str, bold: bool = False, color: RGBColor | None = None, size: int = 9) -> None:
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(str(text))
    set_run_font(run, size=size, bold=bold, color=color or GRAY)


def style_header_row(row) -> None:
    for cell in row.cells:
        shade_cell(cell, "003057")
        for p in cell.paragraphs:
            for run in p.runs:
                set_run_font(run, size=9, bold=True, color=WHITE)


def setup_doc(doc: Document, header: str) -> None:
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.font.color.rgb = GRAY
    pf = style.paragraph_format
    pf.space_after = Pt(8)
    pf.space_before = Pt(0)
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    section = doc.sections[0]
    section.top_margin = Cm(2.2)
    section.bottom_margin = Cm(2.2)
    section.left_margin = Cm(2.4)
    section.right_margin = Cm(2.4)
    hp = section.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = hp.add_run(header + "  |  Internal  |  QA-893")
    set_run_font(r, size=8, color=GRAY)
    fp = section.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r2 = fp.add_run(f"QA Automation AMSQUAD  ·  {SIGNOFF_DATE}  ·  No credentials")
    set_run_font(r2, size=8, color=GRAY)
    pp = section.footer.add_paragraph()
    pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pr = pp.add_run("Page ")
    set_run_font(pr, size=8, color=GRAY)
    fld1 = OxmlElement("w:fldChar")
    fld1.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    fld2 = OxmlElement("w:fldChar")
    fld2.set(qn("w:fldCharType"), "end")
    pr2 = pp.add_run()
    pr2._r.append(fld1)
    pr2._r.append(instr)
    pr2._r.append(fld2)


def heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = NAVY
        run.font.name = "Calibri"
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(8)


def para(doc, text, size=11, bold=False, color=None, center=False):
    p = doc.add_paragraph()
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    set_run_font(r, size=size, bold=bold, color=color or GRAY)
    return p


def callout(doc, text, bg=GREEN_BG):
    table = doc.add_table(rows=1, cols=1)
    cell = table.rows[0].cells[0]
    shade_cell(cell, bg)
    set_cell_text(cell, text, bold=True, color=NAVY, size=11)
    for p in cell.paragraphs:
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(10)
        p.paragraph_format.line_spacing = 1.15
    doc.add_paragraph()


def kv_table(doc, rows, last_green=False):
    t = doc.add_table(rows=len(rows), cols=2)
    t.style = "Table Grid"
    t.autofit = True
    for i, (k, v) in enumerate(rows):
        shade_cell(t.rows[i].cells[0], LIGHT_BG)
        set_cell_text(t.rows[i].cells[0], k, bold=True, color=NAVY, size=10)
        bg = GREEN_BG if last_green and i == len(rows) - 1 else "FFFFFF"
        shade_cell(t.rows[i].cells[1], bg)
        col = GREEN if last_green and i == len(rows) - 1 else GRAY
        set_cell_text(t.rows[i].cells[1], v, bold=(last_green and i == len(rows) - 1), color=col, size=10)
    doc.add_paragraph()
    return t


def grid_table(doc, headers, data, status_col=None):
    t = doc.add_table(rows=1 + len(data), cols=len(headers))
    t.style = "Table Grid"
    for i, h in enumerate(headers):
        set_cell_text(t.rows[0].cells[i], h, bold=True, color=WHITE, size=8)
    style_header_row(t.rows[0])
    for ri, row in enumerate(data, start=1):
        for ci, val in enumerate(row):
            bg = "FFFFFF"
            if status_col is not None and ci == status_col:
                s = str(val).lower()
                if "defer" in s:
                    bg = AMBER_BG
                elif "done" in s:
                    bg = GREEN_BG
            elif ci == 0:
                bg = LIGHT_BG
            shade_cell(t.rows[ri].cells[ci], bg)
            set_cell_text(t.rows[ri].cells[ci], val, size=8, color=NAVY if ci == 0 else GRAY)
    doc.add_paragraph()


def cover(doc, title, subtitle, status, status_color):
    for _ in range(3):
        doc.add_paragraph()
    para(doc, title.upper(), size=26, bold=True, color=NAVY, center=True)
    para(doc, subtitle, size=16, color=TEAL, center=True)
    para(doc, status, size=16, bold=True, color=status_color, center=True)
    para(doc, f"{SIGNOFF_DATE}  ·  QA Automation (AMSQUAD)  ·  QA-893", size=11, color=GRAY, center=True)
    para(doc, "Classification: Internal — handover to engineering and support", size=10, color=GRAY, center=True)
    doc.add_page_break()


def chart():
    ASSETS.mkdir(parents=True, exist_ok=True)
    path = ASSETS / "enrollment_coverage.png"
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    labels = ["Automated (25)", "Deferred partner (3)"]
    values = [25, 3]
    colors = ["#2E7D32", "#E65100"]
    ax.barh(labels, values, color=colors, height=0.45)
    ax.set_title("Enrollment catalog (28 rows)", fontsize=12, fontweight="bold", color="#003057")
    ax.set_xlim(0, 30)
    for y, v in enumerate(values):
        ax.text(v + 0.4, y, str(v), va="center", color="#334155")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    return path


def save(doc, name):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    doc.save(path)
    print(f"Created {path}")


def doc_index():
    doc = Document()
    setup_doc(doc, "Enrollment API  ·  Documentation index")
    cover(doc, "Enrollment API", "Documentation index for support onboarding", "PACKAGE COMPLETE", GREEN)
    heading(doc, "1. Purpose")
    para(doc, "Single index for Unite MSC Enrollment API automation handoff. Code lives in GitLab api-test-automation. Published documentation lives on the SharePoint API Testing Documentation Hub.")
    heading(doc, "2. Document control")
    kv_table(doc, [
        ("Jira", "QA-893 (subtasks QA-2039–QA-2047)"),
        ("Epic", "QA-796"),
        ("Code repo", "gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation"),
        ("Module", "mobile/enrollment"),
        ("Published docs", "SharePoint API Testing Documentation Hub"),
    ])
    heading(doc, "3. Pack contents")
    grid_table(doc, ["Document", "Audience", "Subtask"], [
        ["Architecture, setup, environments", "Engineers onboarding", "QA-2040"],
        ["Execution and troubleshooting", "Anyone running suites", "QA-2041"],
        ["Reporting and triage", "On-call / lead", "QA-2042"],
        ["Sign-off and coverage matrix", "ACM / leadership", "QA-2043"],
        ["Post DB-refresh checklist", "Ops after refresh", "QA-2044"],
        ["AI scenario guide", "Engineers adding cases", "QA-2046"],
        ["Secrets + independent review", "Second reviewer", "QA-2045 / 2047"],
    ])
    heading(doc, "4. SharePoint")
    para(doc, "Publish only: Home, How to run, Sign-off, After DB refresh. Attach Word files. Do not upload host properties or Postman environments with secrets.")
    save(doc, "Enrollment-API-Documentation-Index.docx")


def doc_setup():
    doc = Document()
    setup_doc(doc, "Enrollment API  ·  Architecture and setup")
    cover(doc, "Architecture, setup, environments", "Local machine through Stage1 and QC4", "GUIDE", TEAL)
    heading(doc, "1. Stack")
    kv_table(doc, [
        ("Language / build", "Java 17 · Maven 3.9+"),
        ("Tests", "TestNG · Rest Assured · EnrollmentBaseTest"),
        ("Not used", "Cucumber (legacy UniteMSC archived)"),
        ("Encryption", "Required on POST for Stage1 and QC4"),
    ])
    heading(doc, "2. First-time setup")
    for b in [
        "Clone api-test-automation. Do not clone this KB as the test runtime.",
        "mvn -f mobile/pom.xml clean install -DskipTests",
        "Create gitignored host file: mobile/enrollment/src/test/resources/config/<COMPUTERNAME>.properties",
        "Point enrollment URI at unite-bff-cloud (not WTN).",
    ]:
        doc.add_paragraph(b, style="List Number")
    heading(doc, "3. Environments")
    grid_table(doc, ["Env", "Enrollment host pattern", "DB", "Use"], [
        ["Stage1", "unite-bff-cloud.stage1.unite529.com", "Tunnel localhost:41521 typical", "Regression"],
        ["QC4", "unite-bff-cloud.qc4.unite529.com", "qc4.properties Oracle", "Integration"],
        ["Plan-branded", "okd.stage1.acs529.com (example)", "Same plant DB rules", "Plant-specific"],
    ])
    heading(doc, "4. Auth and secrets")
    callout(doc, "Never commit JWT, SSN, passwords, or host property files. Prospect JWT is runtime-only.", AMBER_BG)
    para(doc, "GET /enrollmentapi/v1/certificate then encrypt plaintext with jsonapi-encryption Runner (-m encrypt -e stage -s enrollment).")
    heading(doc, "5. Test data")
    para(doc, "SQL under mobile/enrollment/src/test/resources/sql/mobile.sql. Automation accounts use QAAUTOTEST% style names. After refresh see the handoff checklist.")
    save(doc, "Enrollment-Architecture-Setup-Environments.docx")


def doc_exec():
    doc = Document()
    setup_doc(doc, "Enrollment API  ·  Execution")
    cover(doc, "Execution and troubleshooting", "Commands to run suites and classify failures", "GUIDE", TEAL)
    heading(doc, "1. Commands (repo root)")
    grid_table(doc, ["Suite", "Command (edit host file name)"], [
        ["Smoke Stage1", 'mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=LT12800.properties"'],
        ["Regression Stage1", 'mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-regression,acceptance-stage1" "-Dhost.properties=LT12800.properties"'],
        ["Integration QC4", 'mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-integration,acceptance-qc4" "-Denvironment.properties=qc4.properties" "-Dhost.properties=qc4.properties"'],
    ])
    heading(doc, "2. Troubleshooting")
    grid_table(doc, ["Symptom", "Cause", "Action"], [
        ["401 / decrypt fail", "Stale JWT or double encrypt", "New prospect; encrypt from plaintext"],
        ["426", "x-app-version", "1.8.0+ or DB min version"],
        ["DB timeout", "No Frogger", "PuTTY Frogger session"],
        ["Session test skipped", "groups=functional", "Expected in regression filter"],
        ["nmdirect missing", "Not in CI XML", "Known gap — not a product bug"],
    ])
    heading(doc, "3. Pipeline")
    para(doc, "Enrollment GitLab nightly is not in local gitlab-ci yet. Mobile 2 nightly is the pattern to copy (QA-1405). Same Maven profiles locally and in CI.")
    save(doc, "Enrollment-Execution-Troubleshooting.docx")


def doc_report():
    doc = Document()
    setup_doc(doc, "Enrollment API  ·  Reporting")
    cover(doc, "Reporting, triage, evidence", "What to keep after a run", "GUIDE", TEAL)
    heading(doc, "1. Artifacts")
    kv_table(doc, [
        ("Surefire", "mobile/enrollment/target/surefire-reports/"),
        ("HTML", "target/mobile-ms-report/ when listener is enabled"),
        ("Do not commit", "target/, host properties, raw tokens"),
    ])
    heading(doc, "2. Triage")
    for b in [
        "Classify environment vs script vs product (automation-bug-lifecycle).",
        "Do not log partner-deferred APIs as product bugs.",
        "Redact Authorization headers before Jira.",
    ]:
        doc.add_paragraph(b, style="List Bullet")
    heading(doc, "3. Retention")
    callout(doc, "Keep date, plant, suite, counts. Never keep JWT, passwords, or SSN.", AMBER_BG)
    save(doc, "Enrollment-Reporting-Triage.docx")


def doc_signoff():
    doc = Document()
    setup_doc(doc, "Enrollment API  ·  Formal sign-off")
    cover(doc, "Enrollment API automation", "Formal sign-off and handover", "STATUS: COMPLETE (defined scope)", GREEN)
    heading(doc, "1. Document control")
    kv_table(doc, [
        ("Title", "Enrollment API Automation — Sign-Off"),
        ("Version", "1.0"),
        ("Date", SIGNOFF_DATE),
        ("Jira", "QA-893 / QA-2043"),
        ("Determination", "COMPLETE — happy path + subsequent on OK Direct and New York"),
    ], last_green=True)
    heading(doc, "2. Executive summary")
    callout(doc, "25 of 28 catalog endpoints automated (89%). Wizard 15/15. Three partner rows deferred. NM Direct and GitLab nightly are follow-up, not missing wizard code.")
    p = chart()
    if p.exists():
        doc.add_picture(str(p), width=Inches(6.0))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    heading(doc, "3. KPIs")
    kv_table(doc, [
        ("Catalog / automated / deferred", "28 / 25 / 3"),
        ("Test classes", "23 + EnrollmentBaseTest"),
        ("@Test methods", "25"),
        ("CI plants", "okdirect, newyork"),
        ("Local-only plant", "nmdirect"),
        ("Enrollment nightly", "Not created"),
    ])
    heading(doc, "4. Endpoint register")
    grid_table(
        doc,
        ["ID", "Method", "Path", "Area", "Class", "Status", "Plants"],
        [list(r) for r in ENDPOINTS],
        status_col=5,
    )
    heading(doc, "5. Exclusions")
    grid_table(doc, ["Item", "Reason"], [
        ["POST /enrollments/submit", "QA-1808 partner"],
        ["GET /upromiseaccount", "QA-1807"],
        ["POST /oauth/token", "Not MSC E2E"],
        ["Negatives", "Enhancement for receiving team"],
        ["nmdirect CI", "Follow-up story"],
        ["GitLab nightly", "Follow-up story"],
    ])
    heading(doc, "6. Approvals")
    para(doc, "Names are blank until leadership assigns ACM / sign-off contacts.")
    grid_table(doc, ["Role", "Name", "Signature", "Date"], [
        ["QA Automation Lead", "", "", ""],
        ["Program / ACM", "", "", ""],
        ["Engineering", "", "", ""],
        ["Support / Operations", "", "", ""],
    ])
    save(doc, "Enrollment-API-Automation-Sign-Off.docx")


def doc_handoff():
    doc = Document()
    setup_doc(doc, "Enrollment API  ·  DB refresh")
    cover(doc, "Post database-refresh checklist", "Operational steps before calling regression green", "CHECKLIST", TEAL)
    heading(doc, "1. After refresh")
    grid_table(doc, ["#", "Task", "Done"], [
        ["1", "VPN + Frogger/PuTTY (gwtpsshrelay01)", ""],
        ["2", "Host properties still valid (not committed)", ""],
        ["3", "Recreate QAAUTOTEST% (or current pattern) accounts", ""],
        ["4", "Re-enroll test MFA devices only", ""],
        ["5", "GET certificate — encrypt with new cert", ""],
        ["6", "Smoke okdirect", ""],
        ["7", "Wizard regression okdirect + newyork", ""],
        ["8", "Allocation fund ids still valid", ""],
        ["9", "Freshservice if Linux/DB access dropped", ""],
    ])
    heading(doc, "2. Minimum bar")
    callout(doc, "Green smoke + one wizard regression on okdirect = env usable. Two-plant regression = sustainment bar.")
    save(doc, "Enrollment-Handoff-DB-Refresh-Checklist.docx")


def doc_ai():
    doc = Document()
    setup_doc(doc, "Enrollment API  ·  AI scenarios")
    cover(doc, "AI-assisted scenario development", "Cursor pattern with mandatory human review", "GUIDE", TEAL)
    heading(doc, "1. Copy a neighbor class")
    para(doc, "Clone OwnerEnteredTests (or similar). Extend EnrollmentBaseTest. Same TestNG groups. Wire regression + integration XML for okdirect and newyork only.")
    heading(doc, "2. Prompt rules")
    callout(doc, "Do not put passwords, JWT, or SSN in the prompt. Attach stripped Postman from GitLab api-test-automation (no secrets).", AMBER_BG)
    heading(doc, "3. Human review")
    for b in [
        "Path and method match catalog",
        "No SkipException hiding 500s",
        "One local run",
        "Second person reviews the MR (QA-2047)",
    ]:
        doc.add_paragraph(b, style="List Bullet")
    save(doc, "Enrollment-AI-Scenario-Guide.docx")


def main():
    doc_index()
    doc_setup()
    doc_exec()
    doc_report()
    doc_signoff()
    doc_handoff()
    doc_ai()
    print("Done.")


if __name__ == "__main__":
    main()
