# 05 — Unite Enrollment Migration Tracker

**Last verified:** 2026-09-02  
**Source of truth (code):** `C:\Workspace\GitLab\api-test-automation\mobile\enrollment`  
**Coverage matrix:** `programs/unite-msc/api-test-automation/postman/EnrollmentE2E/Enrollment-Automation-Coverage-Status.md`

## Executive Summary

Unite Enrollment API automation is **coding-complete for the MSC happy path and subsequent enrollment** on **OK Direct (`okdirect`) and New York (`newyork`)**. Mobile 1 and Mobile 2 API coding is **complete** and signed off. Remaining Enrollment work is **documentation, sign-off, pipeline plants (NM Direct), negatives as enhancement, Postman/Bruno consolidation, and handoff**.

| Field | Value |
|-------|-------|
| Module | Unite Enrollment (API / MSC) |
| Target folder | `api-test-automation/mobile/enrollment/` |
| Program status | **Happy path + subsequent Done** (okdirect + newyork). Handoff / CI / docs remaining. |
| Framework | Java, TestNG, Rest Assured, Maven (not Cucumber) |

---

## Module Metadata

| Attribute | Value |
|-----------|-------|
| Source (legacy) | UniteMSC app-repo Cucumber + Postman (historical) |
| Target repository | `api-test-automation` — `mobile/enrollment` |
| Primary groups | `integration`, `regression`, `functional` (smoke) |
| Environments | QC4 (integration), Stage1 (regression) |
| Target plants | **OK Direct, New York, NM Direct** |

---

## Discovery Inventory (verified Sep 2026)

| Category | Count | Notes |
|----------|-------|-------|
| Feature files | 0 | TestNG only |
| `@Test` methods | 25 | 17 wizard/subsequent (`integration`+`regression`); 8 smoke (`functional`) |
| Test classes | 23 + `EnrollmentBaseTest` | Flat `src/test/java` |
| Unique endpoints automated | 25 catalog + 3 subsequent Java-only | See coverage status |
| Suites | smoke / integration / regression / localhost example | |

---

## Scenario Migration Tracker

| ID | Area | Decision | Status | Execution | Notes |
|----|------|----------|--------|-----------|-------|
| ENR-WIZ | Initial wizard prospect → review-confirm | Migrate + expand | **Migrated** | okdirect + newyork in regression/integration | QA-1604 review-confirm Done |
| ENR-SUB | Subsequent banks / bene / bank / recurring / review-confirm | New in MSC | **Migrated** | okdirect + newyork | QA-1791/1792/1853/1854/1855 |
| ENR-SMOKE | ping, certificate, states, country, plans | New + migrate | **Migrated** | okdirect smoke | |
| ENR-NMD | NM Direct plant | Keep | **Localhost only** | Not in CI XML | Gap for next sprint |
| ENR-NEG | Negative / validation cases | Enhance later | **Not started** | — | Handover enhancement |
| ENR-PARTNER | submit / Upromise / OAuth | Exclude from MSC E2E | **Deferred** | — | Existing QA-1807 / QA-1808 |

**Status values:** Not started | In progress | Migrated | Stabilized | Excluded | Parked

---

## Plant coverage

| Suite | okdirect (OK Direct) | newyork (New York) | nmdirect (NM Direct) |
|-------|----------------------|--------------------|----------------------|
| Regression | Full wizard + subsequent | Full wizard + subsequent | — |
| Integration | Full wizard + subsequent | Full wizard + subsequent | — |
| Smoke | Bootstrap GETs | — | — |
| Localhost example | Yes | Yes | Yes (local only) |

Mobile 1 / Mobile 2: OK Direct + NM Direct. **New York is enrollment-only** in API automation.

---

## Exclusions / deferred

| Scenario / area | Decision | Reason |
|-----------------|----------|--------|
| `/enrollments/submit` | Deferred | Partner (Vanguard) — QA-1808 |
| `/upromiseaccount` | Deferred | Partner — QA-1807 |
| `/oauth/token` | Deferred | Not needed for MSC E2E |
| Negative payloads | Enhancement | Happy path first; handover to receiving team |

---

## Blockers and remaining (not coding of wizard)

| ID | Item | Impact | Status |
|----|------|--------|--------|
| R1 | nmdirect missing from CI suites | Third target plant not gated | Open — story |
| R2 | `MobileMemberSessionRequestTest` is `functional` but listed in regression XML | Filtered out of regression | Open — hygiene |
| R3 | localhost XML stale vs regression class list | Local 3-plan runs incomplete | Open — hygiene |
| R4 | Coverage Excel catalog missing 3 subsequent POSTs | Mapping drift | Open — docs |
| R5 | No enrollment GitLab nightly in local `.gitlab-ci.yml` | Pipeline gap | Open — story |

---

## Module Milestones

| Milestone | Status |
|-----------|--------|
| Discovery complete | Done |
| Vertical slice green | Done |
| Smoke suite | Done (okdirect) |
| Regression suite (okdirect + newyork) | Done in code — plant evidence / nightly still needed |
| Pipeline integrated | Partial — Mobile 2 nightly exists; Enrollment nightly missing |
| Sign-off pack | **Not started** (Mobile 1/2 packs exist) |

---

## Related Pages

| Page | Purpose |
|------|---------|
| [Enrollment-Automation-Coverage-Status.md](../api-test-automation/postman/EnrollmentE2E/Enrollment-Automation-Coverage-Status.md) | Endpoint coverage |
| [legacy-new-postman-excel-mapping.md](../api-test-automation/mappings/legacy-new-postman-excel-mapping.md) | Legacy / new / Postman / Excel |
| [upcoming sprint stories](../../upcoming-sprints-2026-09/README.md) | Next two sprints backlog |
