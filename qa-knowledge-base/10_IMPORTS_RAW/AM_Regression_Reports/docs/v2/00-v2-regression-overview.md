# Prime V2 – Nightly Regression Suite Overview

**Version:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)  
**Environment:** Stage 1  
**Execution:** Nightly (Mon–Fri) via Jenkins  
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`  
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST  
**Reporting:** TestNG HTML reports + qTest Regression Dashboard  
**Owner:** QA Automation Team (AM Squad)

---

## Purpose

The V2 nightly regression suite validates core 529 and ABLE plan functionality across enrollment, contribution, withdrawal, account maintenance, balance validation, web registration, web login, and Sardine (fraud-detection enrollment) flows. It runs every weeknight against Stage 1 to catch regressions introduced by daily code deployments before they reach downstream environments.

---

## Why We Run It

- **Release gate:** V2 regression is the primary automated validation gate for the monolith application on Stage 1. Failures here trigger bug reporting and main-branch lock per the Bug Handling process.
- **Coverage breadth:** Covers ~95% of core 529 flows across 10+ plans (NYD, NYA, NYB, MID, MND, AKB, ILB, CAD, TNB, PAB, and more).
- **Stability signal:** Nightly pass/fail trend is the leading indicator for release readiness and environment health.

---

## High-Level Structure

The V2 regression is organized into **10 active daily modules**, each with its own TestNG suite XML, plus **smoke**, **release**, **weekly (backoffice)**, and **other (specialty)** suites:

| Category | Suite Count | Purpose |
|----------|-------------|---------|
| **Daily (Active)** | 10 | Nightly front-office regression against Stage 1 |
| **Smoke (Stage 5 / Stage 2)** | 10 | Quick-validation for CAT / partner environments |
| **Release (Stage 1 / Stage 2)** | 3 | Release-gate regression |
| **Weekly (Backoffice)** | 2 | Tuesday & Wednesday backoffice feed processing |
| **Other (Specialty)** | 3 | Flywire, SSgA Conversion, ACH Debit |
| **Archive (Daily – replaced)** | 15 | Older monolithic suites superseded by modular daily suites |

---

## Active Daily Modules (10)

| # | Module | Suite XML | Tests | Approx Duration | Thread Count |
|---|--------|-----------|-------|-----------------|--------------|
| 1 | Enrollment | `stage1-enrollments.xml` | 28 tests / 119 methods | ~3 hrs | 3 |
| 2 | Legacy Web Registration | `stage1-web-registration.xml` | 11 tests / 54 methods | ~10 min | 1 |
| 3 | Legacy Web Login | `stage1-web-login.xml` | 19 tests / 27 methods | ~15 min | 1 |
| 4 | CSR Account Maintenance | `stage1-csr-acct-maintenance.xml` | 14 tests / 24 methods | ~3.5 hrs | 1 |
| 5 | Contributions | `stage1-contributions.xml` | 15 tests / 49 methods | ~9 hrs | 4 |
| 6 | Withdrawals | `stage1-withdrawals.xml` | 14 tests / 73 methods | ~4.5–6 hrs | 4 |
| 7 | Account Balance Page | `stage1-acct-overview.xml` | 10 tests / 10 methods | — | 4 |
| 8 | Sardine Regression | `stage1-sardine-regression.xml` | 10 tests / 29 methods | ~3.5 hrs | 1 |
| 9 | Investment Options | `stage1-investment-options.xml` | 2 tests | — | 1 |
| 10 | Empower Plan | `stage1-empower-plan.xml` | 20 tests | — | 4 |

**Total active daily:** ~143 tests / ~454+ methods (scenarios) executed nightly.

> Duration data sourced from Confluence PDFs (`1.1–1.8`). Modules 9 and 10 are newly added and do not appear in the older Confluence documentation.

---

## Approximate Total Execution Time

Based on available duration data (from Confluence PDFs and sequential/parallel execution):

| Module | Duration |
|--------|----------|
| Enrollment | ~3 hrs |
| Legacy Web Registration | ~10 min |
| Legacy Web Login | ~15 min |
| CSR Account Maintenance | ~3.5 hrs |
| Contributions | ~9 hrs |
| Withdrawals | ~4.5–6 hrs |
| Sardine | ~3.5 hrs |
| Balance Page, Investment Options, Empower | TODO: Needs timing from Jenkins |

Total estimated nightly wall-clock time depends on parallelization across Jenkins executors. Individual module durations suggest **~24–26 hours of sequential test time**, compressed by parallel execution across modules and within modules (thread counts 1–4).

---

## Key Notes for Readers

- **Module-per-XML:** Each module has its own TestNG suite XML under `Regression Suites XMLs/daily/`. This replaced the older monolithic `stage1-frontoffice.xml` (now in `Archive/`).
- **Runner classes:** `com.cs529.qa.prime.runner.FeatureRunner` (sequential) and `com.cs529.qa.prime.runner.ParallelFeatureRunner` (parallel). Most modules use one or both.
- **Tags:** Tests are filtered by `@regression and @dailyrun` (plus module-specific tags like `@sardinerun`, `@ablerun`, `@dailyrun-naa`, `@dailyrun-non-naa`, `@agebasedfundrun`).
- **Parameters:** Each test block specifies `traunch` (plan code, e.g. `nyd`, `mid`, `akb`) and `features` (path to `.feature` file).
- **HTML reports:** Available in `10_IMPORTS_RAW/AM_Regression_Reports/` as `Regression Test Suite - <Module> {1,2,3}.html`. The three numbered files per module are different views of the same execution run.
- **Newly added modules** (not in old Confluence docs): **Investment Options** (`stage1-investment-options.xml`) and **Empower Plan** (`stage1-empower-plan.xml`).

---

## Related Documentation

| Document | Location |
|----------|----------|
| Module-by-module breakdown | [`01-v2-module-coverage.md`](01-v2-module-coverage.md) |
| Suite & job details | [`02-v2-suite-and-job-details.md`](02-v2-suite-and-job-details.md) |
| Documentation delta (old vs current) | [`03-v2-documentation-delta.md`](03-v2-documentation-delta.md) |
| Old Confluence PDFs | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/` |
| Suite XMLs | `10_IMPORTS_RAW/AM_Regression_Reports/Regression Suites XMLs/daily/` |
| HTML reports | `10_IMPORTS_RAW/AM_Regression_Reports/Regression Test Suite - *.html` |

---

**Last refreshed:** 03/2026  
**Source of truth:** Suite XMLs + HTML reports + Confluence PDF exports
