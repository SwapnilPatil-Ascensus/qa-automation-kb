# Withdrawals – Automation Regression Suite (Prime Version 2)

**Module:** Withdrawals (Make a Withdrawal)  
**Suite XML:** `suites/v2/daily/stage1-withdrawals.xml`  
**Suite Name:** Regression Test Suite - Withdrawals  
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)  
**Environment:** Stage 1  
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`  
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri)

*Reference (format & structure):* `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.6. Make a Withdrawal – Automation Regression Suite (Prime Version 2).pdf`

---

## Withdrawals suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | CSR and member withdrawal flows: qualified/non-qualified distributions, K-12 education withdrawals, greenscreen (legacy) withdrawals, systematic withdrawal plan (SWP), Flywire international withdrawals, and negative scenarios. |
| **When** | Daily, Mon–Fri, as part of Stage 1 nightly regression. |
| **Time** | Suite starts ~12:00 AM – 1:00 AM EST; module duration ~4.5–6 hours. |
| **Where** | Stage 1. Jenkins job: `STAGE1-Daily-Unite-Prime-Regression`. |
| **What plans** | MID, NYD, MND, NYA, NYB, IND, WVD. |
| **What cases** | 14 test blocks (73 scenarios/methods in latest report). See **Module & plan coverage** and **Test scenarios** below. |
| **Reports** | `reports/v2/Regression Test Suite - Withdrawals 1.html` (and 2, 3). Refresh from Jenkins for latest. |
| **Suite definition** | `suites/v2/daily/stage1-withdrawals.xml`. |

---

## Purpose

This module validates CSR and member withdrawal flows across multiple plan types, including qualified and non-qualified distributions, K-12 education withdrawals, greenscreen (legacy) withdrawals, systematic withdrawal plans (SWP), and Flywire international withdrawals. It ensures end-to-end withdrawal functionality for both IDP and non-IDP plans.

---

## Latest Report Summary (from TestNG HTML)

*Source: `reports/v2/Regression Test Suite - Withdrawals 1.html` (and views 2, 3). Run date reflected in report URL (e.g. 20260313).*

| Metric | Value |
|--------|--------|
| Suite | 1 suite, Regression Test Suite - Withdrawals |
| Tests | 14 tests |
| Methods | 73 methods |
| Passed | 69 passed |
| Failed | 4 failed |
| Skipped | 0 |
| XML | stage1-withdrawals.xml |

For the latest numbers and method-level details (scenario names, pass/fail), open the HTML reports locally or from Jenkins.

---

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | 14 test blocks |
| Methods (from report) | 73 |
| Approx Duration | ~4.5–6 hours |
| Thread Count | 4 (parallel: tests) |
| Runner | FeatureRunner |
| Tags | @regression and @dailyrun |
| Plans Covered | MID, NYD, MND, NYA, NYB, IND, WVD |

---

## Module & plan coverage

*Same format as Confluence PDF. Scenario counts and qTest mapping can be updated from the latest HTML report and qTest.*

| Plan | Flow type | Feature file | Scenario count | qTest mapping | Tags |
|------|-----------|--------------|----------------|---------------|------|
| MID | CSR Member Withdrawal – Direct (Qualified/Non-Qualified) | QandNQDistribution.feature | — | — | @regression, @dailyrun |
| NYD | CSR Member Withdrawal – K-12 (EBT Prorated) | K12Distribution.feature | — | — | @regression, @dailyrun |
| MND | CSR Member Withdrawal – K-12 (AO Partial, Prorated) | MNDWithdrawal.feature | — | — | @regression, @dailyrun |
| MID | Member Withdrawal – Direct Non-IDP (Qualified/Non-Qualified) | MemberWithdrawal.feature | — | — | @regression, @dailyrun |
| NYD | CSR Member Withdrawal Negative (IDP) | MemberWithdrawalNegativeScenarios.feature | — | — | @regression, @dailyrun |
| MID | CSR Member Withdrawal Negative (Non-IDP) | MemberWithdrawalNegativeScenarios.feature | — | — | @regression, @dailyrun |
| NYA | CSR Member Withdrawal Negative (Advisor) | MemberWithdrawalNegativeScenarios.feature | — | — | @regression, @dailyrun |
| NYD | CSR Greenscreen Withdrawal – Direct (Qualified/Non-Qualified) | CSR_Distribution.feature | — | — | @regression, @dailyrun |
| NYA | CSR Greenscreen Withdrawal – Advisor (Qualified/Non-Qualified) | CSR_Advisor_Distribution.feature | — | — | @regression, @dailyrun |
| NYB | CSR Greenscreen Withdrawal – Able (AO Partial) | CSR_Able_Distribution.feature | — | — | @regression, @dailyrun |
| MND | CSR Systematic Withdrawal (IDP) | SWPAutoNotation.feature | — | — | @regression, @dailyrun |
| MID | CSR Systematic Withdrawal (Non-IDP) | SWPAutoNotation.feature | — | — | @regression, @dailyrun |
| IND | CSR Member Withdrawal – Flywire | INDMODDistribution.feature | — | — | @regression, @dailyrun |
| WVD | CSR Member Withdrawal – Flywire | Distribution.feature | — | — | @regression, @dailyrun |

*Scenario count:* Total 73 methods in latest HTML report; per-feature counts can be taken from the report or qTest.  
*qTest mapping:* Link automation to qTest; fill from Confluence or qTest (e.g. TR-xxxxx style IDs).

---

## Test Scenarios (from suite XML)

*Full list of test blocks and feature paths as defined in `suites/v2/daily/stage1-withdrawals.xml`.*

| # | Test name | Traunch | Feature path |
|---|------------|---------|--------------|
| 1 | CSR Member Withdrawal - MID Direct (Qualified/Non-Qualified) | mid | frontoffice/mid/csr/member/transactions/withdrawal/feature/QandNQDistribution.feature |
| 2 | CSR Member Withdrawal - NYD K-12 (EBT Prorated) | nyd | /frontoffice/csr/member/transactions/withdrawal/feature/K12Distribution.feature |
| 3 | CSR Member Withdrawal - MND K-12 (AO Partial, Prorated) | mnd | frontoffice/csr/member/transactions/withdrawal/feature/MNDWithdrawal.feature |
| 4 | Member Withdrawal - MID Direct Non-IDP (Qualified/Non-Qualified) | mid | frontoffice/common/member/transactions/withdrawal/feature/MemberWithdrawal.feature |
| 5 | CSR Member Withdrawal Negative Scenarios - NYD IDP | nyd | frontoffice/csr/member/transactions/withdrawal/feature/MemberWithdrawalNegativeScenarios.feature |
| 6 | CSR Member Withdrawal Negative Scenarios - MID Non-IDP | mid | frontoffice/csr/member/transactions/withdrawal/feature/MemberWithdrawalNegativeScenarios.feature |
| 7 | CSR Member Withdrawal Negative Scenarios - NYA Advisor | nya | frontoffice/csr/member/transactions/withdrawal/feature/MemberWithdrawalNegativeScenarios.feature |
| 8 | CSR Greenscreen Withdrawal - NYD Direct (Qualified/Non-Qualified) | nyd | frontoffice/csr/csr-greenscreen/transactions/withdrawal/feature/CSR_Distribution.feature |
| 9 | CSR Greenscreen Withdrawal - NYA Advisor (Qualified/Non-Qualified) | nya | frontoffice/csr/csr-greenscreen/transactions/withdrawal/feature/CSR_Advisor_Distribution.feature |
| 10 | CSR Greenscreen Withdrawal - NYB Able (AO Partial) | nyb | frontoffice/csr/csr-greenscreen/transactions/withdrawal/feature/CSR_Able_Distribution.feature |
| 11 | CSR Systematic Withdrawal - MND IDP | mnd | frontoffice/csr/member/transactions/systematicwithdrawal/feature/SWPAutoNotation.feature |
| 12 | CSR Systematic Withdrawal - MID Non-IDP | mid | frontoffice/csr/member/transactions/systematicwithdrawal/feature/SWPAutoNotation.feature |
| 13 | CSR Member Withdrawal - IND Flywire | ind | frontoffice/csr/member/transactions/withdrawal/feature/INDMODDistribution.feature |
| 14 | CSR Member Withdrawal - WVD Flywire | wvd | frontoffice/csr/member/transactions/withdrawal/feature/Distribution.feature |

*Note:* NYD K-12 feature path in XML has a leading slash (`/frontoffice/...`); behavior may depend on runner resolution.

---

## What's covered

- **CSR member withdrawal (positive):** MID direct qualified/non-qualified; NYD K-12 (EBT prorated); MND K-12 (AO partial, prorated).
- **Member portal withdrawal:** MID direct non-IDP (qualified/non-qualified).
- **CSR member withdrawal negative:** NYD (IDP), MID (non-IDP), NYA (advisor) — validation and error scenarios.
- **CSR greenscreen (legacy):** NYD direct (Q/NQ), NYA advisor (Q/NQ), NYB Able (AO partial).
- **CSR systematic withdrawal (SWP):** MND IDP, MID non-IDP — add/edit SWP and auto-notation validation.
- **Flywire (international):** IND, WVD — CSR member withdrawal. *May be flaky; monitor for stability.*

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-withdrawals.xml` |
| HTML Report (main) | `reports/v2/Regression Test Suite - Withdrawals 1.html` |
| HTML Report (view 2) | `reports/v2/Regression Test Suite - Withdrawals 2.html` |
| HTML Report (view 3) | `reports/v2/Regression Test Suite - Withdrawals 3.html` |
| Old Confluence PDF | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.6. Make a Withdrawal – Automation Regression Suite (Prime Version 2).pdf` |

*Latest results:* Re-run the suite in Jenkins and open the report URL, or replace the HTML files under `reports/v2/` with the latest export to refresh numbers and scenario lists in this doc.

---

## Notes

- **14 test blocks** in suite XML; **73 methods** (scenarios) in latest HTML report.
- **Thread count 4:** Suite runs with `parallel="tests"` and `thread-count="4"` for faster execution (~4.5–6 hours).
- **Flywire tests (IND, WVD):** Noted in XML as flaky/out of sync; monitor for stability.
- **Module & plan coverage:** Fill *Scenario count* and *qTest mapping* from the latest TestNG report and qTest/Confluence when updating this page.
- All tests use **FeatureRunner**.
