# Onboarding Workflow Saga

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Onboarding-Workflow-Saga-299386051.aspx) | Created: 2025-01-17 | Last modified: 2025-05-05 | Author: Federico Pizzaro | Last editor: Diego Emanuel Travieso

---

### Sequence Diagram

*🚧 Gliffy diagram 'Onboarding Workflow' replaced by image:*

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Onboarding-Workflow-Saga-299386051/Onboarding%20Workflow.png)

### Onboarding Workflow Api

In order to interact with the Onboarding Workflow, a web api exposes different endpoints to be able to start an onboarding workflow, resume it, get the current status, retry a failed one, etc.

The main usage of this Api is through the Onbarding Api, consumed by the FrontEnd of the DOE, but then there is some additional functionality that can be used to troubleshoot or fix potential issues in failed workflows.

Additional information about how to use this api is [here](https://internal-api-dev.ascensus.com/onboarding/workflow/api/onboardings/workflows/docs).
