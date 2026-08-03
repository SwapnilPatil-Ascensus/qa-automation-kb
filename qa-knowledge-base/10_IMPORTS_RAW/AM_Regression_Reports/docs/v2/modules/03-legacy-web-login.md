# Legacy Web Login – Automation Regression Suite (Prime Version 2)

**Module:** Legacy Web Login  
**Suite XML:** `suites/v2/daily/stage1-web-login.xml`  
**Suite Name:** Regression Test Suite - Legacy Web Registration *(labeling mismatch in XML — content is login flows)*  
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)  
**Environment:** Stage 1  
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`  
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri)

*Reference (format & structure):* `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.3. Legacy Web Login – Automation Regression Suite (Prime Version 2).pdf`

---

## Legacy Web Login suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | Legacy (non-IDP) member login: positive and negative login, forgot username (positive/negative), forgot password (positive), and CSR password update. |
| **When** | Daily, Mon–Fri, as part of Stage 1 nightly regression. |
| **Time** | Suite starts ~12:00 AM – 1:00 AM EST; module duration ~15 minutes. |
| **Where** | Stage 1. Jenkins job: `STAGE1-Daily-Unite-Prime-Regression`. |
| **What plans** | MID, CAD, COD, OKD, RIB, PAB, COB. |
| **What cases** | 19 test blocks (27 scenarios/methods in latest report). See **Module & plan coverage** and **Test scenarios** below. |
| **Reports** | `reports/v2/Regression Test Suite - Legacy Web Login 1.html` (and 2, 3). Refresh from Jenkins for latest. |
| **Suite definition** | `suites/v2/daily/stage1-web-login.xml`. |

---

## Purpose

This module validates legacy (non-IDP) member login flows across multiple plans. It covers positive and negative login, forgot username (positive/negative), forgot password (positive), and CSR password update so non-IDP users have secure access to the portal.

---

## Latest Report Summary (from TestNG HTML)

*Source: `reports/v2/Regression Test Suite - Legacy Web Login 1.html` (and views 2, 3). Run date reflected in report URL (e.g. 20260313).*

| Metric | Value |
|--------|--------|
| Suite | 1 suite, Regression Test Suite - Legacy Web Registration *(content = login)* |
| Tests | 19 tests |
| Methods | 27 methods |
| Passed | 27 passed |
| Failed | 0 failed |
| Skipped | 0 |
| XML | stage1-web-login.xml |

For the latest numbers and method-level details (scenario names, pass/fail), open the HTML reports locally or from Jenkins.

---

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | 19 test blocks |
| Methods (from report) | 27 |
| Approx Duration | ~15 minutes |
| Thread Count | 1 |
| Runner | FeatureRunner |
| Tags | @regression and @dailyrun |
| Plans Covered | MID, CAD, COD, OKD, RIB, PAB, COB |

---

## Module & plan coverage

*Same format as Confluence PDF. Scenario counts and qTest mapping can be updated from the latest HTML report and qTest.*

| Plan | Flow type | Feature file | Scenario count | qTest mapping | Tags |
|------|-----------|--------------|----------------|---------------|------|
| MID | Member Login – Positive | T101_LoginPositive.feature | — | — | @regression, @dailyrun |
| MID | Member Login – Negative | T101_LoginNegative.feature | — | — | @regression, @dailyrun |
| CAD | Member Login – Positive | T101_LoginPositive.feature | — | — | @regression, @dailyrun |
| CAD | Member Login – Negative | T101_LoginNegative.feature | — | — | @regression, @dailyrun |
| COD | Member Login – Positive | T101_LoginPositive.feature | — | — | @regression, @dailyrun |
| COD | Member Login – Negative | T101_LoginNegative.feature | — | — | @regression, @dailyrun |
| OKD | Member Login – Positive | T101_LoginPositive.feature | — | — | @regression, @dailyrun |
| OKD | Member Login – Negative | T101_LoginNegative.feature | — | — | @regression, @dailyrun |
| RIB | Able Member Login – Positive | T101_LoginPositive.feature | — | — | @regression, @dailyrun |
| RIB | Able Member Login – Negative | T101_LoginNegative.feature | — | — | @regression, @dailyrun |
| PAB | Able Member Login – Positive | T101_LoginPositive.feature | — | — | @regression, @dailyrun |
| PAB | Able Member Login – Negative | T101_LoginNegative.feature | — | — | @regression, @dailyrun |
| COB | Able Member Login – Positive | T101_LoginPositive.feature | — | — | @regression, @dailyrun |
| COB | Able Member Login – Negative | T101_LoginNegative.feature | — | — | @regression, @dailyrun |
| MID | Forgot Username – Positive (until email send) | T101_ForgotUsernamePositive.feature | — | — | @regression, @dailyrun |
| MID | Forgot Username – Negative | T101_ForgotUsernameNegative.feature | — | — | @regression, @dailyrun |
| OKD | Forgot Username – Positive (until email send) | T101_ForgotUsernamePositive.feature | — | — | @regression, @dailyrun |
| OKD | Forgot Username – Negative | T101_ForgotUsernameNegative.feature | — | — | @regression, @dailyrun |
| MID | Forgot Password – Positive | T101_ForgotPasswordPositive.feature | — | — | @regression, @dailyrun |

*Scenario count:* Total 27 methods in latest HTML report; per-feature counts can be taken from the report or qTest.  
*qTest mapping:* Link automation to qTest; fill from Confluence or qTest (e.g. TR-xxxxx style IDs).

---

## Test Scenarios (from suite XML)

*Full list of test blocks and feature paths as defined in `suites/v2/daily/stage1-web-login.xml`.*

| # | Test name | Traunch | Feature path |
|---|------------|---------|--------------|
| 1 | Legacy(Non-IDP) MID - Member Login - Positive Scenarios | mid | frontoffice/common/login/feature/T101_LoginPositive.feature |
| 2 | Legacy(Non-IDP) MID - Member Login - Negative Scenarios | mid | frontoffice/common/login/feature/T101_LoginNegative.feature |
| 3 | Legacy(Non-IDP) CAD - Member Login - Positive Scenarios | cad | frontoffice/common/login/feature/T101_LoginPositive.feature |
| 4 | Legacy(Non-IDP) CAD - Member Login - Negative Scenarios | cad | frontoffice/common/login/feature/T101_LoginNegative.feature |
| 5 | Legacy(Non-IDP) COD - Member Login - Positive Scenarios | cod | frontoffice/common/login/feature/T101_LoginPositive.feature |
| 6 | Legacy(Non-IDP) COD - Member Login - Negative Scenarios | cod | frontoffice/common/login/feature/T101_LoginNegative.feature |
| 7 | Legacy(Non-IDP) OKD - Member Login - Positive Scenarios | okd | frontoffice/common/login/feature/T101_LoginPositive.feature |
| 8 | Legacy(Non-IDP) OKD - Member Login - Negative Scenarios | okd | frontoffice/common/login/feature/T101_LoginNegative.feature |
| 9 | Legacy(Non-IDP) RIB - Able Member Login - Positive Scenarios | rib | frontoffice/common/login/feature/T101_LoginPositive.feature |
| 10 | Legacy(Non-IDP) RIB - Able Member Login - Negative Scenarios | rib | frontoffice/common/login/feature/T101_LoginNegative.feature |
| 11 | Legacy(Non-IDP) PAB - Able Member Login - Positive Scenarios | pab | frontoffice/common/login/feature/T101_LoginPositive.feature |
| 12 | Legacy(Non-IDP) PAB - Able Member Login - Negative Scenarios | pab | frontoffice/common/login/feature/T101_LoginNegative.feature |
| 13 | Legacy(Non-IDP) COB - Able Member Login - Positive Scenarios | cob | frontoffice/common/login/feature/T101_LoginPositive.feature |
| 14 | Legacy(Non-IDP) COB - Able Member Login - Negative Scenarios | cob | frontoffice/common/login/feature/T101_LoginNegative.feature |
| 15 | Legacy(Non-IDP) MID Login - Forgot Username - Positive Scenarios until Email send | mid | frontoffice/common/login/feature/T101_ForgotUsernamePositive.feature |
| 16 | Legacy(Non-IDP) MID - Forgot Username - Negative Scenarios | mid | frontoffice/common/login/feature/T101_ForgotUsernameNegative.feature |
| 17 | Legacy(Non-IDP) OKD Login - Forgot Username - Positive Scenarios until Email send | okd | frontoffice/common/login/feature/T101_ForgotUsernamePositive.feature |
| 18 | Legacy(Non-IDP) OKD - Forgot Username - Negative Scenarios | okd | frontoffice/common/login/feature/T101_ForgotUsernameNegative.feature |
| 19 | Non-IDP MID Login - Forgot Password - Positive Test Case | mid | frontoffice/common/login/feature/T101_ForgotPasswordPositive.feature |

*Commented out in XML (not run):* Legacy(Non-IDP) Member Login - Forgot Password - Negative Test Case.

---

## What's covered

- **Member login – positive:** Legacy (non-IDP) login success (MID, CAD, COD, OKD, RIB, PAB, COB).
- **Member login – negative:** Invalid credentials, login page validation (same plans).
- **ABLE member login:** RIB, PAB, COB – positive and negative.
- **Forgot username:** Positive (until email send) and negative for MID and OKD.
- **Forgot password:** Positive for MID. (Forgot password negative is commented out in suite.)
- **CSR password update:** Covered via login flow (e.g. positive login scenarios).

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-web-login.xml` |
| HTML Report (main) | `reports/v2/Regression Test Suite - Legacy Web Login 1.html` |
| HTML Report (view 2) | `reports/v2/Regression Test Suite - Legacy Web Login 2.html` |
| HTML Report (view 3) | `reports/v2/Regression Test Suite - Legacy Web Login 3.html` |
| Old Confluence PDF | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.3. Legacy Web Login – Automation Regression Suite (Prime Version 2).pdf` |

*Latest results:* Re-run the suite in Jenkins and open the report URL, or replace the HTML files under `reports/v2/` with the latest export to refresh numbers and scenario lists in this doc.

---

## Notes

- **19 test blocks** in suite XML; **27 methods** (scenarios) in latest HTML report.
- **Labeling mismatch:** Suite `name` in XML and HTML is "Regression Test Suite - Legacy Web Registration"; the suite runs **login** flows (stage1-web-login.xml). Keep this in mind when searching reports.
- **Module & plan coverage:** Fill *Scenario count* and *qTest mapping* from the latest TestNG report and qTest/Confluence when updating this page.
- All tests use **FeatureRunner** (thread-count 1). Forgot Password Negative is commented out in XML.
