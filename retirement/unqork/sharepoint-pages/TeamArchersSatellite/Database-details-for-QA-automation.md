# Database details for QA automation

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Database-details-for-QA-automation-326732618.aspx) | Created: 2025-06-05 | Last modified: 2025-06-26 | Author:  | Last editor: 

---

Below data represents the associated SQL Server\Sybase table names and a column names for each DataPoint that is passed over to massimport endpoint of PAS system. The information of DataPoints getting setup from Unqork data is provided on [Understanding of InitializePlanAdoptionDocuments API](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Understanding-of-InitializePlanAdoptionDocuments-API-310463103.aspx) and [Input details for QA testing](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Input-details-for-QA-testing-321341062.aspx) pages.

Below data is applicable only for BAML IK plans as of now.

##### Below data is defaulted for DataPoints collection in SQL server(Msvc_Onboarding_Ark) and can be fetched using below SQL query

SELECT 'Product' AS DataPointType, pdp.DataPointName, pdp.DataPointValue FROM Product p JOIN ProductPASDefaultParameter pdp ON pdp.ProductId = p.ProductId WHERE ( pdp.DataPointType IS NULL OR pdp.DataPointType=0 ) AND p.**ProductKey = 'ARKPlan4One'**
UNION
SELECT 'Offering' AS DataPointType, odp.DataPointName, odp.DataPointValue FROM Offering o JOIN OfferingPASDefaultParameter odp ON odp.OfferingId = o.OfferingId WHERE ( odp.DataPointType IS NULL OR odp.DataPointType=0 ) AND o.**OfferingKey = 'BAMLDailyIKNoAdv'**

| **Sr No** | **DataPoint Name** | **Default Value** |
| --- | --- | --- |
| <br> | ContributionSources | PreTaxDef,RothDef,PS |
| <br> | EligAgeReqIKSpecifyAge | 21 |
| <br> | EligServiceReqIK | OneYOS |
| <br> | ERCountry | USA |
| <br> | FreezePlanAdd | false |
| <br> | HardshipBPDAmendment | true |
| <br> | LifeInsurance | false |
| <br> | LimitedTrustee | Other |
| <br> | Loans | true |
| <br> | NondeductibleEmployee | No |
| <br> | PlanAttachmentsNeeded | false |
| <br> | QLACAllowed | false |
| <br> | RothDefAllowed | true |
| <br> | TrusteeCountry1 | USA |
| <br> | TrustTIN | <empty> |

##### Below Plan4One DataPoint collection data is retrieved from Sybase database for multiple tables.

| **Sr No** | **DataPoint Name** | **Table Name** | **Column Name** | **Comments** |
| --- | --- | --- | --- | --- |
| <br> | AccountNumber | RULES..PRGEN | GenPlanIDSys | <br> |
| <br> | ERPhone | RULES..PRGEN | GenClientPhone | <br> |
| <br> | ERAddress | RULES..PRGEN | GenClientAddr1 + " " + GenClientAddr2 | <br> |
| <br> | ERCity | RULES..PRGEN | <br> | <br>GenClientAddr4.Split(',') and use 0th object from collection<br>Ex: "Green Bay,WI,54304". Use "Green Bay"<br> |
| <br> | ERState | RULES..PRGEN | <br> | <br>GenClientAddr4.Split(',') and use 1st object from collection<br>Ex: "Green Bay,WI,54304". Use "WI"<br> |
| <br> | ERZip | RULES..PRGEN | <br> | <br>GenClientAddr4.Split(',') and use 2nd object from collection<br>Ex: "Green Bay,WI,54304". Use "54304"<br> |
| <br> | ERFiscalYEDate | RULES..PRGEN | <br> | <br> |
| <br> | <br> | RULES..PRGEN | (GenEndTaxYrMo + 1) + "/" + GenEndTaxYrDay | <br>Ex: (11 + 1)  + "/" + 31<br>Final value = "12/31"<br> |
| <br> | PlanEntityPlanID | RULES..PRGEN | GenPlanIDSys | <br> |
| <br> |  |  |  |  |
| <br> | CoronavirusLoansNotPermitted | Client..PlanInfo | <br> | <br>If InitEffctvDate < "9/23/2020" then "false"<br> |
| <br> | CoronavirusOnlyLoansPermitted | Client..PlanInfo | <br> | If InitEffctvDate > "9/23/2020" then "false" |
| <br> | Loans2020 | Client..PlanInfo | <br> | <br>If InitEffctvDate < "9/23/2020" then "true"<br>If InitEffctvDate > "9/23/2020" then "false"<br> |
| <br> |  |  |  |  |
| <br> | ERTIN | Web..PlanCrossRef | PlanTaxEIN | <br> |
| <br> | PlanSequenceNumber | Web..PlanCrossRef | PlanTaxIRS | <br> |
| <br> |  |  |  |  |
| <br> | PlanType | Client..PlanConversionYES | <br> | <br>If ConversionType == "5" then "New"<br>If ConversionType == "1" then "Restatement"<br> |
| <br> | PlanEffectiveDate | Client..PlanConversionYES | <br> | <br>If ConversionType == "5" then InitEffctvDate column value<br>If ConversionType == "1" then RecKpEffctvDate column value<br> |
| <br> | IkElectDefAdd | Client..PlanConversionYES | <br> | <br>If ConversionType == "5" then "true"<br>If ConversionType == "1" then "false"<br> |
| <br> | IKDefDate | Client..PlanConversionYES | <br> | <br>If ConversionType == "5" then "Other"<br>Not passed to PAS if ConversionType == "1"<br> |
| <br> | IKDefDateOtherSpecify | Client..PlanConversionYES | RecKpEffctvDate | <br>If ConversionType == "5"<br>Not passed to PAS if ConversionType == "1"<br> |
| <br> | AgreementEffectiveDate | Client..PlanConversionYES | <br> | <br>If ConversionType == "5" then InitEffctvDate column value<br>If ConversionType == "1" then RecKpEffctvDate column value<br> |
| <br> | IkElectDefAdd | Client..PlanConversionYES | <br> | If ConversionType is other than "1" or "5" then "false" |
| <br> |  |  |  |  |
| <br> | EligWaiveSpecifiedDateApply | Client..EligibilityByPlanRulesSetup | <br> | <br>If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate == [Client..PlanInfo].InitEffctvDate<br>then "NotApply"<br> |
| <br> | EligWaiveSpecifiedDateApply | Client..EligibilityByPlanRulesSetup | <br> | <br>If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate != [Client..PlanInfo].InitEffctvDate<br>then "Yes"<br> |
| <br> | EligWaiveSpecifiedDateSpecifyDate | Client..EligibilityByPlanRulesSetup | ReqmtWvDate | If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate != [Client..PlanInfo].InitEffctvDate |
| <br> | EligWaiveSpecifiedDateClassification | Client..EligibilityByPlanRulesSetup | <br> | <br>If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate != [Client..PlanInfo].InitEffctvDate<br>then "AllEmployees"<br> |
| <br> | EligWaiveSpecifiedDateEntryDate | Client..EligibilityByPlanRulesSetup | <br> | <br>If (EligibilityRuleNo == "1" &&  !string.IsNullOrEmpty(ReqmtWvDate)) && ReqmtWvDate != [Client..PlanInfo].InitEffctvDate<br>then "EligWaiveOnDate"<br> |
| <br> | EligWaiveSpecifiedDateApply | Client..EligibilityByPlanRulesSetup | <br> | If none of above conditions apply then "NotApply" |

##### Below data is defaulted for ServiceAgreements DataPoints collection in SQL server(Msvc_Onboarding_Ark) and can be fetched using below SQL query

SELECT 'Product' AS DataPointType, pdp.DataPointName, pdp.DataPointValue FROM Product p JOIN ProductPASDefaultParameter pdp ON pdp.ProductId = p.ProductId WHERE pdp.DataPointType=1 AND p.**ProductKey = 'ARKPlan4One'**
UNION
SELECT 'Offering' AS DataPointType, odp.DataPointName, odp.DataPointValue FROM Offering o JOIN OfferingPASDefaultParameter odp ON odp.OfferingId = o.OfferingId WHERE odp.DataPointType=1 AND o.**OfferingKey = 'BAMLDailyIKNoAdv'**

| **Sr No** | **ServiceAgreements DataPoint Name** | **Default Value** |
| --- | --- | --- |
| <br> | SACustodianAddress | <empty> |
| <br> | SACustodianDesignation | true |
| <br> | SACustodianName | <empty> |
| <br> | SAProduct | PAiBAMLIK |
| <br> | SATrusteeAddress1 | 1655 43rd Street South, Suite 100, Fargo, ND 58103 |
| <br> | SATrusteeAppointment | FinOrg |
| <br> | SATrusteeName1 | Ascensus Trust Company |
| <br> | SATrusteePhone1 | (701) 234-0207 |
| <br> | AutoIRARolloverAgreementEffectiveDate | <empty> |
| <br> | AutoIRARolloverService | NotApplicable |
| <br> | SATrusteeType | Directed |

##### Below Plan4One DataPoint collection data is retrieved from Sybase database for multiple tables.

| **Sr No** | **ServiceAgreements DataPoint Name** | **Table Name** | **Column Name** | **Calculated Value** | **Comments** |
| --- | --- | --- | --- | --- | --- |
| <br> | PlanEntityPlanID | RULES..PRGEN | GenPlanIDSys | <br> | <br> |
| <br> | SAFeeArrangement | RULES..PRGEN | <br> | "FeeBased" | If GroupID is present in "PAIIKRIA", "PAIIKRIAETF", "PAIMICRORIA", "PAIMICRIAETF","MLEPAIIKRIA", "MLEPAIMICRIA", "SHAREPAIMETF", "SHAREPAIKETF" list |
| "CommissionBased" | If GroupID is present in "PAIIKCB", "PAIMICROCB" list |  |  |  |  |
| "LevelCommission" | If GroupID is present in "PAIIKLC", "PAIMICROLC" list |  |  |  |  |
| <br> | SAProduct | RULES..PRGEN | <br> | "PAiBAML" | If GroupID == "MLEPAIMICRIA" |
| <br> | <br> | <br> | <br> | "PAiSharebuilderIK" | If GroupID == "SHAREPAIKETF" |
| <br> | <br> | <br> | <br> | "PAiSharebuilder" | If GroupID == "MLEPAIMICRIA" |
| <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | RSAEffectiveDate | Client..PlanInfo | RecKpEffctvDate | <br> | If [Client..PlanConversionYES].ConversionType == 5 OR 1 otherwise this datapoint will not be provided to PAS system |
| <br> |  |  |  |  |  |
| <br> | SACoverLetterDelivery | Client..PlanConversionYES | <br> | "Restatement" | If ConversionType == "1" |
| <br> | "NewBusiness" | If ConversionType == "5" |  |  |  |
| <br> | <empty> | If ConversionType is neither 1 nor 5 |  |  |  |
| <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |
