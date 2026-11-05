# Onboarding SecureAuth Realm for getting token for Kong

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841.aspx) | Created: 2024-12-19 | Last modified: 2025-05-09 | Author: Eddie Hooper | Last editor: Eddie Hooper

---

Onboarding integration is utilizing SecureAuth as means to secure communication between Unqork UX experience and Ascensus Onboarding API via Kong API gateway. For this purpose, we have established a new SecureAuth realm 288.

#### SecureAuth Management

|  |  |  |
| --- | --- | --- |
| DEV | [https://rdre1-dsauth03/SecureAuth0](https://rdre1-dsauth03/SecureAuth0)/ | [https://secureauth.dev.ascensus.com/SecureAuth0](https://secureauth.dev.ascensus.com/SecureAuth0) |
| QA | [https://rdre1-qsauth03/secureauth0/](https://rdre1-qsauth03/secureauth0/) | [https://secureauth.qa.ascensus.com/SecureAuth0](https://secureauth.qa.ascensus.com/SecureAuth0) |
| PRO | [https://rdre1-psauth07/secureauth0/](https://rdre1-psauth07/secureauth0/) | [https://secureauth.ascensus.com/SecureAuth0](https://secureauth.ascensus.com/SecureAuth0) |

#### SecureAuth288 Configuration

- Make sure the data  tablet doe not have  data store
![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-24_10-24-20.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-24_10-24-55.png)

- Workflow tab  needs  Default workflow as**username and password |second factor**

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-24_10-26-26.png)

- Post Authentication

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-24_10-42-30.png)

Issuer- need to be [https://secureauth.qa.ascensus.com/SecureAuth288](https://secureauth.qa.ascensus.com/SecureAuth288)

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-24_10-44-41.png)

Scope need to have the scope of the query for it - OnboardingAPIConsumer_QA

Sign cert should be given by secops for each env:

DEV - secureauth06292101dev

QA - 14VM

PRO - 08VM

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-26_12-45-15.png)

- Client detail tab

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-24_10-47-17.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-24_10-46-28.png)

- Open ID Connect ID Token Claims

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-24_10-48-59.png)

- Roles -select group list

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-24_10-49-54.png)

All information  for Qa/PRO is in passwordstate and can be access by any devops

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-SecureAuth-Realm-for--getting-token-for-Kong-294992841/image-2024-12-26_13-34-0.png)

References:

[Secure Auth Configuration](https://ascensus0.sharepoint.com/sites/CorporateCF/SitePages/CPDV-Secure-Auth-Configuration-279271349.aspx)

[🚧👉[missing page or no access] GLOBAL:Secureauth OAuth👈](https://localhost/wt/unresolved?wtPtl=OpenID%20Connect%20SSO&wtPky=MTP&wtPct=Page)
