# General API testing strategy

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-General-API-testing-strategy-299370894.aspx) | Created: 2025-01-03 | Last modified: 2025-06-02 | Author: Anitha Moturi | Last editor: Anitha Moturi

---

Create the <ServiceName>API folder on SharePoint and paste the links to the respective endpoint folders on SharePoint containing the test case results in both Word document and Excel formats for each story.

To create the folder structure for your Onboarding Service,  follow these steps:

1. 1. Create the main folder                • Name it OnboardingAPI.   2. Create subfolders for each endpoint under the main folder OnboardingAPI               • Name it <EndPoint1>               • Repeat for <EndPoint2>, <EndPoint3>, etc.   3. Create subfolders for TestCasesResults under the EndPoint folders           • Name it TestCasesResults.
2. Repeat for other endpoints.
3. Store the test cases results ( like Json requests and responses and screen shots etc ) in a word document for each end point per sprint.
4. Store the high level test results (success/failure) against each test case in an excel sheet along with the dates on which those test cases were executed to maintain the history.
5. Paste the links to the above two documents (word and excel) for each story in TFS

***Onboarding API  :***

[T](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=647787&suiteId=647788) [estsuites documentation link :](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=647787&suiteId=647788)[http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=647787&suiteId=647788](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=647787&suiteId=647788)

High Level Test Results With Date : [https://ascensus0.sharepoint.com/:x:/s/TeamWhite/EbuCDBS6KWdKolggM7gYWZgBbNMNVAn_CgC-ZQuIZWxEHQ?e=BIByOB](https://ascensus0.sharepoint.com/:x:/s/TeamWhite/EbuCDBS6KWdKolggM7gYWZgBbNMNVAn_CgC-ZQuIZWxEHQ?e=BIByOB)

Location of the Test Results:  [Onboarding.Api](https://ascensus0.sharepoint.com/:f:/s/TeamWhite/EiFK4TrXYRROiTuvj0Qxv24B22HINj6Eb2r2GrPHE8E0Qw?e=6ZGzea)

Test Results Template : [https://ascensus0.sharepoint.com/:w:/s/TeamWhite/EbuZvLGG19ZCvZXkeFCoMSEBCWe3vdEORGPRP49xYNXdfA?e=GGZTru](https://ascensus0.sharepoint.com/:w:/s/TeamWhite/EbuZvLGG19ZCvZXkeFCoMSEBCWe3vdEORGPRP49xYNXdfA?e=GGZTru)

***Onboarding Workflow API  :***

Testsuites documentation link :  [http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=658093&suiteId=658094](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=658093&suiteId=658094)

High Level Test Results With Date :

Location of the Test Results:

Test Results Template :

***Onboarding.Setup.Plan API TestSuites documentation link :***

T[estsuites documentation link :](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=656891&suiteId=656892)[http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=656891&suiteId=656892](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=656891&suiteId=656892)

High Level Test Results With Date :

Location of the Test Results:

Test Results Template :

**Onboarding.UI:**

**Auxo UI bugs:  [Onboarding.UI Bugs.xlsx](https://ascensus0.sharepoint.com/:x:/s/TeamWhite/EXBPU1w-xTRJlW1yOoAZwSoBAtBA5kbnZmpfJkPLJ79Dyg?e=NLrxEN)**

| **Product Name** | **Advisor CRD Number Present** | **Dealer CRD Number Present** | **Agent Number Present** | **RepID Present** |
| --- | --- | --- | --- | --- |
| StateFarm | No | No | Yes | No |
| Amundi | No | Yes | No | Yes |
| Advisor Daily LC | No | Yes | No | Yes |
| Ascensus DailyFB | Yes | Yes | No | No |
| Balance Forward Products | Yes | No | No | No |
