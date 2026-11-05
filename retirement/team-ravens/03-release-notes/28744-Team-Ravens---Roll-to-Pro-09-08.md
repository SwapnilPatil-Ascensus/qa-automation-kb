# [28744] [Team Ravens] - Roll to Pro 09/08

> Source: [Team Ravens SharePoint](https://ascensus0.sharepoint.com/sites/TeamRavens/SitePages/[28744]-[Team-Ravens]---Roll-to-Pro-09-08.aspx) | Created: 2026-09-04 | Last modified: 2026-09-08 | Author: Palak Bhatt | Last editor: Palak Bhatt

---

![image](https://ascensus0.sharepoint.com/_layouts/15/images/sleektemplateimagetile.jpg)

| <br>#### **TrackIT info:**<br> |  |
| --- | --- |
| TrackIT # | [28744] |
| TrakIT Name | Team Ravnens - Roll to PRO 09/08 |
| Implementation Date Start time | 09-08-2026 10:00AM EST |
| Implementation Date End time | <br>09-08-2025 10:35AM EST<br> |
| <br>Implementation Items:<br>List of Modules of Unqork<br> | <br>**Modules to promote:**<br>\| **Story** \| **Group** \| **App Name** \| **Module Name** \| **Module ID** \|<br>\| --- \| --- \| --- \| --- \| --- \|<br>\| 852093 \| G2 \| Advisor Plan Onboarding \| Advisor Information : Dealer Information \| 6909c4169330e6ba05ad2471 \|<br>\| G2 \| Advisor Plan Onboarding \| Advisor information : RIA Payment Contact Information \| 690da732d61dbd559f8c17c9 \|  \|<br>\| G2 \| IK : CoPilot : Fee Based / Comm Based : Advisor \| IK : CoPilot : Fee Based / Comm Based : Advisor (Workflow) \| 6908830f84a31a390b1542f6 \|  \|<br>\|  \|  \|  \|  \|  \|<br>\| <br>852116<br> \| G2 \| Sponsor Plan Onboarding \| Effective date: RK Effective Date \| 686b4c1e7f0a6af4544f31b3 \|<br>\|  \|  \|  \|  \|  \|<br>\| <br>850334<br> \| G1 \| eApp \| eApp: About Business (Advisor) (Ameriprise) (JPMorgan) (Pershing) \| 67d1c564670d26eb9d680ed8 \|<br> |
| <br>Summary of Changes<br> | <br> |
| User stories to be deployed | <br>1. 1. [Bug 852093](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/852093): Dealer Information Page Validations<br>2. 2. [Task 852116](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/852116): Recordkeeping Effective Date Display<br>3. 3. [Product Backlog Item 850334](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/850334): [Group 1] - Remove Dealer CRD field from advisor information screen for Ameriprise and JP Morgan products only<br> |

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
| <br>☒<br> | <br>A new TrakIT is created for the deployment<br> | Palak Bhatt | <br> | [28744] |
| <br>☒<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | Team Ravens | 09-04-2025 |  |
| <br>☐<br> | <br>All current Onboarding database stories for Group1,2 and 2.2<br> | Aashay Bhargava | <br> | Not required for this implementation |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | Palak Bhatt | <br> |  |
| <br>☐<br> | <br>Team approves our TrakIT by 4:00 ET cutoff time<br> | Ian / Team Ravens | <br> |  |
| <br>☐<br> | <br>Update TrakIT status to Awaiting Implementation to Production<br> | Palak Bhatt |  |  |
| <br>☐<br> | <br>Identify & order items to be implemented<br> | <br> |  |  |
|  |  |  |  |  |

#### **Implementation Tasks**

| <br> | **Date/Time** | **Task** | **Owner** | **Dependency** | **Task Details** |
| --- | --- | --- | --- | --- | --- |
| ☐ | 09/08 [10:32 AM] | Implement G2 changes | @aashay.bhargava | None | <br>Run Data Updating Utility for 4 records of Page Schema.<br> |
| ☐ | 09/08 [10:32 AM] | Implement G1 changes | @aashay.bhargava | None | <br>Promote the release to Pro:<br>[https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=6a42846151b79fbfa8df59eb](https://retsupport-qax.unqork.io/app/udlc-release#/display/release-view?releaseId=6a42846151b79fbfa8df59eb)<br> |
| ☐ | 09/08 [10:32 AM] | Verify the changes | <br>@himanshu.mishra<br> | Above Tasks | Verify G1 and G2 changes |
| ☐ | 09/08 [10:32 AM] | Test following items (see comments) | <br>[@ian.macphail](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)<br> | <br> | <br>Test following products for Auto Funding Screen removal:<br>- BAML i(k) (G2)<br>- ShareBuilder i(k) (G2)<br>- Ascensus Daily Fee Based (G1)<br>- Ascensus Daily Level Commission (G1)<br>- State Farm (G1)<br>- Victory (fka Amundi) (G1)<br> |
| <br>☐<br> | 09/08 [10:55 AM] | TrakIT update Status = "Completed" | [Palak Bhatt/Aashay Bhargava](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) |  |  |
| <br>☐<br> | 09/08 [10:59 AM] | <br>Notify NOC of monitoring and Application support work is completed<br>([psl_noc@ascensus.com](mailto:psl_noc@ascensus.com); [application.support@ascensus.com](mailto:application.support@ascensus.com))<br> | DevOps |  |  |
|  |  |  |  |  |  |

#### **Rollback strategy**

|  | <br>**Rollback scenario**<br> | <br>**Rollback strategy**<br> | <br>**Owner**<br> | <br>**Comment**<br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Rollback Code<br> | <br> |  |  |
| <br>☐<br> | Rollback DBA |  |  |  |

**Lessons Learned from Implementation and Action Items:**

Emanuel PedrazaAashay BhargavaDiego Emanuel TraviesoNish AryaHimanshu MishraErik YoudalPaul PecaJodi MorrisonIan MacphailAnitha MoturiEmanuel.Pedraza@ascensus.comAashay.Bhargava@ascensus.comDiegoEmanuel.Travieso@ascensus.comNish.Arya@ascensus.comHimanshu.Mishra@ascensus.comErik.Youdal@ascensus.comPaul.Peca@ascensus.comJodi.Morrison@ascensus.comIan.Macphail@ascensus.comAnitha.Moturi@ascensus.com
