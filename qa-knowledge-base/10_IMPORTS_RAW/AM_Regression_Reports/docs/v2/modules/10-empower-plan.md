# Empower Plan – Automation Regression Suite (Prime Version 2)

**Module:** Empower Plan
**Suite XML:** `suites/v2/daily/stage1-empower-plan.xml`
**Suite Name:** Regression Test Suite - Empower Plan
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)
**Environment:** Stage 1
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri)

---

## Purpose

This module provides full CSR regression coverage for the Empower/Whitecap partner plan (COE). It validates contributions (single, AIP, negative), withdrawals (positive, negative, K-12, greenscreen, systematic, Flywire, fee), P/E and share adjustments, and profile maintenance across personal info, bank, beneficiary, delivery preferences, payroll deduction, and interested party.

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests / Methods | 20 tests |
| Approx Duration | Not available |
| Thread Count | 4 (parallel) |
| Runners | FeatureRunner, ParallelFeatureRunner |
| Tags | @regression and @dailyrun |
| Plans Covered | COE (CO Empower), MID |

## Test Scenarios

| Test Name | Plan(s) | Runner | Notes |
|-----------|---------|--------|-------|
| COE - Direct CSR Member Single Contribution | COE | FeatureRunner | Single contribution |
| Non-IDP plan - CO Empoer CSR Member Single AIP Contribution | COE | FeatureRunner | AIP contribution |
| Non-IDP Plan - CO Empower AIP update via CSR for member | COE | FeatureRunner | AIP update |
| Non-IDP - CO Empower Member Contribution Negative Scenarios via CSR | COE | FeatureRunner | Contribution negative |
| CSR Member Withdrawal - COE Direct (Qualified/Non-Qualified) | MID | FeatureRunner | Direct withdrawal |
| CSR Member Withdrawal - COE K-12 (AO Partial, Prorated) | COE | FeatureRunner | K-12 withdrawal |
| Member Withdrawal - COE Direct Non-IDP (Qualified/Non-Qualified) | COE | FeatureRunner | Member withdrawal |
| CSR Member Withdrawal Negative Scenarios - coe IDP | COE | FeatureRunner | Withdrawal negative IDP |
| CSR Member Withdrawal Negative Scenarios - COE Non-IDP | COE | FeatureRunner | Withdrawal negative non-IDP |
| CSR Greenscreen Withdrawal - COE Direct (Qualified/Non-Qualified) | COE | FeatureRunner | Greenscreen withdrawal |
| CSR Systematic Withdrawal - COE Direct | COE | FeatureRunner | Systematic withdrawal |
| CSR Member Withdrawal - COE Flywire | COE | FeatureRunner | Flywire withdrawal |
| CSR Fee Withdrawal - COE | COE | FeatureRunner | Fee withdrawal |
| P/E Adjustment - COE | COE | FeatureRunner | P/E adjustment |
| Share Adjustment - COE | COE | FeatureRunner | Share adjustment |
| Profile Maintenance - Personal Info | COE | FeatureRunner | Personal info |
| Profile Maintenance - Bank | COE | FeatureRunner | Bank info |
| Profile Maintenance - Beneficiary | COE | FeatureRunner | Beneficiary |
| Profile Maintenance - Delivery Preferences | COE | FeatureRunner | Delivery preferences |
| Profile Maintenance - Payroll Deduction, Interested Party | COE | FeatureRunner | Payroll, interested party |

## What's Covered

- CSR member single contribution
- AIP contribution and update
- Member contribution negative scenarios
- CSR member withdrawal (positive, negative, K-12, greenscreen, systematic, Flywire, fee)
- P/E adjustment
- Share adjustment
- Profile maintenance (personal info, bank, beneficiary, delivery preferences, payroll deduction, interested party)

## Report & Artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-empower-plan.xml` |
| HTML Report | Not available (TODO: obtain from Jenkins) |
| Old Confluence PDF | None — this module is NEW and represents cross-team Empower/Whitecap support |

## Notes

- This module was added to support the Empower/Whitecap partner plan (COE). It was not in any original Confluence documentation.
- Typo in XML: "CO Empoer" (test name) and "coe" (parameter value) — document as-is for traceability.
