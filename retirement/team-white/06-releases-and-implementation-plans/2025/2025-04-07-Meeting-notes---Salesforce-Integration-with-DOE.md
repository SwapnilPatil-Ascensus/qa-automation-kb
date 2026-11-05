# 2025-04-07 Meeting notes - Salesforce Integration with DOE

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2025-04-07-Meeting-notes---Salesforce-Integration-with-DOE-321345558.aspx) | Created: 2025-05-29 | Last modified: 2025-05-29 | Author: Palak Bhatt | Last editor: Palak Bhatt

---

#### Date

2025-04-07

#### Attendees

- Christopher McCoy
- [@Paul Peca](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Paul.Peca%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a34acb2c57014acb59e8a30468)
- [@Franklin Zabala](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Franklin.Zabala%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a34c885b44014ca379d80b0002)
- [@Max Shakirov](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Max.Shakirov%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a36e77c028016f3b8fdd770025)
- [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022)
- [@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)

#### Goals

- SalesForce Integration with DOE
- Link to the recording - [Salesforce Integration with DOE](https://teams.microsoft.com/l/meetingrecap?driveId=b%21DIk5QiiwuUW1ej129OqLlugN0km-IJpIo4EDVOKuINELM1PBAuAFTpBGBaYm1MYd&driveItemId=01CGFUQWGVWNE6YZLYQNHZTHFCNX42BA44&sitePath=https://ascensus0-my.sharepoint.com/:v:/g/personal/palak_bhatt_ascensus_com/EdWzSexleINPmZyibfmgg5wBPN_skJ9vkPTcBknnXV3YwA&fileUrl=https://ascensus0-my.sharepoint.com/:v:/g/personal/palak_bhatt_ascensus_com/EdWzSexleINPmZyibfmgg5wBPN_skJ9vkPTcBknnXV3YwA&iCalUid=040000008200e00074c5b7101a82e00800000000a67e25086ba5db0100000000000000001000000043d8d7c2a419524e9aaa540dd86ca2b9&threadId=19:meeting_OTYzMGUyMzctMTQwZi00YzA2LWE2MjgtYzMwOTY0NWEwYjIx%40thread.v2&organizerId=96fde839-b366-460d-9f83-6958d9c31fd2&tenantId=1d3bed01-6d09-498e-ab05-f1e2fdb1b138&callId=009c9483-2884-4cd1-af07-2c87ee11c438&threadType=Meeting&meetingType=Scheduled&subType=RecapSharingLink_RecapChiclet)

#### Discussion items

| **Item** | **Notes** |
| --- | --- |
| **Integration Phases** | <br>- The integration involves two phases - one where the advisor fills out details and another where the plan sponsor fills out details. A new record will be created in Salesforce when the advisor fills out the details, and it will be updated when the plan sponsor completes their part.<br> |
| **Applicability** | <br>- There was a discussion on whether the integration applies to all offering keys or only those with advisors. It was clarified that it applies to all, even those without advisors.<br> |
| **Salesforce Objects** | <br>- Christopher McCoy explained the main objects in Salesforce - opportunity, account, and contact - and how they are interconnected. He emphasized the importance of ensuring that accounts and contacts are created before opportunities to maintain data integrity.<br> |
| **Data Requirements** | <br>- The team discussed the necessary data fields for accounts and contacts, including CRD numbers, which are essential for preventing duplicate entries and ensuring accurate data.<br> |
| **Challenges with CRD Numbers** | <br>- A significant challenge identified was the collection of CRD numbers, especially since it is not a required field in the current UI. This could lead to issues with data matching and duplication in Salesforce.<br> |
| **API's and Lower environment access** | <br>- Team White will be needing the access to Salesforce API's and Lower environment access to identify the data fields which will be sent across to Salesforce in Advisor as well as Plan Sponsor have added the data and test the integration.<br> |

#### Action items

- ☒ Team White to confirm with Business regarding the challenges with the CRD number.
- ☒ Christopher to provide with the API's and the list of mandatory fields which needs to be added in Salesforce.
