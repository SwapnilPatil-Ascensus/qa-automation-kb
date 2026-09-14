# AM Squad Biweekly Status — Rajib & Henry

**Meeting:** Thursday, September 11, 2026 · 9:00 AM  
**Audience:** Rajib (Chapter Lead), Henry (Director), Persistent Delivery Managers  
**Presenter:** Swapnil Patil  
**Sprint scope:** AMSQUAD Sprints **26.14** and **26.15** (current)

## Deliverables

| File | Purpose |
|------|---------|
| [AM-Squad-Biweekly-Status-Rajib-Henry-Sep11-2026.pptx](./deliverables/AM-Squad-Biweekly-Status-Rajib-Henry-Sep11-2026.pptx) | **Meeting deck** — 16 slides |
| [AM-Squad-Biweekly-Status-Rajib-Henry-Sep11-2026.docx](./deliverables/AM-Squad-Biweekly-Status-Rajib-Henry-Sep11-2026.docx) | **Detailed briefing** |
| [01-executive-summary.md](./01-executive-summary.md) | One-page talking points |
| [02-mr-265-pending-merge.md](./02-mr-265-pending-merge.md) | GitLab MR !265 brief |
| [03-v2-regression-gaps-venkatesh.md](./03-v2-regression-gaps-venkatesh.md) | V2 gap analysis (full detail) |

## Regenerate

```powershell
cd programs/leadership-updates/2026-09-11-rajib-henry-biweekly/tools
python generate_biweekly_deliverables.py
```

## Key messages

| Area | Status |
|------|--------|
| Mobile 1 & 2 | **100%** — on main, sign-off ready |
| Enrollment | **25/28** catalog — coding complete; 3 partner deferred |
| MR !265 | **Pending** — Snyk gate; closes QA-1938 |
| MSC wrap-up | Sign-off docs, traceability, qTest, Bruno (Sprint 26.15) |
| V2 gaps | Venkatesh P0/P1/P2 analysis — 8 P0 are wire existing tests |
| Perf | Contribution JMX done; M1 scripts in progress |

## Data sources

- [GitLab MR !265](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/merge_requests/265)
- [Jira AMSQUAD board](https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/2515/backlog)
- [Enrollment endpoint CSV](../../unite-msc/api-test-automation/mappings/enrollment-endpoint-current-state.csv)
- [Previous biweekly (Aug 28)](../2026-08-28-rajib-henry-biweekly/README.md)
