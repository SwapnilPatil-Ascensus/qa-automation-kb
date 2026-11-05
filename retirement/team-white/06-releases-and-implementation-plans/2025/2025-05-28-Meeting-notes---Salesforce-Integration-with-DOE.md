# 2025-05-28 Meeting notes - Salesforce Integration with DOE

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2025-05-28-Meeting-notes---Salesforce-Integration-with-DOE-321345565.aspx) | Created: 2025-05-29 | Last modified: 2025-05-29 | Author: Palak Bhatt | Last editor: Palak Bhatt

---

#### Date

2025-05-28

#### Attendees

- Christopher McCoy
- [@Max Shakirov](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Max.Shakirov%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a36e77c028016f3b8fdd770025)
- [@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)

#### Goals

- SalesForce Integration with DOE for the three IK Flows(Level Comp, Amundi and StateFarm) where we are not having Advisor CRD
- Link to the recording - [Salesforce Integration with DOE](https://ascensus0-my.sharepoint.com/personal/palak_bhatt_ascensus_com/_layouts/15/stream.aspx?id=/personal/palak_bhatt_ascensus_com/Documents/Recordings/Salesforce%20Integration%20with%20DOE%20queries-20250528_210306-Meeting%20Recording.mp4&referrer=StreamWebApp.Web&referrerScenario=AddressBarCopied.view.69f4f7e1-c39a-4771-bd97-8ca9a37dfcce)

#### Discussion items

| **Item** | <br>**Notes**<br> |
| --- | --- |
| **IK Plans of Group 1 where Advisor CRD is not available** | <br>- Since Level Comp, Amundi, and State Farm do not have the Advisor CRD number, we will not be sending their data to Salesforce CRM in the Sales Cloud."<br> |
| **Data extraction and reporting** | <br>- For Level Comp, Amundi and State Farm once we get the Plan sponsor data , Christopher has requested to send across data as a Excel to a dedicated email address. This data as discussed over the call will be sent on daily basis and a dedicated excel will be there for each plan.<br>- If there is not data for the day, we will send across a blank email, mentioning about no sales for the day.<br> |
| **Weekly/Monthly report for all IK Plans** | <br>- Discussion on the possibility of a weekly or monthly roll-up report to ensure no data is missed. This is for all Group-1 Plans.<br>- This report will contain Plan ID, Type of Group-1 Plan and Status<br> |
| **Testing discussion** | <br>- Christopher McCoy confirmed that creating test entries in Salesforce would not cause issues and could be easily deleted.<br> |
| **Field Matching and CRD Numbers:** | <br>- Discussion on matching broker dealer CRD numbers and handling multiple CRD numbers for accounts.<br>- Christopher McCoy suggested updating the CRD field to allow multiple numbers separated by commas.<br> |

#### Summary

- For specific products (Amundi, State Farm, Level Comp), no entries will be made in Salesforce.
- Daily emails with Pek files for plans not fed into Salesforce.
- Monthly summary reports to verify all plans and their statuses.

#### Action items

- ☐ Discussion with Paul Peca for the new requirements i.e.
  - ☐ Sending daily and weekly/monthly data for all IK plans and
  - ☐ PEK files to be sent for all plans once Sponsor workflow is completed for Amundi, State Farm and Level Comp.
