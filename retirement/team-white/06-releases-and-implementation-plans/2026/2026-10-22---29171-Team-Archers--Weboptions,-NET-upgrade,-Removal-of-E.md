# 2026-10-22 -[29171] Team Archers -Weboptions, NET upgrade, Removal of Excel dependency for SB

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-10-22 -[29171] Team Archers -Weboptions, NET upgrade, Removal of Excel dependency for SB.aspx) | Created: 2026-10-19 | Last modified: 2026-10-21 | Author: Milind Sawde | Last editor: Milind Sawde

---

#### **Implementation Tasks**

| <br>#### **TrakIT info:**<br> |  |
| --- | --- |
| TrakIT # | 29171 |
| TrakIT Name | Team Archers -Weboptions, NET upgrade, Removal of Excel dependency for SB |
| Implementation Date: | 10-22-2026 7.30 AM ET |
| Implementation Items: | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.2018 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases/1.0.2018)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1879 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases/1.0.1879)<br> |
| Octopus variable for PRO | NA |
| Summary of Changes | <br>Deployment includes<br>- Update Plan Online Option in ARK.<br>- Update .NET version and removal of Excel dependency for SB.<br>- Verify SB Default fund not writing to ARK issue.<br> |

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
| <br>☒<br> | A new TrakIT is created for the deployment | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) | Oct 21 | Done |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 21 | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 95 are completed<br> | <br> | <br> | NA |
|  | <br>Confirm with Milind that DB Scipt dependency TrkIt is implemented in PRO<br> | Anitha | Oct 22nd | <br>Setup Plan Api DB TrakIT - [29170]<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 21st |  |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 21st |  |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 21st | <br> |
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
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky<br> |  | <br>Test- Create below offering plan from DoE<br>- SB Group<br>- "StateFarm IK" (StateFarmDailyIk)<br>Plan Setup from DOE<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Not Started" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |

#### Verification Details

| # | ARK Screen Details | Verification Details | Comments |
| --- | --- | --- | --- |
| 1 | ARK / Plan / Web Options / Plan Online Options | <br>Verify<br>Allow Ppt Deferrals for all EE Sources - Checked  <br>Allow Ppt Initiated RMD - Checked  <br>Allow PayrollSync Report - Unchecked<br> | Test with "StateFarm IK" (StateFarmDailyIk) |
| 2 | ARK/Plan/Rules/MTGroups/Investment Info | Verify - Fund defaults are set for SB offering | Test with "ShareBuilder Group Plan" |
| 3 | ARK/Plan/Rules/Funds | Verify - Funds and Models are set | Test with "ShareBuilder Group Plan" |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1895 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases/1.0.1895)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1772 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases/1.0.1772)<br> |  |  |
| <br>☐<br> | Rollback DBA | <br> |  |  |
