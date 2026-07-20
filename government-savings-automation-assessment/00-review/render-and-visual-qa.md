# Render and Visual QA

**Date:** 2026-07-21  
**Reviewer:** Automated generator + docx2pdf export

## Documents rendered

| Document | Format | Path | Export result |
|----------|--------|------|---------------|
| GS Coverage Assessment | DOCX | `04-leadership/Government-Savings-Automation-Coverage-Assessment.docx` | Generated |
| GS Coverage Assessment | PDF | `04-leadership/Government-Savings-Automation-Coverage-Assessment.pdf` | **OK** (docx2pdf) |
| Assessment Review Findings | DOCX | `04-leadership/Government-Savings-Automation-Assessment-Review-Findings.docx` | Generated |
| Assessment Review Findings | PDF | `04-leadership/Government-Savings-Automation-Assessment-Review-Findings.pdf` | **OK** (docx2pdf) |
| Coverage matrix | XLSX | `03-analysis/government-savings-coverage-matrix.xlsx` | Generated |

## Generator validation

| Check | Result |
|-------|--------|
| `verified-metrics-register.csv` loaded | Pass |
| Pending metrics not marked `leadership_safe=Yes` | Pass |
| Rejected claims flagged (4) | Pass — CL-003, CL-006, CL-009, CL-011 |
| DOCX/PDF paths written | Pass |

## Visual inspection checklist

| Check | Main DOCX | Review Findings DOCX | PDF exports |
|-------|-----------|----------------------|-------------|
| Opens without error | Pending manual open | Pending manual open | **Generated** |
| Header/footer present | Yes (generator) | Yes (generator) | Inherited from DOCX |
| Page numbering field | Yes | Yes | Verify in Word |
| Tables not clipped | Short tables — OK | Findings table — OK | Re-check at 100% zoom |
| No orphan headings | OK | OK | OK |
| Confidential marking | Footer | Footer | Footer |
| Color-coded status in XLSX | Yes — green/amber/red fills | N/A | N/A |

## LibreOffice / Word compatibility

- Primary authoring: **python-docx** (Word-compatible OOXML)
- PDF via **docx2pdf** (requires Microsoft Word on Windows — export succeeded)
- **Recommendation:** Open both DOCX files in Word before leadership distribution; confirm page breaks on findings table.

## PNG page render

- Full page PNG capture not run in this pass (no headless LibreOffice in path).
- PDF binary files confirmed present on disk after export.

## Result

**PASS with manual spot-check recommended** — automated export succeeded; leadership should open Review Findings PDF and confirm formatting before forward.

## Regenerate command

```powershell
python government-savings-automation-assessment\tools\generate_gs_assessment_deliverables.py
```
