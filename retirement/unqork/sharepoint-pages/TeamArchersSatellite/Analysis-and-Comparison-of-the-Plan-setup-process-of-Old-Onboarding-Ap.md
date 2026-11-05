# Analysis and Comparison of the Plan setup process of Old Onboarding Application and DOE application for the BAMLIK Plans

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Analysis-and-Comparison-of-the-Plan-setup-process-of-Old-Onboarding-Application-and-DOE-application-for-the-BAMLIK-Plans-321347418.aspx) | Created: 2025-05-30 | Last modified: 2025-06-09 | Author:  | Last editor: 

---

**Differences found in Mappers while comparing old BAMLIK plan ARKData JSON with the ARKData mapping logic used in DOE Application:**

| **Sr.No** | **Mapper** | **Property** | **Value set in Old Onboarding Application** | **Value set in DOE Application** | **Comment/Question** | **Implementation Status** | **Response** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Company | PortfolioName | Portfolio selected by user on UI | Null | There's no Unqork property available for this property so as per the discussion with team will hardcoded this property with "**Moderate** " Value in Step 4 | Implementation is done. | N/A |
| 2 | Employees | EligibilityDate | Eligibility date selected by user on UI | Null | We're setting this property with null value for all the Group1 Offerings because we don't have any Unqork property to map with this property so do we need to set null value for BAMLIK plan too or we will get Unqork property from the business? | we have set **Null**  value for this property same as Group 1 Offerings. We will change it in future in case we get any Unqork property for this property from the business. | <br> |
| 3 | NRADrawdown | Insert595 | False | True | We're setting True in this property after the BAT feedback for all of the Group 1 Offerings but in old BAMLIK plan it was set with False value so do we need to set it to False as per Old BAMLIK Plan or we need to set it to true similar to Group1 Offerings? | <br>We have set this property with "**False** " value as per the Old BAML plan.<br> | <br> |
| 4 | PayrollSchedule | Name | Sitecode A, P and Z | Sitecode A and Z | We're only setting Sitecode A and Z  and removed Sitecode P for all the Group1 offering after the BAT feedback but in Old BAMLIK Plan all 3 Sitecodes A,P and Z are set so do we need to set all 3 Sitecodes A, P and Z as per the old BAMLIK plan or we just need to set only 2 Sitecodes A and Z similar to Group 1 Offerings? | We have set all of the three Sitecodes A,P and Z in the code as per the Old BAML plans. | <br> |
| PayrollScheduleFrequencyType |  |  |  |  |  |  |  |
| SiteCode |  |  |  |  |  |  |  |

**Differences found in Unqork Sheet while comparing Unqork properties and its value for BAMLIK and Group1 Offerings Plans:**

| **Sr.No** | **Row Number** | **Unqork Property** | <br>**Value set in Old Onboarding**<br>**Application**<br> | **Value set in DOE Application** | **Comment/ Question** | **Implementation status** | **Response** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 5 | groupID | Set from Step 3 | Set from Step 3 | We will set it from step 3 in all the applicable table with value **MLEPAIIKRIA** | Updated Plan Default excel sheet | <br> |
| 2 | 100 | recordkeepingFeePaymentElection | Not Applicable for the BAMLIK plan as per Unqork sheet so we need to set null for this property irrespective what we're setting Old application and DOE Application | We have defaulted its value to **P**  in step 4 for all the Group1 offerings but for BAMLIK plan we need to leave it blank as it is not applicable for BAMLIK Plans | Implementation is done for this property as per the comments. | <br> |  |
| 3 | 106 | automaticFundingCtbnAmt | Populated in **PSPct**  column in **Client..PlanEnroll**  table from **InsertProfitSharingInfo()**  method | Populated in **PSMaxPct**  column in **Client..PlanEnroll**  table from **InsertContributionData()**  method | As per Unqork sheet this property value should be populated in **PSPct** column but in code we're populating this value in **PSMaxPct** column in **Client…PlanEnroll**  Table | I think column mentioned in Unqork sheet is incorrect as PSPct  is of type  tinyint and this property returns decimal value so I haven't modified the existing logic and inserting this property value in **PSMaxPct** column only which is of type decimal. | <br> |
| 4 | 107 | trusteeType | INDIVIDUAL TRUSTEE | INDIVIDUAL TRUSTEE | We need to confirm its value from business Whether it will be **INDIVIDUAL TRUSTEE**  or **Ascensus Trust** , as per the Unqork sheet it's still in discussion | <br>As of now we have not updated the logic as same value was set in Old BAML Plans. We will update it in future in casse we get any changes/feedback from the business.<br> | <br> |
| 5 | 130 | defaultInvestment | Set from step 3 | Set from step 3 | Value of this property need to be populated in **MTGroupInvElectOption** column in **Rules..PRMTG**  table but currently we're setting **1**  in this column from Step 3 and In Unqork sheet as well it is mentioned that value for this property will be fixed it will not change so can we populate it from step 3 similar to Group1 Offerings? | Already Implemented in Step 3 | <br> |
| 6 | 139 | planID | These values currently  we're not setting in both Old and new onboarding application | No Information provided regarding these properties in Unqork sheet whether this information we need to populate in ARK or not that we need to confirm with the business | Not implemented yet as we didn't get any updates on this from the business. | <br> |  |
| 7 | 140 | salesPhoneNumber |  |  |  |  |  |
| 8 | 141 | contactPreferenceEmail |  |  |  |  |  |
| 9 | 142 | contactPreferencePhone |  |  |  |  |  |

**BAMLIK ARK Data JSON:**

**PlanID** : 289063(QA plan)

[BAMLIKARKDataJSON.json](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SiteAssets/SitePages/TARC-Analysis-and-Comparison-of-the-Plan-setup-process-of-Old-Onboarding-Application-and-DOE-application-for-the-BAMLIK-Plans-321347418/BAMLIKARKDataJSON.json?wtAid=321347480)⠀

**Unqork Sheet Link:**

[Unqork Data Dictionary (OLD).xlsx (sharepoint.com)](https://ascensus0.sharepoint.com/:x:/s/TeamWhite/EfmPtecib1lIh2fliH4eyqMBE2d5w8LYNup2vgevry9KuQ?e=BAynLf&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNDEyMDEwMDIxNyIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D)
