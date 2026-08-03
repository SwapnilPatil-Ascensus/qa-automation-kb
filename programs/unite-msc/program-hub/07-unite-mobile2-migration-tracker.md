# 07 — Unite Mobile 2 Migration Tracker

## Executive Summary

**Unite Mobile 2** is the IdP-aware BFF with the **broadest cross-service exposure** (auth, on-prem account, dashboard) and highest schema-drift risk. In the **Cucumber migration program**, it is **priority 3** after Enrollment and Mobile 1. The **integration-test design proposal** pilots here first with smoke → critical-path coverage.

| Field | Value |
|-------|-------|
| Module | Unite Mobile 2 |
| Priority | 3 (Cucumber migration program) / 1 (Path B proposal) |
| Target folder | `mobile-automation/unite-mobile2/` |
| Program status | Not started |
| Estimate | 2–4 weeks (Cucumber track) |

---

## Module Metadata

| Attribute | Value |
|-----------|-------|
| Source repository | TBD — `unite-mobile2` in UniteMSC |
| Target repository | API Automation Framework |
| Primary tags | `@mobile`, `@uniteMobile2`, `@smoke`, `@regression` |
| Cross-service deps | Auth, account, metadata services (TBD inventory) |
| Path B submodule | `unite-msc/jsonapi-mobile2` (if adopted) |

---

## Coverage Targets (Path B reference — if adopted)

| Stage | Coverage | Definition of done |
|-------|----------|-------------------|
| Day 1 / smoke | Health, login, dashboard golden path | Pipeline green; hard-block check live |
| v1 / critical path | Auth, dashboard, account list, contribution view, UX-breaking endpoints | Delta vs OpenAPI `mobile2.yaml` |
| Beyond v1 | Comprehensive happy + error paths | Out of initial program scope |

---

## Discovery Inventory (TBD)

| Category | Count | Notes |
|----------|-------|-------|
| Feature files | TBD | |
| Cucumber `*IT.java` suites | TBD | May deprecate under Path B |
| Scenarios (total) | TBD | |
| OpenAPI endpoints (`mobile2.yaml`) | TBD | Coverage mapping |

---

## Scenario Migration Tracker

| ID | Scenario name | Source feature | Decision | Status | Execution | Owner | Notes |
|----|---------------|----------------|----------|--------|-----------|-------|-------|
| M2-001 | TBD | TBD | TBD | Not started | — | TBD | |
| M2-002 | TBD | TBD | TBD | Not started | — | TBD | |

---

## Exclusions Log

| Scenario / area | Decision | Reason | Date | Approved by |
|-----------------|----------|--------|------|-------------|
| — | — | — | — | — |

---

## Blockers and Dependencies

| ID | Blocker | Impact | Mitigation | Status |
|----|---------|--------|------------|--------|
| B1 | IdP integration incomplete in legacy suite | No trusted baseline | QC4 real-env tests; config refresh | Open |
| B2 | Shared QC4 DB drift from other teams | Flaky/false failures | Unique test keys; env health probes | Open |
| B3 | Pilot order: Mobile 2 first vs Enrollment first | Schedule conflict | Leadership decision in RAID | Open |

---

## Module Milestones

| Milestone | Target date | Actual | Status |
|-----------|-------------|--------|--------|
| Discovery complete | TBD | — | Not started |
| Vertical slice green | TBD | — | Not started |
| Smoke suite green | TBD | — | Not started |
| Regression suite green | TBD | — | Not started |
| Pipeline integrated | TBD | — | Not started |

---

## Sprint Breakdown Reference (Nick estimate — 1 QA)

| Step | Scope | Estimate |
|------|-------|----------|
| QC4 smoke + pipeline | 1–2 GET endpoints + DevOps pipeline integration | 1 sprint |
| QC4 full coverage | All critical endpoints | 2 sprints |
| Stage1 data | Stage1 alignment | 0.5 sprint |

## Related Pages

| Page | Purpose |
|------|---------|
| [08-regression-suite-and-pipeline-strategy.md](./08-regression-suite-and-pipeline-strategy.md) | Pipeline and suite design |
| [09-raid-log.md](./09-raid-log.md) | Path A vs Path B decision |
