# 2026-06-15 -[28029] Team Ravens- updating the BPD for secure 2.0 and contact details change

> Source: [Team Ravens SharePoint](https://ascensus0.sharepoint.com/sites/TeamRavens/SitePages/2026-06-15--[27673]-TeamRavens-Group-1 and Group-2 changes.aspx) | Created: 2026-06-12 | Last modified: 2026-08-28 | Author: Palak Bhatt | Last editor: Emanuel Pedraza

---

![image](https://ascensus0.sharepoint.com/_layouts/15/images/sleektemplateimagetile.jpg)

#### **Implementation Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28029] |
| TrakIT Name | Team Ravens- updating the BPD for secure 2.0 and contact details change |
| Implementation Date: | 06-15-2026 11.00AM |
| Implementation Items: | Module ID's 6802ab6a872ba2501e7043f6, 680a3f7f86c460a4a7ac9492, 68715161e9ff3edc0ed612cc |
| Summary of Changes | For all group 1 plans and the Balance Forward (no advisor): Update of the Sales email address to [SmallBusiness@ascensus.com](mailto:SmallBusiness@ascensus.com) and updating the BPD on the Confirmation of Completion email |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer |  | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Suraj Kumar | Required |
|  |  |  |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team Ravens |  |  |  |  |  |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | Palak Bhatt | <br> | [28029] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | Team Ravens | 15-June-2026 |  |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up<br> | [@Aashay Bhargava](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | 15-June-2026 |  |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | ?? | 15-June-2026 |  |
| <br>☐<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | Erik Youdal | 15-June-2026 |  |
| <br>☐<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | [Aashay Bhargava](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | 15-June-2026 |  |
| <br>☐<br> | <br>Identify & order items to be implemented<br> | <br> |  |  |
|  |  |  |  |  |

#### **Implementation Tasks**

| [ ] | 4/9 | <br>Octopus variable for PRO in DCA.Partner.Dashboard.UI<br>- FeatureFlags:EnableISTDashboard = false<br> | DevOps |  |  |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | April6th | <br>Onboarding.Data<br> | DevOps | See above | (include Link to Octopus) |
|  | follow | <br>Onboarding.Api<br> | DevOps | See above | (include Link to Octopus) |
|  | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | (include Link to Octopus) |
|  | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | (include Link to Octopus) |
| <br>☐<br> | follow | Onboarding.Portal | DevOps | N/A | (include Link to Octopus) |
|  | follow | Partner Dashboard MFE | <br>DevOps<br> | <br>See above<br> | (include Link to Octopus) |
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Test Ascensus Partner is added on the DCA partner dashboard<br>Test that search by business name, search by first name and last name is working on the Partner dashboard<br>Test AllowDuplicateEIN button on the internal user dashboard<br>Test IST dashboard is hidden<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  |  |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  |  |
|  |  |  |  |  |  |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br> |  |  |
| <br>☐<br> | Rollback DBA |  |  |  |

**Lessons Learned from Implementation and Action Items:**
