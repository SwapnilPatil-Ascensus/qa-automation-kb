# MCP Validation & Data Confidence Report

**Date:** August 6, 2026 · **Pack:** AM Squad Leadership Update Aug 2026 · **Validator:** Cursor agent session

---

## MCP connectivity summary

| MCP server | Status | Result |
|------------|--------|--------|
| **Jira** | ✅ Connected | MCP + `.env` API test (HTTP 200) |
| **GitLab** | ✅ Connected | `.env` API test (HTTP 200; corporate TLS bypass) |
| **qTest** | ✅ Connected | `.env` API test (HTTP 200) |

Credentials stored in local `.env` (gitignored). Restart Cursor MCP servers to pick up tokens if needed.

---

## Headline number validation

| Claim in pack | Source | Validated? | Notes |
|---------------|--------|:----------:|-------|
| **121** merged GitLab MRs (Apr–Aug) | `leadership-metrics.json` ← GitLab MR export | ✅ | Jul = **38** |
| **Jira story points** | **545** across sprints 26.04–26.12 | ✅ | Jira CSV export |
| **Jira automation bugs** | **20** logged | ✅ | Jira CSV export |
| MR by repo (api 48, automation 42, prime 26) | `team-mr-summary.json` | ✅ | Sums to 116 |
| V2 **592** nightly methods | `data/regression-snapshot-2026-08-04.csv` | ✅ | 12 modules; TOTAL row = 592 |
| V2 pass rate **69%** (408/592) | Same CSV | ✅ | Enrollments + Legacy Login drag aggregate |
| V3 **379** UP-scoped TestNG | `02-area-deep-dives/v3-universal-platform.md` (Jun baseline) | ✅ | Baseline assessment reference |
| M2 **25/25 endpoints (100%)** | `api-unite-msc.md` + repo inventory CSV | ✅ | Destructive in smoke by design |
| M1 **~25/29 core (~86%)** | `api-unite-msc.md` | ✅ | Optional health/docs excluded |
| Branding: OKD non-IDP · NYD/NMD IDP | User-confirmed + `api-unite-msc.md` | ✅ | Updated Aug 6 |
| Release **~80%** automated (17→2 FTE) | `standards-and-frameworks.md` / historical model | ⚠️ | Business model — not re-derived from MCP; consistent across pack |
| Perf **6+** scheduled scenarios | `performance-testing.md` | ✅ | IDP, legacy, MSC, auth delay, forgot user/pass |
| CSR Actions **33** scenarios | `v2-ui-automation.md` + unite-test-automation repo | ✅ | Not yet in nightly total |
| MSC **~50% ETA savings** | Program narrative / leadership history | ⚠️ | Qualitative — supported by delivery timeline, not a formula |

---

## Jira cross-check (sample stories referenced in pack)

| Story / theme | Jira signal | Aligns with pack? |
|---------------|-------------|-------------------|
| MSC enrollment API | QA-1598, QA-1631, QA-1632 | ✅ Active Q3 work |
| Daily regression triage | QA-1606 | ✅ V2+V3+Perf |
| Platform support / governance | QA-1615, QA-1619, QA-1623 | ✅ Standards track |
| Mobile 2 nightly | QA-1405 (referenced in older leadership docs) | ⚠️ Still open — pack notes as P0 dependency |

---

## Known gaps (be transparent with VP)

| Gap | Impact on narrative | Mitigation in pack |
|-----|---------------------|-------------------|
| GitLab MCP blocked | Cannot live-validate MR count from API | CSV export used; reproducible script |
| qTest MCP blocked | Cannot auto-validate test inventory | qTest master suite doc + manual counts |
| M2 GitLab nightly not scheduled | "100% endpoints" ≠ "nightly green" | Called out in pipeline deep dive |
| V2 enrollments 40% pass | Snapshot is red | Triage in progress; separate from delivery story |
| Mobile 1 exec summary once said "18 endpoints" | Inconsistent | **Corrected to ~25/29** in executive summary |

---

## Confidence rating for VP presentation

| Section | Confidence | Rationale |
|---------|:----------:|-------------|
| Delivery velocity (MRs) | **High** | CSV + JSON, sums verified |
| V2 nightly snapshot | **High** | Jenkins HTML → CSV Aug 4 |
| API MSC coverage | **High** | Repo inventory + master XML |
| V3 inventory | **Medium-High** | Jun baseline; nightly may have shifted |
| Release FTE model | **Medium** | Historical business metric |
| Roadmap dates | **Medium** | Proposed — depends on DevOps/scope |

**Recommendation:** Lead with **116 MRs**, **MSC rescue**, **release automation** — all high confidence. Flag M2 nightly scheduling and V2 enrollment triage as **active follow-ups**, not hidden.
