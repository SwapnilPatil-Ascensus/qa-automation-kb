# 2026-11-03 [29251] Team White- Onboarding API Platform Migration (New Cluster)

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-11-03-[29251]-Team-White--Onboarding-API-Platform-Migration-(New-Cluster).aspx) | Created: 2026-10-29 | Last modified: 2026-11-03 | Author: Anitha Moturi | Last editor: Sharon Chaggar

---

#### **Implementation Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [29251] |
| TrakIT Name | Team White- Onboarding API Platform Migration (New Cluster) |
| Implementation Date: | Nov3rd 2026  4.00PM |
| Implementation Items: | <br>- Onboarding.Experience.Api => N/A<br>- Onboarding.Experience.UI => N/A<br>- DCA Partner Dashboard UI => [https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.195](https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/deployments/releases/1.0.195)<br>- Onboarding.Data => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.346](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-data/deployments/releases/1.0.346)<br>- Onboarding.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.2033](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/deployments/releases/1.0.2033)<br>- Onboarding.Messaging.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1354](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-messaging-api/deployments/releases/1.0.1354)<br>- Onboarding.Dashboard => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-dashboard/deployments/releases/1.0.74](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-dashboard/deployments/releases/1.0.74)<br>- Onboarding.Portal => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.191](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-portal/deployments/releases/1.0.191)<br>- Onboarding.Workflow.Api => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.1270](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-workflow-api/deployments/releases/1.0.1270)<br>- Onboarding.Setup.Plan=> [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.2043](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.2043)<br>- Onboarding.Setup.Plan.Consumer => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/deployments/releases/1.0.1895](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/deployments/releases/1.0.1895)<br>- Onboarding.Setup.Plan.Engine => N/A<br>- Onboarding.Tools => [https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-tools/deployments/releases/1.0.118](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-tools/deployments/releases/1.0.118)<br> |
| Summary of Changes | <br>No changes to Apis.<br>Redeploy the versions already existing in PRO to the new cluster<br> |
| Octopus Variables for PRO | <br>Kubernetes:HttpRoute:Enabled = true<br>Kubernetes:Deployment:ReplicaCount = at least 2 or as many as in the old cluster<br> |
| Database Scripts to be executed | <br> |

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

| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | <br>Enes Ulukaya<br> | <br>Oct 23rd<br> | [29251] |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Oct 23rd<br> | <br> |
| <br>☒<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Oct 23rd<br> | <br> |
| <br>☒<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Oct 23rd<br> |  |
| <br>☒<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br>Oct 23rd<br> | <br> |
| <br>☒<br> | <br>Identify & order items to be implemented<br> |  |  |  |
|  | OCTOPUS | <br> | <br> | <br> |

**Implementation Tasks**

| ☐ | Oct 15th | DBA execution of database scripts granting user permissions | DBA |  | <br> |
| --- | --- | --- | --- | --- | --- |
| <br>☐<br> | Oct 15th | <br>Octopus variables are updated:<br>- [Onboarding.Experience.UI](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-experience-ui/variables)<br>- [DCA.Partner.Dashboard.UI](https://octopus.ascensus.com/app#/Spaces-1/projects/dca-partner-dashboard-ui/variables)<br> | DevOps | See above | <br>API as of Oct 23rd 2026 (EOD)<br> |
| ☐ | follow | Onboarding.Experience.Api | DevOps | See above | API as of Oct 23rd 2026 (EOD) |
| <br>☐<br> | follow | <br>Onboarding.Experience.UI<br> | DevOps | See above | API as of Oct 23rd 2026 (EOD) |
| ☐ | follow | DCA.Partner.Dashboard.UI | <br>DevOps<br> | <br>See above<br> | <br>Current PRO version redeployed with latest variables<br> |
| ☐ | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Russ Holm](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> | <br> | <br>Group1 , Group2 and Group2.2<br>Partner Dashboard<br>IST dashboard<br>**Onboarding Experience**<br>**DCA Sponsor Site → Vanguard Onboarding Sales SSO**<br>**DCA.Partner.Dashboard.UI → Sales Bridge**<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |
|  |  | <br> |  |  |  |

#### **Rollback strategy**

| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Experience.Api => N/A<br>- Onboarding.Experience.UI =>N/A<br>- DCA Partner Dashboard UI => N/A<br>- Onboarding.Data => N/A<br>- Onboarding.Api => N/A<br>- Onboarding.Messaging.Api => N/A<br>- Onboarding.Dashboard => N/A<br>- Onboarding.Portal => N/A<br>- Onboarding.Workflow.Api => N/A<br>- Onboarding.Setup.Plan=> N/A<br>- Onboarding.Setup.Plan.Consumer => N/A<br> | **Note** : Determine whether Octopus vars need to be reverted if a rollback becomes necessary | <br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | Rollback DBA | N/A |  |  |
