# Feb21st 2025- TrkIT 24553: Onboarding Implementation Plan

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Feb21st-2025--TrkIT-24553-Onboarding-Implementation-Plan-305967490.aspx) | Created: 2025-02-14 | Last modified: 2025-11-06 | Author: Chris Reynolds | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### ****TrackIT info:****<br> |  |
| --- | --- |
| TrackIT # | 24553 |
| TrakIT Name | Team White Onboarding.Api and Onboarding.Api.Workflow Api deployments |
| Implementation Date: | Feb 21st 2025 |
| Implementation Items: | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.10](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.10)<br>- Onboarding.Api=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.284](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.284)<br>- Onboarding.Workflow.Api=>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.107](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.107)<br>- Onboarding.Setup.Plan=>N/A<br>- Database Scripts:<br>  - [DataLoad_Msvc_PlanSetupToMsvc_Onboarding.sq](http://tfs.ascensus.com:8080/tfs/Archive/Source/_versionControl?path=$/Source/1.%20Dev/Database/SqlServer/Msvc_Onboarding/Sql/DataLoad_Msvc_PlanSetupToMsvc_Onboarding.sql)l (TrakIT 24332)<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer | <br> | Required |
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
| <br>☐<br> | Implementation Planning Meeting | [@Max Shakirov](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Max.Shakirov%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a36e77c028016f3b8fdd770025) | <br> | Done |
| <br>☐<br> | A new TrakIT is created for the deployment | [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022) | <br> | Done |
| <br>☐<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Feb 21st | Done |
| <br>☐<br> | <br>FeatureFlag implementation story is complete - Team White<br> | [@Diego Emanuel Travieso](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=DiegoEmanuel.Travieso%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a389c88ae20189f97a0e740019) | <br> | <br>what is the name of it ? How do we verify?<br>WriteToArk is set to false for QA and PRO<br>Confirm there are different entries in Octopus for QA and PRO<br> |
| <br>☐<br> | <br>FeatureFlag implementation story is complete - Team Archers<br> | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) | <br> | <br>what is the name of it ? How do we verify?<br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) Please find the details here -<br>[Feature Flags: EnableMockBehavior - Team Archers (Satellite) - Ascensus - Confluence](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Feature-Flags-EnableMockBehavior-305971927.aspx)<br> |
| <br>☐<br> | <br>All current Onboarding database stories are completed<br> | <br> | <br> | <br> |
| <br>☐<br> | <br>DBAs have created an empty Msvc_Onboarding database with our DB user (msvc_onboarding)<br> | <br> | <br> | <br> |
| <br>☒<br> | <br>The variables within the Feature Flag file is setup to be replaced during deployment<br> | [@Franklin Zabala](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Franklin.Zabala%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a34c885b44014ca379d80b0002) | <br> | Done |
| <br>☐<br> | <br>Verify that all project variables and library variables in Octopus have PRO value<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br> | Done |
| <br>☐<br> | <br>Talk to Team Ember and ensure that our connection string and EIM db user/pwd to DataWarehouse is accurate<br> | <br>@Anitha Moturi<br>EIM_Onboarding<br> | Feb 20th | Done |
| <br>☐<br> | <br>Verify the setup of FeatureFlag values in PRO on Octopus<br> | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br> | Done |
| <br>☐<br> | <br>Read-only access to Msvc_Onboarding SQL database in PRO is obtained ahead of the deployment<br> | <br>@Anitha Moturi<br>[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br>@Matthew Cox<br> | Feb 21st | Submitted the fresh service tickets |
| <br>☐<br> |  | <br> | <br> | <br> |
| <br>☐<br> | <br>The SecureAuth realm for PRO is functioning<br> | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br> | Done |
| <br> | <br>FileShare/NetworkShare<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br> | Done |
| <br> | <br>Rabbit MQ for PRO<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br> | <br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | Done |
| <br>☐<br> | Workbook is reviewed and checked into TrakIT | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | Done |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | Done |
| <br>☐<br> | Update TrakIT 24332 status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Feb 20th | Done |
| <br>☐<br> | Update TrakIT 24534 status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Feb 20th | Done |
| <br>☐<br> | Business Awareness of PRO rolls (if needed) | <br> | <br> | <br> |
| <br>☐<br> | DBA Awareness of PRO rolls (if needed) | <br> | <br> | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br> | <br>**Expected Start Time (ET)**<br> | <br>**Task**<br> | <br>**Owner**<br> | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | 10:00 AM | <br>Notify NOC of monitoring and Application support is starting<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps | Notify that there will be new services tracked |
| <br>☐<br> | TIME | <br>Onboarding.Data => version TBD<br> | DevOps | (include Link to Octopus) |
| <br>☐<br> | TIME | <br>Onboarding.Api=> version TBD<br> | DevOps | (include Link to Octopus) |
| <br>☐<br> | TIME | <br>Onboarding.Workflow.Api=> version TBD<br> | <br> | <br> |
| <br>☐<br> | TIME | <br>Onboarding.Setup.Plan=> version TBD<br> | Consult with Pankaj what kind of testing is needed | <br> |
| <br>☐<br> | TIME | <br>DBA Step<br> | DBA | Data seed |
| <br>☐<br> | TIME | Verify state of the database | <br> | <br> |
| <br> | <br> | <br>Postman collection for external endpoints exposed through Kong is created for PRO<br> | Dev | <br> |
| <br>☐<br> | TIME | <br>Verify that RabbitMQ exchanges that we expect to be in place are present:<br> | DevOps | <br> |
| <br>☐<br> | TIME | Verify that Elk logs exist in PRO.  Also, ensure that an index is created. | <br> | <br> |
| <br>☐<br> | TIME | Verify that New Relic is registering it's own APM transactions and deployment tracking | [@Franklin Zabala](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Franklin.Zabala%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a34c885b44014ca379d80b0002) | <br> |
| <br>☐<br> | TIME | Verify swagger for all APIs | <br> | <br> |
| <br>☐<br> | TIME | QE Testing | <br> | <br> |
| <br> | <br> |  | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> |
| <br> | <br> |  | <br> | <br> |
| <br> | <br> |  | <br> | <br> |
| <br> | TIME | <br>Verify the setup of FeatureFlag values in PRO<br> | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)/@Irina Stensky<br> | <br> |
| <br>☐<br> | TIME | Business Testing | <br> | <br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | DevOps | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps | <br> |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Roll-forward<br> | <br>Roll-forward to a new version that address any issue(s)<br> | <br> | <br> |
| <br>☐<br> | Rollback DBA | Roll-forward to a new version that address any issue(s) | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
