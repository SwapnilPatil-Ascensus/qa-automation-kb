# [10-29-2026] - Trigger Sharebuilder welcome email- Trakit [29232]

> Source: [Team Ravens SharePoint](https://ascensus0.sharepoint.com/sites/TeamRavens/SitePages/[10-29-2026]---Trigger-Sharebuilder-welcome-email--Trakit-[29232].aspx) | Created: 2026-10-27 | Last modified: 2026-10-29 | Author: Palak Bhatt | Last editor: Palak Bhatt

---

![image](https://ascensus0.sharepoint.com/_layouts/15/images/sleektemplateimagetile.jpg)

#### **Implementation Tasks**

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [29232] |
| TrakIT Name | Team Ravens- Trigger Sharebuilder welcome email |
| Implementation Start Date: | 10-29-2026 10:00AM EST |
| Implementation End Date: | 10-29-2026 11:00PM EST |
| <br>Implementation Items:<br>List of Modules of Unqork<br> | <br>details in the user story [Product Backlog Item 879779](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/879779): Roll to Production 10/29 - [29232]<br> |
| <br>Summary of Changes<br> | <br> |
| User stories to be deployed | <br>[Product Backlog Item 861431](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/861431): Trigger ShareBuilder welcome email on landing page<br>[Product Backlog Item 856679](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/856679): Persist and expose ShareBuilder sponsor welcome-email sent flag<br>[Product Backlog Item 848741](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/848741): [Group Transfer Plans] - Update the Plan Sponsor reminder-email trigger so emails are not sent while Ascensus prefill or prior RK communications are pending<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer |  | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Suraj Kumar | Not Required |
|  |  |  |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team Ravens | Paul Peca |  | Palak Bhatt | Emanuel Pedraza | Team Ravens Developers |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | Palak Bhatt | <br> | [29232] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | Team Ravens | 26-October-2026 |  |
| <br>☐<br> | <br>All current Onboarding database stories for Group1,2 and 2.2<br> | Himanshu Mishra | 28-October-2026 | Not required for this implementation |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | Paul Peca | 28-October-2026 |  |
| <br>☐<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | Ian / Team Ravens | 28-October-2026 |  |
| <br>☐<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | Palak Bhatt | 28-October-2026 |  |
| <br>☐<br> | <br>Identify & order items to be implemented<br> | <br> |  |  |
|  |  |  |  |  |

#### **Implementation Tasks**

| <br> | **Date/Time** | **Task** | **Owner** | **Dependency** | **Task Details** |
| --- | --- | --- | --- | --- | --- |
| ☐ | 10/29 [10:02 AM] | Implement G2 changes | @aashay.bhargava | None | <br>Run Data Updating Utility for 4 records of Page Schema.<br> |
| ☐ | 10/29 [10:05 AM] | Implement G1 changes | @aashay.bhargava | None | <br>Promote the release to Pro:<br>[https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=6a42846151b79fbfa8df59eb](https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=6a42846151b79fbfa8df59eb)<br> |
| ☐ | 10/29 [10:07 AM] | Verify the changes | <br>@himanshu.mishra<br> | Above Tasks | Verify G1 and G2 changes |
| ☐ | 10/29 [11:00PM] | Test following items (see comments) | <br>[@ian.macphail](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br> | <br>Testing CSS and user story changes<br> |
| <br>☐<br> | 10/29 [11:00 AM] | TrakIT update Status = "Completed" | [Palak Bhatt/Aashay Bhargava](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  |  |
| <br>☐<br> | 10/29 [11:00AM] | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  |  |
|  | <br> |  |  |  |  |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br> |  |  |
| <br>☐<br> | Rollback DBA |  |  |  |

**Lessons Learned from Implementation and Action Items:**

Paul PecaAnitha MoturiIan MacphailEmanuel PedrazaJodi MorrisonHimanshu MishraAashay BhargavaErik YoudalPalak BhattDiego Emanuel TraviesoNish AryaPaul.Peca@ascensus.comAnitha.Moturi@ascensus.comIan.Macphail@ascensus.comEmanuel.Pedraza@ascensus.comJodi.Morrison@ascensus.comHimanshu.Mishra@ascensus.comAashay.Bhargava@ascensus.comErik.Youdal@ascensus.comPalak.Bhatt@ascensus.comDiegoEmanuel.Travieso@ascensus.comNish.Arya@ascensus.com
