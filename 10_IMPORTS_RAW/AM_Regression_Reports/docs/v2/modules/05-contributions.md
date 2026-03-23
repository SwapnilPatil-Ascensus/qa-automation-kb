# Contributions – Automation Regression Suite (Prime Version 2)

**Module:** Contributions  
**Suite XML:** `suites/v2/daily/stage1-contributions.xml`  
**Suite Name:** Regression Test Suite - Contributions  
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)  
**Environment:** Stage 1  
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`  
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri)

*Reference (format & structure):* `10_IMPORTS_RAW/confluence_exports/Automation QA - Home & Documentation Hub/Automation Regression Suite - Master Overview/1.5. Contributions – Automation Regression Suite (Prime Version 2).pdf`

---

## Contributions suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | Contribution flows: CSR member single contribution (direct, advisor, ABLE), AIP (recurring) setup and contribution, AIP update/add/edit/delete via CSR, and member contribution negative scenarios. |
| **When** | Daily, Mon–Fri, as part of Stage 1 nightly regression. |
| **Time** | Suite starts ~12:00 AM – 1:00 AM EST; module duration ~9 hours. |
| **Where** | Stage 1. Jenkins job: `STAGE1-Daily-Unite-Prime-Regression`. |
| **What plans** | NYD, NYA, NYB, MID. |
| **What cases** | 15 test blocks (49 scenarios/methods in latest report). See **Module & plan coverage** and **Test scenarios** below. |
| **Reports** | `reports/v2/Regression Test Suite - Contributions 1.html` (and 2, 3). Refresh from Jenkins for latest. |
| **Suite definition** | `suites/v2/daily/stage1-contributions.xml`. |

---

## Purpose

This module validates contribution flows including single contributions, AIP (Automatic Investment Plan) setup and updates, and negative scenarios. It covers IDP and non-IDP AIP flows, CSR-driven single and recurring contributions, and member contribution negative validation across NY and MI plans.

---

## Latest Report Summary (from TestNG HTML)

*Source: `reports/v2/Regression Test Suite - Contributions 1.html` (and views 2, 3). Run date reflected in report URL (e.g. 20260313).*

| Metric | Value |
|--------|--------|
| Suite | 1 suite, Regression Test Suite - Contributions |
| Tests | 15 tests |
| Methods | 49 methods |
| Passed | 42 passed |
| Failed | 7 failed |
| Skipped | 0 |
| XML | stage1-contributions.xml |

For the latest numbers and method-level details (scenario names, pass/fail), open the HTML reports locally or from Jenkins.

---

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | 15 test blocks |
| Methods (from report) | 49 |
| Approx Duration | ~9 hours |
| Thread Count | 4 (parallel: tests) |
| Runner | FeatureRunner |
| Tags | @regression and @dailyrun, @ablerun (NY Able AIP) |
| Plans Covered | NYD, NYA, NYB, MID |

---

## Module & plan coverage

*Same format as Confluence PDF. Scenario counts and qTest mapping can be updated from the latest HTML report and qTest.*

| Plan | Flow type | Feature file | Scenario count | qTest mapping | Tags |
|------|-----------|--------------|----------------|---------------|------|
| NYD | CSR Member Single Contribution (Direct) | MemberSingleContribution.feature | — | — | @regression, @dailyrun |
| NYA | CSR Member Single Contribution (Advisor) | MemberSingleContribution.feature | — | — | @regression, @dailyrun |
| NYB | CSR Member Single Contribution (Able) | AbleMemberSingleContribution.feature | — | — | @regression, @dailyrun |
| NYD | CSR Member Single AIP Contribution (IDP Direct) | AIPContribution.feature | — | — | @regression, @dailyrun |
| MID | CSR Member Single AIP Contribution (Non-IDP Direct) | AIPContribution.feature | — | — | @regression, @dailyrun |
| NYA | CSR Member Single AIP Contribution (Advisor) | AIPContribution.feature | — | — | @regression, @dailyrun |
| NYB | CSR Member Single AIP Contribution (Able) | AIPContribution.feature | — | — | @regression, @ablerun |
| NYD | AIP update via CSR for member (IDP Direct) | AIPAddEditDeleteNonCustom.feature | — | — | @regression, @dailyrun |
| MID | AIP update via CSR for member (Non-IDP Direct) | AIPAddEditDeleteNonCustom.feature | — | — | @regression, @dailyrun |
| NYB | AIP update via CSR for member (Able) | AIPAddEditDeleteNonCustom.feature | — | — | @regression, @dailyrun |
| NYA | AIP update via CSR for member (Advisor) | AIPAddEditDeleteNonCustom.feature | — | — | @regression, @dailyrun |
| NYA | AIP Add/Edit/Delete via CSR for member | AIPAddEditDelete.feature | — | — | @regression, @dailyrun |
| NYD | Member Contribution Negative via CSR (IDP Direct) | MemberContributionNegative.feature | — | — | @regression, @dailyrun |
| MID | Member Contribution Negative via CSR (Non-IDP Direct) | MemberContributionNegative.feature | — | — | @regression, @dailyrun |
| NYA | Member Contribution Negative via CSR (Advisor) | MemberContributionNegative.feature | — | — | @regression, @dailyrun |

*Scenario count:* Total 49 methods in latest HTML report; per-feature counts can be taken from the report or qTest.  
*qTest mapping:* Link automation to qTest; fill from Confluence or qTest (e.g. TR-xxxxx style IDs).

---

## Test Scenarios (from suite XML)

*Full list of test blocks and feature paths as defined in `suites/v2/daily/stage1-contributions.xml`.*

| # | Test name | Traunch | Feature path |
|---|------------|---------|--------------|
| 1 | NYD - Direct CSR Member Single Contribution | nyd | frontoffice/csr/member/transactions/contributions/feature/MemberSingleContribution.feature |
| 2 | NYA - Advisor CSR Member Single Contribution | nya | frontoffice/csr/member/transactions/contributions/feature/MemberSingleContribution.feature |
| 3 | NYB - Able CSR Member Single Contribution | nyb | frontoffice/csr/member/transactions/contributions/feature/AbleMemberSingleContribution.feature |
| 4 | IDP plan - NY Direct CSR Member Single AIP Contribution | nyd | frontoffice/csr/member/transactions/contributions/feature/AIPContribution.feature |
| 5 | Non-IDP plan - MI Direct CSR Member Single AIP Contribution | mid | frontoffice/csr/member/transactions/contributions/feature/AIPContribution.feature |
| 6 | NY Advisor CSR Member Single AIP Contribution | nya | frontoffice/csr/member/transactions/contributions/feature/AIPContribution.feature |
| 7 | NY Able CSR Member Single AIP Contribution | nyb | frontoffice/csr/member/transactions/contributions/feature/AIPContribution.feature |
| 8 | IDP Plan - NY Direct AIP update via CSR for member | nyd | frontoffice/csr/member/transactions/contributions/feature/AIPAddEditDeleteNonCustom.feature |
| 9 | Non-IDP Plan - MI Direct AIP update via CSR for member | mid | frontoffice/csr/member/transactions/contributions/feature/AIPAddEditDeleteNonCustom.feature |
| 10 | NY Able AIP update via CSR for member | nyb | frontoffice/csr/member/transactions/contributions/feature/AIPAddEditDeleteNonCustom.feature |
| 11 | NY Advisor AIP update via CSR for member | nya | frontoffice/csr/member/transactions/contributions/feature/AIPAddEditDeleteNonCustom.feature |
| 12 | NYA AIP update via CSR for member | nya | frontoffice/csr/member/transactions/contributions/feature/AIPAddEditDelete.feature |
| 13 | IDP - NY Direct Member Contribution Negative Scenarios via CSR | nyd | frontoffice/common/csr/transactions/contributions/feature/MemberContributionNegative.feature |
| 14 | Non-IDP - MI Direct Member Contribution Negative Scenarios via CSR | mid | frontoffice/common/csr/transactions/contributions/feature/MemberContributionNegative.feature |
| 15 | NY Advisor Member Contribution Negative Scenarios via CSR | nya | frontoffice/common/csr/transactions/contributions/feature/MemberContributionNegative.feature |

---

## What's covered

- **CSR member single contribution:** Direct (NYD), Advisor (NYA), Able (NYB) — `MemberSingleContribution.feature` / `AbleMemberSingleContribution.feature`.
- **CSR member single AIP (recurring):** IDP NY Direct, Non-IDP MI Direct, NY Advisor, NY Able — `AIPContribution.feature`. NY Able uses `@ablerun` tag.
- **AIP update via CSR:** Add/edit/delete or non-custom AIP for NYD, MID, NYB, NYA — `AIPAddEditDeleteNonCustom.feature` and `AIPAddEditDelete.feature` (NYA).
- **Member contribution negative:** Invalid or boundary scenarios via CSR for NYD, MID, NYA — `MemberContributionNegative.feature`.

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-contributions.xml` |
| HTML Report (main) | `reports/v2/Regression Test Suite - Contributions 1.html` |
| HTML Report (view 2) | `reports/v2/Regression Test Suite - Contributions 2.html` |
| HTML Report (view 3) | `reports/v2/Regression Test Suite - Contributions 3.html` |
| Old Confluence PDF | `10_IMPORTS_RAW/confluence_exports/Automation QA - Home & Documentation Hub/Automation Regression Suite - Master Overview/1.5. Contributions – Automation Regression Suite (Prime Version 2).pdf` |

*Latest results:* Re-run the suite in Jenkins and open the report URL, or replace the HTML files under `reports/v2/` with the latest export to refresh numbers and scenario lists in this doc.

---

## Notes

- **15 test blocks** in suite XML; **49 methods** (scenarios) in latest HTML report.
- **Thread count 4:** Suite runs with `parallel="tests"` and `thread-count="4"` for faster execution (~9 hours).
- **NY Able AIP** uses tag `@ablerun` (in addition to `@regression and @dailyrun` in other tests).
- **Module & plan coverage:** Fill *Scenario count* and *qTest mapping* from the latest TestNG report and qTest/Confluence when updating this page.
- All tests use **FeatureRunner**.
