# Messaging Command Sagas

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Messaging-Command-Sagas-336423254.aspx) | Created: 2025-08-29 | Last modified: 2026-01-08 | Author: Diego Emanuel Travieso | Last editor: Diego Emanuel Travieso

---

#### Command Sagas and Possible States

**InitializePlanDesign** - Saves initial plan data and creates plan id in ARK

| **Step** | **Pending** | **Failed** |
| --- | --- | --- |
| SavePlanDesignData | SavePlanDesignDataSubmitted | <br>SavePlanDesignDataFailed<br> |
| <br> | PlanIdCreationPending |  |
| CreatePlanInArk | CreatePlanInArkSubmitted | CreatePlanInArkFailed |

**InitiatePlanTransfer** - Transfers information of an existing plan that will be transfered to Ascensus

| **Step** | **Pending** | **Failed** |
| --- | --- | --- |
| SendDocumentsToCliff | SendDocumentsToCliffSubmitted | SendDocumentsToCliffFailed |
| CreateChorusWorkItem | CreateChorusWorkItemSubmitted | CreateChorusWorkItemFailed |
| SendDocumentsToChorus | SendPriorPlanDocsToChorusSubmitted | SendPriorPlanDocsToChorusFailed |

**InitiateStartupPlan** - Creates a Chorus Workitem assigning the installation coordinator

| **Step** | **Pending** | **Failed** |
| --- | --- | --- |
| AssignInstallationCoordinator | AssignInstallationCoordinatorSubmitted | AssignInstallationCoordinatorFailed |

**InitializePlanEstablishment** - Once all the participants and plan data is saved from the DOE it establishes the plan in Ark and in PAS

| **Step** | **Pending** | **Failed** |
| --- | --- | --- |
| InitializeRKSystem | EstablishPlanSubmitted | InitializeRKSystemFailed |
| InitializeRKPlanDefaults | EstablishPlanSubmitted | InitializeRKPlanDefaultsFailed |
| EstablishPlan | EstablishPlanSubmitted | EstablishPlanFailed |
| InitializePlanInPAS | EstablishPlanSubmitted | ComplianceCheckFailed (Final), InitializePlanInPASFailed |

**InitializePlanDocuments**  - After the plan is established in ARK and PAS the request is made to PAS to generate the documents

| **Step** | **Pending State** | **Failed State** |
| --- | --- | --- |
| GeneratePASDocuments | GeneratePASDocumentsSubmitted | GeneratePASDocumentsFailed |
| VerifyDocumentStatus | VerifyingDocumentsStatus | VerifyPlanDocumentsStatusTimedOut, VerifyDocumentsStatusFailed |
| ProcessPASDocumentsData | ProcessPASDocumentsDataSubmitted | ProcessPASDocumentsDataFailed |
| UpdatePASDocumentsStatus | UpdatePASDocumentsStatusSubmitted | UpdatePASDocumentsStatusFailed |

**InitiatePlanInstallation**  - Remaining tasks to complete the plan creation after the documents are created.  This saga will continue from start to finish regardless of any intermediate step failing.

| **Step** | **Pending State** | **Failed State** |
| --- | --- | --- |
| CreateAuditDocumentPek | CreateAuditDocumentPekSubmitted | CompletedWithFailures (CreateAuditDocumentPek step will be marked as Failed in StepHistoryJson) |
| UploadDocumentToCliff | UploadDocumentToCliffSubmitted | CompletedWithFailures (UploadDocumentToCliff step will be marked as Failed in StepHistoryJson) |
| UpdatePASDocumentsStatus | UpdatePASDocumentsStatusSubmitted | CompletedWithFailures (UpdatePASDocumentsStatus step will be marked as Failed in StepHistoryJson) |
| CreateNBInstallChorusWorkItem | InitiatePlanInstallationInChorusSubmitted | CompletedWithFailures (InitiatePlanInstallationInChorus step will be marked as Failed in StepHistoryJson) |
| CloseOpportunityInSalesforce | CloseOpportunityInSalesforceSubmitted | CompletedWithFailures (CloseOpportunityInSalesforce step will be marked as Failed in StepHistoryJson) |

**UpdateBusinessInformation**  - Updates the business info in Salesforce

| **Step** | **Pending State** | **Failed State** |
| --- | --- | --- |
| ValidateOpportunityAndContactData | ValidateOpportunityAndContactDataSubmitted | AwaitingCompleteOpportunityAndContactData (Final), ValidateOpportunityAndContactDataFailed |
| CreateOpportunityInSalesforce | CreateOpportunityInSalesforceSubmitted | CreateOpportunityInSalesforceFailed |
| UpdateOpportunityInSalesforce | UpdateOpportunityInSalesforceSubmitted | UpdateOpportunityInSalesforceFailed |

**PrefillSponsorEmail** - Prefills the sponsor email in unquork

| **Step** | **Pending State** | **Failed State** |
| --- | --- | --- |
| PrefillSponsorEmail | PrefillSponsorEmailSubmitted | PrefillSponsorEmailFailed |

#### Mock Configuration for Testing

It is possible to setup a configuration when calling a Command/Saga execution that allows to mock certain steps in their execution as successful or failed. The endpoints to call Commands and the Command event messages include a MockConfig property, a json structure that allows to specify the expected behavior for each consumer called. It has the following structure:

{   "mockConfig": {     "defaultBehavior": "Success",     "consumerBehaviors": {        "ConsumerA" : "Fail"     }   } }

The defaultBehavior can have 3 valid values: "Execute", "Success" or "Fail". If nothing is provided "Execute" will always be the default value, that means the Consumer will execute without mocking any results. "Success" will make Consumers return a successful mocked message to allow the Saga to continue its execution. "Fail" will make a Consumer publish a fake failure message that the Saga will handle as such. In the ConsumerBehaviors object we can add new properties for specific Consumers and the expected mocked behavior. In the above example every Consumer in the Saga will return a fake Success message, except for the Consumer with name "ConsumerA", which will publish a mocked failure message.

In the specific case of InitializePlanEstablishment, the PlanSetup consists of 4 steps: Initialize Record Keeping System, Initialize Record Keeping Plan Defaults, Establish Plan and Initialize Plan Adoption Documents. These 4 steps are going to be executed by a single consumer, but since we still want to keep track of the state of which of these steps failed, the message published by the PlanSetup Consumer upon a failure will contain information of which particular step failed and thus, the Saga will be set in the corresponding state.

In order to be able to mock this behavior for testing, Each of the failed steps will be treated as a Consumer Name that can be included in the ConsumerBehaviors object. For instance:

{   "mockConfig": {     "defaultBehavior": "Success",     "consumerBehaviors": {        "MockInitializeRKPlanDefaultsFailed" : "Fail"     }   } }

In the above mock config "MockInitializeRKPlanDefaultsFailed" is used as if it was a Consumer name (although it is not), but will be properly interpreted by the Saga and mapped into a mock behavior that PlanSetupConsumer will handle.

The valid values that can be used to mimic a Consumer, representing a step of the plan setup to mock a failure are the following:

- MockInitializeRKSystemFailed
- MockInitializeRKPlanDefaultsFailed
- MockEstablishPlanFailed
- MockInitializePlanInPASFailed
- MockPASComplianceFailed

#### Retry Policy

The following Sagas are displayed in order of execution. Each Step refers to a specific consumer called within the Saga. Each item within a Step refers to a specific action that gives functionality to the step. These actions could be idempotent (meaning that they could be executed several times with the same end result for the same Onboarding) or not. This will be important when treating the whole step as able to be retried or not.

**InitializePlanDesign** - Saves initial plan data and creates plan id in ARK
    - Step SavePlanDesignData: Idempotent. **Retry available.**
        - Generates link for unquork
        - Saves data from Purchase (if present)

    - Step CreatePlanInArk: Idempotent. **Retry available.**
        - Creates Plan in ARK retrieving the PlanId. Idempotent

**InitiatePlanTransfer** - Transfers information of an existing plan that will be transfered to Ascensus
    - Step SendDocumentsToCliff : Not idempotent. **Retry available.**
    - Step CreateChorusWorkItem : Not idempotent. **Retry available.**
    - Step SendDocumentsToChorus: Not idempotent. **Retry available.**

**InitiateStartupPlan**
    - Step AssignInstallationCoordinator: Not Idempotent. **Retry available.**
    - Step StoreChorusWorkItem: Not Idempotent. **Retry available.**

**InitializePlanEstablishment** - Once all the participants and plan data is saved from the DOE it establishes the plan in Ark
    - Step InitializeRKSystem - Idempotent. **Retry available.**
    - Step InitializePlanDefaults - Idempotent. **Retry available.**
    - Step EstablishPlan - Not Idempotent (almost, does not delete already created information) - **Retry available.**     - Step InitializePlanInPAS. Not idempotent - **Retry available.**
        - Calls InitializePlanAdoptionDocuments in PlanSetup. This call could return a NonCompliant result. Leaving the whole saga in a failed-final state.

**InitializePlanDocuments**
    - Step GeneratePASDocuments. Not Idempoent. **Retry available.**
        - Calls GeneratePASDocuments in PlanSetup

- Step VerifyDocumentStatus. Idempotent. **Retry available,**
    - Step ProcessPASDocumentsData. Not Idempotent - **Retry available.**
    - Step UpdatePASDocumentsStatus. Idempotent. **Retry available.**

**NOTE: The DOE will move forward within 15 seconds to the skipped DocuSign experience after any failures in InitializePlanDocuments, so retries here should be avoided.**

**InitiatePlanInstallation**
    - Step CreateAuditDocumentPek : Not Idempotent. **Retry available.**
    - Step UploadDocumentToCliff: Not Idempotent. **Retry available.**    - Step UpdatePASDocumentsStatus: Not Idempotent.**Retry available.**
    - Step CreateNBInstallChorusWorkItem. Not Idempotent. **Retry available.**
    - Step CloseOpportunityInSalesforce. Idempotent. **Retry available.**

**UpdateBusinessInformation -** This complete Saga is idempotent and can be Re-executed as a whole.
    - Step CreateOpportunityInSalesforce or UpdateOpportunityInSalesforce. **Retry available.** Makes no sense to retry anyway. The whole saga is idempotent, can be executed from scratch every time.

#### How Retry Works

The retry can be executed by calling an API endpoint in Onboarding.Messaging.Api [https://internal-api-qa.ascensus.com/onboarding/messaging/api/swagger/index.html](https://internal-api-qa.ascensus.com/onboarding/messaging/api/swagger/index.html)

The Retry endpoint will accept the OnboardingId as part of the url path and internally it will look for any failed Saga/Command (CommandState table) for that Onboarding and pick the failed Step of the failed Saga. Since the execution of the whole Onboarding process is sequential, it is assumed that only one failed state will be found at a certain time for an OnboardingId. With that particular Saga/Step failed, a specific RetryCommandRequested event will be generated and published. This event will be picked up by the corresponding Saga and such Saga (Statemachine) will validate the current State and the requested Retry. If all is valid it will publish the event to re-execute the failed Step and the execution of the Saga will resume its course.
