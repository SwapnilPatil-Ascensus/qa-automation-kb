# DOE - PlayWright Testing

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-DOE---PlayWright-Testing-331384736.aspx) | Created: 2025-07-02 | Last modified: 2025-07-08 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

**[Initial Setup:](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Initial-Setup-Python,-Taurus,-and-JMeter-310459396.aspx)**

Follow instructions listed on the [PlayWright Setup and Installation](https://ascensus0.sharepoint.com/sites/Confluence-Test4/SitePages/GLOBAL-PlayWright-Setup-and-Installation-207782553.aspx) page for initial setup

**Onboarding Playwright project links in TFS[:](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Initial-Setup-Python,-Taurus,-and-JMeter-310459396.aspx)**

Group1 Offering Keys - [http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/Onboarding?version=GBmaster&path=/Onboarding.UI/Test/Onboarding.UI.AutomationTest](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/Onboarding?version=GBmaster&path=/Onboarding.UI/Test/Onboarding.UI.AutomationTest)

Group2 Offering Keys -

**Playwright folder structure[:](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Initial-Setup-Python,-Taurus,-and-JMeter-310459396.aspx)**

| **Folder/File** | **Description** |
| --- | --- |
| /Configuration | Playwright settings classes |
| `/Tests` | Contains all test classes for advisor/sponsor flows for Group1 |
| `/Pages` | Page Object Model classes |
| `/Database` | Database connection classes |
| `/Queries` | Database queries |
| `/ServicesData` | Data Validation classes |
| `/AppData` | Sample files for uploads |

**How to Run Tests[:](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Initial-Setup-Python,-Taurus,-and-JMeter-310459396.aspx)**

- Headed Mode while debugging
- Headless mode on TeamCity
- Select RunSettings file
-

**Test Reporting[:](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Initial-Setup-Python,-Taurus,-and-JMeter-310459396.aspx)**

- **Where to find logs for data validation:**  \Onboarding\Onboarding.UI\Test\Onboarding.UI.AutomationTest\bin\Debug\net8.0\Logs
- **Where to view test results:**  TeamCity link

**Questions:**

1. Is there a one-click playwright test that does both the advisor flow and sponsor flow for Group1 offering keys? **-** NO
2. Is Advisor data, sponsor data and documents data getting validated for each product offering key ?  YES
3. Are there advisor tests and sponsor tests for all the offering keys in Group1 ?**-** YES
4. Are tests taking care of required properties being present ? - YES, if required property value missing, the test will fail
5. Are there tests for both New plans and Transfer plan flows - YES
