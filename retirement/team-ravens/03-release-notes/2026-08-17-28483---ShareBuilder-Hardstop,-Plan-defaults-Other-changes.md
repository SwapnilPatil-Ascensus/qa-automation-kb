# 2026-08-17 [28483]- ShareBuilder Hardstop, Plan defaults & Other changes

> Source: [Team Ravens SharePoint](https://ascensus0.sharepoint.com/sites/TeamRavens/SitePages/2026-08-07-[28483]--Sharebuilder-Hardstop,-Plan-defaults-&-Dashboard-changes.aspx) | Created: 2026-08-06 | Last modified: 2026-08-28 | Author: Palak Bhatt | Last editor: Emanuel Pedraza

---

![image](https://ascensus0.sharepoint.com/_layouts/15/images/sleektemplateimagetile.jpg)

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28483] |
| TrakIT Name | Team Ravens- [**Sharebuilder Hardstop, Plan defaults & Dashboard changes**](https://ascensus0.sharepoint.com/sites/TeamRavens/SitePages/2026-08-07-[28483]--Sharebuilder-Hardstop,-Plan-defaults-%26-Dashboard-changes.aspx?Mode=Edit) |
| Implementation Date Start time | 08-17-2026 10:30AM EST |
| Implementation Date End time |  |
| <br>Implementation Items:<br>List of Modules of Unqork<br> | <br>Group 1:<br>Group 2:<br>Group 2.2  <br>Workflow:<br> |
| <br>Summary of Changes<br> | <br>- Changes in the email address for Sharebuilder hardstop<br>- Plan defaults election page changes<br>- Dashboard changes for group 2.2<br> |
| User stories to be deployed | <br>1. [Product Backlog Item 837439](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/837439): [ShareBuilder] – Change hard stop email recipient<br>2. [Bug 840868](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/840868): [Group Plans / Employee Upload] - Fix hire date validation to allow hire date equal to business establishment date<br>3. [Product Backlog Item 831117](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/831117): [Plan Defaults Page] - Add annual age-band update language to glidepath interface for Hybrid, Passive, 25 bps, and 50 bps fund lineups<br>4. [Product Backlog Item 834492](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/834492): [i(k) Startup] - Use recordkeepingEffectiveDate for eligibility waiver (DocuSign Group 1)<br>5. [Product Backlog Item 811078](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/811078): [Unqork / QDIA Notices] - Dynamic generation of model tables for Ascensus Essentials documents<br>6. [Product Backlog Item 839636](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/839636): Advisor Fee - Dynamic messaging for Asset-Based Fee<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer |  | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | Suraj Kumar | Not Required |
|  |  |  |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team Ravens | Paul Peca |  | Palak Bhatt | Emanuel Pedraza | Team Ravens developers |
|  |  |  |  |  |  |

**Pre-Implementation Tasks**

| <br> | <br>**Task**<br> | <br>**Owner**<br> | **Due Date** | <br>**Comments**<br> |
| --- | --- | --- | --- | --- |
| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | Palak Bhatt | <br> | [28483] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | Team Ravens | 17-August-2026 |  |
| <br>☐<br> | <br>All current Onboarding database stories for Group1,2 and 2.2<br> | Aashay Bhargava | 17-August-2026 | Not required for this implementation |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | Palak Bhatt | 13-August-2026 |  |
| <br>☐<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | Ian / Team Ravens | 17-August-2026 |  |
| <br>☐<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | Palak Bhatt | 17-August-2026 |  |
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
