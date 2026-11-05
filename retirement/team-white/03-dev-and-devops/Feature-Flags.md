# Feature Flags

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Feature-Flags-305970872.aspx) | Created: 2025-02-19 | Last modified: 2025-02-19 | Author: Diego Emanuel Travieso | Last editor: Diego Emanuel Travieso

---

#### Workflow - Onboarding.Workflow.Api

For the workflow api we introduced the Microsoft Feature Management library, that allows to handle functionality based on conditions. In Octopus these variables are referenced by the prefix "FeatureManagement:" and they reflect the configuration in features.json in the project.

**WriteToArk** : For the time being it is a simple boolean flag (true/false) called FeatureManagement:WriteToArk in Octopus, When this flag is set to **true** , all the execution of the Saga Consumers will be running normally, making the calls to the PlanSetup api in "Execute" mode.

When this flag is set to **false** all the calls to PlanSetup api will no longer be made in "Execute" mode. Depending on the MockWorkflowConsumerBehaviour that is provided, each Consumer will resolve if the call to PlanSetup has to be made with a "Success" or a "Fail". In none of these two cases PlanSetup api will be saving data to ARK.

**Note** : Bare in mind when running the workflow, even if the WriteToArk is off, it does not mean it can't fail due to other reasons. Each consumer will still be running the logic to gather the information, build the requests and make the calls to PlanSetup api. If any of these things fail, the process will still fail, regardless of the actual writting to ark being mocked.
