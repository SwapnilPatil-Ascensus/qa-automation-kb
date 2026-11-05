# 2026-07-06 - [28157] Team White: Add fund network path to messaging API

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-07-06---[28157]-Team-White--Add-fund-network-path-to-messaging-API.aspx) | Created: 2026-07-02 | Last modified: 2026-07-06 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28157] |
| TrakIT Name | Team White IST Features |
| Implementation Date: | July 6th 2026 2.00PM |
| Implementation Items: | <br>- Onboarding.Data => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.290<br>- Onboarding.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1698<br>- Onboarding.Messaging.Api =>  https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1037<br>- Onboarding.Dashboard => N/A<br>- Onboarding.Portal => N/A<br>- DCA Partner Dashboard UI =>  https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.143<br>- Onboarding.Workflow.Api =>  N/A<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br> |
| Summary of Changes | <br>[Product Backlog Item 808568](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/808568): IST Dashboard - Display available documents in the investment detail modal in the dashboard<br>[Product Backlog Item 815205](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/815205): IST Dashboard - Remove Hardcoded Filters for Product and Fiduciary Service Provider<br>[Product Backlog Item 811708](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/811708): IST Dashboard (Complete status) - Restrict option to return to In Progress<br>[Product Backlog Item 814788](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/814788): IST - Document names in IST Dashboard detail<br>Add funds persistent volume to messaging.api<br> |
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

| <br>☒<br> | A new TrakIT is created for the deployment | <br>[@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)<br> | July 6th | [28157] |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 6th |  |
| <br>☒<br> | <br>All current Onboarding database stories for Group2 up to sprint 94  are completed<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 6th |  |
|  | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April15th | <br>SetUp Plan Api DB TrakIT - [XXXXX]<br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 6th |  |
| <br>☒<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 6th |  |
| <br>☒<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July 6th |  |
| <br>☒<br> | Identify & order items to be implemented |  |  |  |
|  |  |  |  |  |

**Implementation Tasks**

| <br>☒<br> | April6th | <br>Onboarding.Data<br> | DevOps | See above | <br>API as of July 6th 2026 (EOD)<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | See above | API as of July 6th 2026 (EOD) |
|  | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | API as of June24th 2026 (EOD) |
|  | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | API as of July 6th 2026 (EOD) |
|  | follow | Onboarding.Portal | DevOps | N/A | API as of July 6th 2026 (EOD) |
|  | follow | Partner Dashboard MFE | <br>DevOps<br> | <br>See above<br> | UI version as of July 6th 2026 (EOD) |
|  | follow | SEED CommandCenter | DevOps | <br> | <br> |
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>**IST - Frontend**   <br>Test that IST dashboard is showing up on DCA as internal user<br>Test that IST dashboard is NOT showing up on DCA for the external user (BAML and ShareBuilder)  <br>  <br>**IST - Backend**   <br>Test that network shares exist and are accessible:  <br>- Fund List Files Folder: here   <br>- Command Center Folder: here  <br>- PEK Folder: here  <br>- Investment Summary folder: here<br>**Initial Seed:**   <br>- Make sure that tables under the investments schema table are empty.  <br>- Drop the latest command center file in the corresponding folder.  <br>- Verify the number of imported rows.  <br>- Check the command center updates table<br>**Test CRM webhook:**   <br>- Test CRM webhook using the provided proposal Ids.  <br>- Negative testing<br>**Onboarding:**   <br>  <br>See that Chorus WorkItems are updated in PRO<br>Test that BAML IK, SB IK are working<br>Test Group2 Employee File upload from DOE with more than 30 employees having few unformatted SSNs and see that SSNs are formatted on ARK<br>See that not filling the Bank Account information for fees does not have any impact on status of the BusinessInformation section of Sponsor History<br>See that PRO duplicate Primary users are removed from DB<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  |  |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  |  |
|  |  |  |  |  |  |

#### **Rollback strategy**

| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Data => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.289<br>- Onboarding.Api => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1668<br>- Onboarding.Messaging.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1010](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1010)<br>- Onboarding.Dashboard => https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-dashboard/deployments/releases/1.0.48<br>- Onboarding.Workflow.Api =>  N/A<br>- Onboarding.Portal => N/A<br>- DCA Partner Dashboard UI => https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.140<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br>- Onboarding.Workflow.Api =>  N/A<br>- Onboarding.Portal => N/A<br> |  |  |
| --- | --- | --- | --- | --- |
| <br>☐<br> | Rollback DBA |  |  |  |
