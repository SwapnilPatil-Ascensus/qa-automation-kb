# Group2 Additional Unqork Properties and its details

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Group2-Additional-Unqork-Properties-and-its-details-326739781.aspx) | Created: 2025-06-12 | Last modified: 2025-07-07 | Author:  | Last editor: 

---

| **Color** | <br> | <br> | <br> |
| --- | --- | --- | --- |
| **Desc** | Mapped for P4M | Mapped for P4M but need confirmation from Business | No mapping found with ARK fields |

​

| **#** | **PropertyName** | **IK Product Defaults** | **ARK Column Name** | **ARK Table Name** | <br>**Type(IK/Group/Both)**<br>**(Required From Business)**<br> | <br>**ARK Field Name in UI**<br>**(Required From Business)**<br> | <br>**ARK UI**<br>**(Required From Business)**<br> | **DB Type** | **Nullable (Y/N)** | **Comments** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | payrollContactFirstName | none collected | <br> | <br> | <br> | <br> | <br> |  | <br> | <br>It will be visible on Unqork UI only if payrollContactName = No and If PayrollContact is same as PlanContact then PayrollContact values will be same as PlanContact else it will be different then PlanContact depending upon the User Input<br> |
| 2 | payrollContactLastName | none collected | <br> | <br> | <br> | <br> | <br> | <br> | <br> |  |
| 3 | payrollContactEmail | none collected | <br> | <br> | <br> | <br> | <br> | <br> | <br> |  |
| 4 | payrollContactPhoneNumber | none collected | <br> | <br> | <br> | <br> | <br> | <br> | <br> |  |
| 5 | trusteeNameOrg | hidden | <br> | <br> | <br> | <br> | <br> | <br> | <br> | Most probably these data will not be inserted from our API. It might be inserted from Workflow like Group 1 Offerings |
| 6 | trusteeAddress1 | hidden | GlobAgentAddr1 | Global..GAGENT | <br> | <br> | <br> | char | Y |  |
| 7 | trusteeAddress2 | hidden | GlobAgentAddr2 | Global..GAGENT | <br> | <br> | <br> | char | Y |  |
| 8 | trusteeCity | hidden | GlobAgentAddr4 | Global..GAGENT | <br> | <br> | <br> | char | Y |  |
| 9 | trusteeState | hidden | GlobAgentAddr4 | Global..GAGENT | <br> | <br> | <br> | char | Y |  |
| 10 | trusteeZip | hidden | GlobAgentAddr4 | Global..GAGENT | <br> | <br> | <br> | char | Y |  |
| 11 | recordkeepingEffectiveDateStartupEarliestDate | (not applicable) | RecKpEffctvDate | Client..PlanInfo | <br> | <br> | <br> | smalldatetime | N | <br> |
| 12 | recordkeepingEffectiveDateStartup | (not applicable) | RecKpEffctvDate | Client..PlanInfo | <br> | <br> | <br> | smalldatetime | N | <br> |
| 13 | recordkeepingEffectiveDateTransfer | (not applicable) | RecKpEffctvDate | Client..PlanInfo | <br> | <br> | <br> | smalldatetime | N | <br> |
| 14 | unionEmployees | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 15 | planHoursRequirement | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 16 | planEntryFrequency | Semi-Annually | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 17 | eligibilityWaiver | Yes when installationType = Startup | <br> | <br> | <br> | <br> | <br> | <br> | <br> | It will be visible on Unqork UI only if InstallationType = Startup |
| 18 | eligibilityWaiverDate | recordkeepingEffectiveDate when installationType = Startup | <br> | <br> | <br> | <br> | <br> | <br> | <br> |  |
| 19 | participantMiddleInitial | (not applicable) | FirstName | EE..EE_MASTER_SECURE | <br> | <br> | <br> | char | Y | <br> |
| 20 | participantDORH | (not applicable) | CurHireDate | EE..EE_MASTER_SECURE | <br> | <br> | <br> | smalldatetime | Y | <br> |
| 21 | participantPriorTerminationDate | (not applicable) | PriTermDate | EE..EE_MASTER_SECURE | <br> | <br> | <br> | smalldatetime | Y | <br> |
| 22 | participantKeyEmployee | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 23 | participantHCE | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 24 | partTimeStatus | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | It will be visible on Unqork UI only if planEligibiilyMethod = Actual Hours, AND planHoursRequirement = 1000, AND participantEmploymentStatus = Active or Unpaid leave |
| 25 | partTimePriorYrHours1 | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | It will be visible on Unqork UI only if partTimeStatus = Yes,   <br>participantDOH or participantDORH is 1 year or more ago  <br>planEligibilityMethod = Actual Hours  <br>planHoursRequirement = 1000 |
| 26 | partTimePriorYrHours2 | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | It will be visible on Unqork UI only if partTimeStatus = Yes,   <br>participantDOH or participantDORH is 1 year or more ago  <br>planEligibilityMethod = Actual Hours  <br>planHoursRequirement = 1000 |
| 27 | partTimeEligibilityDate | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 28 | rothDeferrals | Yes, except JP Morgan | <br> | RULES..PRMT | <br> | <br> | <br> | <br> | <br> | MTNumber =20 mentioned in ARK Column |
| 29 | automaticEnrollment | (not applicable) | AutoEnrollmentType | Client..PlanSmartAutoEnrollment | <br> | <br> | <br> | tinyint | N | It will be visible on Unqork UI Only if InstallationType = Startup |
| 30 | automaticEnrollmentType | (not applicable) | AutoEnrollmentType | Client..PlanSmartAutoEnrollment | <br> | <br> | <br> | tinyint | N | Calculated for Startup Plans Only  <br>if installationType = Startup and automaticEnrollment = Yes, set to   <br>*ACA if there are less than 3 months remaining in the plan year  <br>*EACA if there are 3 or more months remaining in the plan year |
| 31 | automaticEnrollmentTypeDDInitial | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | Always hidden on Unqork UI |
| 32 | automaticEnrollmentPercentage | (not applicable) | MinAutoEnrollDef | Client..PlanSmartAutoEnrollment | <br> | <br> | <br> | tinyint | Y | Visible only if  automaticEnrollment = Yes |
| 33 | permissableWithdrawals | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | Visible only if automaticEnrollment = Yes AND automaticEnrollmentType <> ACA |
| 34 | permissableWithdrawalsDDInitial | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | Always hidden on Unqork UI |
| 35 | safeHarborContribution | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 36 | safeHarborContributionDDInitial | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | Always hidden on Unqork UI |
| 37 | profitSharingAllocationFormula | ProRata | <br> | <br> | <br> | <br> | <br> | <br> | <br> | Visible only if ProfitSharingContributions =- Yes |
| 38 | firstYearComp | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | Applicable only if InstallationType = Startup |
| 39 | employerMatchFormula | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> | Applicable only if EmployerMatch = Yes |
| 40 | employerMatchPercentage | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 41 | employerMatchCompensation | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 43 | payrollFrequency | (not applicable) | PayrollFreq | Investments..ClientSite | <br> | <br> | <br> | char | Y | Visible only if InstallationType = Startup |
| 44 | PayrollDate1 | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> |  |
| 45 | PayrollDate2 | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> |  |
| 46 | PayrollDate3 | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> |  |
| 47 | employerProfitSharingVesting | 100% immediate | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 48 | vestingYear1PS | 100% immediate | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 49 | vestingYear2PS | 100% immediate | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 50 | vestingYear3PS | 100% immediate | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 51 | vestingYear4PS | 100% immediate | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 52 | vestingYear5PS | 100% immediate | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 53 | vestingYear6PS | 100% immediate | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 54 | loanAllowed | Yes | LoanAllowed | RULES..PRLOAN | <br> | <br> | <br> | tinyint | Y | <br> |
| 55 | hardshipWithdrawals | Yes | <br> | RULES..PRDWDN | <br> | <br> | <br> | <br> | <br> | DrawOptNumber =2 |
| 56 | InServiceWithdrawals | Yes | <br> | RULES..PRDWDN | <br> | <br> | <br> | <br> | <br> | <br> |
| 57 | InServiceAgeRequirementPS | 59.5 | <br> | RULES..PRDWDN | <br> | <br> | <br> | <br> | <br> | Visible only if inServiceWithdrawals = yes |
| 58 | InServiceConditionsPS | 5 Yrs of Service, 2yrs Contributions (Match and PS) | <br> | RULES..PRDWDN | <br> | <br> | <br> | <br> | <br> |  |
| 59 | normalRetirementAge | 65 | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 60 | earlyRetirementAge | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 61 | advisorCommissionLevel | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 62 | qdiaDesignation | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 63 | modelElection | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 64 | modelRebalanceFrequency | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 65 | modelName | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 66 | modelTicker1 | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 67 | modelTickerPercentage1 | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 68 | planDefaultElection | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 69 | planDefaultElectionTargetDateAutoTransfer | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 70 | planDefaultElectionTargetDateAlternate | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 71 | ageBasedDefaultFundName | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 72 | ageBasedDefaultTicker | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 73 | ageBasedDefaultStartDate | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 74 | ageBasedDefaultEndDate | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 75 | ageBasedDefaultYearType | (varies by product) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 76 | forfeitureInvestment | (not applicable) | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 77 | cancelDate | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| 78 | expirationDate | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
