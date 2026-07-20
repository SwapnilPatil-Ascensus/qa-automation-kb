# Executive Summary — GS Coverage Intelligence Feasibility

**Assessment date:** 2026-07-20  
**Live validation sync:** 2026-07-20 (evening)  
**Metric authority:** `../government-savings-automation-assessment/03-analysis/verified-metrics-register.csv`  
**Do not duplicate percentages here — import from register**

---

## Leadership questions answered

| # | Question | Answer | Status |
|---|----------|--------|--------|
| 1 | Automated coverage tool today? | **Partial** — Python scanners + generators; no live harmonized register | **Verified** |
| 2 | Automation capability? | V3 GitLab nightly; M2 **96% implemented**; M1 **22% implemented**; V2 corpus; metadataweb; GHA deploy slice | **Verified (code)** |
| 3 | Auto-reconcile qTest/Jira/repos/CI? | **Not today** — ALM/CI APIs blocked | **Verified** |
| 4 | Integrations available? | Local repos **yes**; GitLab/Jira/qTest live **blocked** | **Verified** |
| 5 | qTest reliability? | Stale export; row IDs missing | **Stale** |
| 6 | GS-wide %? | **No** | **Verified** |
| 7 | Defensible metrics? | See register — M2 96% impl / 88% stale exec; M1 22% impl / 3.7% exec; V3 86.9% | **Verified** |
| 8 | Source-code gates? | JaCoCo yes; Sonar disabled; no QA pipeline code gate | **Verified** |
| 9 | Business regression gates? | V3 + metadataweb scheduled; M2/M1 not scheduled | **Verified** |
| 10 | Recommended action? | Extend Python register + read-only APIs | **Planned** |

## Current metrics (from register — not independent)

| ID | Label | Result | Layer |
|----|-------|--------|-------|
| M-M2-IMPL | Mobile 2 implemented | **96.0% (24/25)** | Code |
| M-M2-EXEC | Mobile 2 executed (stale) | **88.0% (22/25)** | Execution |
| M-M1-IMPL | Mobile 1 implemented | **22.2% (6/27)** | Code |
| M-M1-EXEC | Mobile 1 executed verified | **3.7% (1/27)** | Execution |
| M-V3-UI | V3 inventory share | **86.9% (379/436)** | Inventory |

---

*Full intelligence pack: sibling folders under `coverage-intelligence-assessment/`*
