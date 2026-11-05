# Workflow Saga - Error Handling

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Workflow-Saga---Error-Handling-310450904.aspx) | Created: 2025-03-10 | Last modified: 2025-03-11 | Author: Federico Pizzaro | Last editor: Federico Pizzaro

---

#### User Stories (Draft)

**Error Handling - Internal Notifications (Team White)**

As a Team White member
I want to be notified via Teams Channel or email about errors that can occur during the Saga execution
So that I can take action and investigate the error in order to resume the Saga execution

**Error Handling - External Notification (Business)**

As a Business employee
I want to be notified via Chrous about errors that can occur during the Saga execution
So that I can take action and investigate the error in order to resume the Saga execution

**Error Handling - Fault State**

As a Team White Dev
I want to leave the Saga in a Fault state after all attempts to complete the consumer execution were exhausted
So that I can stop the saga execution and wait for human intervention

**Error Handling - Failure State**

As a Team White Dev
I want to left the saga in a failure state when the external resources like PlanSetupAPI or Cliff respond with an error code
So that the saga doesn't keep retrying and the error can notified so it can be investigated

**Performance Testing - Plan Setup And Cliff**

As a Team White Dev
I want to gather metrics about the execution time of the different endpoints (Plan Setup API and Cliff)
So that I can determine if we need to evaluate different alternatives for some specific endpoints like using HangFire to complete specific tasks.

**Error Handling - Send Documents to Cliff Consumer**

As a Team White Dev
I want to redesign the SendDocumentsToCliff consumer
So that it can send to cliff all documents independently and to keep an internal status of which documents were sent with success and which don't so in case of failure I can resend only the failed ones.

#### Notepad

Error Notifications

- Internal Notifications (Team White)
- External notifications (Chorus)

Error Handling

- Identify which errors should be retried
  - Some errors could be associated to network issues or timeout and these errors need to be retried, these errors will be addressed by the US xxxx.
  - Since we don't control or validate the blob data we receive from Unqork we don't have a way to ensure if the data we send to the PlanSetup API is valid or not.   If the PlanSetup API responds with an error because some properties are missing or data is not valid then it doesn't make sense to keep retrying.   In this case we need to pause the saga, notify to chorus and provide the ability to manually resume the saga.
  - Are there any PlanSetupAPI endpoint(s) that could take a long to complete? This can be determined by running tests in DEV and QA.
    - Increase timeout
    - Create a HangFire job to execute long running endpoints
    - When the job finishes it could notify to the saga using a new endpoint in the workflow api or publishing an event to RabbitMQ
  - We could create Hold States for Sagas that can be resumed manually after a time or after a human fix.
    - The 4 Ark Plan Setup related Steps could have one single ArkSetupHold State that would indicate that when resumed the Saga should continue from the step right after PlanId creation.
    - The SaveDocumentToCliff Setup could have one single SaveDocumentToCliffHold State that would indicate that the documents properties could be fixed and the saga could be resumed from that step (only uploading the documents that failed).
- Do we need to apply routing slips to the SendDocumentsToCliff consumer?
  - Documents that were already uploaded should not be uploaded again. We need to create a way to identify which documents are pending and which ones are done.
  - Even without a routing slip, documents could be uploaded in different threads with a parallel loop or some other similar approach.
