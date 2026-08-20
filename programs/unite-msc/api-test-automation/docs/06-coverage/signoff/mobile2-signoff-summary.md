# Mobile 2 API Automation — Sign-Off Summary

**Sign-off date:** 2026-08-13  
**Status:** COMPLETE  
**KB path:** `programs/unite-msc/api-test-automation/docs/06-coverage/signoff/`

## Executive metrics

| Metric | Value |
|--------|-------|
| Documented business endpoints | 25 |
| Automated (in-scope) | 24 |
| Coverage percentage | 96.0% |
| Master regression tests | ~40 (OKD + NYD legs) |
| Validation layers | L1–L4 lean |
| Sign-off determination | COMPLETE |

## Endpoint register

| ID | Method | Path | Test | Master |
|----|--------|------|------|--------|
| M2-01 | GET | `/mobile2api/v1/mobileactivity/{ext}` | `MobileActivityRequestTest.getMobileActivity_returnsActivitySummary` | Y |
| M2-02 | GET | `/mobile2api/v1/mobiletransactionhistory/{ext}` | `MobileTransactionHistoryRequestTest.getMobileTransactionHistory_returnsTransactions` | Y |
| M2-03 | GET | `/mobile2api/v1/investments/{ext}` | `MobileInvestmentRequestTest.getMobileInvestments_returnsInvestments` | Y |
| M2-04 | GET | `/mobile2api/v1/mobilebanks` | `MobileBanksRequestTest.getMobileBanks_filterDomesticBanks_returnsBanks` | Y |
| M2-05 | GET | `/mobile2api/v1/mobilebanks/{id}` | `MobileBanksRequestTest.getMobileBankById_returnsBank` | Y |
| M2-06 | POST | `/mobile2api/v1/mobilebanks` | `MobileBanksRequestTest.postMobileBanks_addsDomesticBank_returnsBanks` | Y |
| M2-07 | PUT | `/mobile2api/v1/mobilebanks` | `MobileBanksRequestTest.putMobileBanks_updatesDomesticBank_returnsBanks` | N |
| M2-08 | DELETE | `/mobile2api/v1/mobilebanks` | `MobileBanksRequestTest.deleteMobileBanks_deletesDomesticBank_returnsBanks` | N |
| M2-09 | GET | `/mobile2api/v1/content` | `MobileContentRequestTest.getContent_commonSavingTips_returnsContent` | Y |
| M2-10 | GET | `/mobile2api/v1/plans` | `MobilePlansRequestTest.getMobilePlans_returnsPlans` | Y |
| M2-11 | GET | `/mobile2api/v1/plans/{id}` | `MobilePlansRequestTest.getMobilePlanById_returnsPlan` | Y |
| M2-12 | GET | `/mobile2api/v1/mobilecontribution` | `MobileContributionRequestTest.getMobileContribution_returnsContributionOptions` | Y |
| M2-13 | GET | `/mobile2api/v1/mobilecontributioncheck` | `MobileContributionCheckRequestTest.getMobileContributionCheck_returnsShowContributionFlag` | Y |
| M2-14 | GET | `/mobile2api/v1/mobilecontribution/{ext}/{id}` | `MobileContributionDetailRequestTest.getMobileContributionById_returnsRecurringContribution` | Y |
| M2-15 | POST | `/mobile2api/v1/mobilecontribution` | `MobileContributionPostRequestTest.postMobileContribution_createsRecurringContribution` | Y |
| M2-16 | PUT | `/mobile2api/v1/mobilecontribution/{ext}/{id}` | `MobileContributionPutRequestTest.putMobileContributionById_updatesRecurringContribution` | Y |
| M2-17 | DELETE | `/mobile2api/v1/mobilecontribution/{ext}/{id}` | `MobileContributionDeleteRequestTest.deleteMobileContributionById_removesAutomationOwnedContribution` | N |
| M2-18 | GET | `/mobile2api/v1/mobiledashboard` | `MobileDashboardRequestTest.getMobileDashboard` | Y |
| M2-19 | GET | `/mobile2api/v1/mobileytdsummary/{ext}` | `MobileYtdSummaryRequestTest.getMobileYtdSummary_returnsYtdContributionSummary` | N |
| M2-20 | GET | `/mobile2api/v1/mobilemembers/{planId}/{username}` | `MobileMembersRequestTest.getMobileMembers_returnsMemberForHarness` | N |
| M2-21 | GET | `/mobile2api/v1/mobilebalancetrend/{ext}` | `MobileBalanceTrendRequestTest.getMobileBalanceTrend_returnsBalanceTrend` | Y |
| M2-22 | GET | `/mobile2api/v1/mobileperformance/{ext}` | `MobilePerformanceRequestTest.getMobilePerformance_returnsPerformance` | Y |
| M2-23 | GET | `/mobile2api/v1/mobilestackup/{planId}` | `MobileStackupRequestTest.getMobileStackup_returnsStackup` | N |
| M2-24 | GET | `/mobile2api/v1/mobileugift` | `MobileUgiftRequestTest.getMobileUgift_returnsUgiftPage` | Y |
| M2-25 | PATCH | `/mobile2api/v1/mobileugift/{ext}` | `MobileUgiftRequestTest.patchMobileUgift_assignsUgiftId` | Y |

## DOCX deliverable

- [`mobile2-signoff.docx`](./mobile2-signoff.docx)

## Evidence

- Regression logs: `evidence/regression-runs/`
- Mapping CSV: `mappings/endpoint-signoff-register.csv`
