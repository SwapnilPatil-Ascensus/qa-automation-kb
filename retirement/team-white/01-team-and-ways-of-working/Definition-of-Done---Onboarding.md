# Definition of Done - Onboarding

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Definition-of-Done---Onboarding-321346914.aspx) | Created: 2025-05-29 | Last modified: 2025-05-29 | Author: Pete Bretz | Last editor: Eddie Hooper

---

##### Before a story is pulled into a sprint...

- Through our shaping and refinement sessions, we've met the [Definition of Ready - Onboarding](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Definition-of-Ready---Onboarding-321346919.aspx)

##### Design

- Team will have design discussions as needed. Call out need for design discussion in Refinement, including who needs to be included. Note this in the story and add it as at task in the story.
- During design discussions detail API calls, data dictionary, etc. These deeper details should be documented in Confluence, as Confluence is a more permanent information storage tool than user stories.
- *Unqork* : Developers share low level design verified by experienced team members. Goal is to reduce duplicative efforts.

##### Development

- Logging as needed
  - **TAKEAWAY - ASHAY** : Define logging setup in *Unqork*
- Code coverage and unit tests as needed
  - For *Unqork* , document the test cases that have been performed. Attach the documentation to the story
  - **TAKEAWAY - ASHAY:** Share the example
- Code completed and manually reviewed by another developer. Over time, develop a code review checklist.
- Code deployment/promotion
  - APIs: Code merged into Master and deployed to QA environments
  - *Unqork* : through the promotion cycle, code promoted to QA environment
- *Unqork* : Run Config Analysis Tool at least once per week and fix issues within sprint. This is a code quality test.
- Documentation
- Product Owner review as needed
- Monitoring capabilities as needed
- If we learn something new while developing, add that info to the story. If we learn that reality is significantly different from the story, we need to create a new story for the new reality.
- Review vulnerability reports (Currently using Fortify scans)
- API load testing for 50, and up to 375 concurrent users.
  - **TAKEAWAY - PETE** : Need to more clearly define the UX load testing standards. Question for Kate and Serge. @Pete

##### Testing

- Well defined test cases are created and documented in TFS as needed
  - TFS links for storing test cases
    - UX: [http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=691007&suiteId=691008](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=691007&suiteId=691008)
    - API: [http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=647787&suiteId=647788](http://tfs.ascensus.com:8080/tfs/psg/Portfolio/_testPlans/define?planId=647787&suiteId=647788)
  - Other test case links
    - High Level Test Results With Date : [OnboardingAPI.xls](https://ascensus0.sharepoint.com/:x:/s/TeamWhite/EbuCDBS6KWdKolggM7gYWZgBbNMNVAn_CgC-ZQuIZWxEHQ?e=BIByOB)
    - Location of the Test Results:  [Onboarding.Api](https://ascensus0.sharepoint.com/:f:/s/TeamWhite/EiFK4TrXYRROiTuvj0Qxv24B22HINj6Eb2r2GrPHE8E0Qw?e=6ZGzea)
    - Test Results Template : [Test Results.docx](https://ascensus0.sharepoint.com/:w:/s/TeamWhite/EbuZvLGG19ZCvZXkeFCoMSEBCWe3vdEORGPRP49xYNXdfA?e=GGZTru)
- Test results are documented in a shared location ***Should we add link in here?***
- Complete Integration (End to End) testing as needed/as possible
- All critical tests pass in lower environments
- Documentation
- Product Owner review as needed
- For *Unqork* , need UX team (Kate/Serge) to review test cases.  Engage them early and treat them like PO review.
- If we find issues while story is open, add a bug to that story
- Complete manual testing as needed
- If testing can not be done in QA, use DEV if applicable

##### Production Deployment

- **Need a conversation to figure out rolls to Production**
