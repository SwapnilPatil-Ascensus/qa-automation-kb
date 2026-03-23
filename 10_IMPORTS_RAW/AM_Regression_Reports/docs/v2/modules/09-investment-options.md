# Investment Options – Automation Regression Suite (Prime Version 2)

**Module:** Investment Options
**Suite XML:** `suites/v2/daily/stage1-investment-options.xml`
**Suite Name:** Regression Test Suite - Legacy Web Registration *(labeling mismatch — content is investment options)*
**Framework:** Prime V2 (Java + Selenium + TestNG + Cucumber, Ant build)
**Environment:** Stage 1
**Jenkins Job:** `STAGE1-Daily-Unite-Prime-Regression`
**Schedule:** Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri)

---

## Purpose

This module validates annual exchange and age-based fund rebalancing for direct plans. It ensures members can perform investment option changes (annual exchange) correctly for NY and CO direct plans, including age-based fund flows.

## Coverage Summary

| Attribute | Detail |
|-----------|--------|
| Tests / Methods | 2 tests |
| Approx Duration | Not available |
| Thread Count | 1 |
| Runners | FeatureRunner |
| Tags | @regression and @dailyrun, @agebasedfundrun |
| Plans Covered | NYD, COD |

## Test Scenarios

| Test Name | Plan(s) | Runner | Notes |
|-----------|---------|--------|-------|
| Anual Exchange for Direct Plan - Positive Scenarios | NYD | FeatureRunner | Annual exchange NY Direct |
| Anual Exchange for Direct Plan - Positive Scenarios | COD | FeatureRunner | Annual exchange CO Direct (age-based fund) |

## What's Covered

- Annual exchange for direct plans
- Age-based fund rebalancing (COD)

## Report & Artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v2/daily/stage1-investment-options.xml` |
| HTML Report | Not available (TODO: obtain from Jenkins) |
| Old Confluence PDF | None — this module is NEW and was not in any Confluence documentation |

## Notes

- **Labeling mismatch:** Suite name in XML is "Regression Test Suite - Legacy Web Registration" but the content is investment options (annual exchange). Do not confuse with the actual Legacy Web Registration module.
- This module was added to the nightly regression after the original documentation was published.
- Test name in XML contains typo: "Anual" instead of "Annual".
