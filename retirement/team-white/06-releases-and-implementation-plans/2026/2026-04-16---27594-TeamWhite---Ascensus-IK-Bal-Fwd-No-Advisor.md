# 2026-04-16 - [27594] TeamWhite - Ascensus IK Bal Fwd No Advisor

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2026-04-16---[27594]-TeamWhite---Ascensus-IK-Bal-Fwd-No-Advisor-380116906.aspx) | Created: 2026-04-10 | Last modified: 2026-04-16 | Author: Chris Reynolds | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### ****TrackIT info:****<br> |  |
| --- | --- |
| TrackIT # | [27594] |
| TrakIT Name | Team White DOE Group 2.2 Ascensus I(k) Balance Forward No Advisor |
| Implementation Date: | April 16th 2026 9.30AM |
| Implementation Items: | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.258](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.258)<br>- Onboarding.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1385](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1385)<br>- Onboarding.Messaging.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.791](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.791)<br>- Onboarding.Workflow.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.831](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.831)<br>- Onboarding.Portal => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.148](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.148)<br>- DCA Partner Dashboard UI => [https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.96](https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.96) (to be updated)<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)> N/A<br> |
| Summary of Changes | <br>Deployment includes<br>- [Product Backlog Item 777467](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/787600)[: Ensure Correct Branding Displays Between Sales Portal and Onboarding Portal and Unqork? and Welcome Email?](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/787600)<br>- [Product Backlog Item 742967](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/742967): Plan sponsor email generated from Sales Portal-No Advisor (Direct Sold)<br>- [Product Backlog Item 744581](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/744581): Ability to Resend Email to Plan Sponsor in Case of Incorrect Email<br>- [Product Backlog Item 778914](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/787600)[: Document Upload to Cliff for Group 2.2 Dynamic Product Offering Keys](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/787600) [Product Backlog Item 787582](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/787582): Implement Completion Email and Prior Plan Document Email for IK-Bal Forward<br>- [Product Backlog Item 787600](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/787600): Chorus: NBIKINSTAL Make sure Ascensus BalForwardNoAdvisor plans have a valid ONTP field<br>- [Product Backlog Item 763870](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/763870): [Salesforce Integration] - Replace the Plan ID in the Opportunity name with the Business Name<br>- [Product Backlog Item 788609](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/788609): Bug: Resolve hard stop from partner dashboard failing with 400 bad request<br>- Sales Portal for Ascensus IK BalFwd No Advisor product<br>- DCA Partner Dashboard UI Enhancements for IK BalFwd No Advisor product<br>- DOE (Unqork UI) for Ascensus IK BalFwd No Advisor<br> |
| Octopus Variables for PRO | <br>Octopus variable for PRO in DCA.Partner.Dashboard.UI<br>- FeatureFlags:EnableISTDashboard = false<br> |

| <br>#### ****Release Management (Unqork audit tool) info:****<br> |  |
| --- | --- |
| Qonnectors | [Release Management - QA](https://retsupport-qax.unqork.io/app/udlc-release#/display/release-dashboard) |
| Docusign | [https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=69e0da95f9f5f669daf2240a](https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=69e0da95f9f5f669daf2240a) |

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

| <br>☒<br> | April6th | <br>Onboarding.Data<br> | DevOps | See above | <br>API as of 13 Apr 2026 (EOD)<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | See above | API as of 13 Apr 2026 (EOD) |
| <br> | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | API as of 13 Apr 2026 (EOD) |
| <br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | N/A |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | API as of 13 Apr 2026 (EOD) |
| <br> | follow | Onboarding.Portal | DevOps | N/A | API as of 13 Apr 2026 (EOD) |
| <br> | follow | Partner Dashboard MFE | <br>DevOps<br> | <br>See above<br> | UI version as of 15 April 2026 (EOD) |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Test IST dashboard is hidden<br>Test that Only Balance Forward can be selected in SalesPortal PRO<br>Test IK BalFwd No Advisor Startup Plan<br>Test IK BalFwd No Advisor Transfer plan<br>Verify Branding is correct on all pages and emails<br>Verify the IK BalFwd No Advisor Emails(Welcome Email, Completion Email and Prior Plan Document Email in case of transfer)<br>Verify that the Partner Dashboard is reflecting the progress of Ascensus BalFwd No Advisor plans<br>Verify Documents got uploaded to cliff for IK BalFwd No Advisor Startup and Transfer plans<br>Verify NBIKINSTAL Chorus item got created and check that all LOBs are present and values are correct<br>Verify that the Salesforce opportunity includes the advisor’s business name whenever it is available at the time of creation<br>If the business name is not provided in the advisor data,  Verify that the Salesforce opportunity gets "Plan xxxxx" as it's name<br>Test Hardstop scenarios for Ascensus IK BalFwd No Advisor<br>Test Hardstop and Resolve Hardstop (All Scenarios for BAML and SB except Allow Duplicate Ein case)<br>Test AllowDuplicateEin for BAML and SB and Ascensus IK BalFwd No Advisor<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |

#### **Rollback strategy**

| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.252](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.252)<br>- Onboarding.Api =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1355](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1355)<br>- Onboarding.Messaging.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.773](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.773)<br>- Onboarding.Workflow.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.809](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.809)<br>- Onboarding.Portal => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.130](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.130)<br>- DCA Partner Dashboard UI =>  [https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.92](https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.92)<br>- Onboarding.Setup.Plan=> N/A<br>- [Onboarding.Setup.Plan.Consumer =>](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148) N/A<br> | <br> | <br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | Rollback DBA | <br> | <br> |  |
