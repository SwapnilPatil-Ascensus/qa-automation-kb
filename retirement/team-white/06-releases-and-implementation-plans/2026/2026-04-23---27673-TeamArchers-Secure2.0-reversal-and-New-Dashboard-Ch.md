# 2026-04-23 -[27673] TeamArchers-Secure2.0 reversal and New Dashboard Changes for Setup Plan API

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2026-04-23--[27673]-TeamArchers-Secure2.0-reversal-and-New-Dashboard-Changes-for-Setup-Plan-API-380126606.aspx) | Created: 2026-04-22 | Last modified: 2026-06-12 | Author: Pankaj Dubey | Last editor: Palak Bhatt

---

#### **Implementation Tasks**

| <br>#### ****TrackIT info:****<br> |  |
| --- | --- |
| TrackIT # | [27673] |
| TrakIT Name | TeamArchers-Secure2.0 reversal and New Dashboard Changes for Setup Plan API |
| Implementation Date: | 4-23-2026 11.00AM |
| Implementation Items: | <br>- Onboarding.Setup.Plan=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1377](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1377)<br>- [Onboarding.Setup.Plan.Consumer =>](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148) [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/deployments/releases/1.0.1319](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/deployments/releases/1.0.1319)<br> |
| Summary of Changes | <br>Deployment includes<br>- Revert the changes for Plan Testing Controls in ARK<br>- Revert the changes for Secure 2.0 for Regulatory Distributions for all group plans<br>- Update the logic for "ControlGroup" and "RelatedER" in PAS<br>- Plan Status Tracking Dashboard for Plan Setup APIs.<br>Octopus variable for PRO<br>- Onboarding.Setup.Plan<br>  - OnboardingAPISettings:BaseServicesURL = [http://internal-api.ascensus.com](http://internal-api.ascensus.com)<br>  - PlanPortalSettings:PlanDetailBaseUrl = [https://ark.ascensus.com/Plan/](https://ark.ascensus.com/Plan/)<br>- [Onboarding.Setup.Plan.Consumer](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148)<br>  - OnboardingAPISettings:BaseServicesURL = [http://internal-api.ascensus.com](http://internal-api.ascensus.com)<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer | <br> | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Suraj Kumar | Required |
| <br> | <br> | <br> |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team White |  |  | <br> |  |  |
| Team Archers | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) | April22nd | [27673] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April22nd | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 95 are completed<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April22nd | <br> |
| <br> | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April22nd | <br>Setup Plan Api DB TrakIT - [27668]<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April22nd | <br> |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April22nd | <br> |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | April22nd | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| [ ] | 4/9 | <br>Octopus variable for PRO in DCA.Partner.Dashboard.UI<br>- FeatureFlags:EnableISTDashboard = false<br> | DevOps | <br> | <br> |
| --- | --- | --- | --- | --- | --- |
| <br>☒<br> | April6th | <br>Onboarding.Data<br> | DevOps | See above | (include Link to Octopus) |
| <br> | follow | <br>Onboarding.Api<br> | DevOps | See above | (include Link to Octopus) |
| <br> | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | <br>Onboarding.Workflow.Api<br> | DevOps | N/A | (include Link to Octopus) |
| <br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br>☒<br> | follow | Onboarding.Messaging.Api | DevOps | N/A | (include Link to Octopus) |
| <br>☐<br> | follow | Onboarding.Portal | DevOps | N/A | (include Link to Octopus) |
| <br> | follow | Partner Dashboard MFE | <br>DevOps<br> | <br>See above<br> | (include Link to Octopus) |
| <br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  | <br>Test Ascensus Partner is added on the DCA partner dashboard<br>Test that search by business name, search by first name and last name is working on the Partner dashboard<br>Test AllowDuplicateEIN button on the internal user dashboard<br>Test IST dashboard is hidden<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Setup.Plan=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1364](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1364)<br>- [Onboarding.Setup.Plan.Consumer =>](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1148) [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/deployments/releases/1.0.1306](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/deployments/releases/1.0.1306)<br> | <br> | <br> |
| <br>☐<br> | Rollback DBA | <br> | <br> | <br> |

**Lessons Learned from Implementation and Action Items:**
