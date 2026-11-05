# CSR Account Maintenance – Automation Regression Suite (Prime Version 2)

**Module:** CSR Account Maintenance  
**Suite XML:** `suites/v2/daily/stage1-csr-acct-maintenance.xml`  
**Suite Name:** Regression Test Suite - Account or Profile Maintenance  
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)  
**Environment:** Stage 1  
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`  
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri)

*Reference (format & structure):* `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.4. CSR Account Maintenance – Automation Regression Suite (Prime Version 2).pdf`

---

## CSR Account Maintenance suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | CSR-driven account and profile maintenance: personal information update, bank profile, beneficiary, delivery preferences, security questions, payroll deduction across direct, ABLE, and advisor plans. |
| **When** | Daily, Mon–Fri, as part of Stage 1 nightly regression. |
| **Time** | Suite starts ~12:00 AM – 1:00 AM EST; module duration ~3.5 hours. |
| **Where** | Stage 1. Jenkins job: `STAGE1-Daily-Unite-Prime-Regression`. |
| **What plans** | KSD, NYB, ILB, AKB, NYA, NYD, RID. |
| **What cases** | 14 test blocks (24 scenarios/methods in latest report). See **Module & plan coverage** and **Test scenarios** below. |
| **Reports** | `reports/v2/Regression Test Suite - Account or Profile Maintenance 1.html` (and 2, 3). Refresh from Jenkins for latest. |
| **Suite definition** | `suites/v2/daily/stage1-csr-acct-maintenance.xml`. |

---

## Purpose

This module validates CSR-driven account and profile maintenance flows. It covers personal information updates, bank profile maintenance, beneficiary changes, delivery preferences, security questions, and payroll deduction across multiple plans so CSR agents can correctly maintain member accounts.

---

## Latest Report Summary (from TestNG HTML)

*Source: `reports/v2/Regression Test Suite - Account or Profile Maintenance 1.html` (and views 2, 3). Run date reflected in report URL (e.g. 20260313).*

| Metric | Value |
|--------|--------|
| Suite | 1 suite, Regression Test Suite - Account or Profile Maintenance |
| Tests | 14 tests |
| Methods | 24 methods |
| Passed | 21 passed |
| Failed | 3 failed |
| Skipped | 0 |
| XML | stage1-csr-acct-maintenance.xml |

For the latest numbers and method-level details (scenario names, pass/fail), open the HTML reports locally or from Jenkins.

---

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | 14 test blocks |
| Methods (from report) | 24 |
| Approx Duration | ~3.5 hours |
| Thread Count | 1 |
| Runners | FeatureRunner, ParallelFeatureRunner |
| Tags | @regression and @dailyrun |
| Plans Covered | KSD, NYB, ILB, AKB, NYA, NYD, RID |

---

## Module & plan coverage

*Same format as Confluence PDF. Scenario counts and qTest mapping can be updated from the latest HTML report and qTest.*

| Plan | Flow type | Feature file | Scenario count | qTest mapping | Tags |
|------|-----------|--------------|----------------|---------------|------|
| KSD | CSR-Member Profile – Update Personal Information (Non-IDP Direct) | PersonalInformation.feature | — | — | @regression, @dailyrun |
| NYB | CSR-Member Profile – Update Personal Information (Non-IDP Able) | PersonalInformation.feature | — | — | @regression, @dailyrun |
| ILB | CSR-Member Profile – Update Personal Information (IDP Able) | PersonalInformation.feature | — | — | @regression, @dailyrun |
| AKB | CSR-Member Profile – Update Personal Information (IDP Able) | PersonalInformation.feature | — | — | @regression, @dailyrun |
| NYA | CSR-Member Profile – Update Personal Information (Non-IDP Advisor) | PersonalInformation.feature | — | — | @regression, @dailyrun |
| NYD | CSR-Member Profile – Bank Profile Maintenance (IDP Direct) | BankInformation.feature | — | — | @regression, @dailyrun |
| RID | CSR-Member Profile – Bank Profile Maintenance (Non-IDP Direct) | BankInformation.feature | — | — | @regression, @dailyrun |
| AKB | CSR-Member Profile – Bank Profile Maintenance (IDP Able) | BankInformation.feature | — | — | @regression, @dailyrun |
| NYB | CSR-Member Profile – Bank Profile Maintenance (Non-IDP Able) | BankInformation.feature | — | — | @regression, @dailyrun |
| NYA | CSR-Member Profile – Bank Profile Maintenance (Advisor) | BankInformation.feature | — | — | @regression, @dailyrun |
| NYD | CSR-Member Profile – Maintain Beneficiary Information | Beneficiary.feature | — | — | @regression, @dailyrun |
| NYD | CSR-Member Profile – Update Delivery Preferences | DeliveryPreference.feature | — | — | @regression, @dailyrun |
| KSD | CSR-Member Profile – Maintain Security Questions | SecurityQuestions.feature | — | — | @regression, @dailyrun |
| NYD | CSR-Member Profile – Maintain Payroll Deduction | PayrollDeduction.feature | — | — | @regression, @dailyrun |

*Scenario count:* Total 24 methods in latest HTML report; per-feature counts can be taken from the report or qTest.  
*qTest mapping:* Link automation to qTest; fill from Confluence or qTest (e.g. TR-xxxxx style IDs).

---

## Test Scenarios (from suite XML)

*Full list of test blocks and feature paths as defined in `suites/v2/daily/stage1-csr-acct-maintenance.xml`.*

| # | Test name | Traunch | Feature path |
|---|------------|---------|--------------|
| 1 | Non-IDP Plans - KS Direct CSR-Member Profile Maintenance - Update Personal Information | ksd | frontoffice/csr/member/profileanddocuments/feature/PersonalInformation.feature |
| 2 | Non IDP Plans - NY Able CSR-Member Profile Maintenance - Update Personal Information | nyb | frontoffice/csr/member/profileanddocuments/feature/PersonalInformation.feature |
| 3 | IDP Plans - IL Able CSR-Member Profile Maintenance - Update Personal Information | ilb | frontoffice/csr/member/profileanddocuments/feature/PersonalInformation.feature |
| 4 | IDP Plans - AK Able CSR-Member Profile Maintenance - Update Personal Information | akb | frontoffice/csr/member/profileanddocuments/feature/PersonalInformation.feature |
| 5 | non IDP Plan - NY Advisor CSR-Member Profile Maintenance - Update Personal Information | nya | frontoffice/csr/member/profileanddocuments/feature/PersonalInformation.feature |
| 6 | IDP - NY Direct CSR-Member Profile - Bank Profile Maintenance | nyd | frontoffice/csr/member/profileanddocuments/feature/BankInformation.feature |
| 7 | Non IDP - RI Direct CSR-Member Profile - Bank Profile Maintenance | rid | frontoffice/csr/member/profileanddocuments/feature/BankInformation.feature |
| 8 | IDP - AK Able CSR-Member Profile - Bank Profile Maintenance | akb | frontoffice/csr/member/profileanddocuments/feature/BankInformation.feature |
| 9 | Non IDP - NY Able CSR-Member Profile - Bank Profile Maintenance | nyb | frontoffice/csr/member/profileanddocuments/feature/BankInformation.feature |
| 10 | NY Advisor CSR-Member Profile - Bank Profile Maintenance | nya | frontoffice/csr/member/profileanddocuments/feature/BankInformation.feature |
| 11 | NYD CSR-Member Profile Maintenance - Maintain Beneficiary Information | nyd | frontoffice/csr/member/profileanddocuments/feature/Beneficiary.feature |
| 12 | NYD CSR-Member Profile Maintenance - Update Delivery Preferences | nyd | frontoffice/csr/member/profileanddocuments/feature/DeliveryPreference.feature |
| 13 | NYD CSR-Member Profile Maintenance - Maintain Security Questions | ksd | frontoffice/csr/member/profileanddocuments/feature/SecurityQuestions.feature |
| 14 | NYD CSR-Member Profile Maintenance - Maintain Payroll Deduction | nyd | frontoffice/csr/member/profileanddocuments/feature/PayrollDeduction.feature |

*Commented out in XML (not run):* IDP Plans - NY Direct and NJ Direct CSR-Member Profile Maintenance - Update Personal Information.

---

## What's covered

- **Personal information:** CSR update of member personal info (phone, address, etc.) for KSD (direct), NYB/ILB/AKB (ABLE), NYA (advisor). IDP plans NYD/NJD are commented out.
- **Bank profile:** Add/edit/delete bank information for NYD (IDP direct), RID (non-IDP direct), AKB (IDP able), NYB (non-IDP able), NYA (advisor).
- **Beneficiary:** Maintain beneficiary information (NYD).
- **Delivery preferences:** Update delivery preferences (NYD).
- **Security questions:** Maintain security questions (KSD).
- **Payroll deduction:** Maintain payroll deduction (NYD).

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-csr-acct-maintenance.xml` |
| HTML Report (main) | `reports/v2/Regression Test Suite - Account or Profile Maintenance 1.html` |
| HTML Report (view 2) | `reports/v2/Regression Test Suite - Account or Profile Maintenance 2.html` |
| HTML Report (view 3) | `reports/v2/Regression Test Suite - Account or Profile Maintenance 3.html` |
| Old Confluence PDF | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.4. CSR Account Maintenance – Automation Regression Suite (Prime Version 2).pdf` |

*Latest results:* Re-run the suite in Jenkins and open the report URL, or replace the HTML files under `reports/v2/` with the latest export to refresh numbers and scenario lists in this doc.

---

## Notes

- **14 test blocks** in suite XML; **24 methods** (scenarios) in latest HTML report.
- **Suite name:** XML/report use "Account or Profile Maintenance"; Confluence module title is "CSR Account Maintenance" — same scope.
- **Commented out in XML:** NY Direct and NJ Direct personal information (IDP plans) — profile update not yet updated for IDP plans.
- **Module & plan coverage:** Fill *Scenario count* and *qTest mapping* from the latest TestNG report and qTest/Confluence when updating this page.
- Runners: **FeatureRunner** for personal information tests; **ParallelFeatureRunner** for bank, beneficiary, delivery preferences, security questions, payroll deduction.
