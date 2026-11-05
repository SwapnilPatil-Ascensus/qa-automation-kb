# 2026-06-30 - [28106] Auto funding remove from workflow

> Source: [Team Ravens SharePoint](https://ascensus0.sharepoint.com/sites/TeamRavens/SitePages/2026-06-30---[28106]-Autofunding-remove-from-workflow.aspx) | Created: 2026-06-25 | Last modified: 2026-08-28 | Author: Palak Bhatt | Last editor: Emanuel Pedraza

---

![image](https://ascensus0.sharepoint.com/_layouts/15/images/sleektemplateimagetile.jpg)

#### @a**Implementation Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28106] |
| TrakIT Name | Team Ravens- Autofunding remove from workflow |
| Implementation Date: | 06-30-2026 9:30AM EST |
| <br>Implementation Items:<br>List of Modules of Unqork<br> | <br>Group 1: Run Data Utility and update 4 record in Page Schema<br>Group 2:<br>Module :Review your information  <br>[https://retsupport-dev.unqork.io/app/designer#/display/module-builder?moduleId=68f9cec6e02b2835e6b7120a&fromUD=0](https://retsupport-dev.unqork.io/app/designer#/display/module-builder?moduleId=68f9cec6e02b2835e6b7120a&fromUD=0)  <br>  <br>Workflow: Group I(k)  <br>[https://retsupport-dev.unqork.io/workflow/68858120ac1ef3cba62c24db](https://retsupport-dev.unqork.io/workflow/68858120ac1ef3cba62c24db)<br> |
| Summary of Changes | <br>Auto Funding screen linked above needs to be removed from the following workflows  <br>The Auto Funding screen is no longer displayed for the listed Group 1 products.<br>- Ascensus Daily Fee Based (Group 1)<br>- Ascensus Daily Level Commission (Group 1)<br>- State Farm (Group 1)<br>- Victory (fka Amundi) (Group 1)<br>The Auto Funding screen is no longer displayed for the listed Group 2 i(k) products.<br>- BAML i(k) (Group 2)<br>- ShareBuilder i(k) (Group 2)<br> |
| User stories to be deployed | [Product Backlog Item 812399](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/812399): Auto Funding - Remove from workflow |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer |  | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Suraj Kumar | Not Required |
|  |  |  |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team Ravens | Paul Peca |  | Palak Bhatt | Emanuel Pedraza | Aashay Bhargava, Himanshu Mishra |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | Palak Bhatt | <br> | [28106] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | Team Ravens | 30-June-2026 |  |
| <br>☐<br> | <br>All current Onboarding database stories for Group1,2 and 2.2<br> | Aashay Bhargava | 30-June-2026 | Not required for this implementation |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | Emanuel Pedraza | 30-June-2026 |  |
| <br>☐<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | Ian / Team Ravens | 30-June-2026 |  |
| <br>☐<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | Palak Bhatt | 30-June-2026 |  |
| <br>☐<br> | <br>Identify & order items to be implemented<br> | <br> |  |  |
|  |  |  |  |  |

#### **Implementation Tasks**

| <br> | **Date/Time** | **Task** | **Owner** | **Dependency** | **Task Details** |
| --- | --- | --- | --- | --- | --- |
| ☐ | 6/30 [9:32 AM] | Implement G2 changes | @aashay.bhargava | None | <br>Run Data Updating Utility for 4 records of Page Schema.<br> |
| ☐ | 6/30 [9:35 AM] | Implement G1 changes | @aashay.bhargava | None | <br>Promote the release to Pro:<br>[https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=6a42846151b79fbfa8df59eb](https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=6a42846151b79fbfa8df59eb)<br> |
| ☐ | 6/30 [9:37 AM] | Verify the changes | <br>@himanshu.mishra<br> | Above Tasks | Verify G1 and G2 changes |
| ☐ | 6/30 [9:40 AM] | Test following items (see comments) | <br>[@ian.macphail](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br> | <br>Test following products for Auto Funding Screen removal:<br>- BAML i(k) (G2)<br>- ShareBuilder i(k) (G2)<br>- Ascensus Daily Fee Based (G1)<br>- Ascensus Daily Level Commission (G1)<br>- State Farm (G1)<br>- Victory (fka Amundi) (G1)<br> |
| <br>☐<br> | 6/30 [9:50 AM] | TrakIT update Status = "Completed" | [Palak Bhatt/Aashay Bhargava](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  |  |
| <br>☐<br> | 6/30 [9:52AM] | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  |  |
|  |  |  |  |  |  |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br> |  |  |
| <br>☐<br> | Rollback DBA |  |  |  |

**Lessons Learned from Implementation and Action Items:**
