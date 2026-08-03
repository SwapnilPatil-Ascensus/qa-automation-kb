# 05 — Unite Enrollment Migration Tracker

## Executive Summary

**Unite Enrollment** is the **pilot module** for the Mobile Microservices Automation migration. This tracker records discovery inventory, per-scenario migration decisions, execution status, and blockers. Populate TBD fields during Phase 1 discovery.

| Field | Value |
|-------|-------|
| Module | Unite Enrollment |
| Priority | 1 (pilot) |
| Target folder | `mobile-automation/unite-enrollment/` |
| Source repo | TBD — UniteMSC application repo (read-only) |
| Program status | Not started / TBD |
| Estimate | 3–5 weeks |

---

## Module Metadata

| Attribute | Value |
|-----------|-------|
| Source repository | TBD (`ascensus-gs/products/unitemsc` — confirm enrollment service path) |
| Target repository | API Automation Framework (TBD exact Git URL) |
| Technology | Java, Cucumber, Rest Assured, Maven |
| Primary tags | `@mobile`, `@uniteEnrollment`, `@smoke`, `@regression` |
| Environments | QC4 (primary), Stage1, TBD others |
| Dependencies | May depend on IDP, Universal Platform, encryption patterns from Mobile 1/2 (validate in discovery) |

> **Sequencing note:** Nick/Brian estimates place Enrollment **after** Mobile 2 and Mobile 1 (encryption/setup dependencies). Program brief places Enrollment **first**. Confirm pilot order before locking sprint plan.

---

## Discovery Inventory (TBD)

| Category | Count | Notes |
|----------|-------|-------|
| Feature files | TBD | |
| Scenarios (total) | TBD | |
| Step definition classes | TBD | |
| Unique endpoints | TBD | |
| SQL scripts | TBD | |
| Config files | TBD | |
| Test data files / inline payloads | TBD | |

---

## Scenario Migration Tracker

| ID | Scenario name | Source feature | Decision | Status | Execution | Owner | Notes |
|----|---------------|----------------|----------|--------|-----------|-------|-------|
| ENR-001 | TBD | TBD | TBD | Not started | — | TBD | |
| ENR-002 | TBD | TBD | TBD | Not started | — | TBD | |
| ENR-003 | TBD | TBD | TBD | Not started | — | TBD | |

**Status values:** Not started | In progress | Migrated | Stabilized | Excluded | Parked  
**Execution values:** — | Local pass | Local fail | Pipeline pass | Pipeline fail | Blocked

---

## Vertical Slice Candidates (TBD — select 3–5)

| Candidate | Business value | Complexity | Blockers |
|-----------|----------------|------------|----------|
| TBD | High-value enrollment happy path | TBD | TBD |
| TBD | TBD | TBD | TBD |

---

## Exclusions Log

| Scenario / area | Decision | Reason | Date | Approved by |
|-----------------|----------|--------|------|-------------|
| — | — | — | — | — |

---

## Blockers and Dependencies

| ID | Blocker | Impact | Mitigation | Status |
|----|---------|--------|------------|--------|
| B1 | IDP / Universal Platform integration gaps in legacy suite | Cannot trust legacy baseline | Validate against QC4; update configs | Open |
| B2 | Test data / account availability | Scenarios fail in shared env | TBD — coordinate with data/ACS-5070 | Open |
| B3 | Pilot sequencing vs Mobile 2/1 setup | Schedule conflict | RAID decision | Open |

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
| QC4 smoke | 1–2 GET endpoints + setup | 0.5 sprint |
| QC4 full coverage | All critical endpoints | 2 sprints |
| Stage1 data | Stage1 property/data alignment | 0.5 sprint |

*Assumes dependency on Mobile 1 encryption and Mobile 2 setup if that sequencing is adopted.*

## Related Pages

| Page | Purpose |
|------|---------|
| [04-migration-strategy.md](./04-migration-strategy.md) | Decision matrix and phases |
| [08-regression-suite-and-pipeline-strategy.md](./08-regression-suite-and-pipeline-strategy.md) | Tags and Maven examples |
| [06-unite-mobile1-migration-tracker.md](./06-unite-mobile1-migration-tracker.md) | Next module |
