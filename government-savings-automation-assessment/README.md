# Government Savings Automation Coverage & CI Integration Assessment

**Assessment date:** 2026-07-20  
**Rebuild validated:** 2026-07-21  
**Prepared for:** Michael Blake, Rajiv Akhter, Henry Dittmer, Kevin Daines, Dhanashree, Ascensus leadership  
**Prepared by:** QA Automation (evidence-based repository & pipeline review)  
**Status:** Rebuilt 2026-07-21 — verified vs pending metrics separated; awaiting leadership approval before commit

## Start here (leadership)

| Document | Audience | Path |
|----------|----------|------|
| **Executive summary** | Leadership | [04-leadership/leadership-summary.md](04-leadership/leadership-summary.md) |
| **Review findings (DOCX)** | Leadership / audit | [04-leadership/Government-Savings-Automation-Assessment-Review-Findings.docx](04-leadership/Government-Savings-Automation-Assessment-Review-Findings.docx) |
| **Review findings (PDF)** | Forwardable | [04-leadership/Government-Savings-Automation-Assessment-Review-Findings.pdf](04-leadership/Government-Savings-Automation-Assessment-Review-Findings.pdf) |
| **Email-ready response** | Michael Blake / Rajiv | [04-leadership/leadership-response-draft.md](04-leadership/leadership-response-draft.md) |
| **Talking points** | Meeting prep | [04-leadership/leadership-talking-points.md](04-leadership/leadership-talking-points.md) |
| **Formatted Word report** | Forwardable | [04-leadership/Government-Savings-Automation-Coverage-Assessment.docx](04-leadership/Government-Savings-Automation-Coverage-Assessment.docx) |
| **Coverage matrix (Excel)** | Metrics / PMO | [03-analysis/government-savings-coverage-matrix.xlsx](03-analysis/government-savings-coverage-matrix.xlsx) |
| **Verified metrics (CSV)** | Single source of truth | [03-analysis/verified-metrics-register.csv](03-analysis/verified-metrics-register.csv) |
| **Contradiction ledger** | Rebuild audit | [00-review/contradiction-resolution-ledger.md](00-review/contradiction-resolution-ledger.md) |

## Folder structure

| Folder | Contents |
|--------|----------|
| `00-review/` | Rebuild audit — file manifest, claim register, contradiction ledger, visual QA |
| `01-inventory/` | Repository, automation asset, and pipeline job CSVs |
| `02-evidence/` | Pointers to screenshots and external artifacts (not copied) |
| `03-analysis/` | Coverage matrix, calculation notes, CI gates, gaps |
| `04-leadership/` | Summary, response draft, verification checklist, evidence register, DOCX |
| `05-roadmap/` | 0–30 / 30–90 / 90+ day plan |
| `tools/` | `generate_gs_assessment_deliverables.py` — regenerate XLSX/DOCX from CSV |

## Regenerate Excel & Word

```powershell
cd c:\Workspace\GitLab\qa-automation-kb\government-savings-automation-assessment\tools
python generate_gs_assessment_deliverables.py
```

Requires: `openpyxl`, `python-docx`, `matplotlib` (optional charts in DOCX).

## Related KB baselines (reference only — validated in this assessment)

| Baseline | Path |
|----------|------|
| Universal Platform coverage (Jun–Jul 2026) | `../universal-platform-coverage/` |
| Unite MSC leadership pack (2026-07-17) | `../leadership-updates/unite-msc/2026-07-17-leadership-update/` |
| Mobile 2 API–DB validation KB | `../mobile2-api-db-validation/` |
| Historical imports | `../10_IMPORTS_RAW/` |

## Rules applied

- No production automation code modified.
- Verified facts separated from inferred, planned, and unknown items.
- Application **source-code coverage** (JaCoCo/Sonar gates on app repos) distinguished from **business test automation coverage**.
- GitLab, GitHub Actions, and Jenkins reported separately.

---

*Confidential — Internal Use · Ascensus Government Savings QA Automation*
