# Fortify site and correlated teamcity settings for fortify scan -DRAFT

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616.aspx) | Created: 2025-02-05 | Last modified: 2025-02-05 | Author: Eddie Hooper | Last editor: Eddie Hooper

---

login to ams.fortify.com with your email ,pwd and site = ascensus

navigate to applications tab and click create new

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_17-36-44.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_17-32-23.png)

hit next and set up each microservice

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_17-31-14.png)

add up to 10 microservices

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_17-31-48.png)

fill up application attribute screen with following info or u can add it later

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_18-12-32.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_17-30-36.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_17-11-16.png)

once set all up review and hit next you all set with project

for each microservice go to Static Scan Setup

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_18-21-54.png)

once you fill in and save it will generate release id

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_18-22-49.png)

this will be in the parameter to identify the release of the project. [https://teamcity.ascensus.com/admin/editBuild.html?id=buildType:Onboarding_OnboardingApi_FortifySastScanLinux](https://teamcity.ascensus.com/admin/editBuild.html?id=buildType:Onboarding_OnboardingApi_FortifySastScanLinux)

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Fortify-site-and--correlated-teamcity-settings--for-fortify-scan---DRAFT-305959616/image-2025-2-5_18-24-50.png)
