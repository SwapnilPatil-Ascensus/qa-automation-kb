# 2026-08-03 - [28424] TeamWhite - Onboarding and IST Enhancements

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-08-03---[28424]-TeamWhite---Onboarding-and-IST-Enhancements.aspx) | Created: 2026-07-31 | Last modified: 2026-07-31 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28424] |
| TrakIT Name | TeamWhite - Onboarding and IST Enhancements |
| Implementation Date: | Aug3rd 2026 8.00AM |
| Implementation Items: | <br>- Onboarding.Data => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.311<br>- Onboarding.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1817<br>- Onboarding.Messaging.Api =>  https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1141<br>- Onboarding.Dashboard => N/A<br>- Onboarding.Portal => N/A<br>- DCA Partner Dashboard UI =>  https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.159<br>- Onboarding.Workflow.Api =>  https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.1065<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br> |
| Summary of Changes | <br>[Product Backlog Item 827649](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/827649): [Salesforce Integration Group-2.2] – Sync Installation Coordinator contact details and 3(16) services election to Opportunity<br>[Product Backlog Item 784060](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/784060): ShareBuilder purchases appear in partner analytics as soon as the purchase is recorded<br>[Product Backlog Item 824597](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/824597): IST - Resume Investment - Keep user selections<br>[Product Backlog Item 824582](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/824582): IST - Import funds when command center row is new<br>[Product Backlog Item 827713](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/827713): IST - Create New IST Record - Managed Account Updates<br>[Product Backlog Item 827750](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/827750): IST - Custom Models - Default Model Names endpoint<br>[Product Backlog Item 766954](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/766954): IST Dashboard - Edit model names modal (Status = In Progress)(Custom)<br>[Product Backlog Item 831895](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/831895): Onboarding Dashboard: Update Last Updated timestamp<br>[Product Backlog Item 784575](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/784575): [Salesforce Integration] - Keep Opportunity Sold Date blank on advisor data; set to signing date when plan sponsor signs documents<br>[Product Backlog Item 796518](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/796518): Fix stale search data in partner dashboard<br>[Product Backlog Item 788495](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/788495): Issue with a successful OTP not resetting attempt count<br> |
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

| <br>☒<br> | A new TrakIT is created for the deployment | <br>[@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)<br> | Aug3rd | [28424] |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug3rd |  |
| <br>☒<br> | <br>All current Onboarding database stories for Group2 up to sprint 94  are completed<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug3rd |  |
|  | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April15th | <br>SetUp Plan Api DB TrakIT - [XXXXX]<br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug3rd |  |
| <br>☒<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug3rd |  |
| <br>☒<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Aug3rd |  |
| <br>☒<br> | Identify & order items to be implemented |  |  |  |
|  |  |  |  |  |

**Implementation Tasks**

| <br>☒<br> | April6th | <br>Onboarding.Data<br> | DevOps | See above | <br>API as of July31st 2026 (EOD)<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | See above | API as of  July31st  2026 (EOD) |
|  | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | API as of  July31st  2026 (EOD) |
|  | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | API as of July31st  2026 (EOD) |
|  | follow | Onboarding.Portal | DevOps | N/A | API as of  July31st  2026 (EOD) |
|  | follow | Partner Dashboard MFE | <br>DevOps<br> | <br>See above<br> | UI version as of  July31st  2026 (EOD) |
|  | follow | SEED CommandCenter | DevOps | <br> | <br> |
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Onboarding:<br>Test BAML and SB<br>Test Ascensus Partner IK and Group FB and LC onboardings<br>Test OTP functionality for both Group2 and Group2.2 Onboardings<br>Test serviceElection316 values in Salesforce Opportunity<br>Dashboard:<br>Test Partner Dashboard UI<br>Test IST UI<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  |  |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |
|  |  |  |  |  |  |

#### **Rollback strategy**

| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Data => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.294<br>- Onboarding.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1741<br>- Onboarding.Messaging.Api =>  https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1079<br>- Onboarding.Dashboard =>N/A<br>- Onboarding.Workflow.Api =>  https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.878<br>- Onboarding.Portal => N/A<br>- DCA Partner Dashboard UI => https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.147<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br> |  |  |
| --- | --- | --- | --- | --- |
| <br>☐<br> | Rollback DBA |  |  |  |
