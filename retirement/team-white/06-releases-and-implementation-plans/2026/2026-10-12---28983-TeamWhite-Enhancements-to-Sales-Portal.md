# 2026-10-12 - [28983] TeamWhite-Enhancements to Sales Portal

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-10-12---[28983]-TeamWhite-Enhancements-to-Sales-Portal.aspx) | Created: 2026-10-01 | Last modified: 2026-10-09 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28983] |
| TrakIT Name | TeamWhite-Enhancements to Sales Portal |
| Implementation Date: | Oct12th 2026 4.00PM |
| Implementation Items: | <br>- Onboarding.Experience.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-api/deployments/releases/3.0.22<br>- Onboarding.Experience.UI => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-ui/deployments/releases/3.0.230<br>- DCA Partner Dashboard UI => https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.193<br>- Onboarding.Data => N/A<br>- Onboarding.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1995<br>- Onboarding.Messaging.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1318<br>- Onboarding.Dashboard => N/A<br>- Onboarding.Portal => N/A<br>- Onboarding.Workflow.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.1227<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br> |
| Summary of Changes | <br>[Product Backlog Item 842221](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/842221): IST - Favorites - Create foundations to store user favorites - 1<br>[Product Backlog Item 842279](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/842279): IST - Favorites - Deleted Funds - 3<br>[Product Backlog Item 842292](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/842292): IST - Favorites - Deleted Models - 4<br>[Product Backlog Item 842293](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/842293): IST - Favorites - New Investment records - 2<br>[Product Backlog Item 869052](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/869052): Set SmartStart Express to No when writing to CRM from Vanguard DCA Sales Portal<br>[Product Backlog Item 863142](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/863142): Internal Dashboard Enhancements<br>[Product Backlog Item 862215](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/862215): IST - Favorites - Change Tracker<br> |
| Octopus Variables for PRO | <br> |

| <br>#### **Release Management (Unqork audit tool) info:**<br> |  |
| --- | --- |
| Qonnectors | [Release Management - QA](https://retsupport-qax.unqork.io/app/udlc-release#/display/release-dashboard) |
| Docusign | N/A |

#### **External Resources:**

| App Engineer | [@Siddhartha Singh](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Siddhartha.Singh%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a384b82128018583343abf0042) | Required |
| --- | --- | --- |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) |  | N/A |
|  |  |  |

#### **Teams Involved:**

| Team White |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Team Archers |  |  |  |  |  |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | <br>[@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)<br> | <br>Oct8th<br> | [28983] |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct8th | <br> |
| <br>☒<br> | <br>All current Onboarding database stories for Group2 up to sprint 94  are completed<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct8th |  |
|  | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April15th | <br>SetUp Plan Api DB TrakIT - [XXXXX]<br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct8th |  |
| <br>☒<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct8th |  |
| <br>☒<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct8th |  |
| <br>☒<br> | <br>Identify & order items to be implemented<br> |  |  |  |
|  | OCTOPUS | <br> | <br> | <br> |

**Implementation Tasks**

| <br>☒<br> | April6th | <br>Onboarding.Data<br> | DevOps | See above | <br>API as of Oct5th 2026 (EOD)<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | See above | API as of Oct5th 2026 (EOD) |
|  | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | API as of Oct5th 2026 (EOD) |
|  | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | API as of Oct5th 2026 (EOD) |
|  | follow | Onboarding.Portal | DevOps | N/A | API as of Oct5th 2026 (EOD) |
|  | follow | Partner Dashboard MFE | <br>DevOps<br> | <br>See above<br> | <br>API as of Oct5th2026 (EOD)<br> |
|  | follow | SEED CommandCenter | DevOps | <br> | <br> |
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Russ Holm](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> | <br> | <br>**Test Vanguard Sales Portal from DCA**<br>**Test Sales Portal from DCA for Ascensus proposals**<br>**Test DCA Partner Dashboard, IST dashboard**<br>**Test Group1, Group2, Group2.2 Onboardings and check Salesforce**<br>**Test Salesbridge dashboard is not showing up**<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  |  |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |
|  |  | <br> |  |  |  |

#### **Rollback strategy**

| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Experience.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-api/deployments/releases/3.0.14<br>- Onboarding.Experience.UI => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-ui/deployments/releases/3.0.204<br>- DCA Partner Dashboard UI => https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.189<br>- Onboarding.Data => N/A<br>- Onboarding.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1961<br>- Onboarding.Messaging.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1286<br>- Onboarding.Dashboard => N/A<br>- Onboarding.Portal => N/A<br>- Onboarding.Workflow.Api => N/A<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br> |  |  |
| --- | --- | --- | --- | --- |
| <br>☐<br> | Rollback DBA | N/A |  |  |
