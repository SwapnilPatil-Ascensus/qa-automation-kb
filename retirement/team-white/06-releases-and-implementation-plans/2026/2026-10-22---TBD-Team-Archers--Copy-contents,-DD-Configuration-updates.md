# 2026-10-22 -[TBD] Team Archers -Copy contents, DD Configuration updates, SB Enrollment and Contract-seq update

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/2026-11-05 -[TBD] Team Archers -Copy contents, DD Configuration updates, SB Enrollment and Contract-seq update.aspx) | Created: 2026-11-02 | Last modified: 2026-11-03 | Author: Milind Sawde | Last editor: Milind Sawde

---

#### **Implementation Tasks**

| <br>#### **TrakIT info:**<br> |  |
| --- | --- |
| TrakIT # | TBD |
| TrakIT Name | Team Archers -Copy contents, DD Configuration updates, SB Enrollment and Contract-seq update |
| Implementation Date: | 11-05-2026 7.30 AM ET |
| Implementation Items: | <br>- Onboarding.Setup.Plan =>[Releases > Release 1.0.2087 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases/1.0.2087)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1934 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases/1.0.1934)<br> |
| Octopus variable for PRO | NA |
| Summary of Changes | <br>Deployment includes<br>- Copy content from Ascensus staging template to newly created plan folder for group plans.<br>- Updated the configuration of Drawdowns for BAML and SB group plans.<br>- Update the logic for Enrollment for ShareBuilder group plans.<br>- Validate Contract Seq on Drawdown 74 to General – Separate.<br> |

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
| Team Archers | <br> |  |  |  | Pankaj Dubey/ Milind Sawde |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | A new TrakIT is created for the deployment | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) | Nov 04 | <br> |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Nov 04 | <br> |
| <br>☐<br> | <br>All current Onboarding database stories for Group2 up to sprint 95 are completed<br> | <br> | <br> | NA |
|  | <br>Confirm with Milind that DB Scipt dependency TrkIt is implemented in PRO<br> | Anitha | Nov 05 | <br>NA - DB deployment not needed for this release<br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Nov 04 |  |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Nov 04 |  |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | [@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | Nov 04 | <br> |
| <br>☐<br> | Identify & order items to be implemented |  | <br> |  |
|  |  |  | <br> |  |

#### **Implementation Tasks**

| <br> |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| <br> |  |  |  |  |  |
| <br> |  |  |  |  |  |
| <br> | follow | <br>Onboarding.Setup.Plan.Consumer<br> | DevOps | N/A | (include Link to Octopus) |
| <br> |  |  |  |  |  |
| <br> | follow | <br>Onboarding.Setup.Plan<br> | DevOps | N/A | (include Link to Octopus) |
| <br> |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky<br> |  | <br>Test- Create below offering plan from DoE<br>- SB Group<br>Plan Setup from DOE<br> |
| <br>☐<br> | TIME | TrakIT update Status = "Not Started" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  | <br> |
| <br>☐<br> | TIME | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  | <br> |

#### Verification Details

| # | ARK Screen Details | Verification Details | Comments |
| --- | --- | --- | --- |
| 1 | ARK / Plan / Rules / Drawdowns | <br>Verify<br>DD72 Added   <br>Drawdown 5 for BAML group plans no longer exposes or processes Retirement  <br>Allow PayrollSync Report - Unchecked<br> | Test with BAML Group plan |
| 2 | ARK/Plan/Rules/Enrollment /Auto Enrollment/Auto Increase | <br>Verify - When "automaticEnrollment" is = 'Yes and "automaticEnrollmentType" = QACA/EACA, then<br>1. Under "SECURE 2.0 PROVISION 101" section, update "Exempt from SECURE 2.0 Provision 101" field as "Current date".<br> | Test with "ShareBuilder Group Plan" |
| 3 | ARK / Plan / Rules / Drawdowns | Verify -  Drawdown 74 step 1 shows Contract Seq = General – Separate | Test with "ShareBuilder Group Plan" |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br>- Onboarding.Setup.Plan => [Releases > Release 1.0.2043 - Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan/releases/1.0.2043)<br>- Onboarding.Setup.Plan.Consumer => [Releases > Release 1.0.1895 - Octopus Deploy](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-setup-plan-consumer/releases/1.0.1772)<br> |  |  |
| <br>☐<br> | Rollback DBA | <br> |  |  |
