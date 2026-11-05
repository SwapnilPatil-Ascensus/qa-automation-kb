# Troubleshooting Issues in Test Results

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Troubleshooting-Issues-in-Test-Results-315564083.aspx) | Created: 2025-04-09 | Last modified: 2025-04-16 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

#### 400 Bad Request response in PUT Documents tests

*Update: We've decided to duplicate the PUT Document endpoint as a POST to move forward with performance testing.  The fix below does not work once the pod executing the performance tests is deployed to rancher, so for now the performance tests are using POST Document in place of PUT Document.  As a result, the instructions below can be ignored, however they are being preserved for clarity on the issue.*

There is a known issue with how Taurus is handling this test which requires a modification to one of Taurus's python files for resolution.  Specifically, the scenario setup for this endpoint must specify the name of the request parameter expected by our endpoint in Onboarding.Api which holds the file information (shown below for reference):

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Troubleshooting-Issues-in-Test-Results-315564083/image-2025-4-9_15-39-32.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Troubleshooting-Issues-in-Test-Results-315564083/image-2025-4-9_15-30-26.png)

However, when Taurus transforms this scenario into the "BZT Generated Test Plan", the "param" attribute is being wiped out due to our request using an HTTP method type of PUT.  To fix this issue, we can modify the **requests_model.py**  file in the Python site-packages for Taurus by commenting out the following two lines:

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Troubleshooting-Issues-in-Test-Results-315564083/image-2025-4-9_15-34-28.png)

This file can be found in the following location for Python v3.11 after installing Taurus:

> %AppData%\..\Local\Programs\Python\Python311\Lib\site-packages\bzt\requests_model.py
