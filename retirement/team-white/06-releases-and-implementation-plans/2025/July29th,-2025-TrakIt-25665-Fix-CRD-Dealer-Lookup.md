# July29th, 2025 TrakIt [25665]: Fix CRD Dealer Lookup

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-July29th,-2025-TrakIt-[25665]-Fix-CRD-Dealer-Lookup-331399060.aspx) | Created: 2025-07-23 | Last modified: 2025-07-29 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br> |  |
| --- | --- |
| TrakIT | 25665 |
| TrakIT Name | Fix CRD Dealer Lookup |
| Implementation Date: | July29th at 4PM |
| Implementation Items: | <br>DB Backup by DBA at 3.50pm<br>Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.102](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.102)<br>Onboarding.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.590](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.590)<br>Onboarding.Workflow.api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.412](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.412)<br>Onboarding.Messaging.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.128](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.128)<br>Onboarding.PlanSetUp.Api => N/A<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer | Irina stensky | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Suraj Kumar | Required for DB Backup |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team White | <br>Paul Peca<br> |  | Enes Ulakaya | <br>Pete Bretz<br> | <br>Team White Developers<br> |
| Team Archers | Paul Peca | <br> | <br> | <br> | Team Archers |
| <br> | <br> | <br> | <br> | <br> | <br> |

#### **Notification to be sent to :**

| <br>**Team**<br> |
| --- |
| Team White Developers |
| Team Archers |
| Aashay Bhargava |
| Himanshu Mishra |
| Ian Macphail |
| Jodi Morrison |
| Rebecca Wichner |
| Suraj Kumar |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | Implementation Planning Meeting | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | July28th | <br> |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022) | July25th | Done |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July28th | <br> |
| <br>☒<br> | <br>All current Onboarding database stories for Group2 up to sprint 74  are completed<br> | <br> | July28th | <br> |
| <br> | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July25h | <br>SetUp Plan Api- TrakIT<br> |
| <br>☐<br> | <br>Verify that all project variables and library variables in Octopus have PRO value<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br>  <br> | <br>Need to setup Octopus variables for Onboarding.Setup.Plan work with [@Unknown User (ivrodrig)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28ivrodrig%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a392cc9278019366730465002a) /[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | Done |
| <br>☒<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>July28th | <br> |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July28th  <br> | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br> | <br>**Expected Start Time (ET)**<br> | <br>**Task**<br> | <br>**Owner**<br> | <br>**Version**<br> | <br>**Comments**<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | 4.00 pm July28th 2025 | <br>Onboarding.Data<br> | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.102](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.102) | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.590](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.590) | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.412](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.412) | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Setup.Plan<br> | Consult with Pankaj what kind of testing is needed | <br> | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.128](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.128) | (include Link to Octopus) |
| <br>☐<br> | TIME | Verify state of the database | <br> | <br> | <br> |
| <br>☐<br> | TIME | QE Testing with Feature Flags On | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> |  | <br> |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Create one plan from AscensusDailyFB from PRO DOE with unregistered Advisor CRD number (Nick)<br>Check Workflow gets to Final for that plan in DB (Nick)<br>Chorus item gets created (Alex)<br>Save document to cliff is successful  (Alex)<br>PEK Excel is downloadable  in xlsx and rendered for the 8 plans (Alex)<br>PDFs are downloadable from Cliff in pdf format for all the plans (Alex)<br>"View as PDF" option working on cliff for all the PDF docs (Alex)<br>Verify that plan got all the required document types (Alex)<br>Check Hangfire jobs in PRO (verify if the Hangfire job is listed without error on the Hangfire Dashboard, in case we see an error, then try to execute the job one more time )<br>Verify the ARK data in PRO for the plan created (Pankaj)<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Roll-forward<br> | <br>Roll-forward to a new version that address any issue(s)<br> | <br> | <br> |
| <br> | <br>all apps need version to roll back<br> | <br>- Onboarding.Data => Invalidate build 102 and restore the DB Onboarding.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.5](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.519)51 Onboarding.Workflow.api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.3](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.364)89 Onboarding.SetUpPlan.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.458](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.458)<br> | <br> | <br> |
| <br>☐<br> | Rollback DBA | Roll-forward to a new version that address any issue(s) | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
