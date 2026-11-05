# 2026-07-16 -[28288] Team Archers - for Loan Fees, Financial Wellness, Drawdown and dealer changes

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-07-16--[28288]-Team-Archers----for-Loan-Fees,-Financial-Wellness,-Drawdown-and-dealer-informati.aspx) | Created: 2026-07-15 | Last modified: 2026-07-16 | Author: Pankaj Dubey | Last editor: Milind Sawde

---

#### **Implementation Tasks**

| <br>#### **TrakIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28288] |
| TrakIT Name | Team Archers - PRO deployment - for Loan Fees, Financial Wellness, Drawdown and dealer information changes, Billing Option Fix |
| Implementation Date: | 07-16-2026 3.30 PM ET |
| Implementation Items: | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1570 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1570)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1498 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/deployments/releases/1.0.1498)<br> |
| Octopus variable for PRO | <br>Name: PlanPortalSettings:PasComplianceCheckDashboardBaseUrl<br>Values:<br>- **Dev** : https://pasdev.ascensus.com/conversion/dashboard/<br>- **QA** : https://pasqa.ascensus.com/conversion/dashboard/<br>- **PRO** : https://pas.ascensus.com/conversion/dashboard/<br> |
| Summary of Changes | <br>Deployment includes<br>- Update the logic for Loan Fees screen in ARK.<br>- Set "DrawContractOrder" to "General/Separate" for Drawdown Steps 5, 7, and 13 ARK<br>- Implement the logic to add the details for "Financial Wellness" in ARK<br>- Refrain the dealer information for all the BF plans<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer |  | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Scott.Kirkpatrick@ascensus.com | Required |
|  |  |  |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team White | Paul Peca | <br> | Enes | <br> | <br> |
| Team Archers | <br> |  |  |  | Pankaj Dubey |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) | Jul 15th | [28288] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jul 15th | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 95 are completed<br> | <br> | <br> | NA |
|  | <br>Confirm with Pankaj that DB Scipt dependency TrkIt is implemented in PRO<br> | Anitha | Jul 15th | <br>Setup Plan Api DB TrakIT - [28203]<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jul 15th |  |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jul 15th |  |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Jul 15th | Done - Pankaj |
| <br>☐<br> | Identify & order items to be implemented |  |  |  |
|  |  |  |  |  |

#### **Implementation Tasks**

| <br> |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | (include Link to Octopus) |
| <br> |  |  |  |  |  |
| <br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br> |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky<br> |  | <br>Test- Create below offering plan from DoE<br>- CoPilot Group Fee Based - With Advisor<br>  - With fundLineupSelection - hybrid<br>  - With fundLineupSelection - Raymond James<br>- Create AscensusBalFwdIk/AscensusBalFwdIKNoAdv  (Balance forward plan)<br>Plan Setup from DOE<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |
|  | <br> | <br> |  |  | <br> |

#### Verification Details

| # | ARK Screen Details | Verification Details | Comments |
| --- | --- | --- | --- |
| 1 | ARK/Plan/Web Options/Payroll Website Options | "Vendor to Resolve File Errors via EditingOnline" check box should be checked. | Test with CoPilot Group Fee Based - With Advisor plan |
| 2 | ARK/Plan/Web Options/Plan Online Options | "Require Loan Paperwork" should be unchecked. | Test with CoPilot Group Fee Based - With Advisor plan |
| 3 | ARK/Plan/Rules/Drawdowns | “Automated Force Out Process” as Checked  <br>“Frequency” as 3 (Q2 Annual) | Test with CoPilot Group Fee Based - With Advisor plan |
| 4 | Ark/Plan/Rules/Loan/Loan Fees | <br>1. Loan Maintenance fee exists set to checked<br>2. Loan Maintenance fee amount should be = 95<br>3. Loan maintenance cadence should be = anniversary<br> | Test with CoPilot Group Fee Based - With Advisor plan |
| 5 | ARK/Plan/Rules/Drawdowns | <br>1. 5    59.5  PAYOUT  \| General/Separate<br>2. 7     INSERVICE      \| General/Separate<br>3. 13   NRAPAYOUT   \|  General/Separate<br> | Test with CoPilot Group Fee Based - With Advisor plan |
| 6 | ARK/Plan/Rules/Financial Wellness | <br>1. "Start Date" equal to "recordkeepingEffectiveDateStartup/recordkeepingEffectiveDateTransfer"<br>2. "URL" to: "https://www.ffhub.com/ascensus"<br>3. "Sender Name" to "Financial Wellness"<br>4. "Sender Email" to "financialwellness@ascensus.com"<br> | Test with CoPilot Group Fee Based - With Advisor plan |
| 7 | ARK/Plan/Rules/Plan Agents | <br>"Display contact information for" -Dealer<br>Dealer information should be blank.<br> | Test with AscensusBalFwdIk plan |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.1551 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/deployments/releases/1.0.1551)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1481 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/deployments/releases/1.0.1481)<br> |  |  |
| <br>☐<br> | Rollback DBA | <br> |  |  |

**Lessons Learned from Implementation and Action Items:**
