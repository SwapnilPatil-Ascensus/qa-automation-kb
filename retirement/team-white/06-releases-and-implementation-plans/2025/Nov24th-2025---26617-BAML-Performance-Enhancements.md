# Nov24th 2025 - [26617] BAML Performance Enhancements

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Nov24th-2025----[26617]-BAML-Performance-Enhancements-352342455.aspx) | Created: 2025-11-24 | Last modified: 2025-11-24 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br> |  |
| --- | --- |
| TrakIT | [26617] |
| TrakIT Name | Team White - BAML Performance Enhancements |
| Implementation Date: | Nov24th at 2.30PM |
| Implementation Items: | <br>Onboarding.Portal - [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.115](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.115)<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer | <br>Sharon Chaggar<br>Siddhartha Singh<br> | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Scott Kirkpatrick | N/A |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team White | <br>Paul Peca<br> |  | Enes Ulakaya | <br>Pete Bretz<br> | <br>Team White Developers<br> |
| Team Archers | Paul Peca | <br> | <br> | <br> | Team Archers |
| <br> | <br> | <br> | <br> | <br> | <br> |

#### **Notification to be sent to :**

| <br>**Team**<br> |
| --- |
| Team White Developers, Team Archers, Aashay Bhargava, Himanshu Mishra, Ian Macphail, Jodi Morrison, Rebecca Wichner, Scott Kirkpatrick |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | Implementation Planning Meeting | [@Sharon Chaggar](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Sharon.Chaggar%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37bd837f6017be0c0e89a0005) | Nov24th | <br> |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022) | Nov24th | [26617] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Nov24th | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 84  are completed<br> | Nov17th | Nov24th | <br> |
| <br> | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Nov17th | <br>SetUp Plan Api DB TrakIT - []<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Nov24th | <br> |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Nov24th | <br> |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Nov24th | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Variables in Octopus that needs configuration for PRO**

|  | <br>**Api**<br> | <br>**Add To Library Set**<br> | <br>**Variable name**<br> | <br>**PRO Value**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | <br>Onboarding.Api<br> |  |  | <br> | <br> |
| <br> | <br>Onboarding.Messaging.Api<br> |  |  | <br> | <br> |
| <br>☒<br> | Onboarding.Workflow.Api | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br> | <br>**Expected Start Time (ET)**<br> | <br>**Task**<br> | <br>**Owner**<br> | <br>**Version**<br> | <br>**Comments**<br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | Nov17th | <br>Onboarding.Data<br> | DevOps | <br> | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | <br> | (include Link to Octopus) |
| <br>☐<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | <br> | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Portal | DevOps | [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.115](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.115) | (include Link to Octopus) |
| <br>☐<br> | TIME | QE Testing with Feature Flags On | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> |  | <br> |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Verify that BAML landing page is loading faster<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Roll-forward<br> | <br>Roll-forward to a new version that address any issue(s)<br> | <br> | <br> |
| <br> | <br>all apps need version to roll back<br> | <br>- Onboarding.Data - [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.167](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.167) Onboarding.Portal - [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.110](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.110) (check with Sharon on Octopus variables) Onboarding.Api - [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.965](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.965) Onboarding.Messaging.Api - [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.458](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.458) Onboarding.Workflow.Api - [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.611](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.611)<br> | <br> | <br> |
| <br>☐<br> | Rollback DBA | Roll-forward to a new version that address any issue(s) | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
