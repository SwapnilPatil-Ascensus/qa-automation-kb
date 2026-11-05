# Sprint 65 - Production Implementation - Infrastructure

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Sprint-65---Production-Implementation---Infrastructure-305972008.aspx) | Created: 2025-02-20 | Last modified: 2025-03-01 | Author: Franklin Zabala | Last editor: Franklin Zabala

---

| **TrakIT** | **Deployment Item** | **Version** | **Completed** | **Notes** |
| --- | --- | --- | --- | --- |
| <br>24534<br> | <br>Onboarding.Data<br> | <br>1.0.10<br> | 2/20/25 3:46 PM | Initial deployment failed due to SQL user msvc_onboarding does not have permission to create tables during migrations. Scott K. helped solved the issue and should be fixed moving forward. |
| <br>24332<br> | <br>DataLoad_Msvc_PlanSetupToMsvc_Onboarding.sql<br> |  | 2/21/25 9:20 AM | Asked DBA to implement to PRO 2/21/25 9AM if possible |
| <br>24553<br> | <br>Onboarding.Api<br> | <br>1.0.284<br> | 2/21/25 4:07 PM | <br> |
| <br>24553<br> | <br>Onboarding.Workflow.Api<br> | <br>1.0.107<br> | 2/21/25 4:09 PM | <br> |
| <br>TBD<br> | <br>Onboarding.Setup.Plan<br> | <br>TBD<br> | <br> | TBD - I recommend not deploying this to PRO, as there's a lot to review in the Octopus as it's using some values from the original Onboarding.SetupPlan.Api project  <br>[@Pankaj Dubey](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Pankaj.Dubey%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a3839729110183d6a39d790022) |
|  |  |  | <br> | <br> |
