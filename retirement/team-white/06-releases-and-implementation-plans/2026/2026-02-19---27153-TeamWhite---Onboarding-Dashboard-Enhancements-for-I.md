# 2026-02-19 -[27153] TeamWhite - Onboarding Dashboard Enhancements for Internal Users

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2026-02-19--[27153]-TeamWhite---Onboarding-Dashboard-Enhancements-for-Internal-Users-368319424.aspx) | Created: 2026-02-05 | Last modified: 2026-02-19 | Author: Nic Kopetsky | Last editor: Nic Kopetsky

---

#### **Implementation Tasks**

| <br>#### ****TrackIT info:****<br> |  |
| --- | --- |
| TrackIT # | [27153] |
| TrakIT Name | TeamWhite - Onboarding Dashboard Enhancements for Internal Users |
| Implementation Date: | 2-19-2026 |
| Implementation Items: | <br>- Onboarding.Api => 1.0.1179<br>- Onboarding.Dashboard => 1.0.47<br>- Partner Dashboard => 1.0.52<br> |
| Summary of Changes | <br>Addition of features for internal dashboard users that includes the following:  <br>Ability to cancel a plan from the plan Modal  <br>Ability to reactive/extend a plan that has previously expired   <br>Ability to resolve a hard stop in the plan modal so that the user can resume onboarding  <br>Ability to view the Data Blob from Plan Modal<br>Add feature flags so that Cancel and Extend functions are disabled in PRO<br> |

#### **External Resources:**

| App Engineer | <br> | Required |
| --- | --- | --- |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | <br> | n/a |

#### **Teams Involved:**

| Team White | <br>Paul Peca<br> |  | Enes Ulakaya | <br>Pete Bretz<br> | <br>Team White Developers<br> |
| --- | --- | --- | --- | --- | --- |
| <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |

#### **Notification to be sent to :**

| Ian Macphail, Jodi Morrison, Rebecca Wichner, Sherry McNeal, Team White Developers |
| --- |

**Pre-Implementation Tasks**

| <br>☒<br> | Implementation Planning Meeting |  | <br> | <br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | A new TrakIT is created for the deployment | <br> | <br> | [27153] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | <br> | <br> | 2/19/2026 at 3:30 ET |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | <br> | <br> | <br> |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | <br> | <br>  <br> | <br> |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | <br> | <br>  <br> | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br>☒<br> | Jan27th | <br>Onboarding.Data<br> | DevOps | See above | (include Link to Octopus) |
| --- | --- | --- | --- | --- | --- |
|  | follow | <br>Onboarding.Api<br> | DevOps | See above | (include Link to Octopus) |
| <br> | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Portal | DevOps | N/A | (include Link to Octopus) |
| <br> | follow | Partner Dashboard MFE | <br>DevOps<br> | <br>See above<br> | (include Link to Octopus) |
| <br>☐<br> | TIME | QE Testing with Feature Flags On | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> |  | <br> |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Test Partner dashboard<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |

#### **Rollback strategy**

| <br>☐<br> | <br>Roll-forward<br> |  | <br> | <br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>all apps need version to roll back<br> |  | <br> | <br> |
| <br>☐<br> | Rollback DBA | <br> | <br> | <br> |
