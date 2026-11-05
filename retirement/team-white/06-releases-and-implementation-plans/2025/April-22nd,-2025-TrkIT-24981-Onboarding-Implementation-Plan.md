# April 22nd, 2025 TrkIT 24981: Onboarding Implementation Plan

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-April-22nd,-2025-TrkIT-24981-Onboarding-Implementation-Plan-315567824.aspx) | Created: 2025-04-15 | Last modified: 2025-04-21 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br> |  |
| --- | --- |
| TrakIT | 24981 |
| TrakIT Name | Team White Onboarding.Api and Onboarding.Api.Workflow Api and Onboarding.Setup.Plan deployments |
| Implementation Date: | April 22nd 2025 at 8.30AM |
| Implementation Items: | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.54](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.54)<br>- Onboarding.Api=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.401](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.401)<br>- Onboarding.Workflow.Api=>[https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.144](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.144) [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.212](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.212)<br>- Onboarding.Setup.Plan=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.307](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.307)<br>- Database Scripts<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer | Irina stensky | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | <br> | Required |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team White |  |  | <br> |  |  |
| Team Archers | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | Implementation Planning Meeting | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br> | Done |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022) | <br> | Done |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Apr22nd | Done |
| <br>☐<br> | <br>All current Onboarding database stories up to sprint 69 are completed<br> | <br> | Apr21st | Done |
| <br>☐<br> | <br>Verify that all project variables and library variables in Octopus have PRO value<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br>  <br> | <br>Need to setup Octopus variables for Onboarding.Setup.Plan work with [@Unknown User (ivrodrig)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28ivrodrig%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a392cc9278019366730465002a) /[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> |
| <br>☐<br> | <br>Verify the setup of FeatureFlag values in PRO on Octopus<br> | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br>  <br> | <br>Onbording.Workflow.API Notifications:Targets:Enabled =  **false for pro**<br>Onbording.Workflow.API Feature Flag WriteToArk is set to **false for Pro**<br>Onboarding.Workflow.API Feature Flag CreateChorusWorkItem  is set to**false**  **for Pro**<br>Onboarding.Plan.Setup Feature flag -  EnableMockBehaviour is set to **true for PRO**<br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Done | <br> |
| <br>☒<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Done  <br> | <br> |
| <br>☐<br> | Update TrakIT 24647 status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> Done | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br> | <br>**Expected Start Time (ET)**<br> | <br>**Task**<br> | <br>**Owner**<br> | <br>**Version**<br> | <br>**Comments**<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☐<br> | 8:30 April 22,2025 | <br>Onboarding.Data<br> | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.54](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.54) | (include Link to Octopus) |
| <br>☐<br> | follow | <br>Onboarding.Api<br> | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.401](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.401) | (include Link to Octopus) |
| <br>☐<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.212](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.212) | (include Link to Octopus) |
| <br>☐<br> | follow | <br>Onboarding.Setup.Plan<br> | Consult with Pankaj what kind of testing is needed | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.307](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.307) | (include Link to Octopus) |
| <br>☐<br> | TIME | Verify state of the database | <br> | <br> | <br> |
| <br> | <br> | <br>Postman collection for external endpoints exposed through Kong is created for PRO<br> | Dev | <br> | check new end points [@Diego Emanuel Travieso](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=DiegoEmanuel.Travieso%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a389c88ae20189f97a0e740019) |
| <br>☐<br> | TIME | Verify that Elk logs exist in PRO.  Also, ensure that an index is created. | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br> |  |
| <br> | TIME | Verify hangfire in pro.  Test in UI | [@Shankar Satijani](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Shankar.Satijani%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a34acb2c57014acb59e45d0318) | <br> |  |
| <br>☐<br> | TIME | QE Testing with Feature Flag On | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> |  | <br> |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Test Dealer Endpoint<br>Test ResumeWorkflow feature<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Roll-forward<br> | <br>Roll-forward to a new version that address any issue(s)<br> | <br> | <br> |
| <br> | <br>all apps need version to roll back<br> | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.46](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.46)<br>- Onboarding.Api=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.375](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.375)<br>- Onboarding.Workflow.Api=>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.190](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.190)<br>- Onboarding.Setup.Plan=>[https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.2](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.277)77<br> | <br> | <br> |
| <br>☐<br> | Rollback DBA | Roll-forward to a new version that address any issue(s) | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
