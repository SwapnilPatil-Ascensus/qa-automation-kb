# June10th 2025 - TrakIT 25358: Onboarding Implementation Plan

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-June10th-2025---TrakIT-25358-Onboarding-Implementation-Plan-326735007.aspx) | Created: 2025-06-09 | Last modified: 2025-11-06 | Author: Pankaj Dubey | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### ****TrakIT info:****<br> |  |
| --- | --- |
| TrakIT # | 25358 |
| TrakIT Name | Team White Onboarding.Setup.Plan deployments |
| Implementation Date: | Jun 10th, 2025 1:00 PM EST |
| Implementation Items: | <br>- Onboarding.Setup.Plan=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.382](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.382)<br>- Database Scripts - [Msvc_Onboarding_Ark - Repos](https://tfs.ascensus.com/tfs/Archive/Source/_versionControl?path=$/Source/1.%20Dev/Database/SqlServer/Msvc_Onboarding_Ark)<br> |

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
| <br>☒<br> | A new TrakIT is created for the deployment | <br>[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> | Jun 09th | Done |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jun 09th | Done |
| <br>☒<br> | <br>All current Onboarding database stories in sprint 72 are completed<br> | <br> | Jun 09th | Done |
| <br>☐<br> | <br>Verify that all project variables and library variables in Octopus have PRO value<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br>Jun 09th | <br>Need to setup Octopus variables for Onboarding.Setup.Plan work with [@Unknown User (ivrodrig)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28ivrodrig%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a392cc9278019366730465002a) /[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> |
| <br>☐<br> | <br>Verify the setup of FeatureFlag values in PRO on Octopus<br> | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br>Jun 09th | <br>every deployment to verify:<br>WriteToArk is set to False<br>EnableMockBehaviour is set to true<br> |
| <br> | <br>FileShare/NetworkShare<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br> | Done |
| <br> | <br>Rabbit MQ for PRO<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br> | <br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | <br>[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> | Jun 09th | Done |
| <br>☐<br> | Workbook is reviewed and checked into TrakIT 25356 | <br>[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> | <br>Jun 09th | Done |
| <br>☒<br> | Team approves our TrakIT 25358 by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Jun 09th | Done |
| <br>☐<br> | Update TrakIT 25358 status to Awaiting Implementation to Production | <br>[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> | <br>Jun 09th | Done |
| <br>☐<br> | Business Awareness of PRO rolls (if needed) | <br>[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> | Jun 09th | Done |
| <br>☐<br> | DBA Awareness of PRO rolls (if needed) | <br> | <br> | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br> | <br>**Expected Start Time (ET)**<br> | <br>**Task**<br> | <br>**Owner**<br> | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | 1:00 PM | <br>Notify NOC of monitoring and Application support is starting<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps | Notify that there will be new services tracked |
| <br>☐<br> | 11AM | <br>Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.25](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.25)<br> | DevOps | (include Link to Octopus) |
| <br>☐<br> | follow | <br>Onboarding.Api=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.334](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.334)<br> | DevOps | (include Link to Octopus) |
| <br>☐<br> | follow | <br>Onboarding.Workflow.Api=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.145](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.145)<br> | <br> | <br> |
| <br>☐<br> | follow | <br>Onboarding.Setup.Plan=> [Releases > Release 1.0.382 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.382)<br> | Consult with Pankaj what kind of testing is needed |  |
| <br>☐<br> | TIME | <br>DBA Step<br> | DBA | Data seed |
| <br>☐<br> | TIME | Verify state of the database | <br> | <br> |
| <br> | <br> | <br>Postman collection for external endpoints exposed through Kong is created for PRO<br> | Dev | <br> |
| <br>☐<br> | TIME | Verify that Elk logs exist in PRO.  Also, ensure that an index is created. | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) |  |
| <br> | TIME | Verify hangfire in pro.  Test in UI | [@Shankar Satijani](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Shankar.Satijani%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a34acb2c57014acb59e45d0318) |  |
| <br>☐<br> | TIME | Verify that New Relic is registering it's own APM transactions and deployment tracking | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br> |
| <br>☐<br> | TIME | QE Testing with Feature Flag On | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br> |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Matt<br> | <br>- Test outcome of daily jobs  next day (Job will run at 6:00AM)<br>- Test bank routing endpoint<br>- Test either one of the brand endpoints: colors or styles<br>- Test document endpoint and ensure that newly submitted documents have metadata fields (DocumentType, Department, TransactionType) in Document table.<br>- Test CRD lookup and ensure that advisor dealer info is present now<br> |
| <br>☐<br> | TIME | Business Testing | <br> | <br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps | <br> |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Roll-forward<br> | <br>Roll-forward to a new version that address any issue(s)<br> | <br> | <br> |
| <br> | <br>all apps need version to roll back<br> | <br>- Onboarding.Setup.Plan=><br>[Releases > Release 1.0.356 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.356) | <br> | <br> |
| <br>☐<br> | Rollback DBA | Roll-forward to a new version that address any issue(s) | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
