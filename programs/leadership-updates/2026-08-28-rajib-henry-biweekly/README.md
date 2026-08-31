# AM Squad Biweekly Status — Rajib & Henry

**Meeting:** Friday, August 28, 2026 · 9:00 AM  
**Audience:** Rajib (Chapter Lead), Henry (Director), Persistent Delivery Managers  
**Presenter:** Swapnil Patil  
**Sprint scope:** AMSQUAD Sprints **26.13** and **26.14** (current)

## Deliverables

| File | Purpose |
|------|---------|
| [AM-Squad-Biweekly-Status-Rajib-Henry-Aug28-2026.pptx](./deliverables/AM-Squad-Biweekly-Status-Rajib-Henry-Aug28-2026.pptx) | **Meeting deck** — 15 slides, color-coded charts |
| [AM-Squad-Biweekly-Status-Rajib-Henry-Aug28-2026.docx](./deliverables/AM-Squad-Biweekly-Status-Rajib-Henry-Aug28-2026.docx) | **Detailed briefing** — sprint evidence, Jira refs, asks |
| [01-executive-summary.md](./01-executive-summary.md) | One-page talking points for the call |

## Regenerate

```powershell
cd programs/leadership-updates/2026-08-28-rajib-henry-biweekly/tools
python generate_biweekly_deliverables.py
```

Close Word/PowerPoint if files are open before regenerating.

## Slide map (15 slides)

1. Title  
2. Executive pulse (2-sprint KPIs)  
3. Sprint focus — 26.13 · 26.14 · 26.15 plan  
4. Unite MSC program status (M1/M2 100%, enrollment 95%)  
5. **Enrollment endpoint coverage** (new chart)  
6. M1/M2 endpoint coverage (26/26 + 25/25)  
7. Pipeline & environments (GitLab nightly delivered, DB refresh)  
8. V2/V3 UI — maintenance + migration discussion  
9. Performance — contribution JMX in progress; M1+enrollment perf next sprint  
10. Performance governance ask  
11. Capacity — 1 resource MSC wrap-up vs 3.5 FTE new work  
12. V2 → V3 migration path  
13. Incoming ACS-5678 Atlas (Oct delivery)  
14. Leadership asks & decisions  
15. Q&A  

## Key messages

| Area | Status |
|------|--------|
| Mobile 1 & 2 | **100%** — sign-off ready |
| Enrollment API | **95%** core E2E (19/20) · 17 TestNG classes · submit in flight |
| MSC close-out | **1 resource ~1 sprint** — docs, qTest, Bruno, KT (not full squad exit) |
| New work capacity | **3.5 FTE** — Atlas (Oct) or V2/V3 backlog per leadership |
| Perf | Preeti slightly behind; M1+enrollment perf next sprint |

## Data sources

- Jira: [QA AMSQUAD board](https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/2515/backlog)
- Repo: `api-test-automation/mobile/enrollment` (refreshed Aug 2026)
- KB: `programs/unite-msc/api-test-automation/postman/EnrollmentE2E/`
- Previous pack: [2026-08-14 biweekly](../2026-08-14-rajib-henry-biweekly/README.md)
- Capacity ask: [2026-08-20 post-MSC ask](../../leadership-capacity-planning/2026-08-20-post-msc-capacity-ask.md)
