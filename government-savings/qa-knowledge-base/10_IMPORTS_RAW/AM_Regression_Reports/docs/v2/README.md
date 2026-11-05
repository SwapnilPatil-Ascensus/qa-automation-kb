# Prime V2 – Regression Documentation (Start Here)

**↑ Parent hub:** [Automation Regression Suite – docs hub](../README.md) · [full master TOC](../00-automation-regression-master-overview.md)

This folder contains the refreshed, Confluence-ready documentation for the **Prime V2 nightly automation regression suite**.

> **Last refreshed:** 03/2026  
> **Source of truth:** TestNG suite XMLs + HTML execution reports + Confluence PDF exports

---

## Documents

| # | File | What It Covers |
|---|------|----------------|
| 0 | [**00-v2-regression-overview.md**](00-v2-regression-overview.md) | Purpose, environment, schedule, high-level structure, module summary, approximate durations. **Start here.** |
| 1 | [**01-v2-module-coverage.md**](01-v2-module-coverage.md) | Module-by-module breakdown: coverage areas, plans, tags, test counts, runner details, feature paths. |
| 2 | [**02-v2-suite-and-job-details.md**](02-v2-suite-and-job-details.md) | TestNG suite XML details, runner structure, Jenkins job, smoke/release/weekly suites, HTML report locations, archive suites. |
| 3 | [**03-v2-documentation-delta.md**](03-v2-documentation-delta.md) | What changed from old Confluence PDFs: new modules, test growth, restructuring, outdated items. |

## Per-Module Detail Pages (Confluence-Ready)

Located in `modules/` — one page per module, matching the old Confluence format (1.1–1.8) with all details needed to learn about each module.

| # | File | Module |
|---|------|--------|
| 01 | [01-enrollment.md](modules/01-enrollment.md) | Enrollment |
| 02 | [02-legacy-web-registration.md](modules/02-legacy-web-registration.md) | Legacy Web Registration |
| 03 | [03-legacy-web-login.md](modules/03-legacy-web-login.md) | Legacy Web Login |
| 04 | [04-csr-account-maintenance.md](modules/04-csr-account-maintenance.md) | CSR Account Maintenance |
| 05 | [05-contributions.md](modules/05-contributions.md) | Contributions |
| 06 | [06-withdrawals.md](modules/06-withdrawals.md) | Withdrawals |
| 07 | [07-account-balance-page.md](modules/07-account-balance-page.md) | Account Balance Page |
| 08 | [08-sardine-regression.md](modules/08-sardine-regression.md) | Sardine Regression |
| 09 | [09-investment-options.md](modules/09-investment-options.md) | Investment Options (NEW) |
| 10 | [10-empower-plan.md](modules/10-empower-plan.md) | Empower Plan (NEW) |
| 11 | [11-smoke-suites.md](modules/11-smoke-suites.md) | Smoke Suites (CAT / Stage 5 / Stage 2) |
| 12 | [12-release-suites.md](modules/12-release-suites.md) | Release Gate Suites |
| 13 | [13-weekly-backoffice.md](modules/13-weekly-backoffice.md) | Weekly Backoffice Feed Suites |
| 14 | [14-other-specialty.md](modules/14-other-specialty.md) | Other / Specialty Suites |

---

## Quick Facts

| Metric | Value |
|--------|-------|
| Active daily modules | **10** |
| Total nightly tests (XML test blocks) | ~143 |
| Total nightly methods/scenarios | **454+** |
| Plans covered | 25+ |
| Jenkins job | `STAGE1-Daily-Unite-Prime-Regression` |
| Schedule | Daily @ 12:00 AM EST (Mon–Fri) |
| Environment | Stage 1 |
| Framework | Java + Selenium + TestNG + Cucumber (Ant) |
| New modules vs old docs | 2 (Investment Options, Empower Plan) |

---

## Source Files

| Source | Location |
|--------|----------|
| Suite XMLs | `10_IMPORTS_RAW/AM_Regression_Reports/suites/v2/` |
| HTML reports | `10_IMPORTS_RAW/AM_Regression_Reports/reports/v2/` (often gitignored) |
| Master Overview PDF | `10_IMPORTS_RAW/AM_Regression_Reports/reports/Automation Regression Suite – Master Overview.pdf` |
| Old Confluence PDFs | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/` |

---

## How to Use

1. **New to V2 regression?** Read `00-v2-regression-overview.md` for the big picture.
2. **Need module details?** See `01-v2-module-coverage.md` for per-module breakdown.
3. **Need suite/job/pipeline info?** See `02-v2-suite-and-job-details.md`.
4. **Comparing old docs to current?** See `03-v2-documentation-delta.md`.
5. **Publishing to Confluence?** All files are Confluence-ready Markdown — copy and paste.
