# 2026-11-17 [29062] TeamWhite - Sales Bridge and Vanguard SSO Roll to PRO

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-11-17-[29062]-TeamWhite---Sales-Bridge-and-Vanguard-SSO-Roll-to-PRO.aspx) | Created: 2026-10-07 | Last modified: 2026-10-13 | Author: Anitha Moturi | Last editor: Chris Reynolds

---

#### **Implementation Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [29062] |
| TrakIT Name | [29062] TeamWhite - Sales Bridge and Vanguard SSO Roll to PRO |
| Implementation Date: | Nov 17th 2026, **TBD** |
| Implementation Items: | <br>- Onboarding.Experience.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-api/deployments/releases/3.0.34](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-api/deployments/releases/3.0.34)<br>- Onboarding.Experience.UI => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-ui/deployments/releases/3.0.248](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-ui/deployments/releases/3.0.248)<br>- DCA Partner Dashboard UI => **Redeploy current PRO version after updating Octopus vars**<br>- Onboarding.Data => N/A<br>- Onboarding.Api => N/A<br>- Onboarding.Messaging.Api => N/A<br>- Onboarding.Dashboard => N/A<br>- Onboarding.Portal => N/A<br>- Onboarding.Workflow.Api => N/A<br>- Onboarding.Setup.Plan=> N/A<br>- Onboarding.Setup.Plan.Consumer => N/A<br>- Platform - ORY Hydra Clients => [https://octopus.ascensus.com/app#/Spaces-1/projects/platform-ory-hydra-clients/deployments/releases/0.0.1-r1.202610131519](https://octopus.ascensus.com/app#/Spaces-1/projects/platform-ory-hydra-clients/deployments/releases/0.0.1-r1.202610131519)<br> |
| Summary of Changes | <br>- Apply internal users access to view “Onboarding” menu item in DCA, which will direct users access to our Partner Dashboard MFE with separate tabs for IST and Sales Bridge dashboard<br>- Apply access to Vanguard specific DCA user IDs to view “Submit New Plan" button in My Plans Dashboard, which will SSO the user into our Vanguard Sales Portal - Proposal Look-up page<br>- Enable SalesBridge Portal URL to write to CRM<br>- Enable tab to Sales Bridge Dashboard to appear in Partner Dashboard MFE<br>- ORY Hydra client clean-up (removing separate client creds for *onboarding-experience-api* , in favor of allowing the scope in *onboarding-experience-ui*  instead)<br> |
| Octopus Variables for PRO | <br>- [Onboarding.Experience.UI](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-ui/variables)<br>  - SalesBridge:SaveSalesPortalLinkToCrm<br>  - Set PRO value to “true”<br>- [DCA.Partner.Dashboard.UI](https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/variables)<br>  - FeatureFlags:EnableSalesBridgeDashboard<br>  - Set PRO value to “true”<br> |
| Database Scripts to be executed | <br>- “EDB - insert dca sso permissions.sql”      This script will grant internal users access to ViewOnboardingDashboard in EDB.Administrator table, which will enable the "Onboarding" menu item to appear after signing into DCA.  Clicking the "Onboarding" menu item will direct the user to our Partner Dashboard MFE, which contains a tab for the sales bridge dashboard along with our separate tabs for group 2 Onboarding dashboard and IST<br>- “msvc_onboarding_experience vanguard_sso_permissions.sql”      This script will grant specified Vanguard DCA User IDs the permission to see the "Submit New Plan" button in the My Plans Dashboard of DCA.  Clicking the "Submit New Plan" button will SSO the user to our Vanguard Sales Portal - Proposal Look-up page.<br> |

#### **External Resources:**

| App Engineer | [@Siddhartha Singh](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Siddhartha.Singh%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a384b82128018583343abf0042) | Required |
| --- | --- | --- |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) |  | Yes |
|  |  |  |

#### **Teams Involved:**

| Team White |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | <br>Enes Ulukaya<br> | <br>Oct 8th<br> | [29062] |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 8th | <br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 13th | <br> |
| <br>☒<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 13th |  |
| <br>☒<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Oct 13th | <br> |
| <br>☒<br> | <br>Identify & order items to be implemented<br> |  |  |  |
|  | OCTOPUS | <br> | <br> | <br> |

**Implementation Tasks**

| ☐ | Oct 15th | DBA execution of database scripts granting user permissions | DBA |  | <br> |
| --- | --- | --- | --- | --- | --- |
| <br>☐<br> | Oct 15th | <br>Octopus variables are updated:<br>- [Onboarding.Experience.UI](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-ui/variables)<br>- [DCA.Partner.Dashboard.UI](https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/variables)<br> | DevOps | See above | <br>API as of Oct 14th 2026 (EOD)<br> |
| ☐ | follow | Onboarding.Experience.Api | DevOps | See above | API as of Oct 14th 2026 (EOD) |
| <br>☐<br> | follow | <br>Onboarding.Experience.UI<br> | DevOps | See above | API as of Oct 14th 2026 (EOD) |
| ☐ | follow | DCA.Partner.Dashboard.UI | <br>DevOps<br> | <br>See above<br> | <br>Current PRO version redeployed with latest variables<br> |
| ☐ | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Russ Holm](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> | <br> | <br>**Onboarding Experience**<br>**DCA Sponsor Site → Vanguard Onboarding Sales SSO**<br>**DCA.Partner.Dashboard.UI → Sales Bridge**<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |
|  |  | <br> |  |  |  |

#### **Rollback strategy**

| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Experience.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-api/deployments/releases/3.0.22](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-api/deployments/releases/3.0.22)<br>- Onboarding.Experience.UI =>[https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-ui/deployments/releases/3.0.230](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-ui/deployments/releases/3.0.230)<br>- DCA Partner Dashboard UI => [https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.193](https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.193)<br>- Onboarding.Data => N/A<br>- Onboarding.Api => N/A<br>- Onboarding.Messaging.Api => N/A<br>- Onboarding.Dashboard => N/A<br>- Onboarding.Portal => N/A<br>- Onboarding.Workflow.Api => N/A<br>- Onboarding.Setup.Plan=> N/A<br>- Onboarding.Setup.Plan.Consumer => N/A<br> | **Note** : Determine whether Octopus vars need to be reverted if a rollback becomes necessary | <br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | Rollback DBA | N/A |  |  |
