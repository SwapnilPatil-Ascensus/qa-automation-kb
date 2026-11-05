# July31st, 2025 TrakIt [25766]: SetUp Plan Api Deployment

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-July31st,-2025-TrakIt-[25766]-SetUp-Plan-Api-Deployment-336399249.aspx) | Created: 2025-07-30 | Last modified: 2025-07-30 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br> |  |
| --- | --- |
| TrakIT | 25766 |
| TrakIT Name | SetUp Plan Api Deployment |
| Implementation Date: | July31st at 4PM |
| Implementation Items: | <br>Onboarding.PlanSetUp.Api => [Releases > Release 1.0.554 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.554)<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer | Irina stensky | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Scott Kirkpatrick | - |

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
| Scott Kirkpatrick |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | Implementation Planning Meeting | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | July30th | <br> |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022) | July30th | Done |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July30th | <br> |
| <br>☒<br> | <br>All current Onboarding database stories for Group2 up to sprint 76  are completed<br> | <br> | July30th | <br> |
| <br> | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July31st | <br>SetUp Plan Api DB TrakIT - 25767<br> |
| <br>☐<br> | <br>Verify that all project variables and library variables in Octopus have PRO value<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br>  <br> | <br>Need to setup Octopus variables for Onboarding.Setup.Plan work with [@Unknown User (ivrodrig)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28ivrodrig%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a392cc9278019366730465002a) /[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | Done |
| <br>☒<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>July30th | <br> |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July30th  <br> | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br> | <br>**Expected Start Time (ET)**<br> | <br>**Task**<br> | <br>**Owner**<br> | <br>**Version**<br> | <br>**Comments**<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | 4.00 pm July28th 2025 | <br>Onboarding.Data<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Setup.Plan<br> | Consult with Pankaj what kind of testing is needed | [Releases > Release 1.0.554 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.554) | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | (include Link to Octopus) |
| <br>☐<br> | TIME | Verify state of the database | <br> | <br> | <br> |
| <br>☐<br> | TIME | QE Testing with Feature Flags On | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> |  | <br> |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Create one plan for Pershing from PRO DOE (Anitha)<br>Check Workflow gets to Final for that plan in DB (Anitha)<br>Chorus item gets created (Anitha)<br>Save document to cliff is successful  (Anitha)<br>PEK Excel is downloadable  in xlsx and rendered for the 8 plans (Anitha)<br>PDFs are downloadable from Cliff in pdf format for all the plans (Anitha)<br>"View as PDF" option working on cliff for all the PDF docs (Anitha)<br>Verify that plan got all the required document types (Anitha)<br>Check Hangfire jobs in PRO (verify if the Hangfire job is listed without error on the Hangfire Dashboard, in case we see an error, then try to execute the job one more time - Anitha )<br>Verify the ARK data in PRO for the plan created (Pankaj)<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Roll-forward<br> | <br>Roll-forward to a new version that address any issue(s)<br> | <br> | <br> |
| <br> | <br>all apps need version to roll back<br> | <br>- Onboarding.Data => Invalidate build 102 and restore the DB Onboarding.Api => Onboarding.Workflow.api => Onboarding.SetUpPlan.Api =><br> | <br> | <br> |
| <br>☐<br> | Rollback DBA | Roll-forward to a new version that address any issue(s) | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
