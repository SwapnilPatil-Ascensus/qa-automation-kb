# 2026-09-01 -[28688] Team Archers -for Inve/Contact List,OtherFee, CustomDate,ElapsedTime,Fiduciary changes

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-09-01--[28688]-Team-Archers---for InvestmentInfo and Other Fee changes.aspx) | Created: 2026-08-24 | Last modified: 2026-09-08 | Author: Milind Sawde | Last editor: Milind Sawde

---

#### **Implementation Tasks**

| <br>#### **TrakIT info:**<br> |  |
| --- | --- |
| TrakIT # | 28688 |
| TrakIT Name | Team Archers - PRO deployment - for Inv/Contact List,OtherFee,CustomDate, ElapsedTime and Fiduciary changes. |
| Implementation Date: | 09-01-2026 7.30 AM ET / 09-01-2026 4.00 PM ET [deployed Updates after PAS changes] |
| Implementation Items: | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1807 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1701 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases)<br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1813 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1706 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases)<br> |
| Octopus variable for PRO | NA |
| Summary of Changes | <br>Deployment includes<br>- Update the Investment/Contact List and Information City, State and ZipCode as per unqork properties in ARK.<br>- Add FieldNum 36 with current date as description in Custom Date.<br>- Set Deafult to None for Elapsed Time for IK Fee Based No Adv (AscensusCoPilotFBIKNoAdv)<br>- Update Allow Investment Center Display as unchecked for Fiduciary Services screen for 2.2IK.<br>- Update the Other Fees Screen in ARK ("Loan fee" should be $95 and "Check fee" should be $0).<br>Changes from @Kelly Strong (To be deployed at 4:00 PM ET]):<br>- When the "fundLineupSelection" is "One Digital 3(38)" do not send IFAEffectiveDate and IFAOption datapoints in the massimportasync request packets. There is no other check/dependency required.<br> |

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
| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) | Aug 31st | 28688 |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug 31st | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 95 are completed<br> | <br> | <br> | NA |
|  | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | Anitha | Sep 01st | <br>Setup Plan Api DB TrakIT - [28689]<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug 31st |  |
| <br>☐<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug 31st |  |
| <br>☐<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug 31st | <br> |
| <br>☐<br> | <br>Identify & order items to be implemented<br> |  | <br> |  |
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
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky<br> |  | <br>Test- Create below offering plan from DoE<br>- IK Commission Based ( AscensusDailyLCIKFdcv)<br>- CoPilot Commission Based   (AscensusDailyLCGroupFdcv)<br>Plan Setup from DOE<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Not Started" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |
|  | <br> | <br> |  |  | <br> |

#### Verification Details

| # | ARK Screen Details | Verification Details | Comments |
| --- | --- | --- | --- |
| 1 | ARK/Plan/Process/Investment/Contact List and Information | City' should be mapped with "businessAddressCity"  <br>  <br>'State' should be mapped with "businessAddressState"  <br>  <br>'Zip Code' should be mapped with "businessAddressZipCode" | Test with AscensusDailyLCIKFdcv |
| 2 | ARK/Plan/Rules/Other Fees | "Loan fee" should be $95   <br>"Check fee" should be $0 | Test with AscensusDailyLCGroupFdcv |
| 3 | ARK/Plan/Rules/Forfeiture/AFCA Information/Forfeiture General Rules | Elapsed Time" should be set as default value to "None" | AscensusCoPilotFBIKNoAdv |
| 4 | ARK/Plan/Web Options/Fiduciary Services | "Allow Investment Center Display" should be unchecked | AscensusDailyLCIKFdcv |
| 5 | ARK/Plan/Rules/Custom Dates | Custom Date 36 is set "Current Date" to ARK for Group 1, Group 2, and Group 2.2 | AscensusDailyLCIKFdcv |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1807 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1701 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases)<br> |  |  |
| <br>☐<br> | Rollback DBA | <br> |  |  |
