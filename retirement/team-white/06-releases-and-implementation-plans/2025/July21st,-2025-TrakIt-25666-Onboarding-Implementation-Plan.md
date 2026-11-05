# July21st, 2025 TrakIt [25666]: Onboarding Implementation Plan

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-July21st,-2025-TrakIt-[25666]-Onboarding-Implementation-Plan-331396038.aspx) | Created: 2025-07-18 | Last modified: 2025-07-21 | Author: Anitha Moturi | Last editor: Eddie Hooper

---

#### **Implementation Tasks**

| <br> |  |
| --- | --- |
| TrakIT | 25666 |
| TrakIT Name | Team White Add Chorus Email LOB |
| Implementation Date: | July21st at 4PM |
| Implementation Items: | <br>Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.97](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.97)<br>Onboarding.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.551](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.551)<br>Onboarding.Workflow.api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.389](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.389)<br>Manually update ingress with following annotation<br>annotations:  <br>    meta.helm.sh/release-name: onboarding-workflow-api  <br>    meta.helm.sh/release-namespace: onboarding  <br>    [nginx.ingress.kubernetes.io/proxy-connect-timeout](http://nginx.ingress.kubernetes.io/proxy-connect-timeout): "300"  <br>    [nginx.ingress.kubernetes.io/proxy-read-timeout](http://nginx.ingress.kubernetes.io/proxy-read-timeout): "300"  <br>    [nginx.ingress.kubernetes.io/proxy-send-timeout](http://nginx.ingress.kubernetes.io/proxy-send-timeout): "300"<br>Onboarding.Messaging.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.94](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.94)<br>Onboarding.PlanSetUp.Api => N/A<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer | Irina stensky | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Suraj Kumar | Required |

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
| <br>☒<br> | Implementation Planning Meeting | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | July18th | Done |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022) | July18th | Done |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July18th | Done |
| <br>☒<br> | <br>All current Onboarding database stories for Group2 up to sprint 74  are completed<br> | <br> | July18th | <br> |
| <br> | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July9th | <br>SetUp Plan Api- TrakIT<br> |
| <br>☐<br> | <br>Verify that all project variables and library variables in Octopus have PRO value<br> | [@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003) | <br>  <br> | <br>Need to setup Octopus variables for Onboarding.Setup.Plan work with [@Unknown User (ivrodrig)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28ivrodrig%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a392cc9278019366730465002a) /[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022)<br> |
| <br>☐<br> | <br>Verify the setup of FeatureFlag values in PRO on Octopus<br> | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br>change the value of  EnableMockBehaviour only after TeamWhite finishes their testing of other features first | <br>Enable TeamsNotifications, Enable writing to Ark and Enable creating chorus items in PRO<br>Onbording.Workflow.API Feature Flag WriteToArk is set to true **for Pro**<br>Onboarding.Workflow.API Feature Flag CreateChorusWorkItem  is set to**true**  **for Pro**<br>Onboarding.Plan.Setup Feature flag -  EnableMockBehaviour is set to false**for PRO**<br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | Done |
| <br>☒<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>July18th | Done |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | July18th  <br> | Done |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br> | <br>**Expected Start Time (ET)**<br> | <br>**Task**<br> | <br>**Owner**<br> | <br>**Version**<br> | <br>**Comments**<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | 3.00 pm June26th 2025 | <br>Onboarding.Data<br> | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.97](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.97) | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.551](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.551) | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.389](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.389) | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Setup.Plan<br> | Consult with Pankaj what kind of testing is needed | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.512](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.512) | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.94](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.94) | (include Link to Octopus) |
| <br>☐<br> | TIME | Verify state of the database | <br> | <br> | <br> |
| <br> | <br> | <br>Postman collection for external endpoints exposed through Kong is created for PRO<br> | Dev | <br> | <br>check new admin end points - Get Advisor , Get Sponsor<br>check new end point for workflow<br> |
| <br>☐<br> | TIME | Verify that Elk logs exist in PRO.  Also, ensure that an index is created. | <br>[@Unknown User (istensky)](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Unknown%20User%20%28istensky%29&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3591489ef015984a1a0c40003)<br> | <br> |  |
| <br>☐<br> | TIME | QE Testing with Feature Flags On | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> |  | <br> |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Create one plan from AscensusDailyFB from PRO DOE with unregistered Advisor CRD number (Nick)<br>Check in DB that OnboardingState is "PlanIdInArkCreated" state (Anitha)<br>Sponsor flow is done from DOE (Nick)<br>Check in DB that OnboardingState is still "PlanIdInArkCreated" state (Anitha)<br>Update the advisor blob with advisor CRD number "123456" through swagger for that Onboarding Id (Anitha)<br>Complete Docusign for that plan from DOE (Nick)<br>Check Workflow gets to Final for that plan in DB (Anitha)<br>Cliff Document Ids saved by document type in DB (Anitha)<br>Chorus item gets created with EMAL LOB (Anitha)<br>Save document to cliff is successful  (Alex)<br>PEK Excel is downloadable  in xlsx and rendered for the 8 plans (Alex)<br>PDFs are downloadable from Cliff in pdf format for all the plans (Alex)<br>"View as PDF" option working on cliff for all the PDF docs (Alex)<br>Verify that plan got all the required document types (Alex)<br>Check Hangfire jobs in PRO (verify if the Hangfire job is listed without error on the Hangfire Dashboard, in case we see an error, then try to execute the job one more time ) - Anitha<br>Verify the ARK data in PRO for the plan created (Pankaj)<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Roll-forward<br> | <br>Roll-forward to a new version that address any issue(s)<br> | <br> | <br> |
| <br> | <br>all apps need version to roll back<br> | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.86](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.86) Onboarding.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.519](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.519) Onboarding.Workflow.api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.364](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.364) Onboarding.SetUpPlan.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.458](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.458)<br> | <br> | <br> |
| <br>☐<br> | Rollback DBA | Roll-forward to a new version that address any issue(s) | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
