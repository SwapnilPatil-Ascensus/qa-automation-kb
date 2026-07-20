# Executive Summary — GS Coverage Intelligence Feasibility

**Assessment date:** 2026-07-20  
**Audience:** Michael Blake, Rajiv Akhter, Ascensus GS leadership  
**Tone:** Neutral — fragmented data; reconciliation required; no unsupported enterprise %

---

## Leadership questions answered

| # | Question | Answer | Status |
|---|----------|--------|--------|
| 1 | Do we have an automated coverage tool today? | **Partial.** Python assessment utilities exist (UP coverage, GS assessment). No live enterprise coverage intelligence platform. | **Verified** |
| 2 | What automation capability exists? | V3 UI GitLab nightly; metadataweb API nightly; Mobile2 24/24 endpoints in code; V2/Astro large Cucumber suites; MSC service BDD; perf assets. | **Verified** |
| 3 | Can qTest, Jira, repos, pipelines reconcile automatically? | **Not today.** Repo→pipeline **yes** locally. Full chain **blocked** without qTest/Jira/GitLab API access. | **Verified** |
| 4 | Which integrations are available? | Local repos + KB exports: **yes**. MCP Jira/GitLab: **blocked**. qTest MCP: **none**. qTest REST: **not configured**. | **Verified** |
| 5 | How reliable is qTest today? | **Stale export** (2026-06-29). Module-level V2 map SME-reviewed; row-level IDs missing; V3 not qTest-keyed. | **Stale/Partial** |
| 6 | Defensible GS-wide % today? | **No.** No approved GS denominator. | **Verified** |
| 7 | Which percentages are defensible? | See table below — each scoped with formula. | **Verified** |
| 8 | Source-code coverage gates? | JaCoCo on services **yes**; Sonar **disabled**; no blocking code-coverage gate on QA pipelines. | **Verified** |
| 9 | Business regression gates? | V3 UI + metadataweb API scheduled hard-fail **yes**. Mobile2, V2 full, ASTRO, most API modules **no**. | **Verified** |
| 10 | Recommended action? | Establish read-only GS quality coverage register; separate metrics A–E; remediate data quality before blocking gates. | **Planned** |
| 11 | 30 / 60 / 90 day delivery? | See `minimum-viable-implementation-plan.md` | **Planned** |
| 12 | Leadership support needed? | Approve denominators; provision read-only API access; sponsor QA-1405; accept no single GS % until register matures. | **Planned** |

## Defensible metrics (documented scope only)

| Domain | Metric | Value | Formula | Timestamp | Evidence |
|--------|--------|------:|---------|-----------|----------|
| V3 UI | Inventory share | **86.9%** | 379÷436 TestNG methods | 2026-07-01 | UP reconciliation ledger |
| V2 UI (UP-scoped) | Inventory share | **36.0%** | 268÷744 qTest cases | 2026-06-29 | qTest PDF + module map |
| Mobile 2 API | Endpoint automation | **100%** | 24÷24 in-scope endpoints | 2026-07-20 | `api-test-automation` @ `cee0de9` |
| Mobile 1 API | Endpoint automation | **22.2%** | 6÷27 endpoints | 2026-07-20 | Code scan |
| Mobile 2 | CI-integration (D) | **0%** | 0 scheduled jobs | 2026-07-20 | No GitLab job |
| UP API | Operations mapped | **11 ops** | Subset only — not full GS API % | 2026-07-01 | api-operation-mapping.csv |

**Disclaimer:** Inventory share is **not** requirement-level or functional completeness.

## Cannot calculate yet

- Enterprise GS business automation %  
- GS execution coverage % (live pipeline data blocked)  
- GS gate coverage % (critical list not approved)  
- Jira AC-level coverage  
- qTest-linked traceability completeness  
- Current nightly pass rates (artifacts not refreshed)  
- COPACS coverage (scope unknown)  
- ASTRO / full V2 scheduled execution status  

## Recommended action (one sentence)

**Establish an automated Government Savings quality coverage register that reconciles approved scope from Jira, test inventory from qTest, automated implementation from repositories, and execution evidence from CI/CD — with separate source-code, business automation, execution, CI-integration, and gate metrics — beginning with read-only reporting and data-quality remediation before introducing blocking gates.**

## Leadership support required

1. Read-only API credentials (qTest, Jira, GitLab)  
2. Approval of domain-specific denominators (not one GS %)  
3. DevOps priority for QA-1405 (Mobile2 nightly)  
4. ~30–40% BA capacity for scope hygiene  
5. Quarterly register review cadence  

---

*Full report: `automated-coverage-feasibility-report.md` · Artifacts: `../README.md`*
