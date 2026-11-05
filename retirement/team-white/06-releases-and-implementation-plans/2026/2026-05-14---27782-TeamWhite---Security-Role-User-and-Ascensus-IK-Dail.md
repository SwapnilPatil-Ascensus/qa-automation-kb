# 2026-05-14 - [27782] TeamWhite - Security Role User and Ascensus IK Daily Updates

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2026-05-14---[27782]-TeamWhite---Security-Role-User-and-Ascensus-IK-Daily-Updates-385550373.aspx) | Created: 2026-05-07 | Last modified: 2026-05-12 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### ****TrackIT info:****<br> |  |
| --- | --- |
| TrackIT # | [27782] |
| TrakIT Name | Team White DOE Group 2.2 Ascensus I(k) Balance Forward No Advisor |
| Implementation Date: | May 14th 2026 9.30AM |
| Implementation Items: | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.272](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.272)<br>- Onboarding.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1488](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1488)<br>- Onboarding.Messaging.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.856](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.856)<br>- Onboarding.Workflow.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.878](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.878)<br>- Onboarding.Portal => N/A<br>- DCA Partner Dashboard UI => [https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.112](https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.112)<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br> |
| Summary of Changes | <br>Deployment includes<br>- [Product Backlog Item 793716](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/793716): Create Plan ID After Successful Advisor OTP<br>- [Product Backlog Item 791725](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/791725): Research and Fix Dealer CRD not being passed to Salesforce - Due to Chris Cervantes Fix<br>- [Product Backlog Item 782037](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/782037): Access Digital Onboarding Experience 2.0 as an Advisor<br>- [Product Backlog Item 788241](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/788241): Group 2.2 B,C,D document configuration creation and indexing<br>- [Product Backlog Item 776818](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/776818): [Salesforce Integration Group-2.2B] - Create default Account for Ascensus (Co-Pilot) Fee Based IK no advisor product<br>- [Product Backlog Item 787275](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/787275): [Salesforce Integration Group 2.2B] - Create Plan Sponsor Contact Processing for Ascensus (Copilot) Ik Fee Based No Advisor product<br>- [Product Backlog Item 788441](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/788441): [Salesforce Integration Group 2.2B] - Create and Close an opportunity in Salesforce for Ascensus (Co-Pilot) Ik Fee Based No Advisor<br>- [Product Backlog Item 788254](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/788254): Group 2.2 B,C,D DCA batch replication update<br>- [Product Backlog Item 789543](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/789543): Add flag to indicate when Allow Duplicate EIN should prevent EIN lookups<br>- [Product Backlog Item 791206](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/791206): Chorus Configuration for Plan Type field<br>- [Product Backlog Item 791516](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/791516): Add logic to prevent some commands to be executed twice (duplicate Chorus issues)<br>- DCA Partner Dashboard UI Enhancements for IST features (hidden in PRO due to feature flag)<br> |
| Octopus Variables for PRO | <br>Octopus variable for PRO in DCA.Partner.Dashboard.UI<br>- FeatureFlags:EnableISTDashboard = false<br> |

| <br>#### ****Release Management (Unqork audit tool) info:****<br> |  |
| --- | --- |
| Qonnectors | [Release Management - QA](https://retsupport-qax.unqork.io/app/udlc-release#/display/release-dashboard) |
| Docusign | N/A |

#### **External Resources:**

| App Engineer | [@Siddhartha Singh](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Siddhartha.Singh%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a384b82128018583343abf0042) | Required |
| --- | --- | --- |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | <br> | N/A |
| <br> | <br> | <br> |

#### **Teams Involved:**

| Team White |  |  | <br> |  |  |
| --- | --- | --- | --- | --- | --- |
| Team Archers | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |

**Pre-Implementation Tasks**

| <br>☒<br> | A new TrakIT is created for the deployment | <br>[@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)<br> | April15th | [27594] |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April15th | <br> |
| <br>☒<br> | <br>All current Onboarding database stories for Group2 up to sprint 94  are completed<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April15th | <br> |
| <br> | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April15th | <br>SetUp Plan Api DB TrakIT - [XXXXX]<br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April15th | <br> |
| <br>☒<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>April15th | <br> |
| <br>☒<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>April15th | <br> |
| <br>☒<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

**Implementation Tasks**

| <br>☒<br> | April6th | <br>Onboarding.Data<br> | DevOps | See above | <br>API as of 12 May 2026 (EOD)<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | See above | API as of 12 May 2026 (EOD) |
| <br> | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | API as of 12 May 2026 (EOD) |
| <br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | API as of 12 May 2026 (EOD) |
| <br> | follow | Onboarding.Portal | DevOps | N/A | API as of 12 May 2026 (EOD) |
| <br> | follow | Partner Dashboard MFE | <br>DevOps<br> | <br>See above<br> | UI version as of 12 May 2026 (EOD) |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Test IST dashboard is hidden<br>Test that Only Balance Forward can be selected in SalesPortal PRO<br>Test that Group2 flows for BAML and SB are working as expected in all the downstream systems<br>Test that Ascensus Grp2.2A is working as expected in all the downstream systems<br>Test that when DCA Document Replication Hangfire job ran, relevant documents for Ascensus Grp2.2A are getting replicated to DCA<br>Test that New Security end points are working in PRO using swagger as the related UI is not present in PRO<br>Test that Commands cannot be duplicated for a specific onboardingId<br>Test that Advisor Sold enhancements to Onboarding.Api didn't impact Group2 and Group2.2A<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |

#### **Rollback strategy**

| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.258](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.258)<br>- Onboarding.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1385](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1385)<br>- Onboarding.Messaging.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.791](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.791)<br>- Onboarding.Workflow.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.831](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.831)<br>- Onboarding.Portal => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.148](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.148)<br>- DCA Partner Dashboard UI => [https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.96](https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.96) (to be updated)<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br> | <br> | <br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | Rollback DBA | <br> | <br> |  |
