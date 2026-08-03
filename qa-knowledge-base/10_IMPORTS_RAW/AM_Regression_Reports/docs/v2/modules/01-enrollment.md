# Enrollment – Automation Regression Suite (Prime Version 2)

**Module:** Enrollments  
**Suite XML:** `suites/v2/daily/stage1-enrollments.xml`  
**Suite Name:** Regression Test Suite - Enrollments  
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)  
**Environment:** Stage 1  
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`

*Reference (format & structure):* `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.1. Enrollment – Automation Regression Suite (Prime Version 2).pdf`

---

## Enrollment suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | Enrollment regression: NextGen and legacy member/CSR/advisor enrollment, NAA/Non-NAA ABLE, save-as-draft, prefill (Wealthfront, PAD, Vanguard, NVU). |
| **When** | Daily, Mon–Fri, as part of Stage 1 nightly regression. |
| **Time** | Suite starts ~12:00 AM – 1:00 AM EST; module duration ~3 hours. |
| **Where** | Stage 1. Jenkins job: `STAGE1-Daily-Unite-Prime-Regression`. |
| **What plans** | MID, NYD, NYA, NYB, AKB, WVD, OKD, MND, COA, RIA, NMA, AKA, RIB, PAB, TNB, TND, PAD, VGI, NVU, KSD, WFD. |
| **What cases** | 28 test blocks (119 scenarios/methods in latest report). See **Module & plan coverage** and **Test scenarios** below. |
| **Reports** | `reports/v2/Regression Test Suite - Enrollments 1.html` (and 2, 3). Refresh from Jenkins for latest. |
| **Suite definition** | `suites/v2/daily/stage1-enrollments.xml`. |

---

## Purpose

This module validates enrollment flows across multiple ABLE plans and registration paths. It covers NextGen and legacy enrollment (member, CSR, advisor), prefill enrollment, save-as-draft, and negative scenarios to ensure enrollment functionality works correctly across plan configurations.

---

## Latest Report Summary (from TestNG HTML)

*Source: `reports/v2/Regression Test Suite - Enrollments 1.html` (and views 2, 3). Run date reflected in report URL (e.g. 20260313).*

| Metric | Value |
|--------|--------|
| Suite | 1 suite, Regression Test Suite - Enrollments |
| Tests | 28 tests |
| Methods | 119 methods |
| Passed | 103 passed |
| Failed | 16 failed |
| Skipped | 0 |
| XML | stage1-enrollments.xml |

For the latest numbers and method-level details (scenario names, pass/fail), open the HTML reports locally or from Jenkins.

---

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | 28 test blocks |
| Methods (from report) | 119 |
| Approx Duration | ~3 hours |
| Thread Count | 3 (parallel: tests) |
| Runners | ParallelFeatureRunner, FeatureRunner |
| Tags | @regression and @dailyrun, @dailyrun-naa, @dailyrun-non-naa |
| Plans Covered | MID, NYD, NYA, NYB, AKB, MIA, ILB, WVD, OKD, MND, COA, RIA, NMA, AKA, RIB, PAB, TNB, TND, PAD, PAG, VGI, NVU, KSD, WFD |

---

## Module & plan coverage

*Same format as Confluence PDF. Scenario counts and qTest mapping can be updated from the latest HTML report and qTest.*

| Plan | Flow type | Feature file | Scenario count | qTest mapping | Tags |
|------|-----------|--------------|----------------|--------------|------|
| MID | Direct Member – NextGen Positive | T100_NextGenEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| MID | NextGen – Multiple Beneficiaries | T101_NextGenEnrollmentMultipleBeneficiary.feature | — | — | @regression, @dailyrun |
| PAB | Legacy ABLE – Negative | T100_NAA_EnrollmentNegative.feature | — | — | @regression, @dailyrun |
| WVD | Direct Legacy – Single beneficiary | LegacyEnrollmentSpecificDirectPositive.feature | — | — | @regression, @dailyrun |
| OKD | Direct Legacy – Single beneficiary | LegacyEnrollmentSpecificDirectPositive.feature | — | — | @regression, @dailyrun |
| MND | Direct Legacy – Single beneficiary | LegacyEnrollmentSpecificDirectPositive.feature | — | — | @regression, @dailyrun |
| KSD | Direct Legacy – Single beneficiary | LegacyEnrollmentSpecificDirectPositive.feature | — | — | @regression, @dailyrun |
| MID | Direct CSR Enrollment – Positive | G100_CsrEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| MID | CSR Subsequent Enrollment – Positive | G100_CsrSubsequentEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| NYA | Advisor CSR NextGen – Single and Subsequent | G100_CsrEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| COA | Advisor CSR Legacy – Single beneficiary | G100_CsrEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| RIA | Advisor CSR Legacy – Single beneficiary | G100_CsrEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| NMA | Advisor CSR Legacy – Single beneficiary | G100_CsrEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| AKA | Advisor CSR Legacy – Single beneficiary | G100_CsrEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| AKB | NAA ABLE Enrollment – Positive | T100_NAA_EnrollmentPositive.feature | — | — | @regression, @dailyrun-naa |
| RIB | NAA ABLE Enrollment – Positive | T100_NAA_EnrollmentPositive.feature | — | — | @regression, @dailyrun-naa |
| PAB | NAA ABLE Enrollment – Positive | T100_NAA_EnrollmentPositive.feature | — | — | @regression, @dailyrun-naa |
| NYB | Non-NAA ABLE Enrollment – Positive | T100_NAA_EnrollmentPositive.feature | — | — | @regression, @dailyrun-non-naa |
| AKB | ABLE Save as Draft – Self | T100_NAA_EnrollmentSaveAsDraft.feature | — | — | @regression, @dailyrun |
| RIB | ABLE Save as Draft – Self and parent | T100_NAA_EnrollmentSaveAsDraft.feature | — | — | @regression, @dailyrun |
| PAB | ABLE Save as Draft – Self and parent | T100_NAA_EnrollmentSaveAsDraft.feature | — | — | @regression, @dailyrun |
| TNB | ABLE Save as Draft – Self | T100_EnrollmentSaveAsDraft.feature | — | — | @regression, @dailyrun |
| TND | Legacy Direct Save as Draft – Self | LegacyEnrollmentSaveAsDraftDirectPositive.feature | — | — | @regression, @dailyrun |
| NYB | ABLE Save as Draft – Self | T100_NAA_EnrollmentSaveAsDraft.feature | — | — | @regression, @dailyrun |
| WFD | Prefill Enrollment – Positive | PrefillEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| PAD | Prefill Enrollment – Positive | PrefillEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| VGI | Prefill Enrollment – Positive | PrefillEnrollmentPositive.feature | — | — | @regression, @dailyrun |
| NVU | Prefill Enrollment – Negative (SSgA) | PrefillEnrollmentNegative.feature | — | — | @regression, @dailyrun |

*Scenario count:* Total 119 methods in latest HTML report; per-feature counts can be taken from the report or qTest.  
*qTest mapping:* Link automation to qTest; fill from Confluence or qTest (e.g. TR-8281794 style IDs).

---

## Test Scenarios (from suite XML)

*Full list of test blocks and feature paths as defined in `suites/v2/daily/stage1-enrollments.xml`.*

| # | Test Name | Traunch | Feature Path |
|---|------------|---------|--------------|
| 1 | MI Direct Member - NextGen Enrollment Flow - Positive Test Cases | mid | frontoffice/mid/member/enrollment/feature/T100_NextGenEnrollmentPositive.feature |
| 2 | MI Direct Member - NextGen Enrollment - Multiple Beneficiaries | mid | frontoffice/mid/member/enrollment/feature/T101_NextGenEnrollmentMultipleBeneficiary.feature |
| 3 | PA Able Member - Legacy ABLE Enrollment - Negative Test Cases | pab | frontoffice/common/member/enrollment/feature/T100_NAA_EnrollmentNegative.feature |
| 4 | WVD - Direct Legacy Enrollment - Single Enrollment beneficiary | wvd | frontoffice/common/member/enrollment/feature/LegacyEnrollmentSpecificDirectPositive.feature |
| 5 | OKD - Direct Legacy Enrollment - Single Enrollment beneficiary | okd | frontoffice/common/member/enrollment/feature/LegacyEnrollmentSpecificDirectPositive.feature |
| 6 | MND - Direct Legacy Enrollment - Single Enrollment beneficiary | mnd | frontoffice/common/member/enrollment/feature/LegacyEnrollmentSpecificDirectPositive.feature |
| 7 | MI Direct CSR Enrollment - Positive Test Cases | mid | frontoffice/csr/enrollment/feature/G100_CsrEnrollmentPositive.feature |
| 8 | MID CSR Subsequent Enrollment Test Cases - Positive Cases | mid | frontoffice/csr/enrollment/feature/G100_CsrSubsequentEnrollmentPositive.feature |
| 9 | NYA - Advisor CSR NextGen Enrollment - Single and Subsequent Enrollment | nya | frontoffice/csr/enrollment/feature/G100_CsrEnrollmentPositive.feature |
| 10 | COA - Advisor CSR Legacy Specific Enrollment - Single Enrollment beneficiary | coa | frontoffice/csr/enrollment/feature/G100_CsrEnrollmentPositive.feature |
| 11 | RIA - Advisor CSR Legacy Specific Enrollment - Single Enrollment beneficiary | ria | frontoffice/csr/enrollment/feature/G100_CsrEnrollmentPositive.feature |
| 12 | NMA - Advisor CSR Legacy Specific Enrollment - Single Enrollment beneficiary | nma | frontoffice/csr/enrollment/feature/G100_CsrEnrollmentPositive.feature |
| 13 | AKA - Advisor CSR Legacy Specific Enrollment - Single Enrollment beneficiary | aka | frontoffice/csr/enrollment/feature/G100_CsrEnrollmentPositive.feature |
| 14 | KSD - Direct Legacy Specific Enrollment - Single Enrollment beneficiary | ksd | frontoffice/common/member/enrollment/feature/LegacyEnrollmentSpecificDirectPositive.feature |
| 15 | AKB NAA ABLE Enrollment Flow - Positive Cases per custodian | akb | frontoffice/common/member/enrollment/feature/T100_NAA_EnrollmentPositive.feature |
| 16 | RIB Legacy ABLE Enrollment Flow - Positive Flow for SingleEnrollment beneficiary | rib | frontoffice/common/member/enrollment/feature/T100_NAA_EnrollmentPositive.feature |
| 17 | PAB Legacy ABLE Enrollment Flow - Positive Flow for SingleEnrollment beneficiary | pab | frontoffice/common/member/enrollment/feature/T100_NAA_EnrollmentPositive.feature |
| 18 | AKB NAA ABLE Enrollment Flow - Save as a Draft - Self Positive | akb | frontoffice/common/member/enrollment/feature/T100_NAA_EnrollmentSaveAsDraft.feature |
| 19 | RIB NAA LEGACY ABLE Enrollment Flow - Save as a Draft - Self anf parent Positive | rib | frontoffice/common/member/enrollment/feature/T100_NAA_EnrollmentSaveAsDraft.feature |
| 20 | PAB NAA LEGACY ABLE Enrollment Flow - Save as a Draft - Self and parent Positive | pab | frontoffice/common/member/enrollment/feature/T100_NAA_EnrollmentSaveAsDraft.feature |
| 21 | TNB NAA LEGACY ABLE Enrollment Flow - Save as a Draft - Self Positive | tnb | frontoffice/tnb/member/enrollment/feature/T100_EnrollmentSaveAsDraft.feature |
| 22 | TND LEGACY DIRECT Enrollment Flow - Save as a Draft - Self Positive | tnd | frontoffice/common/member/enrollment/feature/LegacyEnrollmentSaveAsDraftDirectPositive.feature |
| 23 | NYB Non-NAA ABLE Enrollment Flow - Positive Cases per custodian | nyb | frontoffice/common/member/enrollment/feature/T100_NAA_EnrollmentPositive.feature |
| 24 | NYB Non-NAA ABLE Enrollment Flow - Save as a Draft - Self Positive | nyb | frontoffice/common/member/enrollment/feature/T100_NAA_EnrollmentSaveAsDraft.feature |
| 25 | Wealthfront Prefill Enrollment - Positive Test Cases | wfd | frontoffice/csr/prefillenroll/feature/PrefillEnrollmentPositive.feature |
| 26 | PAD Prefill Enrollment - Positive Test Cases | pad | frontoffice/csr/prefillenroll/feature/PrefillEnrollmentPositive.feature |
| 27 | Vanguard Prefill Enrollment - Positive Test Cases | vgi | frontoffice/csr/prefillenroll/feature/PrefillEnrollmentPositive.feature |
| 28 | NVU (SSgA) Prefill Enrollment - Negative Test Cases | nvu | frontoffice/csr/prefillenroll/feature/PrefillEnrollmentNegative.feature |

*Commented out in XML (not run):* MI Direct Member - NextGen Enrollment - Negative Test Cases; NHB ABLE NAA Entity Management Enrollment Flow.

---

## What's Covered

- **NextGen enrollment:** Member (MID) — positive, multiple beneficiaries; payroll, check, age-based, UGMA, FUNDID variants.
- **Legacy ABLE enrollment:** Positive (WVD, OKD, MND, KSD, COA, RIA, NMA, AKA); negative (PAB).
- **NAA/Non-NAA ABLE:** Positive and save-as-draft (AKB, RIB, PAB, TNB, TND, NYB); error validation (bank funding, DOB, addresses, delivery preferences, authorized individual hierarchy).
- **CSR enrollment:** MI Direct positive and subsequent; NYA advisor NextGen; COA/RIA/NMA/AKA advisor legacy.
- **Prefill enrollment:** Wealthfront (WFD), PAD, Vanguard (VGI) positive; NVU (SSgA) negative; CSR prefill UGMA/UTMA check, Individual EBT, ROLLOVER; prefill error validation (beneficiary, participant, successor, address).
- **Save as draft:** ABLE save-as-draft self/parent and continue-from-draft flows (AKB, RIB, PAB, TNB, TND, NYB).

---

## Report & Artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-enrollments.xml` |
| HTML Report (main) | `reports/v2/Regression Test Suite - Enrollments 1.html` |
| HTML Report (view 2) | `reports/v2/Regression Test Suite - Enrollments 2.html` |
| HTML Report (view 3) | `reports/v2/Regression Test Suite - Enrollments 3.html` |
| Old Confluence PDF | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.1. Enrollment – Automation Regression Suite (Prime Version 2).pdf` |

*Latest results:* Re-run the suite in Jenkins and open the report URL, or replace the HTML files under `reports/v2/` with the latest export to refresh numbers and scenario lists in this doc.

---

## Notes

- **28 test blocks** in suite XML; **119 methods** (scenarios) in latest HTML report.
- **Commented out in XML (not run):** MI Direct Member - NextGen Enrollment - Negative Test Cases; NHB ABLE NAA Entity Management Enrollment Flow (flaky until fixed).
- **Module & plan coverage:** Fill *Scenario count* and *qTest mapping* from the latest TestNG report and qTest/Confluence when updating this page.
