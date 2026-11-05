# Onboarding.Api Testing Strategy

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Onboarding.Api-Testing-Strategy-310460295.aspx) | Created: 2025-03-21 | Last modified: 2025-04-16 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

#### Which endpoints will be tested?

Essentially all of the publicly exposed endpoints will be tested, with the exception of the endpoint used to retrieve fund details.

- GET
  - /advisors/crds/{crd} (Sybase look-up)
  - /advisors/crds/{crd} (Bright Scope look-up)
  - /sponsors/eins/{ein}
  - /sponsors/banks/{routingNumber}
  - /brand/{brand}/colors
  - /brand/{brand}/styles
  - /onboardings/{onboardingId}
  - /documents/{documentId}
  - /onboardings/{onboardingId}/advisors
  - /onboardings/{onboardingId}/documents
  - /onboardings/{onboardingId}/sponsors
- POST
  - /onboardings
  - /onboardings/{onboardingId}/documents
- PUT
  - /onboardings/{onboardingId}/advisors
  - /onboardings/{onboardingId}/documents
  - /onboardings/{onboardingId}/sponsors

#### Which endpoints will not be tested?

- GET
  - /funds
- POST
  - /admin/funds/refresh
  - /onboardings/workflows
- PUT
  - /onboardings/{onboardingId}/documents
    - Taurus handles file uploads via PUTs in a special way that does not work with the current implementation of our endpoint, so we have temporarily duplicated the endpoint as POST as well.  Please see this link for more information:    [Troubleshooting Issues in Test Results](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Troubleshooting-Issues-in-Test-Results-315564083.aspx)

#### What kinds of tests will be performed?

- Load testing
- Soak testing
- Stress testing
- Scalability testing
  - Adjust CPU/memory constraints between tests to find an appropriate baseline

#### Will the endpoints be tested through Kong, and if so, how do we handle obtaining the authentication token?

Yes, there is a separate set of scripts that can be used to execute these tests against DEV, QA, or QA through Kong.  As of now, the scripts to execute tests against PRO have not been completed, however this can be accomplished by using the following items from the QA setup as a baseline:

- Helm/{env}/Internal and Helm/{env}/External
  - These are currently setup for the internal endpoints for DEV and QA and Kong endpoints in QA, but can copied for PRO with tweaks to the values.yaml file to include the appropriate files referenced in *clientArgs*
- Scripts/[...]
  - A separate set of scripts can be created for testing in PRO.
  - We may only need the run-rancher-{env} scripts here, and it is essentially just ensuring that we are pulling in the appropriate settings file for PRO
- Tests/[...]
  - Each performance test sits within a separate directory.  At a minimum, each test will need a separate Blazemeter{env}.json file setup for PRO to ensure that the name of the test in Blazemeter properly references the environment that it was executed against
  - Each test directory will also need a new set of run scripts that call into the main scripts referenced above.  These are all just copies of the same thing which point to the main script but within the context of the current test

#### How will data clean-up be managed?

Please see the following link:

[How to remove data created during performance tests](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-How-to-remove-data-created-during-performance-tests-315568921.aspx)
