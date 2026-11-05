# 2026-01-22 -[26996] Onboarding Implementation Plan

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2026-01-22--[26996]-Onboarding-Implementation-Plan-362102079.aspx) | Created: 2026-01-13 | Last modified: 2026-01-22 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### ****TrackIT info:****<br> |  |
| --- | --- |
| TrackIT # | 26996 |
| TrakIT Name | TeamWhite - Analytics, Dynamic Product Offering Keys, Extend, Cancel and HardStop Reset changes |
| Implementation Date: | 2026-01-22 at 3pm |
| Implementation Items: | <br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.207](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.207)<br>- Onboarding.Api=>  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1106](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1106)<br>- Onboarding.Workflow.Api=> N/A<br>- Onboarding.Messaging.Api=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.582](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.582)<br>- Onboarding.Setup.Plan=> N/A<br>- Onboarding.Portal => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.130](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.130)<br>- Onboarding.Dashboard => N/A<br> |

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

| <br>☒<br> | Implementation Planning Meeting | [@Sharon Chaggar](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Sharon.Chaggar%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37bd837f6017be0c0e89a0005) | Jan22nd | <br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022) | Jan22nd | [26996] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jan22nd | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 86  are completed<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jan22nd | <br> |
| <br> | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jan22nd | <br>SetUp Plan Api DB TrakIT - []<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jan22nd | <br> |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Jan22nd | <br> |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Jan22nd | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Variables in Octopus that needs configuration for PRO**

| <br>☒<br> | <br>Onboarding.Api<br> |  |  | <br> | <br> |
| --- | --- | --- | --- | --- | --- |
| <br> | <br>Onboarding.Messaging.Api<br> |  |  | <br> | <br> |
| <br>☒<br> | Onboarding.Workflow.Api | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br>☒<br> | Jan22nd | <br>Onboarding.Data<br> | DevOps | See above | (include Link to Octopus) |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | follow | <br>Onboarding.Api<br> | DevOps | See above | (include Link to Octopus) |
| <br>☐<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | See above | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Portal | DevOps | See above | (include Link to Octopus) |
| <br>☐<br> | TIME | QE Testing with Feature Flags On | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> |  | <br> |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Add perspective Sale<br>Portal should not fail for Ascensus partner<br>Add SB Group Plan<br>Add BAML Group Plan<br>Analytics Dashboard<br>Hardstop reset testing for the test plan<br>Cancel Onboarding<br>Extend Onboarding<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |

#### **Rollback strategy**

| <br>☐<br> | <br>Roll-forward<br> | <br>Roll-forward to a new version that address any issue(s)<br> | <br> | <br> |
| --- | --- | --- | --- | --- |
| <br> | <br>all apps need version to roll back<br> | <br>- Onboarding.Data - [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.172](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.172) Onboardng.Api - [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1021](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.1021) Onboarding.Messaging.Api -  [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.504](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.504) Onboarding.Portal - [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.115](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.115) Onboarding.Workflow.Api - n/a<br> | <br> | <br> |
| <br>☐<br> | Rollback DBA | Roll-forward to a new version that address any issue(s) | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
