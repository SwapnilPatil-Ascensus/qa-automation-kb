# Sign-Off Package — Mobile 1 & Mobile 2

Formal handover documents for engineering, support, and leadership.

## Primary deliverables (hand to teams)

| Document | Audience | Format |
|----------|----------|--------|
| [Mobile-1-API-Automation-Sign-Off.docx](./Mobile-1-API-Automation-Sign-Off.docx) | Mobile 1 support / engineering | Word — color-coded, headers, page numbers |
| [Mobile-2-API-Automation-Sign-Off.docx](./Mobile-2-API-Automation-Sign-Off.docx) | Mobile 2 support / engineering | Word — color-coded, headers, page numbers |

## Supporting artifacts

| File | Purpose |
|------|---------|
| [mobile1-signoff-summary.md](./mobile1-signoff-summary.md) | Markdown index — 26 endpoint operations |
| [enrollment-signoff-summary.md](./enrollment-signoff-summary.md) | Markdown draft — Enrollment (Word pack still a story) |
| [../../mappings/endpoint-signoff-register.csv](../../mappings/endpoint-signoff-register.csv) | Machine-readable full mapping |
| [../05-code-coverage-metrics.md](../05-code-coverage-metrics.md) | Coverage & test counts |
| [../../evidence/regression-runs/](../../evidence/regression-runs/) | QC4/Stage1 execution logs |

## Regenerate

```powershell
python programs/unite-msc/api-test-automation/tools/generate_signoff_deliverables.py
```

Requires: `python-docx`, `matplotlib`
