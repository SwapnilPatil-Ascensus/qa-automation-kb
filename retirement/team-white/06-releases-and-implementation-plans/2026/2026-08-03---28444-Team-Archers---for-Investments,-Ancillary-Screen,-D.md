# 2026-08-03 -[28444] Team Archers - for Investments, Ancillary Screen, Drawdown and Money Type changes

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-08-03--[28444]-Team-Archers---for Investments, Ancillary Screen, Drawdown and Money Type changes.aspx) | Created: 2026-07-30 | Last modified: 2026-09-08 | Author: Milind Sawde | Last editor: Milind Sawde

---

#### **Implementation Tasks**

| <br>#### **TrakIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28444] |
| TrakIT Name | Team Archers - PRO deployment - for Investments, Ancillary Screen, Drawdown and Money Type changes, Billing Option Fix |
| Implementation Date: | 08-03-2026 7.30 AM ET |
| Implementation Items: | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1642 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases/1.0.1642)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1563 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases/1.0.1563)<br> |
| Octopus variable for PRO | NA |
| Summary of Changes | <br>Deployment includes<br>- Update the logic for Ancillary screen in ARK.<br>- Update logic of MoneyTypes in ARK<br>- Update the logic of Investment screen  in ARK<br>- Billing Option fix for VG<br> |

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
| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) | Jul 31st | [28444] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jul 31st | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 95 are completed<br> | <br> | <br> | NA |
|  | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | Anitha | Aug 03rd | <br>Setup Plan Api DB TrakIT - [28443]<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jul 31st |  |
| <br>☐<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jul 31st |  |
| <br>☐<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jul 31st | <br> |
| <br>☐<br> | <br>Identify & order items to be implemented<br> |  |  |  |
|  |  |  |  |  |

#### **Implementation Tasks**

| <br> |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | (include Link to Octopus) |
| <br> |  |  |  |  |  |
| <br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br> |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky<br> |  | <br>Test- Create below offering plan from DoE<br>- CoPilot Group VG (Ascensus Essential with Vanguard Funds plan)<br>- Create AscensusBalFwdIk/AscensusBalFwdIKNoAdv  (Balance forward plan)<br>Plan Setup from DOE<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Not Started" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |
|  | <br> | <br> |  |  | <br> |

#### Verification Details

| # | ARK Screen Details | Verification Details | Comments |
| --- | --- | --- | --- |
| 1 | ARK/Plan/Rules/Drawdowns/Options/DD 7/Steps | In ARK: Set "DrawContractOrder" to "General/Separate" for Drawdown Steps | Test with ShareBuilderDailyGroup |
| 2 | ARK/Plan/Rules/Money Types | For Money Type 33, the RolloverID should be blank  <br>For Money Type 44, RolloverID should be set to 5 = Other   <br>For Money Type 54, RolloverID should be set to 0 = ROLLOVER IRA   <br>For Money Type 64, RolloverID should be set to 1 = ROLLOVER 403(B)  <br>For Money Type 74, RolloverID should be set to 2 = ROLLOVER 457(B)  <br>For Money Type 84, RolloverID should be set to 3 = ROLLOVER 403(A) P/T  <br>For Money Type 94, RolloverID should be set to 4 = ROLLOVER 403(A) A/T | Test with ShareBuilderDailyGroup |
| 3 | ARK/Plan/Rules/Ancillary Services | Loan Policy -> offset upon termination should not contain an effective date for i(k) plans. [It should be blank] | Test with AscensusBalFwdIkNoAdv |
| 4 | ARK/Plan/Process/Investment | "ACH and Trade on the same day" and "Files held until Payroll date" should be set as "No" | Test with AscensusBalFwdIkNoAdv plan |
| 5 | ARK/Plan/Process/Investments/Contact List and Information | Map "Address" field with Unqrok propertyID:  <br>"Address1' should be mapped with "businessAddressLine1"  <br>  <br>'Address2' should be mapped with "businessAddressLine2"  <br>  <br>'City' should be mapped with "businessAddressCity"  <br>  <br>'State' should be mapped with "businessAddressState"  <br>  <br>'Zip Code' should be mapped with "businessAddressZipCode" | Test with AscensusBalFwdIkNoAdv plan |
| 6 | ARK/Plan/Rules/EMT | Update mapping of ' 'Waive if employed by:' to unqork propertyID "recordkeepingEffectiveDate" from "PlanEffectiveDateNew" (for Startup only) | Test with AscensusBalFwdIkNoAdv plan |
| 7 | ARK/Process/Contributions/Site Setup | Nothing should be displayed under "Site Code" information | Test with AscensusBalFwdIkNoAdv plan |
| 8 | ARK/Plan/Rules/Options/billing Options | For CoPilot VG, Billing options details should not be populated | Test with AscensusDailyFBGroupNoAdv plan. |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1570 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases/1.0.1570)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1498 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases/1.0.1498)<br> |  |  |
| <br>☐<br> | Rollback DBA | <br> |  |  |
