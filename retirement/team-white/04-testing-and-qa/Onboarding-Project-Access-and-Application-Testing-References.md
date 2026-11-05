# Onboarding Project: Access and Application Testing References

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Onboarding-Project-Access-and-Application-Testing-References-380127076.aspx) | Created: 2026-04-23 | Last modified: 2026-05-11 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

Verify each item with your manager and submit service tickets for any access you are missing.

**1. Partner & sponsor QA applications**

After navigating  to Test Boss **[https://testboss.newportgroup.com/BOSSCoreMVC/Home](https://testboss.newportgroup.com/BOSSCoreMVC/Home)** , confirm Test Sponsor access in the Test environment, then verify you can reach the following URLs.

Newport Group — Partner dashboard (QA): **[https://qa.newportgroup.com/partner/dashboard](https://qa.newportgroup.com/partner/dashboard)**

Cliff QA: **[http://cliff.qa.internal.ascensus.com/edms/Main.aspx](http://cliff.qa.internal.ascensus.com/edms/Main.aspx)**

Chorus QA (SS&C): **[https://bpcascncbeta.ssnc.direct/betaweb/awd/portal/login.html?appcontext=betaapp](https://bpcascncbeta.ssnc.direct/betaweb/awd/portal/login.html?appcontext=betaapp)**

**Action:**  If you cannot access any of these, open a fresh service ticket for each system you need.

Sample fresh service tickets for DCA, Boss, Cliff access and Chorus access below . Mention your ascensus email id in the ticket

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-Project-Access-and-Application-Testing-References-380127076/image-2026-4-28_12-2-41.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-Project-Access-and-Application-Testing-References-380127076/image-2026-5-7_13-44-14.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-Project-Access-and-Application-Testing-References-380127076/image-2026-4-23_9-57-24.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-Project-Access-and-Application-Testing-References-380127076/image-2026-4-23_9-57-47.png)

**2. SQL Server Databases**

- Server:  RDRE1-QDBBEC02,5100 (QA)

- Server:  RDRE1-DDBBE01,2895 (DEV)

- Database name: Msvc_Onboarding

- DBA: Scott Kirkpatrick

**Action:**    Submit a separate fresh service ticket for each environment that you need access to .

If you cannot access any of the above servers through SQLServerManagementStudio even after getting access,  Check with DBA on how to proceed

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-Project-Access-and-Application-Testing-References-380127076/image-2026-4-28_10-54-56.png)

**3. Additional data platforms**

**[Request access to Sybase](https://ascensus0.sharepoint.com/sites/SoftwareDelivery/SitePages/PSDO-Sybase-or-WystarARK-Access-Request-113885717.aspx)** [- Sybase or Wystar/ARK Access Request - Software Delivery - Ascensus - Confluence](https://ascensus0.sharepoint.com/sites/SoftwareDelivery/SitePages/PSDO-Sybase-or-WystarARK-Access-Request-113885717.aspx)

- Sybase QA  (bps_test)

- Sybase DEV (bps_dev)

- ARK QA ([https://ark-qa.ascensus.com](https://ark-qa.ascensus.com))

- ARK DEV ([https://ark-dev.ascensus.com](https://ark-dev.ascensus.com)[)](https://ark-dev.ascensus.com/)

- **Action:**    Submit a separate fresh service ticket for each environment that you need access to .
![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-Project-Access-and-Application-Testing-References-380127076/image-2026-4-28_12-24-28.png)

**4. Build, deploy, and documentation links**

- TeamCity — Onboarding project (builds): [https://teamcity.ascensus.com/project/Onboarding?mode=builds#all-projects](https://teamcity.ascensus.com/project/Onboarding?mode=builds#all-projects)
- Octopus — Onboarding project: [https://octopus.ascensus.com/app#/Spaces-1?projectGroupId=ProjectGroups-541&projectName=Onboarding](https://octopus.ascensus.com/app#/Spaces-1?projectGroupId=ProjectGroups-541&projectName=Onboarding).
- Example partner deployment write-up (Confluence): [2026-04-16 - [27594] TeamWhite - Ascensus IK Bal Fwd No Advisor](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-2026-04-16---[27594]-TeamWhite---Ascensus-IK-Bal-Fwd-No-Advisor-380116906.aspx)
- Useful Links (Confluence): [Useful Links](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Useful-Links-294991068.aspx)
- DOE — Product Links (Confluence): [_ DOE - Product Links](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-_-DOE---Product-Links-310464363.aspx)

**5. Test results storage** **/Test Cases**

1. Manual test results for the Onboarding project are kept in a shared “Test Results” folder - [Test Results](https://ascensus0.sharepoint.com/:f:/r/sites/TeamWhite/Shared%20Documents/General/Onboarding/Test%20Results?csf=1&web=1&e=AkETT0)
2. Test Suites for Onboarding API test cases - [http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=647787&suiteId=666977](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=647787&suiteId=666977)
3. Test Suites for Onboarding Workflow API test cases - [http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=658093&suiteId=658094](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=658093&suiteId=658094)

**6.  Playwright automation test suites:**

1. Group1 UI tests link - [DOE - PlayWright Testing](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-DOE---PlayWright-Testing-331384736.aspx)
2. DCA.Partner.Dashboard.UI  tests - [http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/DCA?path=/MFE/DCA.Partner.Dashboard.UI/Tests](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/DCA?path=/MFE/DCA.Partner.Dashboard.UI/Tests)
3. Group2 UI tests link – [http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.UI.AutomationTest/Test/Onboarding.UI.DOE.Group2.EndToEnd&_a=contents&version=GBmaster](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.UI.AutomationTest/Test/Onboarding.UI.DOE.Group2.EndToEnd&_a=contents&version=GBmaster)

**7. Figma links for Unqork UI**

[https://www.figma.com/files/1161966669115309139/project/224698536?fuid=1497604044177992432](https://www.figma.com/files/1161966669115309139/project/224698536?fuid=1497604044177992432)  (Contact [@Franklin Zabala](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Franklin.Zabala%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a34c885b44014ca379d80b0002) to request access)

**8. TFS Links for Onboarding projects**

[http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/Onboarding?version=GBmaster](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/Onboarding?version=GBmaster)

[http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/DCA?path=/MFE/DCA.Partner.Dashboard.UI](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/DCA?path=/MFE/DCA.Partner.Dashboard.UI)

**9.  Add following Package Sources from Visual Studio**

**Tools->Options→Nuget Packet Manager→ Package Sources**

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-Project-Access-and-Application-Testing-References-380127076/image-2026-5-11_10-44-58.png)

**10. Suggested first-week checklist**

- Confirm VPN / network access for internal QA URLs.

- Log in to Test Boss and validate Test Sponsor access in Test.

- Open tickets for Cliff QA, Chorus QA, Newport QA, Sybase QA, ARK QA, or other systems as needed.

- Confirm TeamCity and Octopus visibility for the Onboarding project.

- Bookmark Confluence pages (Useful Links, DOE Product Links).

- Locate the Test Results folder and the QA SQL Server connection details for Msvc_Onboarding.
- Clone Repository from Visual Studio , add Nuget Package Sources from #9 and Build the Onboarding Solution

*Document generated for internal onboarding use.*
