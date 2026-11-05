# 2026-07-13 - [28248] - Team Ravens Rebranding from CoPilot to Ascensus Essentials

> Source: [Team Ravens SharePoint](https://ascensus0.sharepoint.com/sites/TeamRavens/SitePages/2026-07-13---[28248]---Team-Ravens-Rebranding-from-CoPilot-to-Ascensus-Essentials.aspx) | Created: 2026-07-10 | Last modified: 2026-08-28 | Author: Palak Bhatt | Last editor: Emanuel Pedraza

---

![image](https://ascensus0.sharepoint.com/_layouts/15/images/sleektemplateimagetile.jpg)

#### Implementation**Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28248] |
| TrakIT Name | Team Ravens - Rebranding from CoPilot to Ascensus Essentials |
| Implementation Date: | 07-13-2026 9:30AM EST |
| <br>Implementation Items:<br>List of Modules of Unqork<br> | <br>Group 2.2:<br>Module :Review your information  <br>[https://retsupport-dev.unqork.io/app/designer#/display/module-builder?moduleId=68f9cec6e02b2835e6b7120a&fromUD=0](https://retsupport-dev.unqork.io/app/designer#/display/module-builder?moduleId=68f9cec6e02b2835e6b7120a&fromUD=0)  <br>  <br>Workflow: Group I(k)  <br>[https://retsupport-dev.unqork.io/workflow/68858120ac1ef3cba62c24db](https://retsupport-dev.unqork.io/workflow/68858120ac1ef3cba62c24db)<br> |
| <br>Summary of Changes<br> | <br>This change updates IK and Group product screens by replacing all references to **Co-Pilot**  with **Ascensus Essentials** . On screens that display clickable documents, the existing documents will be replaced with updated versions that reflect **Ascensus Essentials**  as the product name.<br> |
| User stories to be deployed | [Product Backlog Item 819624](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/819624): Rebranding from CoPilot to Ascensus Essentials |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer |  | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Suraj Kumar | Not Required |
|  |  |  |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team Ravens | Paul Peca |  | Palak Bhatt | Emanuel Pedraza | Aashay Bhargava, Himanshu Mishra, Erik Youdal |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | Palak Bhatt | <br> | [28248] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | Team Ravens | 10-July-2026 |  |
| <br>☐<br> | <br>All current Onboarding database/unqork stories for Group 2.2<br> | Aashay Bhargava | 10-July-2026 | Not required for this implementation |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | Emanuel Pedraza | 10-July-2026 |  |
| <br>☐<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | Ian / Team Ravens | 10-July-2026 |  |
| <br>☐<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | Palak Bhatt | 13-July-2026 |  |
| <br>☐<br> | <br>Identify & order items to be implemented<br> | <br> |  |  |
|  |  |  |  |  |

#### **Implementation Tasks**

| <br> | **Date/Time** | **Task** | **Owner** | **Dependency** | **Task Details** |
| --- | --- | --- | --- | --- | --- |
| ☐ | <br>6/30 [9:32 AM]<br> | <br>Implement G2 changes<br> | <br>@aashay.bhargava<br> | <br>None<br> | <br>Run Data Updating Utility for 4 records of Page Schema.<br> |
| ☐ | <br>6/30 [9:35 AM]<br> | <br>Implement G1 changes<br> | <br>@aashay.bhargava<br> | <br>None<br> | <br>Promote the release to Pro:<br>[https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=6a42846151b79fbfa8df59eb](https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=6a42846151b79fbfa8df59eb)<br> |
| ☐ | <br>6/30 [9:37 AM]<br> | <br>Verify the changes<br> | <br>@himanshu.mishra<br> | <br>Above Tasks<br> | <br>Verify G1 and G2 changes<br> |
| ☐ | <br>6/30 [9:40 AM]<br> | <br>Test following items (see comments)<br> | <br>[@ian.macphail](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br> | <br>Test following products for Auto Funding Screen removal:<br>- BAML i(k) (G2)<br>- ShareBuilder i(k) (G2)<br>- Ascensus Daily Fee Based (G1)<br>- Ascensus Daily Level Commission (G1)<br>- State Farm (G1)<br>- Victory (fka Amundi) (G1)<br> |
| <br>☐<br> | 6/30 [9:50 AM] | TrakIT update Status = "Completed" | [Palak Bhatt/Aashay Bhargava](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  |  |
| <br>☐<br> | 6/30 [9:52AM] | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  |  |
|  |  |  |  |  |  |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br> |  |  |
| <br>☐<br> | Rollback DBA |  |  |  |

**Lessons Learned from Implementation and Action Items:**
