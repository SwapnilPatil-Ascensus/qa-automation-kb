# Database details for QA Automation for P4M

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Database-details-for-QA-Automation-for-P4M-331398425.aspx) | Created: 2025-07-23 | Last modified: 2025-07-31 | Author:  | Last editor: 

---

##### Below data is defaulted for DataPoints collection in SQL server(Msvc_Onboarding_Ark) and can be fetched using below SQL query

SELECT 'Product' AS DataPointType, pdp.DataPointName, pdp.DataPointValue FROM Product p JOIN ProductPASDefaultParameter pdp ON pdp.ProductId = p.ProductId WHERE ( pdp.DataPointType IS NULL OR pdp.DataPointType=0 ) AND p.**ProductKey = 'ARKPlan4Most'**
UNION
SELECT 'Offering' AS DataPointType, odp.DataPointName, odp.DataPointValue FROM Offering o JOIN OfferingPASDefaultParameter odp ON odp.OfferingId = o.OfferingId WHERE ( odp.DataPointType IS NULL OR odp.DataPointType=0 ) AND o.**OfferingKey = 'BAMLDailyGroup'**

| **Sr.No** | **Datapoint Name** | **Default Value** |
| --- | --- | --- |
| 1 | AuthDef | TRUE |
| 2 | AuthorizationPS | TRUE |
| 3 | AutoEnrollNewEmployees | NewlyEligible |
| 4 | AutoIncreaseDef | Percent |
| 5 | AutoIncreaseDefNoAutoEnroll | No |
| 6 | AutoIncreasePercentAmount | 0.01 |
| 7 | AutoIncreasePercentAmountMax | 0.1 |
| 8 | AutoIncreaseTiming | FirstDayPlanYear |
| 9 | BenefitAccrualFromDeathOrDisabilityFromMilitaryServiceAllowed | FALSE |
| 10 | Cashout | FiveThousand |
| 11 | CashoutIncludeRollovers | FALSE |
| 12 | CashoutUnder1000 | LumpSum |
| 13 | CatchUpContribution | TRUE |
| 14 | CeasingDef | PAEstablished |
| 15 | ChangingDef | PAEstablished |
| 16 | ClaimingExcessDef | 1-Mar |
| 17 | CompDefinitionDef | W2 |
| 18 | CompDefinitionPS | W2 |
| 19 | CompExcludeDef | NoExclusions |
| 20 | CompExcludeMatch | NoExclusions |
| 21 | CompExcludePS | NoExclusions |
| 22 | CompIncludeDeemed125 | FALSE |
| 23 | CompIncludeDef4Def | TRUE |
| 24 | CompIncludeDef4PS | TRUE |
| 25 | Compliance404c | TRUE |
| 26 | CompPeriodDef | PlanYear |
| 27 | CompPeriodPS | PlanYear |
| 28 | CompPostSevIncludeDeferredComp | FALSE |
| 29 | CompPostSevIncludeLeaveCashouts | FALSE |
| 30 | ControlledOrAffiliatedGroup | TRUE |
| 31 | CoronavirusDistributions | FALSE |
| 32 | CRDRepayment | FALSE |
| 33 | CustodianDesignation | FALSE |
| 34 | DeemedIRAContributionsAllowed | FALSE |
| 35 | DefLimit | DefLimitStatutory |
| 36 | DirectInPlanRothRolloverAllowed | FALSE |
| 37 | DirectRolloverFrom403bNondeductible | TRUE |
| 38 | DirectRolloverFrom457b | TRUE |
| 39 | DirectRolloverFrom457bNondeductible | TRUE |
| 40 | DirectRolloversFrom403b | TRUE |
| 41 | DirectRolloversFromQualifiedPlan | TRUE |
| 42 | DirectRolloversFromQualifiedPlanNondeductible | TRUE |
| 43 | DisabilityDefinition | Definition1 |
| 44 | DiscontinuedContributionsInPlan | NewPlanOrNoDiscontinuedContribs |
| 45 | DistributionDeath5YrRuleBeneficiaries | FALSE |
| 46 | DistributionDeath5YrRuleElection | TRUE |
| 47 | DistributionDisability | TRUE |
| 48 | DistributionQualifiedReservist | TRUE |
| 49 | DistributionRolloverAnytime | TRUE |
| 50 | DistributionTimingDeathOrDisabilityOrNRA | DateOfRequest |
| 51 | DistributionTransferAnytime | FALSE |
| 52 | DistUponSeveranceDefAllowed | TRUE |
| 53 | DistUponTermPriorToNRA | TRUE |
| 54 | EligibilityClassExclusionAllSources | TRUE |
| 55 | EligLongTermPartTime | FALSE |
| 56 | EligServiceReqQNEC | NotApplicable |
| 57 | EligWaiveMergerDateApply | NotApply |
| 58 | EmployeeNondeductibleContributionsAdding | FALSE |
| 59 | EmployeeRolloverContributionsAllowed | YesExceptForExcludedEmployees |
| 60 | ERCountry | USA |
| 61 | ExAggForfAllocation | Reduce |
| 62 | ExclusionServiceVestApply | FALSE |
| 63 | ExpirationDefAgreementsParticipants | No |
| 64 | FreezePlanAdd | FALSE |
| 65 | FrequencyInvestmentChanges | PADetermined |
| 66 | FullyVestDeath | TRUE |
| 67 | FullyVestDisability | TRUE |
| 68 | HardshipBPDAmendment | TRUE |
| 69 | HCECalYrElection | FALSE |
| 70 | HCESalaryReductionAgreement | NotApply |
| 71 | HCETopPdGrpElection | FALSE |
| 72 | HEARTVestingDisability | NotApplicable |
| 73 | InDirectInPlanRothRolloverAllowed | FALSE |
| 74 | IndirectRolloverFrom403b | TRUE |
| 75 | IndirectRolloverFrom457b | TRUE |
| 76 | IndirectRolloverFromQualifiedPlan | TRUE |
| 77 | InitialAutoEnrollDef | Percent |
| 78 | InServiceDefDeemedSeverance | TRUE |
| 79 | IRARollover | TRUE |
| 80 | IrrevocableParticipationElection | FALSE |
| 81 | LifeInsurance | FALSE |
| 82 | LimitationYear | PlanYear |
| 83 | LimitedTrustee | Other |
| 84 | MatchContributionLimit | FALSE |
| 85 | MatchForfAllocation | Reduce |
| 86 | MPP595PS | FALSE |
| 87 | NondeductibleEmployee | No |
| 88 | NRA | AgeOnly |
| 89 | ParticipantDirectionAccounts | EntireAccount |
| 90 | ParticipantDirectionAuthorization | TRUE |
| 91 | PlanAdministrator | FALSE |
| 92 | PlanAttachmentsNeeded | FALSE |
| 93 | PredSvc | FALSE |
| 94 | PredSvcLimitationsApply | FALSE |
| 95 | PSAllocationConditions | NotApply |
| 96 | PSForfAllocation | Reduce |
| 97 | PSFormula | Discretionary |
| 98 | PSLastDayWaiver | FALSE |
| 99 | PSNonHCEDisabled | FALSE |
| 100 | PSPrevailingWage | FALSE |
| 101 | PSServiceWaiver | TRUE |
| 102 | QBAD | FALSE |
| 103 | QBADRepayment | FALSE |
| 104 | QLACAllowed | FALSE |
| 105 | QMACAllowed | FALSE |
| 106 | QMACContributionLimit | FALSE |
| 107 | QNECAllowed | FALSE |
| 108 | RehireHoldout | FALSE |
| 109 | RelatedER | TRUE |
| 110 | RequiredBeginningDate | RBDDelay |
| 111 | RetirementEquityActSH | TRUE |
| 112 | ReturnDef | PAEstablished |
| 113 | RMD2020 | FALSE |
| 114 | RMD2020AnnuityStart | FALSE |
| 115 | RMD2020EligibleRollover | FALSE |
| 116 | RMD2020EmployerDistribution | FALSE |
| 117 | SeparateDefElectionBonuses | FALSE |
| 118 | ServiceRequiredVest | VestHOSApplies |
| 119 | SHRetroCurrentYear | FALSE |
| 120 | SHRetroPriorYear | FALSE |
| 121 | Simple401kApply | FALSE |
| 122 | TaxCharacterElectiveDef | PreTax |
| 123 | TerminationDistributionTiming | DateOfRequest |
| 124 | TopHeavyContributionsMinimumAllocationParticipants | NonKeyEmployeeParticipants |
| 125 | TopHeavyContributionsMinimumAllocationPlan | ThisPlan |
| 126 | TopHeavyContributionsMinimumAllocationRatio | NotApplicable |
| 127 | TopHeavyContributionsMinimumAllocationThisPlanWillOffset | TRUE |
| 128 | TrusteeAddress1 | 1655 43rd Street South, Suite 100, Fargo, ND 58103 |
| 129 | TrusteeAppointment | FinOrg |
| 130 | TrusteeCountry1 | USA |
| 131 | TrusteeName1 | Ascensus Trust Company |
| 132 | TrusteePhone1 | (701) 234-0207 |
| 133 | TrusteeType | Directed |
| 134 | TrustTIN | <br> |
| 135 | UnRelatedER | FALSE |
| 136 | ValuationDate | Daily |
| 137 | VestBISHours | 500 |
| 138 | VestMeasPrd | PrdPlanYear |
| 139 | VestMethodDeterminingService | HOS |
| 140 | VestMethodDeterminingServiceHOS | HOSActualHours |
| 141 | VestRehireHoldout | FALSE |
| 142 | VestYOSHours | 1000 |
| 143 | VoluntaryDistributionAnnuityContracts | FALSE |
| 144 | VoluntaryDistributionInstallmentPayments | FALSE |
| 145 | VoluntaryDistributionLumpSum | TRUE |
| 146 | VoluntaryDistributionPartialPayments | TRUE |

##### Below Plan4One DataPoint collection data is retrieved from Sybase database for multiple tables.

| **Sr, No** | **Datapoint Name** | **Table Name** | **Column** | **Comments** |
| --- | --- | --- | --- | --- |
| <br> | <br> | <br> | <br> | <br> |
| 1 | AccountNumber | RULES..PRGEN | GenPlanIDSys | <br> |
| 2 | ERPhone | RULES..PRGEN | GenClientPhone | <br> |
| 3 | ERAddress | RULES..PRGEN | <br>GenClientAddr1<br>+  " " +<br>GenClientAddr2<br> |  |
| 4 | ERCity | RULES..PRGEN | <br> | GenClientAddr4.Split(',') and use 0th object from collection |
| 5 | ERState | RULES..PRGEN | <br> | GenClientAddr4.Split(',') and use 1st object from collection |
| 6 | ERZip | RULES..PRGEN | <br> | GenClientAddr4.Split(',') and use 2nd object from collection |
| 7 | ERFiscalYEDate | RULES..PRGEN | <br>(GenEndTaxYrMo + 1)<br>+ "/" +<br>GenEndTaxYrDay<br> |  |
| 8 | PlanEntityPlanID | RULES..PRGEN | GenPlanIDSys | <br> |
| <br> |  |  |  |  |
| 10 | CoronavirusLoansNotPermitted | Client..PlanInfo | <br> | If InitEffctvDate < "9/23/2020" then "false" |
| 11 | Loans2020 | Client..PlanInfo | <br> | If InitEffctvDate > "9/23/2020" then "true" else "false" |
| 12 | CoronavirusOnlyLoansPermitted | Client..PlanInfo | <br> | If InitEffctvDate > "9/23/2020" then "false" |
| 13 | <br> | <br> | <br> | <br> |
| 14 | ERTIN | Web..PlanCrossRef | PlanTaxEIN | <br> |
| 15 | PlanSequenceNumber | Web..PlanCrossRef | PlanTaxIRS | <br> |
| 16 | <br> | <br> | <br> | <br> |
| 17 | PlanType | <br> | <br> | If ConversionType==5 then "New"  <br>If ConversionType==1 then "Restatement" |
| 18 | PlanEffectiveDate | Client..PlanInfo | <br> | If ConversionType==5 then InitEffctvDate  <br>If ConversionType==1 then RecKpEffctvDate |
| 19 | IkElectDefAdd | <br> | <br> | If ConversionType==5 then true  <br>If ConversionType==1 then false  <br>else false |
| 20 | IKDefDate | <br> | <br> | If ConversionType==5 then "other" |
| 21 | IKDefDateOtherSpecify | Client..PlanInfo | <br> | If ConversionType==5 then RecKpEffctvDate |
| 22 | AgreementEffectiveDate | Client..PlanInfo | <br> | If ConversionType==5 then InitEffctvDate  <br>If ConversionType==5 then RecKpEffctvDate |
| 23 | InitialPlanEffectiveDate | Client..PlanInfo | <br> | If ConversionType==1 then InitEffctvDate |
| <br> | <br> | <br> | <br> | <br> |
| <br> | ERTIN | Web..PlanCrossRef | PlanTaxEIN | <br> |
| <br> | PlanSequenceNumber | Web..PlanCrossRef | PlanTaxIRS | <br> |
| <br> | <br> | <br> | <br> | <br> |
| <br> | PlanType | Client..PlanInfo | <br> | If ConversionType==5 then "New"  <br>If ConversionType==1 then "Restatement" |
| <br> | PlanEffectiveDate | Client..PlanInfo | <br> | If ConversionType==5 then InitEffctvDate  <br>If ConversionType==1 then RecKpEffctvDate |
| <br> | IkElectDefAdd | Client..PlanInfo | <br> | If ConversionType==5 then true  <br>If ConversionType==1 then false  <br>else false |
| <br> | IKDefDate | Client..PlanInfo | <br> | If ConversionType==5 then "other" |
| <br> | IKDefDateOtherSpecify | Client..PlanInfo | <br> | If ConversionType==5 then RecKpEffctvDate |
| <br> | AgreementEffectiveDate | Client..PlanInfo | <br> | If ConversionType==5 then InitEffctvDate  <br>If ConversionType==5 then RecKpEffctvDate |
| <br> | InitialPlanEffectiveDate | Client..PlanInfo | <br> | If ConversionType==1 then InitEffctvDate |
| <br> | <br> | <br> | <br> | <br> |
| <br> | EligWaiveSpecifiedDateApply | Client..EligibilityByPlanRulesSetup | <br> | <br>If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate == [Client..PlanInfo].InitEffctvDate then "NotApply"<br> |
| <br> | EligWaiveSpecifiedDateApply | Client..EligibilityByPlanRulesSetup | <br> | If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate != [Client..PlanInfo].InitEffctvDate  <br>then "yes" |
| <br> | EligWaiveSpecifiedDateSpecifyDate | Client..EligibilityByPlanRulesSetup | ReqmtWvDate | If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate != [Client..PlanInfo].InitEffctvDate |
| <br> | EligWaiveSpecifiedDateClassification | Client..EligibilityByPlanRulesSetup | <br> | If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate != [Client..PlanInfo].InitEffctvDate  <br>then "AllEmployees" |
| <br> | EligWaiveSpecifiedDateEntryDate | Client..EligibilityByPlanRulesSetup | <br> | If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate != [Client..PlanInfo].InitEffctvDate  <br>then "EligWaiveOnDate" |
| <br> | EligWaiveSpecifiedDateApply | Client..EligibilityByPlanRulesSetup | <br> | If none of above conditions apply then "NotApply" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | EligibilityClassExclusionBySource | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber =="20" then "PreTaxDefSafeHarbor,RothDef,PS"  <br>if [RULES..PRMT]MTNumber =="2" then "PreTaxDefSafeHarbor,Match,PS" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | ExcludePreTaxDefSH | Client..EligibilityByPlanMTRules | <br> | if [Client..EligibilityByPlanMTRules]MTNumber = 3 is present and if ExcludeOtherClassInd == true then   <br>"NonResidentAlien,HCE"  <br>if ExcludeUnionInd == true then "NonResidentAlien,Union" |
| <br> | ExcludePS | Client..EligibilityByPlanMTRules | <br> | if [Client..EligibilityByPlanMTRules]MTNumber = 3 is present and if ExcludeOtherClassInd == true then   <br>"NonResidentAlien,HCE"  <br>if ExcludeUnionInd == true then "NonResidentAlien,Union" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | ExcludeRothDef | Client..EligibilityByPlanMTRules | <br> | if [Client..EligibilityByPlanMTRules]MTNumber = 20 is present and if ExcludeOtherClassInd == true then "NonResidentAlien,HCE"  <br>if ExcludeUnionInd == true then "NonResidentAlien,Union" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | ExcludeMatch | Client..EligibilityByPlanMTRules | <br> | if [Client..EligibilityByPlanMTRules]MTNumber = 3 is present and if ExcludeOtherClassInd == true then "NonResidentAlien,HCE"  <br>if ExcludeUnionInd == true then "NonResidentAlien,Union" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | AuthorizationMatch | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "true" else "false" |
| <br> | MatchAllocationConditions | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "NotApply" else <empty> |
| <br> | MatchCatchUp | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "true" |
| <br> | MatchFormula | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "Discretionary" |
| <br> | SupplementalMatch | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "false"  else <empty> |
| <br> | SHProvisionsApply | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="7" or "8"  is present then "true"  else "false" |
| <br> | SHContributionEligibleEmployees | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="7" or "8"  is present then "All" |
| <br> | SHACPTestMatchApply | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="7" or "8"  is present then "NotApply" |
| <br> | SHRecipientPlan | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="7" or "8"  is present then "ThisPlan" |
| <br> | SHADPContributions | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="8"  is present then "Nonelective" |
| <br> | MatchComputationPeriod | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="8"  is present then "NotApply" else "PayrollPeriod" |
| <br> | ContributionSources | RULES..PRMT | <br> | if only MTNumber = "20" is present then "PreTaxDef,RothDef,PS"  <br>if only MTNumber = "2" is present then "PreTaxDef,Match,PS"  <br>if only MTNumber = "7" or "8" is present then "PreTaxDef,TradSH" |
| <br> | AutomaticDefEnrollment | Client..PlanSmartAutoEnrollment | <br> | if AutoEnrollmentType == '1" then "ACA"  <br>if AutoEnrollmentType == '2" then "EACA" |
| <br> | PermissibleWithdrawals | Client..PlanSmartAutoEnrollment | <br> | if AutoEnrollmentType =="2" then "YesAll" |
| <br> | PermissibleWithdrawalPeriod | Client..PlanSmartAutoEnrollment | <br> | if AutoEnrollmentType =="2" then "NinetyDays" |
| <br> | AutoEnrollCurrentEmployees | Client..PlanSmartAutoEnrollment | <br> | AllCurrentEligibility |
| <br> | InitialAutoEnrollDefPercentSpecify | Client..PlanSmartAutoEnrollment | <br> | MinAutoEnrollDef/ 100 |
| <br> | <br> | <br> | <br> | <br> |
| <br> | SHADPContributions | Client..PlanEnroll | <br> | if [Client..PlanEnroll]MaxMatchPct1 == 3 then "BasicMatch"  <br>if MaxMatchPct1 ==4 \|\| MaxMatchPct1 == 5 \|\| MaxMatchPct1 ==6 then "EnhancedMatch" |
| <br> | SHEnhancedContributionBaseDefPercent | Client..PlanEnroll | <br> | if [Client..PlanEnroll]MaxMatchPct1 ==4 \|\| MaxMatchPct1 == 5 \|\| MaxMatchPct1 ==6 then (planEnroll.MaxMatchPct1 / 100) |
| <br> | SHEnhancedContributionBaseMatchPercent | Client..PlanEnroll | <br> | if [Client..PlanEnroll]MaxMatchPct1 ==4 \|\| MaxMatchPct1 == 5 \|\| MaxMatchPct1 ==6 then "1" |
| <br> | SHADPEnhancedMatchTiers | Client..PlanEnroll | <br> | if [Client..PlanEnroll]MaxMatchPct1 ==4 \|\| MaxMatchPct1 == 5 \|\| MaxMatchPct1 ==6 then "SingleTier" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | DistUponTermPriorToNRATypes | <br> | <br> | "PS,Match" |
| <br> | DistributionDisabilityTypes | <br> | <br> | "Def,PS,Match" |
| <br> | CompDefinitionMatch | <br> | <br> | "W2" |
| <br> | CompPeriodMatch | <br> | <br> | "PlanYear" |
| <br> | CompPreEntryMatch | Forfeitures..ForfRules | <br> | if [Forfeitures..ForfRules]EligCompInd == "0" then "EntryDate"  <br>if [Forfeitures..ForfRules]EligCompInd == "1" then "FullYear" |
| <br> | CompIncludeDef4Match | <br> | <br> | "true" |
| <br> | CompPreEntryPS | Forfeitures..ForfRules | <br> | if EligCompInd == "0" then "EntryDate"  <br>if EligCompInd == "1" then "FullYear" |
| <br> | CompPreEntryDef | Forfeitures..ForfRules | <br> | if EligCompInd == "0" then "EntryDate"  <br>if EligCompInd == "1" then "FullYear" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | PlanYear | Client..PlanInfo | <br> | if [Client..PlanInfo]GenEndPlanYrMo == "11" &&  [Client..PlanInfo]GenEndPlanYrDay=="31" then "CalendarYear" else "FiscalYear" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |
| <br> | ShortPlanYearSpecify | Client..PlanInfo | <br> | if (!string.IsNullOrWhiteSpace(ShortPlanYrBeginDate)  <br>then ShortPlanYrBeginDate  + "-" + ShortPlanYrEndDate |
| <br> | ShortPlanYearApply | Client..PlanInfo | <br> | if ShortPlanYrInd == "1" then "true" else "false" |
| <br> | NRAAgeOnlySpecifyAge | RULES..PRVEST | VestFullyVestAge | <br> |
| <br> | <br> | <br> | <br> | <br> |
| <br> | LoanEffectiveDate | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" and [Client..PlanConversionYES]ConversionType == "5" then [Client..PlanInfo]InitEffctvDate  <br>  <br>if [RULES..PRLOAN]LoanAllowed == "1" and [Client..PlanConversionYES]ConversionType == "1" then [Client..PlanInfo]RecKpEffctvDate |
| <br> | LoanAdministrator | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Plan Administrator" |
| <br> | LoanAdministratorAddress | RULES..PRGEN | <br>GenClientAddr1<br>+ "," +<br>GenClientAddr2<br> | <br>if [RULES..PRLOAN]LoanAllowed == "1"<br> |
| <br> | LoanAdministratorCity | RULES..PRGEN | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then GenClientAddr4.Split(',') and use 0th object from collection |
| <br> | LoanAdministratorState | RULES..PRGEN | <br> | if [RULES..PRLOAN]LoanAllowed == "1" than GenClientAddr4.Split(',') and use 1st object from collection |
| <br> | LoanAdministratorZip | RULES..PRGEN | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then GenClientAddr4.Split(',') and use 2nd object from collection |
| <br> | LoanAdministratorPhone | RULES..PRGEN | GenClientPhone | if [RULES..PRLOAN]LoanAllowed == "1" |
| <br> | LoanAdministratorCountry | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "USA" |
| <br> | LoanApplicationProcedure | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "no additional steps necessary" |
| <br> | LoanPurpose | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "All" |
| <br> | LoanMoneyTypeSecure | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "All" |
| <br> | LoanMoneyTypeDistribution | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "All" |
| <br> | LoanInvestmentType | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Other" |
| <br> | LoanInvestmentTypeOther | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Other" |
| <br> | LoanInvestmentTypeOtherSpecify | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "any Plan assets, except those with restrictions in trading, fees, etc" |
| <br> | LoanApproval | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Value" |
| <br> | LoanMaximumNumber | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "2" |
| <br> | LoanMaximumAvailable | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "FiftyKHalfVested" |
| <br> | LoanInterestRate | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "PrimePlus" |
| <br> | LoanInterestRatePrimePlusSpecify | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "1" |
| <br> | LoanCollateral | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "FALSE" |
| <br> | LoanDefaultSpecify | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "TRUE" |
| <br> | LoanDefault | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Separation" |
| <br> | LoanCurePeriod | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "QuarterAfterQuarter" |
| <br> | LoanCurePeriodSeparationService | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Other" |
| <br> | LoanCurePeriodSeparationServiceOtherSpecify | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "the earlier of a) the date designated by the plan sponsor, or b) 60 days after separation from service" |
| <br> | LoanOffsetProvisions | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Separation" |
| <br> | LoanSuspension | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "YesMonthsSpecify, YesMilitary" |
| <br> | LoanSuspensionNo | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Yes" |
| <br> | LoanRollover | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Yes" |
| <br> | LoanRolloverYes | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "YesAccept, YesAllow" |
| <br> | LoanTransfer | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "Yes" |
| <br> | LoanTransferYes | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "YesAccept, YesAllow" |
| <br> | LoanRefinance | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "FALSE" |
| <br> | LoanPayrollDeduction | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "TRUE" |
| <br> | LoanRepaymentSchedule | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "PayrollBasis" |
| <br> | LoanAdminDesignation | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "TRUE" |
| <br> | LegalAgent | RULES..PRGEN | GenClientContact | if [RULES..PRLOAN]LoanAllowed == "1" |
| <br> | LegalAgentAddress | RULES..PRGEN | <br>GenClientAddr1 + "," +<br>GenClientAddr2<br> | <br>if [RULES..PRLOAN]LoanAllowed == "1"<br> |
| <br> | LegalAgentCity | RULES..PRGEN | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then GenClientAddr4.Split(',') and use 0th object from collection |
| <br> | LegalAgentState | RULES..PRGEN | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then GenClientAddr4.Split(',') and use 1st object from collection |
| <br> | LegalAgentZip | RULES..PRGEN | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then GenClientAddr4.Split(',') and use 2nd object from collection |
| <br> | LegalAgentCountry | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "USA" |
| <br> | LoanInformation | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "TRUE" |
| <br> | LoanInformationProvided | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "SPD, LoanInformation" |
| <br> | LoanSuspensionMonthsSpecify | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1" then "12" |
| <br> | LoanMinimumAvailable | RULES..PRLOAN | LoanAmtMin | if [RULES..PRLOAN]LoanAllowed == "1" |
| <br> | Loans | <br> | <br> | if [RULES..PRLOAN]LoanAllowed == "1"  then "true" else "false" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | MatchVestingScheduleContribution | <br> | <br> | if ["RULES..PRMT]MTNumber == "2" && MTVestTbl1ID == "4" then "ThreeYrCliff" |
| <br> | MatchVestingScheduleContribution | <br> | <br> | if ["RULES..PRMT]MTNumber == "2" && MTVestTbl1ID == "10" then "SixYrGrad" |
| <br> | MatchVestingScheduleContribution | <br> | <br> | if ["RULES..PRMT]MTNumber == "2" && MTVestTbl1ID == "-3" then "Immediate" |
| <br> | MatchVestingScheduleContribution | <br> | <br> | if ["RULES..PRMT]MTNumber == "2"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3" and  and all of the (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4) fields in the GLOBAL..GVEST table are either "0" or "1" then "OtherCliff"  <br>any of  (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4)  these fields is not "0" or "1" then "OtherGrad" |
| <br> | MatchVestOther4 | <br> | <br> | if ["RULES..PRMT]MTNumber == "2"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3" and  and all of the (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4) fields in the GLOBAL..GVEST table are either "0" or "1" then <empty>  <br>any of  (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4)  these fields is not "0" or "1" then [GLOBAL..GVEST]GlobVestTblPctYr_4 |
| <br> | MatchVestOther5 | <br> | <br> | if ["RULES..PRMT]MTNumber == "2"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3" and  and all of the (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4) fields in the GLOBAL..GVEST table are either "0" or "1" then <empty>  <br>any of  (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4)  these fields is not "0" or "1" then [GLOBAL..GVEST]GlobVestTblPctYr_5 |
| <br> | MatchVestOther3 | <br> | <br> | if ["RULES..PRMT]MTNumber == "2"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3" and  and all of the (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4) fields in the GLOBAL..GVEST table are either "0" or "1" then "OtherCliff"  <br>any of  (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4)  these fields is not "0" or "1" then  [GLOBAL..GVEST]GlobVestTblPctYr_3 |
| <br> | MatchVestOther0 | <br> | <br> | if ["RULES..PRMT]MTNumber == "2"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3"  then  [GLOBAL..GVEST]GlobVestTblPctYr_0 |
| <br> | MatchVestOther1 | <br> | <br> | if ["RULES..PRMT]MTNumber == "2"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3"  then  [GLOBAL..GVEST]GlobVestTblPctYr_1 |
| <br> | MatchVestOther2 | <br> | <br> | if ["RULES..PRMT]MTNumber == "2"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3"  then  [GLOBAL..GVEST]GlobVestTblPctYr_2 |
| <br> | <br> | <br> | <br> | <br> |
| <br> | PSVestingScheduleContribution | <br> | <br> | if ["RULES..PRMT]MTNumber == "1" && MTVestTbl1ID == "4" then "ThreeYrCliff" |
| <br> | PSVestingScheduleContribution | <br> | <br> | if ["RULES..PRMT]MTNumber == "1" && MTVestTbl1ID == "10" then "SixYrGrad" |
| <br> | PSVestingScheduleContribution | <br> | <br> | if ["RULES..PRMT]MTNumber == "1" && MTVestTbl1ID == "-3" then "Immediate" |
| <br> | PSVestingScheduleContribution | <br> | <br> | if ["RULES..PRMT]MTNumber == "1"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3" and  and all of the (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4) fields in the GLOBAL..GVEST table are either "0" or "1" then "OtherCliff"  <br>any of  (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4)  these fields is not "0" or "1" then "OtherGrad" |
| <br> | PSVestOther3 | <br> | <br> | if ["RULES..PRMT]MTNumber == "1"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3" and  and all of the (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4) fields in the GLOBAL..GVEST table are either "0" or "1" then <empty>  <br>any of  (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4)  these fields is not "0" or "1" then [GLOBAL..GVEST]GlobVestTblPctYr_3 |
| <br> | PSVestOther4 | <br> | <br> | if ["RULES..PRMT]MTNumber == "1"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3" and  and all of the (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4) fields in the GLOBAL..GVEST table are either "0" or "1" then <empty>  <br>any of  (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4)  these fields is not "0" or "1" then [GLOBAL..GVEST]GlobVestTblPctYr_4 |
| <br> | PSVestOther5 | <br> | <br> | if ["RULES..PRMT]MTNumber == "1"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3" and  and all of the (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4) fields in the GLOBAL..GVEST table are either "0" or "1" then <empty>  <br>any of  (GlobVestTblPctYr_0,GlobVestTblPctYr_1,GlobVestTblPctYr_2,GlobVestTblPctYr_3,GlobVestTblPctYr_4)  these fields is not "0" or "1" then [GLOBAL..GVEST]GlobVestTblPctYr_5 |
| <br> | PSVestOther0 | <br> | <br> | if ["RULES..PRMT]MTNumber == "1"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3"  then  [GLOBAL..GVEST]GlobVestTblPctYr_0 |
| <br> | PSVestOther1 | <br> | <br> | if ["RULES..PRMT]MTNumber == "1"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3"  then  [GLOBAL..GVEST]GlobVestTblPctYr_0 |
| <br> | PSVestOther2 | <br> | <br> | if ["RULES..PRMT]MTNumber == "1"  &&  MTVestTbl1ID != "10" \|\| "4" \|\|"-3"  then  [GLOBAL..GVEST]GlobVestTblPctYr_0 |
| <br> | RothDefAllowed | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber =="20" then "true"  else "false" |
| <br> | DirectRolloversFromQualifiedPlanRoth | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="20" is present then "true" |
| <br> | DirectRolloverFrom403bRoth | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="20"  is present then "true" |
| <br> | DirectRolloverFrom457bRoth | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="20"  is present then "true" |
| <br> | IndirectRolloverRothEarnings | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="20"  is present then "true" |
| <br> | MatchYes | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="20"  and "2" are present then "PreTaxDef,RothDef"  <br>if only  [RULES..PRMT]MTNumber ="20"  is present then "PreTaxDef" |
| <br> | AuthorizationMatch | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "true" else "false" |
| <br> | MatchAllocationConditions | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "NotApply" else <empty> |
| <br> | MatchCatchUp | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "true" |
| <br> | MatchFormula | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "Discretionary" |
| <br> | SupplementalMatch | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="2"  is present then "false"  else <empty> |
| <br> | SHProvisionsApply | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="7" or "8"  is present then "true"  else "false" |
| <br> | SHContributionEligibleEmployees | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="7" or "8"  is present then "All" |
| <br> | SHACPTestMatchApply | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="7" or "8"  is present then "NotApply" |
| <br> | SHRecipientPlan | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="7" or "8"  is present then "ThisPlan" |
| <br> | SHADPContributions | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="8"  is present then "Nonelective" |
| <br> | MatchComputationPeriod | RULES..PRMT | <br> | if [RULES..PRMT]MTNumber ="8"  is present then "NotApply" else "PayrollPeriod" |
| <br> | ContributionSources | RULES..PRMT | <br> | if only MTNumber = "20" is present then "PreTaxDef,RothDef,PS"  <br>if only MTNumber = "2" is present then "PreTaxDef,Match,PS"  <br>if only MTNumber = "7" or "8" is present then "PreTaxDef,TradSH" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | ERADefinition | RULES..PRVEST | <br> | if [RULES..PRVEST]VestRetire1Ind == 1 then "AgeAndYOVS" else "NotApply" |
| <br> | ERAAgeAndYOVSAgeSpecify | RULES..PRVEST | <br> | if [RULES..PRVEST]VestRetire1Ind == 1 then [RULES..PRVEST]VestAs1Age |
| <br> | ERAAgeAndYOVSServiceSpecify | RULES..PRVEST | <br> | if [RULES..PRVEST]VestRetire1Ind == 1 then [RULES..PRVEST]VestAs1Mos) / 12) |
| <br> | FullyVestERA | RULES..PRVEST | <br> | if [RULES..PRVEST]VestRetire1Ind == 1 then "AgeAndYOVS" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | DistributionEmergencyPersonalExpense | <br> | <br> | "false" |
| <br> | DistributionDomesticAbuse | <br> | <br> | "false" |
| <br> | DistributionDisasterRecovery | <br> | <br> | "false" |
| <br> | DistributionTerminalIllness | <br> | <br> | "false" |
| <br> | Secure2SIMPLETerm | <br> | <br> | "false" |
| <br> | <br> | <br> | <br> | <br> |
| <br> | InServiceDistDefAllowed | RULES..PRDWDN | <br> | If any of the DrawOptNumber from (2,5,8,13) is present then true else false |
| <br> | InServiceDistDefAllowedSpecify | <br> | <br> | If  DrawOptNumber from "5" or "8" is present  then [YesSpecifyAge]   <br>If only DrawOptNumber "13" is present then [YesNRA]  <br>if both then [YesSpecifyAge,YesNRA] |
| <br> | InServiceDistDefAllowedSpecifyAge | <br> | <br> | If  DrawOptNumber  "8"  then consider respective DrawAge column value  <br>If  DrawOptNumber  "8"  then 59.5m  <br>Consider Minimun of the two |
| <br> | InServiceDefTypesAllowed | <br> | <br> | If any of the DrawOptNumber from (5,8,13) is present then [PreTaxDef]  <br>if [RULES..PRMT]MTNumber ="2" then [RothDef]  <br>If both then [PreTaxDef,RothDef] |
| <br> | InServiceEmployerContributions | <br> | <br> | If any of the DrawOptNumber from (5,8,13) is present then [PS]   <br>if [RULES..PRMT]MTNumber ="2" then [Match]  <br>if both then [PS, Match] |
| <br> | InServiceMatchCriteria | <br> | <br> | if [RULES..PRMT]MTNumber ="2" &&  DrawOptNumber "5" then "Attain595"  <br>if [RULES..PRMT]MTNumber ="2" &&  DrawOptNumber "13" then "AttainNRA"  <br>if [RULES..PRMT]MTNumber ="2" &&  DrawOptNumber "8" then "AttainAgeSpecify"  <br>whichever condition is satisfied that value will add to list |
| <br> | InServiceMatchAttainAgeSpecify | <br> | <br> | if [RULES..PRMT]MTNumber ="2" &&  DrawOptNumber "8"  then consider respective DrawAge column value |
| <br> | InServicePSCriteria | <br> | <br> | DrawOptNumber = "5" then  "Attain595"  <br>DrawOptNumber = "13" then  "AttainNRA"  <br>DrawOptNumber = "8" then  "AttainAgeSpecify"  <br>whichever condition is satisfied that value will add to list |
| <br> | InServiceWithdrawalsMatch | <br> | <br> | if (MTNumber = "2" && (DrawOptNumber == "5" \|\| DrawOptNumber == "8"  \|\|DrawOptNumber == "13" ) then "Unlimited" |
| <br> | InServiceWithdrawalsPS | <br> | <br> | If all (5,13,8) DrawOptNumber are present then "Unlimited" |
| <br> | HardshipDistributionDef | <br> | <br> | if DrawOptNumber = "2" then "true" else "false" |
| <br> | HardshipDefinitionMatch | <br> | <br> | if DrawOptNumber = "2"  and MTNumber = "2" then "SHNoSuspend" |
| <br> | HardshipDistributionMatch | <br> | <br> | if DrawOptNumber = "2"  and MTNumber = "2" then "Yes" else "No" |
| <br> | HardshipDueToBeneficiaryHardship | <br> | <br> | if DrawOptNumber = "2"  then "false" |
| <br> | HardshipDefinitionPS | <br> | <br> | if DrawOptNumber = "2"  then "SHNoSuspend" |
| <br> | HardshipDistributionPS | <br> | <br> | if DrawOptNumber = "2"  then "Yes" else "No" |
| <br> | HardshipDistributionDefTypes | <br> | <br> | if DrawOptNumber = "2"  then ["PreTaxDef"]  <br>if DrawOptNumber = "2"  &&  MTNumber = "2" then ["PreTaxDef", "RothDef"] |
| <br> | InServicePSAttainAgeSpecify | <br> | <br> | if DrawOptNumber = "8" then consider respective DrawAge column value |

​

| **Sr. No** | **Datapoint Name** | **Unqork property** | **Comment** |
| --- | --- | --- | --- |
| <br> | PSAllocationFormula | ProfitSharingAllocationFormula | If ProfitSharingAllocationFormula == "salaryproportionate" then "ProRata"  <br>If ProfitSharingAllocationFormula == "newcomparability" then "NewComp"  <br>If ProfitSharingAllocationFormula== "integrated" then "Integrated"  <br>IfProfitSharingAllocationFormula == "ageweighted" then "AgeWeighted"  <br>If IsNullOrEmpty(ProfitSharingAllocationFormula) then "ProRata" |
| <br> | SHNonelectiveContributionPercent | SafeHarborContributionType | if SafeHarborContributionType=="NonElective 3%" then "0.03"  <br>if SafeHarborContributionType=="NonElective 4%" then "0.04"  <br>if SafeHarborContributionType=="NonElective 5%" then "0.05"  <br>if SafeHarborContributionType=="NonElective 6%" then "0.06" |
| <br> | <br> | <br> | <br> |
| <br> | PSIntegratedFormulaSub | <br> | if Datapoint PSAllocationFormula == "integrated" then "ExcessIntegrated" |
| <br> | PSIntegratedFormulaIntegrationLevel | <br> | if Datapoint PSAllocationFormula == "integrated" then "TaxableWageBase" |
| <br> | PSAgeWeightedFormReallocations | <br> | if Datapoint PSAllocationFormula == "ageweighted" then "SafeHarbor" |
| <br> | PSNewCompFormula | <br> | if Datapoint PSAllocationFormula == "newcomparability" then "IndividualAllocationGroups" |
| <br> | PSNewCompFormAllocForm | <br> | if Datapoint PSAllocationFormula == "newcomparability" then "ProRata" |
| <br> | PSNewCompFormMinAllocationReqs | <br> | if Datapoint PSAllocationFormula == "newcomparability" then "SatisfyGatewayMinimumAllocation" |
| <br> | PSNewCompGatewayMinimumAllocationMethod | <br> | if Datapoint PSAllocationFormula == "newcomparability" then "PSNewCompGtwyMethodF" |
| <br> | PlanName | Legalplanname | <br> |
| <br> | ERName | BusinessName | <br> |
| <br> | <br>```<br>LimitedTrusteeName1<br>```<br> | <br>limitedTrustee1FirstName<br>+<br>limitedTrustee1LastName<br> | <br> |
| <br> | <br>```<br>LimitedTrusteeAddress1<br>```<br> | BusinessAddressLine1+BusinessAddressLine2+BusinessAddressCity+BusinessAddressState +BusinessAddressZipCode | <br> |
| <br> | LimitedTrusteeCountry | <br> | "USA" |

##### Below Plan4One DataPoint collection data is retrieved from Sybase database for multiple tables.

| **Sr No.** | **Service Agreement Datapoint Name** | **Table Name** | **Column Name** | **Calculated value** | **Comments** |
| --- | --- | --- | --- | --- | --- |
| <br> | <br> | <br> | <br> | <br> | <br> |
| 1 | PlanEntityPlanID | RULES..PRGEN | GenPlanIDSys | <br> | <br> |
| 2 | SAFeeArrangement | RULES..PRGEN | <br> | "FeeBased" | If GroupID is present in "PAIIKRIA", "PAIIKRIAETF", "PAIMICRORIA", "PAIMICRIAETF","MLEPAIIKRIA", "MLEPAIMICRIA", "SHAREPAIMETF", "SHAREPAIKETF" list |
| "CommissionBased" | If GroupID is present in "PAIIKCB", "PAIMICROCB" list |  |  |  |  |
| "LevelCommission" | If GroupID is present in "PAIIKLC", "PAIMICROLC" list |  |  |  |  |
| 3 | SAProduct | RULES..PRGEN | <br> | "PAiBAML" | If GroupID == "MLEPAIMICRIA" |
| "PAiSharebuilderIK" | If GroupID == "SHAREPAIKETF" |  |  |  |  |
| "PAiSharebuilder" | If GroupID == "MLEPAIMICRIA" |  |  |  |  |
| <br> |  |  |  |  |  |
| 4 | RSAEffectiveDate | Client..PlanInfo | RecKpEffctvDate | <br> | If [Client..PlanConversionYES].ConversionType == 5 OR 1 otherwise this datapoint will not be provided to PAS system |
| <br> |  |  |  |  |  |
| 5 | SACoverLetterDelivery | Client..PlanConversionYES | <br> | "Restatement" | If ConversionType == "1" |
| "NewBusiness" | If ConversionType == "5" |  |  |  |  |
| <empty> | If ConversionType is neither 1 nor 5 |  |  |  |  |
| <br> |  |  |  |  |  |
| 6 | AUTOForceOutEffectiveDate | Client..PlanInfo | RecKpEffctvDate | <br> | <br> |
| 7 | AutoIRARolloverAgreementEffectiveDate | Client..PlanInfo | RecKpEffctvDate | <br> | if [Client..PlanConversionYES]ConversionType == "5" |
| if [Client..PlanConversionYES]ConversionType== "1" |  |  |  |  |  |
