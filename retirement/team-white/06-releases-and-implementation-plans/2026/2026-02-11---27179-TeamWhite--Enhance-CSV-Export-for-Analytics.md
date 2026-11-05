# 2026-02-11 -[27179]TeamWhite- Enhance CSV Export for Analytics

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2026-02-11--[27179]TeamWhite--Enhance-CSV-Export-for-Analytics-368323238.aspx) | Created: 2026-02-10 | Last modified: 2026-02-11 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### ****TrackIT info:****<br> |  |
| --- | --- |
| TrackIT # | 27179 |
| TrakIT Name | TeamWhite- Enhance CSV Export for Analytics |
| Implementation Date: | 2026-02-11 at 2.30pm |
| Implementation Items: | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.213](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.213)<br>- Onboarding.Api=>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1175](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1175)<br>- Onboarding.Workflow.Api=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.716](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.716)<br>- Onboarding.Messaging.Api=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.645](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.645)<br>- Onboarding.Setup.Plan=> N/A<br>- Onboarding.Portal => N/A<br>- Onboarding.Dashboard => N/A<br>- Onboarding MFE in DCA =>N/A<br> |
| Summary of Changes | <br>Enhance HardStopReset end point for Analytics<br>Enhance Cancel Onboarding endpoint to accept cancelReason and cancelDetail for Analytics<br>Enhance Extend Onboarding endpoint<br>Enhance CSV Export for Analytics (more datapoints added)<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer | <br> | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | <br> | Required |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team White | <br>Paul Peca<br> |  | Enes Ulakaya | <br>Pete Bretz<br> | <br>Team White Developers<br> |
| Team Archers | Paul Peca | <br> | <br> | <br> | Team Archers |

#### **Notification to be sent to :**

| Ian Macphail, Jodi Morrison, Rebecca Wichner, Sherry McNeal, Team White Developers |
| --- |

**Pre-Implementation Tasks**

| <br>☒<br> | Implementation Planning Meeting | [@Sharon Chaggar](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Sharon.Chaggar%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37bd837f6017be0c0e89a0005) | Feb11th | <br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022) | Feb11th | [27179] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Feb11th | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 86  are completed<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Feb11th | <br> |
| <br> | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Feb11th | <br>SetUp Plan Api DB TrakIT - []<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Feb11th | <br> |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Feb11th | <br> |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Feb11th | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Variables in Octopus that needs configuration for PRO**

| <br>☒<br> | <br>Onboarding.Api<br> |  |  | <br> | <br> |
| --- | --- | --- | --- | --- | --- |
| <br> | <br>Onboarding.Messaging.Api<br> |  |  | <br> | <br> |
| <br>☒<br> | Onboarding.Workflow.Api | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br>☒<br> | Jan27th | <br>Onboarding.Data<br> | DevOps | See above | (include Link to Octopus) |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | See above | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | See above | (include Link to Octopus) |
| <br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | See above | (include Link to Octopus) |
| <br>☐<br> | follow | Onboarding.Portal | DevOps | N/A | (include Link to Octopus) |
| <br> | follow | Onboarding Partner MFE | <br>DevOps<br> | <br>N/A<br> | (include Link to Octopus) |
| <br>☐<br> | TIME | QE Testing with Feature Flags On | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> |  | <br> |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Test BAML Group Plan from PRO DOE<br>Test Group1 Plan from DOE<br>Run StarBackFill Hangfire job and test all CSVs generated in PRO network folder by copying those files to a different folder<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |

#### **Rollback strategy**

| <br>☐<br> | <br>Roll-forward<br> | <br>Roll-forward to a new version that address any issue(s)<br> | <br> | <br> |
| --- | --- | --- | --- | --- |
| <br> | <br>all apps need version to roll back<br> | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.207](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.207)<br>- Onboarding.Api=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1155](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1155)<br>- Onboarding.Messaging.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.629](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.629)<br>- Onboarding.Workflow.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.636](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.636)<br> | <br> | <br> |
| <br>☐<br> | Rollback DBA | Roll-forward to a new version that address any issue(s) | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
