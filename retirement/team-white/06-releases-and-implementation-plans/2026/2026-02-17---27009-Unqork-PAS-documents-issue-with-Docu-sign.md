# 2026-02-17 -[27009] [Unqork] PAS documents issue with Docu-sign

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2026-02-17--[27009]-[Unqork]-PAS-documents-issue-with-Docu-sign-362103155.aspx) | Created: 2026-01-14 | Last modified: 2026-02-26 | Author: Pete Bretz | Last editor: Anitha Moturi

---

#### **Implementation Tasks**

| <br>#### ****TrackIT info:****<br> |  |
| --- | --- |
| TrackIT # | [27009] |
| TrakIT Name | DOE Unqork PAS Document Fixes |
| Implementation Date: | 2/17/2026 at 9:30am ET |
| Implementation Items: | <br>ticket#752117 PROD issue #11 - PAS documents missing in DocuSign<br> |
| Summary of Changes | <br>All the PAS docs generated should be present when the user clicked the refresh button<br>All the PAS docs generated should be present when the user clicked the back button<br>Progress Bar on UI should be 100% for both single signer and multi-signer once all the required signers signed the docs<br>totalProgressRSValue should be 100% in the blob for both single signer and multi-signer once all the required signers signed the docs<br> |

#### **External Resources:**

| <br>**Resource**<br> | <br>**Name**<br> | <br>**Required/Standby?**<br> |
| --- | --- | --- |
| App Engineer | <br> | Required |
| DBA (found [HERE](https://ascensus0.sharepoint.com/sites/TeamDBA/SitePages/DA-DBA-Weekly-Assignments-60162479.aspx)) | <br> | Required |

#### **Teams Involved:**

| <br>**Team**<br> | <br>**Product Owner**<br> | <br>**Project Manager**<br> | <br>**BA/PO**<br> | <br>**Scrum Master**<br> | <br>**Developers**<br> |
| --- | --- | --- | --- | --- | --- |
| Team White | <br>Paul Peca<br> |  | Enes Ulakaya | <br>Pete Bretz<br> | <br>Team White Developers<br> |
| Team Archers | Paul Peca | <br> | <br> | <br> | Team Archers |
| Qonnectors | <br> | <br> | <br> | <br> | <br> |

#### **Notification to be sent to :**

| Ian Macphail, Jodi Morrison, Rebecca Wichner, Sherry McNeal, Team White Developers |
| --- |

**Pre-Implementation Tasks**

| <br> | **Task** | <br>**Who**<br> | **Date** | **Notes** |
| --- | --- | --- | --- | --- |
| <br>☐<br> | Implementation Planning Meeting |  | <br> | <br> |
| <br>☐<br> | A new TrakIT is created for the deployment | <br> | <br> | [27009] |
| <br>☐<br> | <br>Determine the implementation date<br>- Ensure that the date is mostly open for the majority of the team<br> | <br> | <br> | <br> |
| <br>☐<br> | <br>Implementation meeting invitation is sent to all teams in this deployment, interested Parties, Implementations and Sybase/SQL Server DBAs<br> | <br> | <br> | <br> |
| <br>☐<br> | Team approves our TrakIT by 4:00 ET cutoff time | <br> | <br>  <br> | <br> |
| <br>☐<br> | Update TrakIT status to Awaiting Implementation to Production | <br> | <br>  <br> | <br> |
| <br>☐<br> | Identify & order items to be implemented | <br> | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> |

#### **Implementation Tasks**

| <br>☐<br> | <Module Name> | <Module Id> | <br> | <br> | <br> |
| --- | --- | --- | --- | --- | --- |
| <br>☐<br> | <Module Name> | <Module Id> | <br> | <br> | <br> |
| <br>☐<br> | TIME | Test following items (see comments) | <br>[@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) / @Nic Kopetsky     /[@Oleksandr Klysheiko](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Oleksandr.Klysheiko%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3685ca58f016a12ac110f0036)<br> |  |  |
| <br>☐<br> | <br>TIME<br> | TrakIT update Status = "Completed" | [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000) | <br> | <br> |
| <br> | <br> | <br> | <br> | <br> | <br> |
| <br>☐<br> | <br> | <br> | <br> | <br> | <br> |

#### **Rollback strategy**

| <br> | <br>**Task**<br> | <br>**Notes**<br> | <br> | <br> |
| --- | --- | --- | --- | --- |
| <br>☐<br> | <br>Roll-forward<br> |  | <br> | <br> |
| <br>☐<br> | <br>all apps need version to roll back<br> |  | <br> | <br> |
| <br>☐<br> | Rollback DBA | <br> | <br> | <br> |
