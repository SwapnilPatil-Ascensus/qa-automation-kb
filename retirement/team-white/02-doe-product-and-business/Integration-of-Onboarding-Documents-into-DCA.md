# Integration of Onboarding Documents into DCA

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Integration-of-Onboarding-Documents-into-DCA-346540215.aspx) | Created: 2025-10-18 | Last modified: 2025-10-21 | Author: Shankar Satijani | Last editor: Diego Emanuel Travieso

---

**Objective:**  To research and find a approach to integrate certain Onboarding documents into DCA so that business and participants can view and work with them when plan becomes available in DCA.

Documents which are proposed to be Integrated into DCA:

- Adoption Agreement
- Other (RCMA Application) [BAML only]

Since development of BAML flow has not yet started, therefore as of now we will focus on research on the Adoption Agreement document, but whatever approach is decided that will also hold good for BAML documents.

Onboarding Group 1 and Group 2 Documents for the Plans are stored in Cliff. We will be using Cliff as the source of the Documents to the DCA. We also have a information of the documents associates with the OnboardingId stored in the database.

For Group 1 the data is stored in field “CliffDocumenId” in “OnboardingState” table.
For Group 2 the data is stored in field “CliffDocumenId” in “CommandSharedData” table.

**Proposed Approach**

1. Create a new Job in PDXJobs in DCA, the frequency that this Job will execute will be decided by the business. We need to connect with business or DCA SME's to understand when such process or job is triggered, as well as conditions for the plan to be picked up for document processing on DCA side.   This Job will call the endpoint “integratedocumentsintodca” of the Onboarding.Api.    The Plan information inside the EDB database is stored in EDB..DCPlan table. We can add some logic into DCA Job to prevent retry of the process of integrating the documents into DCA for a plan for which the process is already completed.      *🚧 Nested Code Block macro 1️⃣ moved below*
2. Create 2 new database columns “DocumentIntegratedIntoDCA” which is a bit field and “DocumentIntegratedDateTime” which can be a timestamp. The default value o the “DocumentIntegratedIntoDCA” column will be false.
3. Create new endpoints “integratedocumesintodca” and “updatedocumentintegrationstatus”  in Onboarding.API.

*🚧 Nested Code Block macro 1️⃣ moved here:*

select PlatformInternalPlanId_vc as ARKPlanId, PlatformName_vc, * from Edb..DcPlan where PlatformInternalPlanId_vc = '{ARK Plan ID}'  – e.g. 237708

**Purpose of the endpoint "integratedocumesintodca":**

1. This endpoint will fetch the data related to the files which we want to integrate into DCA from the database.   Ex: Adoption Agreement for a Plan.
2. This endpoint will call the Cliff API to fetch the document an will convert this document data into binary format.
3. Since this endpoint will be called by DCA Job the frequency of which will be decided by business.
4. If the frequency of the DCA Job is monthly, then this endpoint will consider the current month and will have a logic to fetch the details of all the Onboarding’s of the last 30 days which have a ARK PlanId and who have completed the entire Onboarding process which can be determined by the OnboardingState or the CommandState fields.

Similar custom logic can be written if the frequency of the DCA Job is weekly or daily.

The response of the API endpoint can be in the following format:

{   "onboardingid" : "Guid",   "documentId" : "Cliff documentId"   "arkplanId" :   "310230”,   "documenttype" : "Adoption Agreement"   "filename": "Document-20250502122025843-2a617d67-bc5e-4fdd-911f-76445e3dd6ab.pdf"  }

4.  DCA Job will process the API response and will then call the Cliff API endpoint with the CliffDocumentId as input

        Ex: [https://internal-api-qa.ascensus.com/documentmanagement/cliff/application/DOCUMENT_MANAGEMENT/document/15510458](https://internal-api-qa.ascensus.com/documentmanagement/cliff/application/DOCUMENT_MANAGEMENT/document/15510458)

Please find some examples below of the API calls from DCA Jobs

| <br>**External API / service calls**<br>a)      Alerts API (AMP) via _alertsClient.Create(planRequest)<br>·         In PNC/ImportFIMRFilesIntoSharedRepositoryJob.cs, SponsorReportingJob.cs, SponsorWelcomEmailJob.cs.<br>b)     HTTP clients<br>·         ThirdPartyIntegration/NYLUpdateApplicantInfoJob.cs: uses NewportWebClient (HTTP) to call NYL service.<br>·         McCamishParticipantResubmitJob.cs: uses HttpClient.<br>·         BaseWebNotifyJob.cs, SystemMonitoringJob.cs: use NewportWebClient (HTTP).<br> |
| --- |

Some more examples can be found by scanning the PDXJobs project through Cursor AI.

5.  Once the file data is available into PDXJobs then the DCA Job will write some custom logic to create database entries into tables

EnterpriseDocumentContent, EnterpriseDocument,PlanFileCategory and PlanFile in the EDB database.

               An existing example of such logic can be found in the PNC/ImportFIMRFilesIntoSharedRepositoryJob.cs under PDXWeb

| <br>EnterpriseDocument doc = EnterpriseDocument.CreateNew(<br>oc: oc,<br>documentTypeId: SharedConstants.EnterpriseDocumentType.FIMRReport,<br>sourceId: SharedConstants.EnterpriseDocumentSource.Automation,<br>filename: incomingFile.Name,<br>extension: "PDF",<br>autoCreateAttributes: false,<br>attributes: new Dictionary<string, string>(),<br>documentContent: File.ReadAllBytes(incomingFile.FullName),<br>isEncrypted: false<br>);  <br>  <br>PlanFile planFile = PlanFile.CreateNew(<br>oc: oc,<br>dcPlanId: dcPlan.DcPlanID,<br>filename: incomingFile.Name,<br>typeId: SharedConstants.FileType.InvestmentResearch,<br>description: "",<br>customName: incomingFile.Name,<br>enterpriseDocumentId: doc.DocumentId<br>);  <br>  <br>return PlanFileCategory.CreateNewWithSave(<br>dcPlanId: dcPlanID,<br>name: _folderName,<br>typeId: SharedConstants.PlanFileCategoryType.Category,<br>adminId: 0,<br>parentCategoryId: null,<br>SharedRepositoryToggleId: SharedConstants.SharedRepositoryToggle.Investment<br>).CategoryId;<br> |
| --- |

Also, in the DCA Job the file which we received from the Cliff API can be stored physically in the DCA network shared folder.
          For Dev and QA environment, the path is: \\web-filestore-dev\System Share\stage\Docs

For Production environment, the path is \\web-filestore\Production\Docs

6.  Once the entire process is completed successfully in the DCA Job we can call a Onboarding API endpoint “updatedocumentintegrationstatus” with OnboardingId as parameter to update the status of the “DocumentIntegratedIntoDCA” to “true” and  “DocumentIntegratedDateTime” to the current date time in the respective Onboarding database tables. This will indicate that file integration into DCA process is completed for this OnboardingId. If there is any better approach, then creation of new endpoint “updatedocumentintegrationstatus” to update the status then that can be implemented.

7. Once all the data related to file are updated properly in the EDB tables then file should be visible for the DCA Plan under the PlanDocuments screen.

Please refer below screenshot:

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Integration-of-Onboarding-Documents-into-DCA-346540215/image-2025-10-18_15-49-40.png)

Example of the DCA Plan Documents URL:

[http://dev.newportgroup.com/participant/document/plandocuments?p=pUBSFADAP](http://dev.newportgroup.com/participant/document/plandocuments?p=pUBSFADAP)

The code for the PlanDocuments Screen can be found in the files PlanDocuments.cshtml and Participant\DocumentController.cs (Line 876)

| <br>//add edb documents<br>files.AddRange(_plandocumentQuery.GetDocuments(PM.SelectedParticipant.DcPlanId, PM.SelectedParticipantId.Value)<br>.Where(a => a.TypeId != SharedConstants.FileType.ParticipantFeeDisclosure \|\| planDocuments.ParticipantFeeDisclosureId.IsNullOrEmpty())<br>.Select(a => new PlanDocumentVM<br>{<br>Title = a.TypeId == SharedConstants.FileType.PlanInfo ? a.CustomTitle : a.Title,<br>Description = a.Description,<br>CreatedDt = a.Created,<br>FileType = PlanFile.TypeFromExtension(a.FileName),<br>Token = [REDACTED] DocViewerSecurityToken(20) { PersonId = PM.PersonId, EnterpriseDocumentId = a.EnterpriseDocumentId, PlanFileId = a.FileId }.Encrypt())}"<br>}).OrderBy(a => a.CreatedDt));<br> |
| --- |

**Proposed Flow Diagram**

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Integration-of-Onboarding-Documents-into-DCA-346540215/Integrate_Onboarding_Into_DCA.png)

**New proposed stories**

New stories which can be added in the Backlog for the above approach:

1. Creation of new endpoints in Onboarding API
2. Add new columns in Onboarding tables and entity framework migration
3. Create new Job in DCA for Integrating selected Onboarding documents into DCA.

**Additional information needed**

1. Need to understand when this proposed DCA Job will get triggered, as well as conditions for the plan to be picked up for document processing on DCA side.
2. Some more understanding of the DCA table structure for files and documents and also the DCA network share location where the files are stored.

**Another Approach**

Instead of creating a job that would run to confirm that the plan is already in DCA so we can create the corresponding reecords directly in EDB, we can setup ARK (sybase) and or whatever is needed for the EIM process that brings the new plans in ARK to DCA includes the generation of the required files. If the files can be consumed from Cliff in DCA, probably the work will be much simpler, since we would only need to provide the reference so DCA can request them from Cliff directly.
