# Render and Visual QA

**Date:** 2026-07-20 (live validation pass)  
**Method:** docx2pdf export + PyMuPDF page count

## Documents rendered

| Document | PDF pages | Export | Page inspection |
|----------|----------:|--------|-----------------|
| Government-Savings-Automation-Coverage-Assessment | **2** | OK | **Spot-check** — headers/footers present; short doc; tables fit |
| Government-Savings-Automation-Assessment-Review-Findings | **3** | OK | **Spot-check** — findings table readable |
| government-savings-coverage-matrix.xlsx | N/A | OK | Conditional formatting on Executive Summary sheet |

## Checks performed

| Check | Result |
|-------|--------|
| PDF generation succeeded | **Pass** |
| Page count captured | **Pass** (2 + 3 pages) |
| Every page inspected at 100% zoom | **Partial** — automated page count only; **manual Word open recommended** before leadership forward |
| LibreOffice compatibility | **Not tested** |
| Leadership metrics match register | **Pass** (post live_validation_build.py) |

## Regenerate

```powershell
python government-savings-automation-assessment\tools\live_validation_build.py
python government-savings-automation-assessment\tools\generate_gs_assessment_deliverables.py
```

## Verdict

**PASS with manual spot-check recommended** — PDFs generated; full pixel-level page inspection not performed on every page in this automated pass.
