# 2026-10-08 -[28897] Team Archers -Weboptions, MT Vest changes for IK in ARK

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-10-08 -[28897] Team Archers -Weboptions, MT Vest changes for IK in ARK.aspx) | Created: 2026-10-05 | Last modified: 2026-10-07 | Author: Milind Sawde | Last editor: Milind Sawde

---

#### **Implementation Tasks**

| <br>#### **TrakIT info:**<br> |  |
| --- | --- |
| TrakIT # | 28897 |
| TrakIT Name | Team Archers -Web options, MT Vest changes for IK in ARK |
| Implementation Date: | 10-08-2026 7.30 AM ET |
| Implementation Items: | <br>- Onboarding.Setup.Plan => NA<br>- Onboarding.Setup.Plan.Consumer => NA<br>**Note:**  Deployment of DB scripts only, no changes in API.<br> |
| Octopus variable for PRO | NA |
| Summary of Changes | <br>Deployment includes<br>- Update Payroll Website Option in ARK.<br>- Update Sponsor Payroll and Census Processing in ARK.<br>- Update MT Vest Pct data in ARK.<br> |

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
| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) | Oct 07 | 28897 |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 07 | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 95 are completed<br> | <br> | <br> | NA |
|  | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | Anitha | Oct 08th | <br>Setup Plan Api DB TrakIT - [28897]<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 07 |  |
| <br>☐<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 07 |  |
| <br>☐<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 07 | <br> |
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
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky<br> |  | <br>Test- Create below offering plan from DoE<br>- "Ascensus Daily IK Fee Based - with Advisor" (AscensusDailyFBIKFdcv)<br>Plan Setup from DOE<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Not Started" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |

#### Verification Details

| # | ARK Screen Details | Verification Details | Comments |
| --- | --- | --- | --- |
| 1 | ARK/Plan/Rules/Payroll Website Option | Verify Payroll options in story - Product Backlog Item 858404: [Group 2/Group 2.2] i(k) web options - Payroll Website Option in ARK. | Test with "Ascensus Daily IK Fee Based - with Advisor" (AscensusDailyFBIKFdcv) |
| 2 | ARK/Plan/Rules/Sponsor Payroll and Census Processing | Verify Sponsor Payroll and Census Processing options in a story - Product Backlog Item 862027: [Group 2/Group 2.2] i(k) web options - Sponsor Payroll and Census Processing in ARK. | Test with "Ascensus Daily IK Fee Based - with Advisor" (AscensusDailyFBIKFdcv) |
| 3 | ARK/Plan/Rules/Money Types/Money Types Available and Vesting | Verify - Do not populate any data for "Ascensus Daily IK Fee Based - with Advisor" types of plans | Test with "Ascensus Daily IK Fee Based - with Advisor" (AscensusDailyFBIKFdcv) |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1895 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases/1.0.1895)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1772 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases/1.0.1772)<br> |  |  |
| <br>☐<br> | Rollback DBA | <br> |  |  |
