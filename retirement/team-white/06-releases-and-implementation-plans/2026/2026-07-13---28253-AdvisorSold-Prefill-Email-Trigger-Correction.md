# 2026-07-13 - [28253] AdvisorSold Prefill Email Trigger Correction

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-07-13---[28253]-AdvisorSold-Prefill-Email-Trigger-Correction.aspx) | Created: 2026-07-13 | Last modified: 2026-07-13 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28253] |
| TrakIT Name | Team White AdvisorSold Prefill Email Trigger Correction |
| Implementation Date: | July 13th 2026 4.00PM |
| Implementation Items: | <br>- Onboarding.Data => N/A<br>- Onboarding.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1735<br>- Onboarding.Messaging.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1072<br>- Onboarding.Dashboard => N/A<br>- Onboarding.Portal => N/A<br>- DCA Partner Dashboard UI =>  https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.146<br>- Onboarding.Workflow.Api =>  N/A<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br> |
| Summary of Changes | <br> |
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

| <br>☒<br> | A new TrakIT is created for the deployment | <br>[@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)<br> | July 13th | [28253] |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 13th |  |
| <br>☒<br> | <br>All current Onboarding database stories for Group2 up to sprint 94  are completed<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 13th |  |
|  | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April15th | <br>SetUp Plan Api DB TrakIT - [XXXXX]<br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 13th |  |
| <br>☒<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 13th |  |
| <br>☒<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 13th |  |
| <br>☒<br> | Identify & order items to be implemented |  |  |  |
|  |  |  |  |  |

**Implementation Tasks**

| <br>☒<br> | April6th | <br>Onboarding.Data<br> | DevOps | See above | <br>API as of July 13th 2026 (EOD)<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | See above | API as of July 13th 2026 (EOD) |
|  | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | API as of July 13th 2026 (EOD) |
|  | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | API as of July 13th 2026 (EOD) |
|  | follow | Onboarding.Portal | DevOps | N/A | API as of July 13th 2026 (EOD) |
|  | follow | Partner Dashboard MFE | <br>DevOps<br> | <br>See above<br> | UI version as ofJuly 13th 2026 (EOD) |
|  | follow | SEED CommandCenter | DevOps | <br> | <br> |
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Onboarding:<br>Test transfer plans of BAML, SB, Direct Sold and Advisor Sold and confirm that **prefill email**  is sent at correct places<br>Test that Ascensus IK and Group FB and LC onboardings have correct **planDefaultElection**  values for all fundLineup selections<br>Test Ascensus Completed plans showing up the values of State and FundLineup values for the plan selected<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  |  |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |
|  |  |  |  |  |  |

#### **Rollback strategy**

| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Data => N/A<br>- Onboarding.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1721<br>- Onboarding.Messaging.Api =>  https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1056<br>- Onboarding.Dashboard =>https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1056<br>- Onboarding.Workflow.Api =>  N/A<br>- Onboarding.Portal => N/A<br>- DCA Partner Dashboard UI => N/A<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br>- Onboarding.Workflow.Api =>  N/A<br>- Onboarding.Portal => N/A<br> |  |  |
| --- | --- | --- | --- | --- |
| <br>☐<br> | Rollback DBA |  |  |  |
