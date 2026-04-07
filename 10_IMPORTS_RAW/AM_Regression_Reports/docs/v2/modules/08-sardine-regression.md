# Sardine Regression – Automation Regression Suite (Prime Version 2)

**Module:** Sardine Regression
**Suite XML:** `suites/v2/daily/stage1-sardine-regression.xml`
**Suite Name:** Stage1 Sardine Regression Suite
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)
**Environment:** Stage 1
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri)

---

## Purpose

This module validates Sardine (fraud-detection) enrollment and distribution flows across multiple plan types. It covers NextGen enrollment (CA Direct), multiple beneficiaries, NAA ABLE enrollment (TNB, PAB), GSP enrollment (PAG), Wealthfront/PAD/Vanguard prefill flows, and CSR member distribution for NY and MI plans.

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests / Methods | 10 tests / 29 methods |
| Approx Duration | ~3.5 hours |
| Thread Count | 1 |
| Runners | ParallelFeatureRunner, FeatureRunner |
| Tags | @regression and @sardinerun, @dailyrun, @dailyrun-naa |
| Plans Covered | CAD, TNB, PAB, PAG, PAD, VGI, NYD, MID |

## Test Scenarios

| Test Name | Plan(s) | Runner | Notes |
|-----------|---------|--------|-------|
| Stage1 - CA Direct Member - NextGen Enrollment Flow - Positive | CAD | ParallelFeatureRunner | NextGen enrollment |
| CA Direct Member - NextGen Enrollment - Multiple Beneficiaries | CAD | ParallelFeatureRunner | Multiple beneficiaries |
| Stage1 - TNB NAA ABLE Enrollment Flow - Positive Cases per custodian | TNB | ParallelFeatureRunner | NAA ABLE |
| Stage1 - PAB NAA ABLE Enrollment Flow - Positive Cases per custodian | PAB | ParallelFeatureRunner | NAA ABLE |
| Stage1 - GSP (PAG) Enrollment Test Cases - Positive Cases | PAG | — | GSP enrollment |
| Wealthfront/PAD/Vanguard Prefill Enrollment | PAD, VGI | — | Prefill flows |
| NY Direct / MI Direct CSR Member Distribution | NYD, MID | — | Sardine distribution |

## What's Covered

- Sardine (fraud-detection) enrollment flows
- NextGen enrollment (CA Direct)
- Multiple beneficiaries enrollment
- NAA ABLE enrollment (TNB, PAB)
- GSP (PAG) enrollment
- Wealthfront/PAD/Vanguard prefill enrollment
- CSR member distribution (NYD, MID)

## Report & Artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-sardine-regression.xml` |
| HTML Report | Not available in this export (TODO: obtain from Jenkins) |
| Old Confluence PDF | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/1.8. Sardine Regression – Automation Regression Suite (Prime Version 2).pdf` |

## Notes

HTML report not available in current export. Obtain from Jenkins artifacts if needed.
