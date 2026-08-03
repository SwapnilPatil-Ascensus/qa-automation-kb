# 06 — Unite Mobile 1 Migration Tracker

## Executive Summary

**Unite Mobile 1** migration follows the pattern established by the pilot module (**Unite Enrollment**). This module adds **encryption-handling** complexity. Tracker fields are TBD until Enrollment vertical slice completes.

| Field | Value |
|-------|-------|
| Module | Unite Mobile 1 |
| Priority | 2 |
| Target folder | `mobile-automation/unite-mobile1/` |
| Program status | Not started |
| Estimate | 2–4 weeks (after Enrollment) |

---

## Module Metadata

| Attribute | Value |
|-----------|-------|
| Source repository | TBD — UniteMSC `unite-mobile1` service path |
| Target repository | API Automation Framework |
| Primary tags | `@mobile`, `@uniteMobile1`, `@smoke`, `@regression` |
| Special focus | Encryption handling (per team estimates) |
| Prerequisites | Enrollment migration pattern proven; encryption utilities reusable |

---

## Discovery Inventory (TBD)

| Category | Count | Notes |
|----------|-------|-------|
| Feature files | TBD | |
| Scenarios (total) | TBD | |
| Step definition classes | TBD | |
| Unique endpoints | TBD | |
| Encryption-related steps | TBD | Flag for refactor |

---

## Scenario Migration Tracker

| ID | Scenario name | Source feature | Decision | Status | Execution | Owner | Notes |
|----|---------------|----------------|----------|--------|-----------|-------|-------|
| M1-001 | TBD | TBD | TBD | Not started | — | TBD | |
| M1-002 | TBD | TBD | TBD | Not started | — | TBD | |

---

## Exclusions Log

| Scenario / area | Decision | Reason | Date | Approved by |
|-----------------|----------|--------|------|-------------|
| — | — | — | — | — |

---

## Blockers and Dependencies

| ID | Blocker | Impact | Mitigation | Status |
|----|---------|--------|------------|--------|
| B1 | Encryption patterns not standardized in target framework | Migration delay | Reuse from Enrollment + Mobile 2 if sequenced first | Open |
| B2 | Enrollment pilot incomplete | No proven template | Complete Enrollment vertical slice | Open |

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
| QC4 smoke | 1–2 GET endpoints + encryption handling | 0.75 sprint |
| QC4 full coverage | All critical endpoints | 2 sprints |
| Stage1 data | Stage1 alignment | 0.5 sprint |

*Assumes setup patterns from Mobile 2.*

## Related Pages

| Page | Purpose |
|------|---------|
| [05-unite-enrollment-migration-tracker.md](./05-unite-enrollment-migration-tracker.md) | Pilot module |
| [07-unite-mobile2-migration-tracker.md](./07-unite-mobile2-migration-tracker.md) | Next module |
