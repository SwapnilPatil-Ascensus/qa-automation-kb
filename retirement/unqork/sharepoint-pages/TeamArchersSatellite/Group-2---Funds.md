# Group 2 - Funds

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Group-2---Funds-326740776.aspx) | Created: 2025-06-16 | Last modified: 2025-06-16 | Author:  | Last editor: 

---

1. Previously to add funds through Onboarding application, we had excel template files containing partner specific data for funds on shared network path below. Now, the dependency on these template files has been removed. The same data from all the applicable excel templates is expected to receive from JSON from Unqork Digital Onboarding application.
  1. DEV: \\nt1\Data1\ASCDev\Onboarding
  2. QA: \\nt1\Data1\ASCTest\Onboarding
2. Below are the considerations for processing funds from Unqork JSON.

1. Funds will have only those fund IDs which are present in funds template in network location.
2. Models will also have at least one model ID passed in "Models JSON Parameter" from the list of models IDs present in template in network location.
3. Default fund will have default value from Funds or Models list as applicable for specific partner.

Reference:

[Funds](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Funds-258382289.aspx)
