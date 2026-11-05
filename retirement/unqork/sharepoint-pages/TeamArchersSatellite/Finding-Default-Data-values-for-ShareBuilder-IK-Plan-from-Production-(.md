# Finding Default Data values for ShareBuilder IK Plan from Production ( for step4)

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Finding-Default-Data-values-for-ShareBuilder-IK-Plan-from-Production-(-for-step4)-326732627.aspx) | Created: 2025-06-05 | Last modified: 2025-07-08 | Author:  | Last editor: 

---

| **#** | **Property Name** | **PRO value** | **Table Name** | **Column Name** | **DB Type** | **Comments** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LoanAmtMaxModule | bps_vrs_calc | RULES..PRLOAN | LoanAmtMaxModule | char | Same value currently we have for Group1 |
| 2 | LoanNumMax | 1 | RULES..PRLOAN | LoanNumMax | int | Same value currently we have for Group1 |
| 3 | LoanUseCodeInd | 0 | RULES..PRLOAN | LoanUseCodeInd | tinyint | Same value currently we have for Group1 |
| 4 | LoanSubmitInd | TRUE | VRU..V_OVERRIDE | LoanSubmitInd | bit | Same value currently we have for Group1 |
| 5 | FundManagerID | <br> | <br> | <br> | <br> | <br> |
| 6 | DisallowLoanRefinanceInd | False | RULES..PRLOAN | DisallowLoanRefinanceInd | tinyint | Same value currently we have for Group1 |
| 7 | LoanIntRate | 0 | RULES..PRLOAN | LoanIntRate | tinyint | Same value currently we have for Group1 |
| 8 | BlankLoanAddressInd | False | RULES..PRLOAN | BlankLoanAddressInd | tinyint | Same value currently we have for Group1 |
| 9 | LoanNewPrdBetweenMos | 0 | RULES..PRLOAN | LoanNewPrdBetweenMos | tinyint | Same value currently we have for Group1 |
| 10 | LoanNewPeriodBetweenType | 0 | RULES..PRLOAN | LoanNewPeriodBetweenType | tinyint | <br>In PRO this column has name "LoanNewPrdBetweenType".<br>Same value currently we have for Group1 . This value set in condition for P4O this condition is false. Pls ref line no. 744 in **EstablishPlanEngine.cs**<br> |
| 11 | LoanNewPrdNumLoan | 0 | RULES..PRLOAN | LoanNewPrdNumLoan | tinyint | Same value currently we have for Group1 |
| 12 | LoanNewPrdMos | 0 | RULES..PRLOAN | LoanNewPrdMos | tinyint | Same value currently we have for Group1 |
| 13 | LoanPreAuthRecdInd | False | Client..PlanInfo | LoanPreAuthRecdInd | char | Same value currently we have for Group1 |
| 14 | PlanType | K | Client..PlanInfo | PlanTypeCode | char | In Group1 it has been set as 401(K). I think we need to set same since value is K |
| 15 | HardSelfCertification | 1 | BISYS..SecureAct2 | HardSelfCertification | tinyint | Not applicable for BAML, hence will not setting for ShareBuilder. |
| 16 | HardSelfCertiEffectDate | 2/10/2021  12:00:00 AM | BISYS..SecureAct2 | HardSelfCertiEffectDate | smalldatetime | Not applicable for BAML, hence will not setting for ShareBuilder. |
| 17 | QDROLimitLoanInd | 1 | RULES..PRGEN | QDROLimitLoanInd | tinyint | Same value currently we have for Group1 |
| 18 | QDROLimitPayoutInd | 1 | RULES..PRGEN | QDROLimitPayoutInd | tinyint | Same value currently we have for Group1 |
| 19 | Insert595 | <br> | <br> | <br> | <br> | For BAMLIK this has been set as false. So, for, SB we will set it false as well. |
| 20 | OnlineEnrollWizard | TRUE | Web..WebPlanOptions | OnlineEnrollWizardInd | bit | This is different than Group1. In Group1 it has been set as false. |
| 21 | RestrictedEnrollment | TRUE | Web..WebPlanOptions | HasRestrictedEnrollmentInd | bit | This is different than Group1. In Group1 it has been set as false. |
| 22 | IsBeneficiaryStepIncluded | TRUE | Web..WebPlanOptions | EnableOnlineEnrollStep4 | bit | This is different than Group1. In Group1 it has been set as false. |
| 23 | DocRecvDate | 10/18/2024  12:00:00 AM | Client..PlanInfo | DocRecvDate | smalldatetime | Set current date like it is in Group1 |
| 24 | DocRevwDate | 10/18/2024  12:00:00 AM | Client..PlanInfo | DocRevwDate | smalldatetime | Set current date like it is in Group1 |
| 25 | LoanRepayAllowedMonthly | 1 | RULES..PRLOAN | LoanRepayAllowedMonthly | int | Same value currently we have for Group1 |
| 26 | LoanRepayAllowedBiweekly | 1 | RULES..PRLOAN | LoanRepayAllowedBiweekly | int | Same value currently we have for Group1 |
| 27 | LoanRepayAllowedWeekly | 1 | RULES..PRLOAN | LoanRepayAllowedWeekly | int | Same value currently we have for Group1 |
| 28 | LoanRepayAllowedSmonthly | 1 | RULES..PRLOAN | LoanRepayAllowedSmonthly | int | Same value currently we have for Group1 |
| 29 | LoanRepayAllowedQtrly | 1 | RULES..PRLOAN | LoanRepayAllowedQtrly | int | Same value currently we have for Group1 |
| 30 | GenTrusteeNum | TCFRONTIER | RULES..PRGEN | GenTrusteeNum | char | Set PRO value as mentioned. |
| 31 | SetupAFCAAccountInd | <br> | <br> | <br> | <br> | For Group1 partners its set as 0 except AscensusDailyFeeBased where it set as 1. For SBIk for now we can set as 0. When it is 1 then data set in table EE..EE_MASTER_SECURE table. Pls ref line no 2460 in **EstablishPlanEngine.cs** |
| 32 | AFCAEligPartStatus | ACTV | PLANS..EE_PLAN | StatusPart | char | Same value currently we have for Group1. Its value depends on property "SetupAFCAAccountInd". For all partners this property is set as "0" , hence StatusPart value will go as null. |
| 33 | Provision109 | 3 | BISYS..SecureAct2 | Provision109 | tinyint | Not seen this set for BAMLIK. Hence not setting for SBIK |
| 34 | Provision109EffectiveDate | 1/1/2025  12:00:00 AM | BISYS..SecureAct2 | Provision109EffectDate | smalldatetime | Not seen this set for BAMLIK. Hence not setting for SBIK. |
| 35 | RecKeepFeeTypeCode | P | Client..PlanInfo | RecKeepFeeTypeCode | char | This need to change as null as per unqork list. However , it is set as P in pro plan. |
| 36 | **SvcTypeCode** | Multiple | Forfeitures..ForfRules | SvcTypeCode | int | <br>Need to set as "null". Currently it is set as "4" for MoneyType 0. Pls ref line no. 1917 in EstablishPlanEngine.cs<br>\| **MoneyType** \| **SvcTypeCode** \|<br>\| --- \| --- \|<br>\| 0 \| null \|<br>\| 1 \| 0 \|<br>\| 3 \| 0 \|<br>\| 4 \| 0 \|<br>\| 20 \| 0 \|<br> |
| 37 | GenTaxYrCycleInd | 1 | RULES..PRGEN | GenTaxYrCycleInd | tinyint | Same value currently we have for Group1 |
| 38 | **ConversionTypeInd** | TRUE | Client..PlanInfo | PlanConvInd | bit | Different value currently we have for Group1 |
| 39 | TradInd | 0 | RULES..PRGEN | TradInd | tinyint | Different value currently we have for Group1 |
| 40 | DBDOption | Multile | Investments..ClientSiteContact | DBDOption | char | <br>Need to set as "E". Currently it is set as "X" for sitecode "A". Pls. ref. line no. 1701 in EstablishPlanEngine.cs<br>\| **SiteCode** \| **DBDOption** \|<br>\| --- \| --- \|<br>\| A \| E \|<br>\| Z \| X \|<br> |
| 41 | **StatusDeterminActive** | 2 | RULES..PRGEN | StatusDeterminActive | tinyint | Same value currently we have for Group1 |
| 42 | **PSFreqTypeCode** | A | Client..PlanEnroll | PSFreqTypeCode | char | Currently in Group1 it has been set as "M" in ContributionDataMapper. Need to add this property in respective classes. |
| 43 | NonPayrollACHLoanRepaymentInd | 0 | Client..PlanInfoAddl | NonPayrollACHLoanRepaymentInd | tinyint | Same value currently we have for Group1 |
| 44 | **MoneyTypeForPS** | null | Client..PlanInfoAddl | MoneyTypeForPS | int | Need to set as null. Currently it is set as "1". Pls ref line no. 118 in EstablishPlanEngine.cs |
| 45 | **TradeSameDay** | 1 | Client..PlanInfoAddl | TradeSameDay | tinyint | Need to set as 1. Currently it is set as "0". Pls ref line no. 119 in EstablishPlanEngine.cs. **Need to create property for this.** |
| 46 | **HoldAchUntilPayrollDate** | TRUE | Client..PlanInfoAddl | HoldAchUntilPayrollDate | bit | Need to set as 1. Currently it is set as "0". Pls ref line no. 120 in EstablishPlanEngine.cs . **Need to create property for this.** |
| 47 | OpsCode | 1 | Reporting..ClientOpsPgm | OpsCode | tinyint | Same value found. No changes. |
| 48 | EmailInd | TRUE | Reporting..ClientOpsPgm | EmailInd | bit | Same value found. No changes |
| 49 | EligibilityRuleNo | <br> | Client..EligibilityByPlanRulesSetup | EligibilityRuleNo | int | No data found. |
| 50 | SortTypeCode | N | Client..PlanEnroll | SortTypeCode | char | **Values mentioned below till number 66 are set in Step3 only.** |
| 51 | PkgRecvCode | C | Client..PlanEnroll | PkgRecvCode | char | Same value found. No changes. |
| 52 | **WebInstructionTextInd** | FALSE | Client..PlanEnroll | WebInstructionTextInd | tinyint | Need to set as "0". Currently set as "1". Pls ref. line no. 1017 in EstablishPlanEngine.cs. Need to create property for this. |
| 53 | SuppressEnrollPhoneInd | FALSE | Client..PlanEnroll | SuppressEnrollPhoneInd | tinyint | Same value set. No Changes |
| 54 | SuppressCensusInd | FALSE | Client..PlanEnroll | SuppressCensusInd | tinyint | Same value set. No Changes |
| 55 | SuppressRolloverInd | FALSE | Client..PlanEnroll | SuppressRolloverInd | tinyint | Same value set. No Changes |
| 56 | **SuppressBeneficiaryInd** | FALSE | Client..PlanEnroll | SuppressBeneficiaryInd | tinyint | Need to change as "0" |
| 57 | SuppressSpousalConsentInd | FALSE | Client..PlanEnroll | SuppressSpousalConsentInd | tinyint | Same value set. No Changes |
| 58 | SuppressIVRInd | FALSE | Client..PlanEnroll | SuppressIVRInd | tinyint | Same value set. No Changes |
| 59 | SuppressWebInd | FALSE | Client..PlanEnroll | SuppressWebInd | tinyint | Same value set. No Changes |
| 60 | SuppressLogoPlanInd | FALSE | Client..PlanEnroll | SuppressLogoPlanInd | tinyint | Same value set. No Changes |
| 61 | SuppressLogoPartnerInd | FALSE | Client..PlanEnroll | SuppressLogoPartnerInd | tinyint | Same value set. No Changes |
| 62 | **DeliveryMethodID** | 0 | Client..PlanEnroll | DeliveryMethodID | tinyint | Need to change as "0" |
| 63 | ProviderID | 0 | Client..PlanEnroll | ProviderID | tinyint | Same value set. No Changes |
| 64 | AllowIncr | 1 | Client..PlanEnroll | AllowIncr | tinyint | Same value set. No Changes |
| 65 | **DiscrInd** | FALSE | Client..PlanEnroll | DiscrInd | tinyint | Need to change as "0". Based on SafeHarbor condition |
| 66 | InclPSCalcInd | FALSE | Client..PlanEnroll | InclPSCalcInd | tinyint | Same value set. No Changes |
| 67 | **EmailAddressType** | 2 | ProcessTrack..ESignEmailAddresses | EmailAddressType | int | Need to change as "2" |
| 68 | **ConvInd** | FALSE | Client..StmtDriver | ConvInd | bit | Need to add Sharebuilder IK condition in function InsertConvInd along with BalanceForward partner. |
| 69 | InclDtlInd | TRUE | Client..StmtDriver | InclDtlInd | bit | Same Value. No changes |
