# Legacy Web Registration – Automation Regression Suite (Prime Version 2)

**Module:** Legacy Web Registration  
**Suite XML:** `suites/v2/daily/stage1-web-registration.xml`  
**Suite Name:** Regression Test Suite - Legacy Web Registration  
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)  
**Environment:** Stage 1  
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`  
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri)

*Reference (format & structure):* `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.2. Legacy Web Registration – Automation Regression Suite (Prime Version 2).pdf`

---

## Legacy Web Registration suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | Legacy (non-IDP) web registration: re-registration (existing account, remove then re-reg and login), first-time account registration, and negative (non–web registered) flows. |
| **When** | Daily, Mon–Fri, as part of Stage 1 nightly regression. |
| **Time** | Suite starts ~12:00 AM – 1:00 AM EST; module duration ~10 minutes. |
| **Where** | Stage 1. Jenkins job: `STAGE1-Daily-Unite-Prime-Regression`. |
| **What plans** | CAD, MND, MID, OKD, COB, RID, COD. |
| **What cases** | 11 test blocks (54 scenarios/methods in latest report). See **Module & plan coverage** and **Test scenarios** below. |
| **Reports** | `reports/v2/Regression Test Suite - Legacy Web Registration 1.html` (and 2, 3). Refresh from Jenkins for latest. |
| **Suite definition** | `suites/v2/daily/stage1-web-registration.xml`. |

---

## Purpose

This module validates legacy (non-IDP) web registration flows for individual account owners. It covers re-registration (existing account removed, then re-reg and login), first-time account registration, and negative scenarios across multiple plans so users can create accounts and access the portal.

---

## Latest Report Summary (from TestNG HTML)

*Source: `reports/v2/Regression Test Suite - Legacy Web Registration 1.html` (and views 2, 3). Run date reflected in report URL (e.g. 20260313).*

| Metric | Value |
|--------|--------|
| Suite | 1 suite, Regression Test Suite - Legacy Web Registration |
| Tests | 11 tests |
| Methods | 54 methods |
| Passed | 52 passed |
| Failed | 2 failed |
| Skipped | 0 |
| XML | stage1-web-registration.xml |

For the latest numbers and method-level details (scenario names, pass/fail), open the HTML reports locally or from Jenkins.

---

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | 11 test blocks |
| Methods (from report) | 54 |
| Approx Duration | ~10 minutes |
| Thread Count | 1 |
| Runner | FeatureRunner |
| Tags | @regression and @dailyrun |
| Plans Covered | CAD, MND, MID, OKD, COB, RID, COD |

---

## Module & plan coverage

*Same format as Confluence PDF. Scenario counts and qTest mapping can be updated from the latest HTML report and qTest.*

| Plan | Flow type | Feature file | Scenario count | qTest mapping | Tags |
|------|-----------|--------------|----------------|---------------|------|
| CAD | Re-registration – Existing account, re-reg and login | Web_Reregistration_Existing_Account.feature | — | — | @regression, @dailyrun |
| MND | Re-registration – Existing account, re-reg and login | Web_Reregistration_Existing_Account.feature | — | — | @regression, @dailyrun |
| MID | Re-registration – Existing account, re-reg and login | Web_Reregistration_Existing_Account.feature | — | — | @regression, @dailyrun |
| OKD | Re-registration – Existing account, re-reg and login | Web_Reregistration_Existing_Account.feature | — | — | @regression, @dailyrun |
| COB | Re-registration (ABLE) – Existing account, re-reg and login | Web_Reregistration_Existing_Account.feature | — | — | @regression, @dailyrun |
| COD | Re-registration – Existing account, re-reg and login | Web_Reregistration_Existing_Account.feature | — | — | @regression, @dailyrun |
| RID | Web Registration – Negative (non–web registered account) | T101_WebRegistrationNegative.feature | — | — | @regression, @dailyrun |
| COD | First-time account – Non–web registered account | Web_Registration_First_Time_Account.feature | — | — | @regression, @dailyrun |
| COB | First-time account (ABLE) – Non–web registered account | Web_Registration_First_Time_Account.feature | — | — | @regression, @dailyrun |
| MND | First-time account – Non–web registered account | Web_Registration_First_Time_Account.feature | — | — | @regression, @dailyrun |
| RID | First-time account – Non–web registered account | Web_Registration_First_Time_Account.feature | — | — | @regression, @dailyrun |

*Scenario count:* Total 54 methods in latest HTML report; per-feature counts can be taken from the report or qTest.  
*qTest mapping:* Link automation to qTest; fill from Confluence or qTest (e.g. TR-xxxxx style IDs).

---

## Test Scenarios (from suite XML)

*Full list of test blocks and feature paths as defined in `suites/v2/daily/stage1-web-registration.xml`.*

| # | Test name | Traunch | Feature path |
|---|-----------|---------|--------------|
| 1 | CAD - Legacy Web Registration and login - Existing, remove registered Accounts, re-reg and login | cad | frontoffice/common/webregistration/feature/Web_Reregistration_Existing_Account.feature |
| 2 | MND - Legacy Web Registration and login - Existing, remove registered Accounts, re-reg and login | mnd | frontoffice/common/webregistration/feature/Web_Reregistration_Existing_Account.feature |
| 3 | MID - Legacy Web Registration and login - Existing, remove registered Accounts, re-reg and login | mid | frontoffice/common/webregistration/feature/Web_Reregistration_Existing_Account.feature |
| 4 | OKD - Legacy Web Registration and login - Existing, remove registered Accounts, re-reg and login | okd | frontoffice/common/webregistration/feature/Web_Reregistration_Existing_Account.feature |
| 5 | COB - Legacy Web Registration and login for ABLE - Existing, remove registered Accounts, re-reg and login | cob | frontoffice/common/webregistration/feature/Web_Reregistration_Existing_Account.feature |
| 6 | RID - Legacy Web Registration Negative-- Non Web Registered Account | rid | frontoffice/common/webregistration/feature/T101_WebRegistrationNegative.feature |
| 7 | COD - Legacy Web Registration and login - Non Web Registered Account | cod | frontoffice/common/webregistration/feature/Web_Registration_First_Time_Account.feature |
| 8 | COB - Legacy Web Registration and login for ABLE - Non Web Registered Account | cob | frontoffice/common/webregistration/feature/Web_Registration_First_Time_Account.feature |
| 9 | MND - Legacy Web Registration and login - Non Web Registered Account | mnd | frontoffice/common/webregistration/feature/Web_Registration_First_Time_Account.feature |
| 10 | RID - Legacy Web Registration and login - Non Web Registered Account | rid | frontoffice/common/webregistration/feature/Web_Registration_First_Time_Account.feature |
| 11 | Legacy Web Registration and login - Existing, remove registered Accounts, re-reg and login | cod | frontoffice/common/webregistration/feature/Web_Reregistration_Existing_Account.feature |

---

## What's covered

- **Re-registration (existing account):** Remove existing web registration, then complete legacy web registration and login (CAD, MND, MID, OKD, COB, COD). Individual account owner flows.
- **First-time account:** Legacy web registration and login for non–web registered accounts (COD, COB, MND, RID).
- **Negative:** Legacy web registration negative – non–web registered account (RID) via `T101_WebRegistrationNegative.feature`.
- **ABLE:** COB-specific flows for ABLE (re-reg and first-time).

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-web-registration.xml` |
| HTML Report (main) | `reports/v2/Regression Test Suite - Legacy Web Registration 1.html` |
| HTML Report (view 2) | `reports/v2/Regression Test Suite - Legacy Web Registration 2.html` |
| HTML Report (view 3) | `reports/v2/Regression Test Suite - Legacy Web Registration 3.html` |
| Old Confluence PDF | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.2. Legacy Web Registration – Automation Regression Suite (Prime Version 2).pdf` |

*Latest results:* Re-run the suite in Jenkins and open the report URL, or replace the HTML files under `reports/v2/` with the latest export to refresh numbers and scenario lists in this doc.

---

## Notes

- **11 test blocks** in suite XML; **54 methods** (scenarios) in latest HTML report.
- **Module & plan coverage:** Fill *Scenario count* and *qTest mapping* from the latest TestNG report and qTest/Confluence when updating this page.
- All tests use **FeatureRunner** (single-threaded). Suite `parallel="tests"` with `thread-count="1"` so tests run sequentially.
