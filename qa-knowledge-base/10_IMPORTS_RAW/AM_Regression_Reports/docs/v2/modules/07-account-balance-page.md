# Account Balance Page – Automation Regression Suite (Prime Version 2)

**Module:** Account Balance Page (Balance Page)  
**Suite XML:** `suites/v2/daily/stage1-acct-overview.xml`  
**Suite Name:** Regression Test Suite - Account Balance Page  
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)  
**Environment:** Stage 1  
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`  
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri)

*Reference (format & structure):* `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.7. Balance Page – Automation Regression Suite (Prime Version 2).pdf`

---

## Account Balance Page suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | Account Balance page validation via CSR and member portal: balance display and validation for IDP/non-IDP direct plans, ABLE plans, advisor plans, and legacy member balance (MND). |
| **When** | Daily, Mon–Fri, as part of Stage 1 nightly regression. |
| **Time** | Suite starts ~12:00 AM – 1:00 AM EST; module duration not separately reported (short run). |
| **Where** | Stage 1. Jenkins job: `STAGE1-Daily-Unite-Prime-Regression`. |
| **What plans** | NJD, NMD, NYD, RID, AKB, MIB, RIB, NYA, RIA, MND. |
| **What cases** | 10 test blocks (10 scenarios/methods in latest report). See **Module & plan coverage** and **Test scenarios** below. |
| **Reports** | `reports/v2/Regression Test Suite - Account Balance Page 1.html` (and 2, 3). Refresh from Jenkins for latest. |
| **Suite definition** | `suites/v2/daily/stage1-acct-overview.xml`. |

---

## Purpose

This module validates the Account Balance page across CSR and member portal interfaces. It covers IDP and non-IDP direct plans, ABLE plans, and advisor plans, ensuring balance display and validation logic work correctly for each plan type and access channel.

---

## Latest Report Summary (from TestNG HTML)

*Source: `reports/v2/Regression Test Suite - Account Balance Page 1.html` (and views 2, 3). Run date reflected in report URL (e.g. 20260313).*

| Metric | Value |
|--------|--------|
| Suite | 1 suite, Regression Test Suite - Account Balance Page |
| Tests | 10 tests |
| Methods | 10 methods |
| Passed | 7 passed |
| Failed | 3 failed |
| Skipped | 0 |
| XML | stage1-acct-overview.xml |

For the latest numbers and method-level details (scenario names, pass/fail), open the HTML reports locally or from Jenkins.

---

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | 10 test blocks |
| Methods (from report) | 10 |
| Approx Duration | Not separately reported |
| Thread Count | 4 (parallel: tests) |
| Runners | ParallelFeatureRunner (9 tests), FeatureRunner (1 test – MND member balance) |
| Tags | @regression and @dailyrun |
| Plans Covered | NJD, NMD, NYD, RID, AKB, MIB, RIB, NYA, RIA, MND |

---

## Module & plan coverage

*Same format as Confluence PDF. Scenario counts and qTest mapping can be updated from the latest HTML report and qTest.*

| Plan | Flow type | Feature file | Scenario count | qTest mapping | Tags |
|------|-----------|--------------|----------------|---------------|------|
| NJD | Account Balance Validation via CSR – Direct (IDP) | BalancePageValidation.feature | — | — | @regression, @dailyrun |
| NMD | Account Balance Validation via CSR – Direct (IDP) | BalancePageValidation.feature | — | — | @regression, @dailyrun |
| NYD | Account Balance Validation via CSR – Direct (Non-IDP) | BalancePageValidation.feature | — | — | @regression, @dailyrun |
| RID | Account Balance Validation via CSR – Direct (Non-IDP) | BalancePageValidation.feature | — | — | @regression, @dailyrun |
| AKB | Account Balance Validation via CSR – Able (IDP) | BalancePageValidation.feature | — | — | @regression, @dailyrun |
| MIB | Account Balance Validation via CSR – Able (IDP) | BalancePageValidation.feature | — | — | @regression, @dailyrun |
| RIB | Account Balance Validation via CSR – Able (Non-IDP) | BalancePageValidation.feature | — | — | @regression, @dailyrun |
| NYA | Account Balance Validation via CSR – Advisor | BalancePageValidation.feature | — | — | @regression, @dailyrun |
| RIA | Account Balance Validation via CSR – Advisor | BalancePageValidation.feature | — | — | @regression, @dailyrun |
| MND | Member Balance Page Validation – Direct Legacy (via member portal) | MemberBalancePageValidation.feature | — | — | @regression, @dailyrun |

*Scenario count:* Total 10 methods in latest HTML report (1:1 with test blocks).  
*qTest mapping:* Link automation to qTest; fill from Confluence or qTest (e.g. TR-xxxxx style IDs).

---

## Test Scenarios (from suite XML)

*Full list of test blocks and feature paths as defined in `suites/v2/daily/stage1-acct-overview.xml`.*

| # | Test name | Traunch | Feature path |
|---|------------|---------|--------------|
| 1 | Account Balance Validation via CSR - NJ Direct (IDP) | njd | frontoffice/csr/balancepage/feature/BalancePageValidation.feature |
| 2 | Account Balance Validation via CSR - NM Direct (IDP) | nmd | frontoffice/csr/balancepage/feature/BalancePageValidation.feature |
| 3 | Account Balance Validation via CSR - NY Direct (Non-IDP) | nyd | frontoffice/csr/balancepage/feature/BalancePageValidation.feature |
| 4 | Account Balance Validation via CSR - RI Direct (Non-IDP) | rid | frontoffice/csr/balancepage/feature/BalancePageValidation.feature |
| 5 | Account Balance Validation via CSR - AK Able (IDP) | akb | frontoffice/csr/balancepage/feature/BalancePageValidation.feature |
| 6 | Account Balance Validation via CSR - MI Able (IDP) | mib | frontoffice/csr/balancepage/feature/BalancePageValidation.feature |
| 7 | Account Balance Validation via CSR - RI Able (Non-IDP) | rib | frontoffice/csr/balancepage/feature/BalancePageValidation.feature |
| 8 | Account Balance Validation via CSR - NY Advisor | nya | frontoffice/csr/balancepage/feature/BalancePageValidation.feature |
| 9 | Account Balance Validation via CSR - RI Advisor | ria | frontoffice/csr/balancepage/feature/BalancePageValidation.feature |
| 10 | Member Balance Page Validation via CSR - MND Direct Legacy | mnd | frontoffice/csr/balancepage/feature/MemberBalancePageValidation.feature |

---

## What's covered

- **CSR balance validation (BalancePageValidation.feature):** IDP direct (NJ, NM), non-IDP direct (NY, RI), IDP Able (AK, MI), non-IDP Able (RI), advisor (NY, RI). One test per plan; validates balance display via CSR.
- **Member balance (MemberBalancePageValidation.feature):** MND direct legacy — legacy web-registered member login and balance validation via member portal.

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-acct-overview.xml` |
| HTML Report (main) | `reports/v2/Regression Test Suite - Account Balance Page 1.html` |
| HTML Report (view 2) | `reports/v2/Regression Test Suite - Account Balance Page 2.html` |
| HTML Report (view 3) | `reports/v2/Regression Test Suite - Account Balance Page 3.html` |
| Old Confluence PDF | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.7. Balance Page – Automation Regression Suite (Prime Version 2).pdf` |

*Latest results:* Re-run the suite in Jenkins and open the report URL, or replace the HTML files under `reports/v2/` with the latest export to refresh numbers and scenario lists in this doc.

---

## Notes

- **10 test blocks** in suite XML; **10 methods** (scenarios) in latest HTML report — one scenario per test.
- **Naming convention (XML):** "Account Balance Validation via CSR - &lt;State&gt; &lt;PlanType&gt; (&lt;IDP|Non-IDP&gt;)". Advisor plans omit IDP qualifier. Do not modify feature or parameter values without product approval.
- **MND test:** Uses **FeatureRunner** and **MemberBalancePageValidation.feature** (member portal / legacy); all other tests use **ParallelFeatureRunner** and **BalancePageValidation.feature** (CSR).
- **Module & plan coverage:** Fill *Scenario count* and *qTest mapping* from the latest TestNG report and qTest/Confluence when updating this page.
