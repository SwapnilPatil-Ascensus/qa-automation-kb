# How to execute the performance tests

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-How-to-execute-the-performance-tests-315559269.aspx) | Created: 2025-04-03 | Last modified: 2025-04-16 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

1. Make sure you have followed the instructions for [Initial Setup: Python, Taurus, and JMeter](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Initial-Setup-Python,-Taurus,-and-JMeter-310459396.aspx) and that you are able to execute that example without any issues
2. Make sure you have followed the instructions for [Initial Setup: Running Tests in Rancher](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Initial-Setup-Running-Tests-in-Rancher-315557114.aspx) and that you are able to execute the commands to validate your setup without any issues.
  1. *Note: This step is not applicable if you are just executing the tests locally*
3. Pull the latest changes for our Onboarding solution
4. Find the test that you'd like to execute in Onboarding.Api/Test/Onboarding.Api.PerformanceTests/Tests
5. Navigate within the test folder and execute the appropriate script, which will call into the core script stored in the Templates folder but within the context of the current test:
  1. run-local-{env}.bat
    1. This script is used to kick the tests off from your local PC against the internal service URL in the applicable environment
  2. run-local-{env}-via-kong.bat
    1. This script is used to kick the tests off from your local PC against the external service URL in the applicable environment (routed through Kong).
  3. run-rancher-{env}.bat
    1. This script is used to deploy a pod to rancher to kick off the tests against the internal service URL in the applicable environment, and will also export the results into Blazemeter
  4. run-rancher-{env}-via-kong.bat
    1. This script is used to deploy a pod to rancher to kick off the tests against the external service URL in the applicable environment (routed through Kong), and will also export the results into Blazemeter
6. When executing either of the "run-rancher-{env}" scripts, the test results will be exported to Blazemeter
  1. [Blazemeter Test Results (demo)](https://a.blazemeter.com/app/#/accounts/406482/workspaces/404690/projects/2493816/tests)
  2. [Blazemeter Test Results (real, not yet used)](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/tests)
  3. *Note: You should be able to find your test results under a test that matches the same name as the "test" parameter in Blazemeter{env}.json or Blazemeter{env}ViaKong.json*
