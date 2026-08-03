# Known Gaps and Dependencies

**Assessment date:** 2026-07-20  
**Tone:** Neutral — gaps framed as scope, integration, or verification items.

---

## P1 — Leadership-visible gaps

| # | Gap | Impact | Owner type | Dependency |
|---|-----|--------|------------|------------|
| 1 | Mobile 2 GitLab nightly not wired | No recurring API regression gate for MSC BFF | DevOps + QA | QA-1405; secure files; runner network |
| 2 | Mobile 2 sign-off evidence stale | Cannot claim projected 96% as verified | QA Automation | Fresh QC4/Stage1 @ `cee0de9` |
| 3 | Prior assessment overstated M2/M1 % | Leadership trust risk | QA Automation | Rebuild complete 2026-07-21 |
| 4 | Mobile 1 — 26/27 endpoints not verified | MSC member API surface largely uncovered | QA Automation | Sprint scope |
| 4 | No single GS-wide coverage denominator | Cannot report one "GS %" number | Program + BA | Business capability map; qTest refresh |
| 5 | GitHub Actions Mobile2 workflow repo not in clone | Deployment validation story incomplete in audit | DevOps + QA | Document workflow repo URL |

---

## P2 — Integration and scope gaps

| # | Gap | Notes |
|---|-----|-------|
| 6 | V2 UI (~2,176 scenarios) not on V3 GitLab nightly | Legacy Jenkins/Ant; migration status unclear |
| 7 | V2 backoffice (1,077 scenarios) separate from frontoffice nightly | Batch/feed coverage may not run on same schedule |
| 8 | ASTRO (1,236 scenarios) not in V2/V3 GitLab schedule | Automation exists; recurring execution not verified |
| 9 | Universal API modules beyond metadataweb | accountweb, auth, financial — manual execution only |
| 10 | MSC performance — manual Jenkins only | IDP perf scheduled; MSC endurance manual |
| 11 | COPACS | No validated automation identified — requires scope confirmation |
| 12 | qTest ↔ automation traceability | Planned; not reconciled in this pass |

---

## P3 — Hygiene and documentation

| # | Gap | Notes |
|---|-----|-------|
| 13 | UP assessment (Jun 2026) vs current suite growth | V2/V3 counts may have changed |
| 14 | mobile2-api-db-validation STATUS (Jun 2026) | API–DB doc progress stale; not endpoint % |
| 15 | Duplicate MobileStackup test class in M2 master | Extra runs; cleanup |
| 16 | YTD may be missing from M2 master XML | Master completeness |
| 17 | Application code coverage vs test coverage | Leadership terminology alignment needed |

---

## Dependencies (neutral)

| Dependency | Affects |
|------------|---------|
| Stage 1 DB tunnel / secure files | API nightly, V3 nightly, metadataweb |
| `QAAUTOTEST` accounts per branding | Mobile 1/2 SQL fixtures |
| Selenium grid / Chrome service | V3 GitLab nightly |
| Load servers `loadtestwt1/2` | Performance Jenkins |
| Dinesh endpoint workbooks (external) | M1/M2 denominators |
| SME validation of UP inventory | V2/V3 inventory-share metrics |
| ~30–40% BA/Scrum reporting capacity | Roadmap intake and metrics hygiene |

---

## What is working (verified)

- V3 UI GitLab nightly regression with hard failure on test errors
- Metadataweb API Stage1 scheduled job on GitLab
- Mobile 2 **verified** endpoint baseline **22/25 (88%)**; projected **24/25 (96%)** pending sign-off
- Mobile 1 **verified** **1/27 (3.7%)**; five endpoints implemented pending evidence
- UP assessment with SME-reviewed inventory shares (V2 36%, V3 87%)
- Performance assets for UP IDP (scheduled) and MSC (manual)

---

*Roadmap actions: `05-roadmap/government-savings-automation-roadmap.md`*
