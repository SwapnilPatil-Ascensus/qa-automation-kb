# 2025-06-03 Meeting notes Salesforce Integration with DOE Group-1

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2025-06-03-Meeting-notes-Salesforce-Integration-with-DOE-Group-1-326731786.aspx) | Created: 2025-06-04 | Last modified: 2025-06-05 | Author: Palak Bhatt | Last editor: Palak Bhatt

---

#### Date

2025-06-03

#### Attendees

- Christopher McCoy
- [@Paul Peca](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Paul.Peca%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a34acb2c57014acb59e8a30468)
- [@Max Shakirov](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Max.Shakirov%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a36e77c028016f3b8fdd770025)
- [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022)
- [@Shankar Satijani](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Shankar.Satijani%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a34acb2c57014acb59e45d0318)
- [@Federico Pizzaro](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Federico.Pizzaro%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3825317f20182d5567cbe009a)
- [@Anitha Moturi](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Anitha.Moturi%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3676d75bf01677e9e5f4b0000)
- [@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)

#### Goals

- Discussion for the missing Broker Dealer CRD's
- SalesForce Integration with DOE for the three IK Flows(Level Comp, Amundi and StateFarm) where we are not having Advisor CRD

Link to the recording - [Salesforce Integration with DOE](https://ascensus0-my.sharepoint.com/personal/palak_bhatt_ascensus_com/_layouts/15/stream.aspx?id=/personal/palak_bhatt_ascensus_com/Documents/Recordings/Salesforce%20Integration%20with%20DOE%20discussion-20250603_120012-Meeting%20Recording.mp4&referrer=StreamWebApp.Web&referrerScenario=AddressBarCopied.view.2de73417-87e2-4fc3-8d11-e11010af517c)

#### Discussion items

| **Item** | **Notes** |
| --- | --- |
| **Default Account for the Missing Broker Dealer CRD** | <br>- Based on the discussion we will be provided with a default account for contacts without a broker dealer CRD.<br>- This default account will be used to assign contacts.<br> |
| **For Level Comp, Amundi and State Farm where we do not contain Advisor details** | <br>- For Level comp, Amundi and State farm we will only be creating opportunities.<br> |
| <br>**Universal Rule for All Products**<br> | <br>- Team White will be creating opportunities for all the IK Group-1 plans irrespective of the Missing Broker Dealer or Advisor CRD's. (Account ID is an optional field for creating an opportunity)<br> |

#### Action items

- ☐ Christopher McCoy will provide us with the default Broker Dealer CRD which we will use when we do not have the Broker Dealer details, this default Broker dealer will be used to create a Contact.
  - ☐ 4 new fields to be added in the Opportunity screen which will be populated when the broker dealer details does not exist.
- ☐ Christopher McCoy will verify the exclusion of opportunities with the lead source of digital onboarding experience from the current flow.
- ☐ Team White will remove the product-specific restrictions and universal application of rules.
