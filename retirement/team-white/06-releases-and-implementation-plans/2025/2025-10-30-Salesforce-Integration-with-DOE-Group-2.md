# 2025-10-30 Salesforce Integration with DOE Group-2

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2025-10-30-Salesforce-Integration-with-DOE-Group-2-346551668.aspx) | Created: 2025-10-31 | Last modified: 2026-04-01 | Author: Palak Bhatt | Last editor: Palak Bhatt

---

#### Date

2025-10-30

#### Attendees

- Christopher McCoy
- [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022)
- [@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)

#### Goals

- Salesforce requirements that were previously put on hold for Group-2.
- Link to the recording - [Salesforce Integration with DOE](https://teams.microsoft.com/l/meetingrecap?driveId=b%21DIk5QiiwuUW1ej129OqLlugN0km-IJpIo4EDVOKuINELM1PBAuAFTpBGBaYm1MYd&driveItemId=01CGFUQWABQ5IKVUDZEVEJPDAAOAGO27YZ&sitePath=https://ascensus0-my.sharepoint.com/:v:/g/personal/palak_bhatt_ascensus_com/EQGHUKrQeSVIl4wAcAztfxkBArfl93R7o3ESbzPa5L7xnw&fileUrl=https://ascensus0-my.sharepoint.com/personal/palak_bhatt_ascensus_com/Documents/Recordings/Salesforce%2520Integration%2520Group-2%2520Additional%2520requirements-20251030_213140-Meeting%2520Recording.mp4?web%3D1&iCalUid=040000008200E00074C5B7101A82E00800000000A12113E05847DC01000000000000000010000000203CE0609049B44AB13B832EBD3456FA&threadId=19:meeting_OWEyMjM5NWEtYTBkZC00ZTFlLTgyZDktNDI2YjVlZmU5YjFi%40thread.v2&organizerId=96fde839-b366-460d-9f83-6958d9c31fd2&tenantId=1d3bed01-6d09-498e-ab05-f1e2fdb1b138&callId=b2ca004d-23e8-4f51-ac35-e15aaabd602c&threadType=Meeting&meetingType=Scheduled&subType=RecapSharingLink_RecapCore)

#### Discussion items

| **Field level changes for Sales Referral details** | <br>- We are currently using **Leadsource**  for both Group-1 and Group-2, and by default, it is set to **"Digital Onboarding Experience"** . This default will remain unchanged, except for **BAML** .<br>  - If the **Plan Sponsor**  has selected "**How did you hear about us** " i.e.  **Referred_By_C   currently mapped in Salesforce** , will be replaced with leadsource:<br>    - Populate the **Leadsource**  field with the referred details.<br>      - The data for this can be<br>        - Bank/Branch Assoicate,<br>        - Bank/Branch flyer<br>        - [BankOfAmerica.com/MerrillEdge.com](http://BankOfAmerica.com/MerrillEdge.com)<br>        - Other<br>    - Update **Merrill_Edge_FSA_Name__C**  to **Web_Submission_Type__c** .<br>  - If the **Plan Sponsor**  has not provided any input, then:<br>    - Default the **Leadsource**  to **"Digital Onboarding Experience"** .<br> |
| --- | --- |
| **Additional data in Contact Screen** | <br>- **Auto-enrollment**  → The**Boolean value**  needs to sent across as **picklist** .<br>- **Profit Sharing**  → A **picklist**  will be provided that includes various profit sharing formulas, along with **"No"**  as one of the selectable options. Based on the **Plan Sponsor's selection**  through the **Digital Onboarding Experience (DOE)** , the corresponding data will be captured and applied accordingly.<br> |
| **Additional data in Opportunity** | <br>- **Current Plan Provider (Other)**  → In the case of a **conversion/ transfer plan** , we will provide the **recordkeeper's business name**  under this field.<br>- **Asset summary details/Total Plan Assets**  → For conversion/ transfer plans, we will provide a **link to the document stored in CLIFF** . This will enable the **Salesforce team**  to determine the **total plan assets**  accurately.<br> |

*🚧 Access to image forbidden: 'https://tfs.ascensus.com/tfs/PSG/a69d2178-e980-458b-8b33-9f83df5f2156/_apis/wit/attachments/e7ee4b89-ebf4-4440-a4ab-9518bb739a10?fileName=image.png'*

*🚧 Access to image forbidden: 'https://tfs.ascensus.com/tfs/PSG/a69d2178-e980-458b-8b33-9f83df5f2156/_apis/wit/attachments/3b4f4bc8-01d5-4592-9d5e-c8b292b82ebd?fileName=image.png'*

#### Action items

- ☒ Christopher McCoy to provide with the API for
  - ☒ Auto-enrollment
  - ☒ Profit Sharing
  - ☒ Current Plan Provider
  - ☒ Total plan assets
