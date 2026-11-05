# 2026-08-13 -[28546] Team Archers - for ServiceElection, Billing Option and Waiver Date changes

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-08-13--[28546]-Team-Archers---for for ServiceElection, Billing Option and Waiver Date changes.aspx) | Created: 2026-08-11 | Last modified: 2026-09-08 | Author: Milind Sawde | Last editor: Milind Sawde

---

#### **Implementation Tasks**

| <br>#### **TrakIT info:**<br> |  |
| --- | --- |
| TrakIT # | 28546 |
| TrakIT Name | Team Archers - PRO deployment - for Investments, Ancillary Screen, Drawdown and Money Type changes, Billing Option Fix |
| Implementation Date: | 08-13-2026 7.30 AM ET |
| Implementation Items: | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1688 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases/1.0.1688)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1610 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases/1.0.1610)<br> |
| Octopus variable for PRO | NA |
| Summary of Changes | <br>Deployment includes<br>- Update the logic based on ServiceElection316 related changes in ARK.<br>- Add new Billing Option type in ARK (One Digital 3(38))<br>- Update the logic of waiver date in ARK<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer |  | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Scott.Kirkpatrick@ascensus.com | Required |
|  |  |  |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team White | Paul Peca | <br> | Enes | <br> | <br> |
| Team Archers | <br> |  |  |  | Pankaj Dubey/ Milind Sawde |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) | Aug 12nd | [28546] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug 12nd | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 95 are completed<br> | <br> | <br> | NA |
|  | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | Anitha | Aug 13rd | <br>Setup Plan Api DB TrakIT - [28545]<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug 12nd |  |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug 12nd |  |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug 12nd | <br> |
| <br>☐<br> | Identify & order items to be implemented |  | <br> |  |
|  |  |  | <br> |  |

#### **Implementation Tasks**

| <br> |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| <br> |  |  |  |  |  |
| <br> |  |  |  |  |  |
| <br> | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | (include Link to Octopus) |
| <br> |  |  |  |  |  |
| <br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br> |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky<br> |  | <br>Test- Create below offering plan from DoE<br>- CoPilot Fee Based (Advisor - AscensusDailyFBGroupFdcv)<br>- Create IK Fee Based (No Advisor)  (AscensusCoPilotFBIKNoAdv)<br>Plan Setup from DOE<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Not Started" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |
|  | <br> | <br> |  |  | <br> |

#### Verification Details

| # | ARK Screen Details | Verification Details | Comments |
| --- | --- | --- | --- |
| 1 | ARK/Plan/Rules/EMT  <br>PAS - DataPoint **EligWaiveSpecifiedDateSpecifyDate** | For all IK Plans - Waiver Date should be updated to "recordkeepingEffectiveDate"  <br>  <br>Group 2 & 2.2 — PAS   <br>Map unqork propertyid "recordkeepingEffectiveDate" with PAS data point "EligWaiveSpecifiedDateSpecifyDate".  <br>Update Adoption Agreement mapping: Section Two Part B Option 1  <br>Date field = recordkeepingEffectiveDate (not planEffectiveDateNew)  <br>When: i(k) startup only | Test with AscensusCoPilotFBIKNoAdv (Startup) |
| 2 | ARK/Plan/Rules/Options/Billing Options | <br>Add new billing Option value as One Digital:  <br>For unqork propertyID: 'fundLineupSelection' add billing option as: One Digital 3(38)   <br>Set Billing Options value in ARK: OneDigital Essentials Small Market 3(38)  <br>Set Product Type as: Standard<br>For PAS, datapoint as below:  <br>SAProduct Value set "CoPilotOneDigital"  <br>RecordkeepingServiceAgreement Value set "Applicable"<br> | Test with AscensusDailyFBGroupFdcv |
| 3 | ARK/Plan/Rules/PDIO | <br>Map unqork propertyID "planDefaultTargetDateAutoTransfer" to field name "Automatically Transfer Defaulted Participants".<br>Mapped the answer options as below:  <br>Yes  <br>Yes, I direct the change of the default investment automatically  <br>No  <br>No, do not change the default investment automatically<br> | Test with AscensusDailyFBGroupFdcv |
| 4 | ARK/Plan/Rules/Ancillary Services | If serviceElection316 equals "Yes", ensure that the "Effective Date" field for all the specified "Managed Services" is mapped to the Unqork property ID "recordkeepingEffectiveDateStartup".  <br>For Hardship Approval, if  unqork property "hardshipWithdrawals = Yes  <br>For In Service Approval, if unqork property "inServiceWithdrawals" = Yes  <br>For Loan Approval, if unqork property "loanAllowed" = Yes  <br>For QDRO Approval, always yes  <br>Termination Approval, always yes | Test with AscensusDailyFBGroupFdcv plan |
| 5 | ARK/Plan/Rules/Compliance/Notices and Fee Disclosure | When "serviceElection316" is set to "Yes", then set below fields to "yes":  <br>  <br>Is the plan currently using the annual notice delivery service?   <br>Is the plan currently using the investment change notice delivery service?   <br>Is the plan currently using the initial notice delivery service?   <br>Is the plan currently using the SAR notice delivery service?   <br>Is the plan currently using the SPD & SMM notice delivery service?   <br>Is the plan currently using cash out notice delivery service? | Test with AscensusDailyFBGroupFdcv plan |
| 6 | ARK/Plan/Rules/Drawdowns | When unqork propertyID "serviceElection316" is set to 'Yes'  <br>Set "Termination Distribution Consent Type" field to 'N'  <br>Set "Hardship Distribution Consent Type" field to 'N' | Test with AscensusDailyFBGroupFdcv plan |
| 7 | ARK/Plan/Rules/Loan/Loan Setup | When unqork propertyID "loanAllowed" and "serviceElection316" is set to 'Yes', then:  <br>"Loan Consent Type" should be updated to "P" [Positive] | Test with AscensusDailyFBGroupFdcv plan |
| 8 | ARK/Plan/Rules/Loan/Loan Repayments | If unqork propertyID "loanallowed" is set to 'Yes', then  <br>"Allow New Loans If Delinquent Loans Exist" checkbox should be checked.  <br>"If Delinquent Loans are not allowed how many days constitute delinquency?" should contain value '120' | Test with AscensusDailyFBGroupFdcv plan. |
| 9 | ARK/Plan/Process/Investments | For "Site Code P" under 'DBD Information', map "Account Name" to unqork propertyID "businessName".  <br>  <br>For "Site Code Z" under 'DBD Information', set "DBD Option" value to "DBD Check". | AscensusDailyFBGroupFdcv |
| 10 | ARK/Plan/Rules/Money Types/Conts/Group | For MT 3, Set "Plan Suggested Savings Rate for Enrollment %" to 6% | AscensusDailyFBGroupFdcv |
| 11 | ARK/Plan/Rules/Alloc/Factors->Financial Info->Money Types Included | All the Money Types present under "Money Types defined for the plan:" section should be moved to "Money types to include:" section for each Allocation factors 70, 71, 72, 80, and 90. | AscensusDailyFBGroupFdcv |
| 12 | ARK/Plan/Web Options/Plan Online Options | For "Offer Auto Funding Enrollment" check box should be checked. | AscensusCoPilotFBIKNoAdv |
| 13 | ARK/Plan/Participant | AFAC2 participant should always be set with below details:  <br>SSN = 989-89-8999  <br>First Name = ADMINISTRATIVE  <br>Last Name = FEE CREDIT ACCOUNT 2  <br>  <br>For ARK Location: ARK/Participant/Indicative Panel/Invest Elections, below should be updated:  <br>Set "Synthetic Cash Account" to "100%" | AscensusDailyFBGroupFdcv |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1642 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases/1.0.1642)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1563 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases/1.0.1563)<br> |  |  |
| <br>☐<br> | Rollback DBA | <br> |  |  |
