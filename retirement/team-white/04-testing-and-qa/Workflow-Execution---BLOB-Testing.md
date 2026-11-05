# Workflow Execution - BLOB Testing

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Workflow-Execution---BLOB-Testing-315559829.aspx) | Created: 2025-04-04 | Last modified: 2025-04-10 | Author: Federico Pizzaro | Last editor: Federico Pizzaro

---

#### Testing Result Summary

| <br> | **Offering Key** | **1st attempt** | **2nd attempt** | **3rd attempt** | **Workflow Completed** |
| --- | --- | --- | --- | --- | --- |
| Amundi | <br>AmundiDailyIk<br> | planName is missing | Success | <br> | <br>**​    OK    ​**<br> |
| Amundi II | <br>AmundiDailyIk<br> | planName is missing | planeffectivedatenew is missing | Success | <br>**​    OK    ​**<br> |
| Ameriprise | <br>AmeripriseBalFwdIk<br> | businessNameDisplay not in Sponsor blob but in Advisor blob | planName is missing | Success | <br>**​    OK    ​**<br> |
| Pershing | <br>PershingBalFwdIk<br> | businessNameDisplay not in Sponsor blob but in Advisor blob | planName is missing | Success | <br>**​    OK    ​**<br> |
| JP Morgan | <br>JPMorganBalFwdIk<br> | businessNameDisplay not in Sponsor blob but in Advisor blob | planName is missing | Success | <br>**​    OK    ​**<br> |
| StateFarm | <br>StateFarmDailyIk<br> | planName is missing | planeffectivedatenew is missing | Success | <br>**​    OK    ​**<br> |
| Ascensus Ik Balance | <br>AscensusBalFwdIk<br> | Sponsor blob is missing | <br> | <br> | <br>**​  FAILED   ​**<br> |
| Ascensus Daily LC | <br>AscensusDailyLCIk<br> | Sponsor blob is missing | <br> | <br> | <br>**​  FAILED   ​**<br> |
| Ascensus Daily Fee Based | <br>AscensusDailyFBIk<br> | Sponsor blob is missing | <br> | <br> | <br>**​  FAILED   ​**<br> |

#### Amundi Flow

##### **Onboarding Id** : **CE9F1730-C1B4-49AB-BE0E-78F915D39F73**

#### **1st Attempt**

**Correlation Id: 01000000-6C74-367B-D4FC-08DD7378581A**

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Failed | Error: Establish plan has failed with the following error:  System.NullReferenceException: Object reference not set to an instance of an object. at Onboarding.Setup.Plan.Domain.Engine. EstablishPlanEngine.InsertCompanyData(String planID, Company company) in /src/Onboarding.Setup.Plan/Source/Onboarding. Setup.Plan/Domain/Engine/EstablishPlanEngine.cs:line 141 at Onboarding.Setup.Plan.Domain. PlanSetupManager.EstablishPlan(EstablishPlanRequest request) in /src/Onboarding.Setup.Plan/Source /Onboarding.Setup.Plan/Domain/PlanSetupManager.cs:line 78 | {  <br>    "PlanID": "283768",  <br>    "Product": "ARKPlan4One",  <br>    "ProductOffering": "AmundiDailyIk",  <br>    "PlanData": {  <br>        "envelopeId": "de3783e1-350a-4652-bea5-0c4dff296a3b",  <br>        "businessNameDisplay": "TesterBusinessDN",  <br>        "businessEIN": "22-2222222",  <br>        "businessEstablishmentDate": "01/01/2020",  <br>        "businessNAICSCode": "111111",  <br>        "businessTaxYearEnd": "31-Jan",  <br>        "businessType": "Corporation",  <br>        "priorYearTaxStatus": "no",  <br>        "taxFilingExtension": "no",  <br>        "planEffectiveDateNew": "02/01/2024",  <br>        "planAgeRequirement": "21",  <br>        "planSvcRequirement": "12",  <br>        "planSuccessorShortcut": "",  <br>        "successorPAEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "successorPAFirstName": "TesterBInfoF",  <br>        "successorPALastName": "TesterBinfoL",  <br>        "achAccountABAContribution": "343434341",  <br>        "achAccountAcctNumberContribution": "434332222",  <br>        "achAccountBankNameContribution": "",  <br>        "achAccountTypeContribution": "checking",  <br>        "automaticFundingElection": "no",  <br>        "recordkeepingEffectiveDate": "2025/04/02",  <br>        "recordkeepingFeePaymentElection": "planassets",  <br>        "textComments": "",  <br>        "onboardingId": "ce9f1730-c1b4-49ab-be0e-78f915d39f73",  <br>        "tickers": "[{\u0022ticker\u0022:\u0022CVFCX\u0022}]",  <br>        "participant1FirstName": "TesterClientFN",  <br>        "participant1LastName": "TesterClientLN",  <br>        "participant1EmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "participant1SSN": "999999999",  <br>        "participant1DOB": "2004-12-22",  <br>        "participant1AddressLine1": "203 Main St",  <br>        "participant1AddressLine2": "",  <br>        "participant1City": "York",  <br>        "participant1State": "NY",  <br>        "participant1ZipCode": "19343",  <br>        "participant1AcctNum": "",  <br>        "participant1RothAcctNum": "",  <br>        "partner": "amundi",  <br>        "advisorEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "advisorFirstName": "TesterFN",  <br>        "advisorLastName": "TesterLN",  <br>        "advisorAddressLine1": "200 Main St",  <br>        "advisorBusinessName": "BusinessName_Tester",  <br>        "advisorCity": "London",  <br>        "advisorPhoneNumber": "8888888888",  <br>        "advisorState": "AK",  <br>        "advisorZipCode": "18232",  <br>        "advisorDealerAddress1": "201 Main St",  <br>        "advisorDealerCRDNumber": "777777777777",  <br>        "advisorDealerCity": "Paris",  <br>        "advisorDealerName": "TesterFN",  <br>        "advisorDealerPhoneNumber": "7777777777",  <br>        "advisorDealerState": "AK",  <br>        "advisorDealerZipCode": "12345",  <br>        "businessAddressCity": "North Wales",  <br>        "businessAddressLine1": "202 Main St",  <br>        "businessAddressState": "AS",  <br>        "businessAddressZipCode": "33333",  <br>        "businessName": "ClientBusinessName_Tester",  <br>        "planContactEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "planContactFirstName": "TesterClientFN",  <br>        "planContactLastName": "TesterClientLN",  <br>        "planContactPhoneNumber": "6666666666",  <br>        "installationType": "Startup"  <br>    },  <br>    "Funds": [ "CVFCX" ],  <br>    "DefaultFund": "CVFCX",  <br>    "MockEndpointBehaviour": 0  <br>} | <br>"planname" is not provided by OnboardingWorkflowAPI<br> | <br>When PlanSetupAPI maps the  ARKReportingPlanName assigns a null value if the PlanName is not provided.<br>arkData.Company.ARKReportingPlanName = unqorkProperties.ContainsKey( PlanDataPropertyIDConstant.PlanName) ? unqorkProperties[PlanDataPropertyIDConstant.PlanName] : null;<br>Then a NullReferenceException is thrown here:<br>prgenTableColumns.Add( DefaultTableColumn.BuildDefaultTableColumn("GenPlanName", company.**ARKReportingPlanName.ToUpper()** , false, "char("));<br> | <br>Add planName to the Sponsor BLOB<br> |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 2nd Attempt

**Correlation Id**  01000000-6216-728c-90f0-08dd738083e6

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Success | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | Success | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | Success | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | Success | <br> | <br> | <br> | <br> | <br> |

#### **Onboarding Id**  9AC5BC36-2C9F-4818-9057-05860F99920B

#### 1st Attempt

**CorrelationId:**  01000000-6216-728C-5F60-08DD738DF4C1

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Failed | Error: Establish plan has failed with the following error: System.NullReferenceException: Object reference not set to an instance of an object. at Onboarding.Setup.Plan.Domain.Engine.EstablishPlanEngine.InsertCompanyData(String planID, Company company) in /src/Onboarding.Setup.Plan/Source/Onboarding.Setup.Plan/Domain/Engine/EstablishPlanEngine.cs:line 141 at | <br>{  <br>    "PlanID": "283791",  <br>    "Product": "ARKPlan4One",  <br>    "ProductOffering": "AmundiDailyIk",  <br>    "PlanData": {  <br>        "envelopeId": "a0aeed5c-9f20-4ec2-a5ee-96dba6ebb9eb",  <br>        "businessNameDisplay": "Amundi SponsorBusinessDisplayAnitha",  <br>        "businessEIN": "11-2323232",  <br>        "businessEstablishmentDate": "11/12/2012",  <br>        "businessNAICSCode": "123456",  <br>        "businessTaxYearEnd": "31-Jan",  <br>        "businessType": "C Corporation",  <br>        "priorYearTaxStatus": "no",  <br>        "taxFilingExtension": "no",  <br>        "planEffectiveDateNew": "",  <br>          <br>        "planAgeRequirement": "21",  <br>        "planSvcRequirement": "12",  <br>        "planSuccessorShortcut": "{\u0022name\u0022:\u0022Add another person\u0022,\u0022participantEmailAddress\u0022:\u0022Add Another Person\u0022}",  <br>        "successorPAEmailAddress": "[AmundiSuccessorPA1F.AmundiSuccessorPA1L@gmail.com](mailto:AmundiSuccessorPA1F.AmundiSuccessorPA1L@gmail.com)",  <br>        "successorPAFirstName": "AmundiSuccessorPA1F",  <br>        "successorPALastName": "AmundiSuccessorPA1L",  <br>        "achAccountABAContribution": "011301536",  <br>        "achAccountAcctNumberContribution": "123456789",  <br>        "achAccountBankNameContribution": "EASTERN BANK",  <br>        "achAccountTypeContribution": "checking",  <br>        "automaticFundingCtbnAmt": "100",  <br>        "automaticFundingElection": "yes",  <br>        "recordkeepingEffectiveDate": "2025/04/04",  <br>        "recordkeepingFeePaymentElection": "planassets",  <br>        "textComments": "",  <br>        "onboardingId": "9ac5bc36-2c9f-4818-9057-05860f99920b",  <br>        "tickers": "[{\u0022ticker\u0022:\u0022AOBLX\u0022},{\u0022ticker\u0022:\u0022CVFCX\u0022},{\u0022ticker\u0022:\u0022FLARX\u0022},{\u0022ticker\u0022:\u0022GLOSX\u0022}]",  <br>        "participant1FirstName": "AmundiSponsorF",  <br>        "participant1LastName": "AmundiSponsorL",  <br>        "participant1EmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "participant1SSN": "123456789",  <br>        "participant1DOB": "2001-12-12",  <br>        "participant1AddressLine1": "30 richards rd",  <br>        "participant1AddressLine2": "Suite 600",  <br>        "participant1City": "WillowGrove",  <br>        "participant1State": "PA",  <br>        "participant1ZipCode": "19025",  <br>        "participant1AcctNum": "",  <br>        "participant1RothAcctNum": "",  <br>        "participant2FirstName": "AmundiPPT1F",  <br>        "participant2LastName": "AmundiPPT1L",  <br>        "participant2RelationshipToIKOwner": "Spouse",  <br>        "participant2SSN": "123456788",  <br>        "participant2DOB": "2001-01-01",  <br>        "participant2EmailAddress": "[AmundiPPT1F@gmail.com](mailto:AmundiPPT1F@gmail.com)",  <br>        "participant2AddressLine1": "30 richards rd",  <br>        "participant2AddressLine2": "Suite 600",  <br>        "participant2City": "WillowGrove",  <br>        "participant2State": "PA",  <br>        "participant2ZipCode": "19025",  <br>        "participant2AcctNum": "",  <br>        "participant2RothAcctNum": "",  <br>        "participant3FirstName": "AmundiPPT2F",  <br>        "participant3LastName": "AmundiPPT2L",  <br>        "participant3RelationshipToIKOwner": "Business Partner",  <br>        "participant3SSN": "123456787",  <br>        "participant3DOB": "2001-01-01",  <br>        "participant3EmailAddress": "[AmundiPPT2F@gmail.com](mailto:AmundiPPT2F@gmail.com)",  <br>        "participant3AddressLine1": "Participant2 address line1",  <br>        "participant3AddressLine2": "Participant2 address line2",  <br>        "participant3City": "Middletown",  <br>        "participant3State": "DE",  <br>        "participant3ZipCode": "10678",  <br>        "participant3AcctNum": "",  <br>        "participant3RothAcctNum": "",  <br>        "partner": "amundi",  <br>        "advisorEmailAddress": "TeamWhiteDevelopers@[ascensus.com](http://ascensus.com)",  <br>        "advisorFirstName": "AdvisorFirst",  <br>        "advisorLastName": "AdvisorLast",  <br>        "advisorAddressLine1": "200 dryden road",  <br>        "advisorAddressLine2": "Suite 400",  <br>        "advisorBranchNumber": "123",  <br>        "advisorBusinessName": "AmundiApril42025AnithaBusiness",  <br>        "advisorCity": "Dresher",  <br>        "advisorPhoneNumber": "1234567890",  <br>        "advisorRepId": "1234567",  <br>        "advisorState": "PA",  <br>        "advisorZipCode": "19025",  <br>        "advisorDealerAddress1": "20 derek court",  <br>        "advisorDealerAddress2": "Suite 500",  <br>        "advisorDealerCRDNumber": "1234567",  <br>        "advisorDealerName": "AmundiAdvisorFirmNameAnitha",  <br>        "advisorDealerState": "NJ",  <br>        "advisorDealerCity": "Edison",  <br>        "advisorDealerPhoneNumber": "1234567890",  <br>        "advisorDealerZipCode": "19025",  <br>        "businessAddressCity": "WillowGrove",  <br>        "businessAddressLine1": "30 richards rd",  <br>        "businessAddressLine2": "Suite 600",  <br>        "businessAddressState": "PA",  <br>        "businessAddressZipCode": "19025",  <br>        "businessName": "Amundi sponsor Business name",  <br>        "planContactEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "planContactFirstName": "AmundiSponsorF",  <br>        "planContactLastName": "AmundiSponsorL",  <br>        "planContactPhoneNumber": "1234567890",  <br>        "installationType": "Startup"  <br>    },  <br>    "Funds": [  <br>        "AOBLX",  <br>        "CVFCX",  <br>        "FLARX",  <br>        "GLOSX"  <br>    ],  <br>    "DefaultFund": "AOBLX",  <br>    "MockEndpointBehaviour": 0  <br>}<br> | Missing plan name in Sponsor BLOB | <br> | Add planName to the Sponsor BLOB |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 2nd Attempt

**Correlation Id:**  01000000-14C3-1228-E319-08DD73908BA3

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Error | Error: "AdoNetCore.AseClient.AseException: **The column InitEffctvDate in table Client..PlanInfo does not allow null values.**  at AdoNetCore.AseClient.Internal. Handler.MessageTokenHandler.AssertNoErrors() in C:\Users\tiennguyen\source\repos\AdoNetCore.AseClient.0.19.2\src\ AdoNetCore.AseClient\Internal \Handler\MessageTokenHandler.cs:line 89 at AdoNetCore.AseClient.Internal.InternalConnection. nternalExecuteNonQueryAsync(AseCommand command, AseTransaction transaction, TaskCompletionSource`1 rowsAffectedSource) | <br>{  <br>    "PlanID": "283792",  <br>    "Product": "ARKPlan4One",  <br>    "ProductOffering": "AmundiDailyIk",  <br>    "PlanData": {  <br>        "envelopeId": "a0aeed5c-9f20-4ec2-a5ee-96dba6ebb9eb",  <br>        "businessNameDisplay": "Amundi SponsorBusinessDisplayAnitha",  <br>        "businessEIN": "11-2323232",  <br>        "businessEstablishmentDate": "11/12/2012",  <br>        "businessNAICSCode": "123456",  <br>        "businessTaxYearEnd": "31-Jan",  <br>        "businessType": "C Corporation",  <br>        "priorYearTaxStatus": "no",  <br>        "taxFilingExtension": "no",  <br>        "planEffectiveDateNew": "",  <br>         "planAgeRequirement": "21",  <br>        "planSvcRequirement": "12",  <br>        "successorPAEmailAddress": "[AmundiSuccessorPA1F.AmundiSuccessorPA1L@gmail.com](mailto:AmundiSuccessorPA1F.AmundiSuccessorPA1L@gmail.com)",  <br>        "successorPAFirstName": "AmundiSuccessorPA1F",  <br>        "successorPALastName": "AmundiSuccessorPA1L",  <br>        "achAccountABAContribution": "011301536",  <br>        "achAccountAcctNumberContribution": "123456789",  <br>        "achAccountBankNameContribution": "EASTERN BANK",  <br>        "achAccountTypeContribution": "checking",  <br>        "automaticFundingCtbnAmt": "100",  <br>        "automaticFundingElection": "yes",  <br>        "recordkeepingEffectiveDate": "2025/04/04",  <br>        "recordkeepingFeePaymentElection": "planassets",  <br>        "textComments": "",  <br>        "onboardingId": "9ac5bc36-2c9f-4818-9057-05860f99920b",  <br>         "participant1FirstName": "AmundiSponsorF",  <br>        "participant1LastName": "AmundiSponsorL",  <br>        "participant1EmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "participant1SSN": "123456789",  <br>        "participant1DOB": "2001-12-12",  <br>        "participant1AddressLine1": "30 richards rd",  <br>        "participant1AddressLine2": "Suite 600",  <br>        "participant1City": "WillowGrove",  <br>        "participant1State": "PA",  <br>        "participant1ZipCode": "19025",  <br>        "participant1AcctNum": "",  <br>        "participant1RothAcctNum": "",  <br>        "participant2FirstName": "AmundiPPT1F",  <br>        "participant2LastName": "AmundiPPT1L",  <br>        "participant2RelationshipToIKOwner": "Spouse",  <br>        "participant2SSN": "123456788",  <br>        "participant2DOB": "2001-01-01",  <br>        "participant2EmailAddress": "[AmundiPPT1F@gmail.com](mailto:AmundiPPT1F@gmail.com)",  <br>        "participant2AddressLine1": "30 richards rd",  <br>        "participant2AddressLine2": "Suite 600",  <br>        "participant2City": "WillowGrove",  <br>        "participant2State": "PA",  <br>        "participant2ZipCode": "19025",  <br>        "participant2AcctNum": "",  <br>        "participant2RothAcctNum": "",  <br>        "participant3FirstName": "AmundiPPT2F",  <br>        "participant3LastName": "AmundiPPT2L",  <br>        "participant3RelationshipToIKOwner": "Business Partner",  <br>        "participant3SSN": "123456787",  <br>        "participant3DOB": "2001-01-01",  <br>        "participant3EmailAddress": "[AmundiPPT2F@gmail.com](mailto:AmundiPPT2F@gmail.com)",  <br>        "participant3AddressLine1": "Participant2 address line1",  <br>        "participant3AddressLine2": "Participant2 address line2",  <br>        "participant3City": "Middletown",  <br>        "participant3State": "DE",  <br>        "participant3ZipCode": "10678",  <br>        "participant3AcctNum": "",  <br>        "participant3RothAcctNum": "",  <br>        "planName": "Amundi-Test-0B"  <br>    "Funds": [  <br>        "AOBLX",  <br>        "CVFCX",  <br>        "FLARX",  <br>        "GLOSX"  <br>    ],  <br>    "DefaultFund": null,  <br>    "MockEndpointBehaviour": 0  <br>}<br> | <br>Missing Properties Values for:<br>planeffectivedatenew<br>or<br>planeffectivedateoriginal<br> | Atlhough planEffectiveNew is provided it has an empty value and PlanSetupAPI expects that either planEffectiveDateNew or planEffectiveDataOriginal to have a valid date. | Assign a valid date to planEffectiveDateNew |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 3rd Attempt

**Correlation Id:**  01000000-14c3-1228-581b-08dd739b6ca2

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Success | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | Success | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | Success | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | Success | <br> | <br> | <br> | <br> | <br> |

#### Ameriprise Flow

**OnboardingId** : B1021BD0-A7C1-4C9B-8008-62FF95CB7C9B

#### 1st Attempt

**Correlation Id** 01000000-C6F4-C2CD-AD07-08DD722CEBF2

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Error | <br>Company Name cannot be blank for onboardingId: b1021bd0-a7c1-4c9b-8008-62ff95cb7c9b<br> | <br> | CreatePlanIdInARK consumer is expecting to receive the  businessNameDisplay property in the sponsor blob but in this case the property is provided in the advisor blob instead | <br> | add the businessNameDisplay property to the sponsor blob |
| InitializeRKSystem | <br> | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | <br> | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 2nd Attempt

**Correlation Id** : 01000000-6216-728C-7580-08DD739D3E77

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Failed | Error: Establish plan has failed with the following error: System.NullReferenceException: Object reference not set to an instance of an object. at Onboarding.Setup.Plan.Domain.Engine.EstablishPlanEngine.InsertCompanyData(String planID, Company company) in /src/Onboarding.Setup.Plan/Source/Onboarding.Setup.Plan/Domain/Engine/EstablishPlanEngine.cs:line 141 at | <br>{  <br>    "PlanID": "283799",  <br>    "Product": "ARKPlan4One",  <br>    "ProductOffering": "AmeripriseBalFwdIk",  <br>    "PlanData": {  <br>        "envelopeId": "4e6a71fa-4f6f-445b-bd56-a247cff9a574",  <br>        "businessEIN": "47-4777777",  <br>        "businessEstablishmentDate": "01/01/2021",  <br>        "businessNAICSCode": "323232",  <br>        "businessTaxYearEnd": "28-Feb",  <br>        "businessType": "Corporation",  <br>        "businessNameDisplay": "AmeripriseBN",  <br>        "priorYearTaxStatus": "no",  <br>        "taxFilingExtension": "no",  <br>        "planEffectiveDateOriginal": "2025-02-02T00:00:00.000Z",  <br>        "planSequenceNumber": "545",  <br>        "planEffectiveDateNew": "03/01/2024",  <br>        "planAgeRequirement": "21",  <br>        "planSvcRequirement": "12",  <br>        "planSuccessorShortcut": "",  <br>        "successorPAEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "successorPAFirstName": "ameripriTesterBInfoF",  <br>        "successorPALastName": "ameripriTesterBinfoL",  <br>        "textComments": "",  <br>        "onboardingId": "b1021bd0-a7c1-4c9b-8008-62ff95cb7c9b",  <br>        "participant1FirstName": "TesterAmeripriseFN",  <br>        "participant1LastName": "TesterAmeripriseLN",  <br>        "participant1EmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "participant1SSN": "676744343",  <br>        "participant1DOB": "2001-12-22",  <br>        "participant1AddressLine1": "205 Main St",  <br>        "participant1AddressLine2": "",  <br>        "participant1City": "New York",  <br>        "participant1State": "NY",  <br>        "participant1ZipCode": "14122",  <br>        "participant1AcctNum": "",  <br>        "participant1RothAcctNum": "",  <br>        "partner": "ameriprise",  <br>        "advisorEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "advisorFirstName": "ameripriseTesterFN",  <br>        "advisorLastName": "ameripriseTesterLN",  <br>        "advisorAddressLine1": "204 Main St",  <br>        "advisorBusinessName": "TesterAdvisorBN",  <br>        "advisorCity": "North Port",  <br>        "advisorDealerName": "Ameriprise F",  <br>        "advisorPhoneNumber": "7777777777",  <br>        "advisorState": "FL",  <br>        "advisorZipCode": "12323",  <br>        "businessAddressCity": "New York",  <br>        "businessAddressLine1": "205 Main St",  <br>        "businessAddressState": "NY",  <br>        "businessAddressZipCode": "14122",  <br>        "businessName": "AmeripriseBN",  <br>        "planContactEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "planContactFirstName": "TesterAmeripriseFN",  <br>        "planContactLastName": "TesterAmeripriseLN",  <br>        "planContactPhoneNumber": "3333333333",  <br>        "installationType": "Startup"  <br>    },  <br>    "Funds": [],  <br>    "DefaultFund": null,  <br>    "MockEndpointBehaviour": 0  <br>}<br> | Missing planName in Sponsor BLOB | <br> | Add planName to the Sponsor BLOB |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 3rd Attempt

**CorrelationId:**  01000000-14C3-1228-C378-08DD739D7C36

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Success | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | Success | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | Success | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | Success | <br> | <br> | <br> | <br> | <br> |

### Pershing Flow

**Onboarding Id**  2DEC8147-77D5-4C25-817F-7EA2D2B53E0B

#### 1st Attempt
**Correlation Id**  01000000-C6F4-C2CD-8351-08DD7231C5C7

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Error | <br>Company Name cannot be blank for onboardingId: 2DEC8147-77D5-4C25-817F-7EA2D2B53E0B<br> | <br> | CreatePlanIdInARK consumer is expecting to receive the  businessNameDisplay property in the sponsor blob but in this case the property is provided in the advisor blob instead | <br> | add the businessNameDisplay property to the sponsor blob |
| InitializeRKSystem | <br> | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | <br> | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 2nd Attempt

**Correlation Id**  01000000-6216-728C-72C1-08DD73A18490

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Failed | Error: Establish plan has failed with the following error: System.NullReferenceException: Object reference not set to an instance of an object. at Onboarding.Setup.Plan.Domain.Engine.EstablishPlanEngine.InsertCompanyData(String planID, Company company) in /src/Onboarding.Setup.Plan/Source/Onboarding.Setup.Plan/Domain/Engine/EstablishPlanEngine.cs:line 141 at | <br> | Missing planName in Sponsor BLOB | <br> | Add planName to the Sponsor BLOB |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 3rd Attempt

**Correlation Id**  01000000-C6F4-C2CD-8351-08DD7231C5C7

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Success | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | Success | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | Success | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | Success | <br> | <br> | <br> | <br> | <br> |

### Morgan Flow

**Onboarding Id** A6C261A5-B24B-47C8-AD04-9F7AF9FA0054

#### 1st Attempt

**Correlation Id** 01000000-C6F4-C2CD-4AD8-08DD7234CBFB

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Error | <br>Company Name cannot be blank for onboardingId: A6C261A5-B24B-47C8-AD04-9F7AF9FA0054<br> | <br> | CreatePlanIdInARK consumer is expecting to receive the  businessNameDisplay property in the sponsor blob but in this case the property is provided in the advisor blob instead | <br> | add the businessNameDisplay property to the sponsor blob |
| InitializeRKSystem | <br> | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | <br> | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 2nd Attempt

**Correlation Id**  01000000-6216-728C-72C1-08DD73A18490

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Failed | Error: Establish plan has failed with the following error: System.NullReferenceException: Object reference not set to an instance of an object. at Onboarding.Setup.Plan.Domain.Engine.EstablishPlanEngine.InsertCompanyData(String planID, Company company) in /src/Onboarding.Setup.Plan/Source/Onboarding.Setup.Plan/Domain/Engine/EstablishPlanEngine.cs:line 141 at | <br>{  <br>    "PlanID": "283804",  <br>    "Product": "ARKPlan4One",  <br>    "ProductOffering": "JPMorganBalFwdIk",  <br>    "PlanData": {  <br>        "businessAddressLine1": "210 Main St",  <br>        "envelopeId": "f25c8c64-a358-4eda-896c-48ee94bea2b0",  <br>        "businessEIN": "45-4434343",  <br>        "businessEstablishmentDate": "01/01/2025",  <br>        "businessNAICSCode": "563434",  <br>        "businessTaxYearEnd": "30-Apr",  <br>        "businessType": "Corporation",  <br>        "businessNameDisplay": "jpmBN",  <br>        "priorYearTaxStatus": "no",  <br>        "taxFilingExtension": "no",  <br>        "planEffectiveDateOriginal": "2025-04-01T00:00:00.000Z",  <br>        "planSequenceNumber": "434",  <br>        "planEffectiveDateNew": "01/01/2025",  <br>        "planAgeRequirement": "21",  <br>        "planSvcRequirement": "12",  <br>        "planSuccessorShortcut": "",  <br>        "successorPAEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "successorPAFirstName": "jpmTesterBInfoF",  <br>        "successorPALastName": "jpmTesterBinfoL",  <br>        "textComments": "",  <br>        "onboardingId": "a6c261a5-b24b-47c8-ad04-9f7af9fa0054",  <br>        "participant1FirstName": "TesterjpmFN",  <br>        "participant1LastName": "TesterjpmLN",  <br>        "participant1EmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "participant1SSN": "434665343",  <br>        "participant1DOB": "2000-12-22",  <br>        "participant1AddressLine1": "210 Main St",  <br>        "participant1AddressLine2": "",  <br>        "participant1City": "Denver",  <br>        "participant1State": "CO",  <br>        "participant1ZipCode": "45323",  <br>        "participant1AcctNum": "",  <br>        "participant1RothAcctNum": "",  <br>        "partner": "jpmorgan",  <br>        "advisorEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "advisorFirstName": "jpmTesterFN",  <br>        "advisorLastName": "jpmTesterLN",  <br>        "advisorAddressLine1": "208 Main St",  <br>        "advisorBusinessName": "jpmBN",  <br>        "advisorCity": "Moscow",  <br>        "advisorDealerName": "jpmAfN",  <br>        "advisorPhoneNumber": "3421647232",  <br>        "advisorState": "AK",  <br>        "advisorZipCode": "43555",  <br>        "businessAddressCity": "Denver",  <br>        "businessAddressState": "CO",  <br>        "businessAddressZipCode": "45323",  <br>        "businessName": "jpmBN",  <br>        "planContactEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "planContactFirstName": "TesterjpmFN",  <br>        "planContactLastName": "TesterjpmLN",  <br>        "planContactPhoneNumber": "5612323534",  <br>        "installationType": "Startup"  <br>    },  <br>    "Funds": [],  <br>    "DefaultFund": null,  <br>    "MockEndpointBehaviour": 0  <br>}<br> | Missing planName in Sponsor BLOB | <br> | Add planName to the Sponsor BLOB |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 3rd Attempt

**Correlation Id**  01000000-14C3-1228-F454-08DD73A4D85C

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Success | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | Success | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | Success | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | Success | <br> | <br> | <br> | <br> | <br> |

### StateFarm Flow

**Onboarding Id** A4686832-886A-475C-A4E9-80BB55460ABC

#### 1st Attempt

**Correlation Id**  01000000-6216-728C-A0C0-08DD73A91636

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Failed | Error: Establish plan has failed with the following error: System.NullReferenceException: Object reference not set to an instance of an object. at Onboarding.Setup.Plan.Domain.Engine. EstablishPlanEngine.InsertCompanyData(String planID, Company company) in /src/Onboarding.Setup.Plan/Source/ Onboarding.Setup.Plan/Domain/Engine/EstablishPlanEngine.cs:line | <br>{  <br>    "PlanID": "283807",  <br>    "Product": "ARKPlan4One",  <br>    "ProductOffering": "StateFarmDailyIk",  <br>    "PlanData": {  <br>        "installationType": "Transfer",  <br>        "envelopeId": "10039277-f302-437a-b30e-9956008b6c8f",  <br>        "businessNameDisplay": "StateFarmTest",  <br>        "businessEIN": "22-2222222",  <br>        "businessEstablishmentDate": "11/23/2011",  <br>        "businessNAICSCode": "111111",  <br>        "businessTaxYearEnd": "31-Jan",  <br>        "businessType": "Corporation",  <br>        "planSequenceNumber": "222",  <br>        "priorYearTaxStatus": "yes",  <br>        "planAgeRequirement": "21",  <br>        "planSvcRequirement": "12",  <br>        "planSuccessorShortcut": "",  <br>        "successorPAEmailAddress": "anitha.moturi@[ascensus.com](http://ascensus.com)",  <br>        "successorPAFirstName": "SuccessorF",  <br>        "successorPALastName": "SuccessorL",  <br>        "achAccountABAContribution": "041203824",  <br>        "achAccountAcctNumberContribution": "123456789",  <br>        "achAccountBankNameContribution": "WELLS FARGO BANK, N.A.",  <br>        "achAccountTypeContribution": "checking",  <br>        "automaticFundingElection": "no",  <br>        "recordkeepingEffectiveDate": "2025/04/02",  <br>        "recordkeepingFeePaymentElection": "planassets",  <br>        "textComments": "",  <br>        "onboardingId": "a4686832-886a-475c-a4e9-80bb55460abc",  <br>        "participant1FirstName": "SponsorClientF",  <br>        "participant1LastName": "SponsorClientL",  <br>        "participant1EmailAddress": "anitha.moturi@[ascensus.com](http://ascensus.com)",  <br>        "participant1SSN": "123456789",  <br>        "participant1DOB": "2001-01-01",  <br>        "participant1AddressLine1": "90 Royal ct",  <br>        "participant1AddressLine2": "Suite 600",  <br>        "participant1City": "Edison",  <br>        "participant1State": "NJ",  <br>        "participant1ZipCode": "08234",  <br>        "participant1AcctNum": "",  <br>        "participant1RothAcctNum": "",  <br>        "partner": "statefarm",  <br>        "advisorEmailAddress": "TeamWhiteDevelopers@[ascensus.com](http://ascensus.com)",  <br>        "advisorFirstName": "AnithaTest5F",  <br>        "advisorLastName": "AnithaTest5L",  <br>        "advisorAddressLine1": "200 dryden road",  <br>        "advisorAddressLine2": "Suite 400",  <br>        "advisorBusinessName": "StateFarm Advisor Business Inc",  <br>        "advisorCity": "Dresher",  <br>        "advisorPhoneNumber": "1234567890",  <br>        "advisorState": "PA",  <br>        "advisorZipCode": "19025",  <br>        "agentNumber": "123456789",  <br>        "businessAddressState": "NJ",  <br>        "businessName": "StateFarm Sponsor Business Inc ",  <br>        "planContactEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "planContactFirstName": "SponsorClientF",  <br>        "planContactLastName": "SponsorClientL",  <br>        "planContactPhoneNumber": "1234567890",  <br>        "businessAddressCity": "Edison",  <br>        "businessAddressLine1": "90 Royal ct",  <br>        "businessAddressLine2": "Suite 600",  <br>        "businessAddressZipCode": "08234"  <br>    },  <br>    "Funds": [  <br>        "BACPX",  <br>        "BAAPX",  <br>        "BAGPX"  <br>    ],  <br>    "DefaultFund": "BAGPX",  <br>    "MockEndpointBehaviour": 0  <br>}<br> | Missing planName in Sponsor BLOB | <br> | Add planName to the Sponsor BLOB |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 2nd Attempt

**Correlation Id**  01000000-14C3-1228-FCC6-08DD73A9C797

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Error | Error: "AdoNetCore.AseClient.AseException: **The column InitEffctvDate in table Client..PlanInfo does not allow null values.**  at AdoNetCore.AseClient.Internal. Handler.MessageTokenHandler.AssertNoErrors() in C:\Users\tiennguyen\source\repos\AdoNetCore.AseClient.0.19.2\src\ AdoNetCore.AseClient\Internal \Handler\MessageTokenHandler.cs:line 89 at AdoNetCore.AseClient.Internal.InternalConnection. nternalExecuteNonQueryAsync(AseCommand command, AseTransaction transaction, TaskCompletionSource`1 rowsAffectedSource) | <br>{  <br>    "PlanID": "283808",  <br>    "Product": "ARKPlan4One",  <br>    "ProductOffering": "StateFarmDailyIk",  <br>    "PlanData": {  <br>        "installationType": "Transfer",  <br>        "envelopeId": "10039277-f302-437a-b30e-9956008b6c8f",  <br>        "businessNameDisplay": "StateFarmTest",  <br>        "businessEIN": "22-2222222",  <br>        "businessEstablishmentDate": "11/23/2011",  <br>        "businessNAICSCode": "111111",  <br>        "businessTaxYearEnd": "31-Jan",  <br>        "businessType": "Corporation",  <br>        "planName": "StateFarm - Test - ABC",  <br>        "planSequenceNumber": "222",  <br>        "priorYearTaxStatus": "yes",  <br>        "planAgeRequirement": "21",  <br>        "planSvcRequirement": "12",  <br>        "planSuccessorShortcut": "",  <br>        "successorPAEmailAddress": "anitha.moturi@[ascensus.com](http://ascensus.com)",  <br>        "successorPAFirstName": "SuccessorF",  <br>        "successorPALastName": "SuccessorL",  <br>        "achAccountABAContribution": "041203824",  <br>        "achAccountAcctNumberContribution": "123456789",  <br>        "achAccountBankNameContribution": "WELLS FARGO BANK, N.A.",  <br>        "achAccountTypeContribution": "checking",  <br>        "automaticFundingElection": "no",  <br>        "recordkeepingEffectiveDate": "2025/04/02",  <br>        "recordkeepingFeePaymentElection": "planassets",  <br>        "textComments": "",  <br>        "onboardingId": "a4686832-886a-475c-a4e9-80bb55460abc",  <br>        "participant1FirstName": "SponsorClientF",  <br>        "participant1LastName": "SponsorClientL",  <br>        "participant1EmailAddress": "anitha.moturi@[ascensus.com](http://ascensus.com)",  <br>        "participant1SSN": "123456789",  <br>        "participant1DOB": "2001-01-01",  <br>        "participant1AddressLine1": "90 Royal ct",  <br>        "participant1AddressLine2": "Suite 600",  <br>        "participant1City": "Edison",  <br>        "participant1State": "NJ",  <br>        "participant1ZipCode": "08234",  <br>        "participant1AcctNum": "",  <br>        "participant1RothAcctNum": "",  <br>        "partner": "statefarm",  <br>        "advisorEmailAddress": "TeamWhiteDevelopers@[ascensus.com](http://ascensus.com)",  <br>        "advisorFirstName": "AnithaTest5F",  <br>        "advisorLastName": "AnithaTest5L",  <br>        "advisorAddressLine1": "200 dryden road",  <br>        "advisorAddressLine2": "Suite 400",  <br>        "advisorBusinessName": "StateFarm Advisor Business Inc",  <br>        "advisorCity": "Dresher",  <br>        "advisorPhoneNumber": "1234567890",  <br>        "advisorState": "PA",  <br>        "advisorZipCode": "19025",  <br>        "agentNumber": "123456789",  <br>        "businessAddressState": "NJ",  <br>        "businessName": "StateFarm Sponsor Business Inc ",  <br>        "planContactEmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "planContactFirstName": "SponsorClientF",  <br>        "planContactLastName": "SponsorClientL",  <br>        "planContactPhoneNumber": "1234567890",  <br>        "businessAddressCity": "Edison",  <br>        "businessAddressLine1": "90 Royal ct",  <br>        "businessAddressLine2": "Suite 600",  <br>        "businessAddressZipCode": "08234"  <br>    },  <br>    "Funds": [  <br>        "BACPX",  <br>        "BAAPX",  <br>        "BAGPX"  <br>    ],  <br>    "DefaultFund": "BAGPX",  <br>    "MockEndpointBehaviour": 0  <br>}<br> | <br>Missing Properties Values for:<br>planeffectivedatenew<br>or<br>planeffectivedateoriginal<br> | PlanSetupAPI expects that either planEffectiveDateNew or planEffectiveDataOriginal to have a valid date. | Assign a valid date to planEffectiveDateNew |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

#### 3rd Attempt

**Correlation Id**  01000000-14C3-1228-6944-08DD73AAD93B

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKSystem | Success | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | Success | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | Success | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | Success | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | Success | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | Success | <br> |  |  |  |  |

### Ascensus Ik Balance Forward

**Onboarding Id** A1698C54-40D8-49F9-8956-C7380EDE9477

#### 1st Attempt

**Correlation Id** 01000000-23C1-6A4A-7781-08DD72B17AB2

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Error | <br>Company Name cannot be blank for onboardingId: A1698C54-40D8-49F9-8956-C7380EDE9477<br> | <br> | Sponsor Data not found in the DB (Advisor Data does exist) | <br> | <br> |
| InitializeRKSystem | <br> | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | <br> | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

### Ascensus Daily LC

**Onboarding Id**  A74AB443-ECFA-4F29-8D8A-CFF65E0CDE1E

#### 1st Attempt

**Correlation Id** 01000000-C6F4-C2CD-65B6-08DD7245DC19

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Error | <br>Company Name cannot be blank for onboardingId: A1698C54-40D8-49F9-8956-C7380EDE9477<br> | <br> | Sponsor Data not found in the DB (Advisor Data does exist) | <br> | <br> |
| InitializeRKSystem | <br> | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | <br> | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |

### Ascensus Daily Fee Based

**Onboarding Id**  FFB4BB45-C759-439D-9982-909DCE0AC161

#### 1st Attempt

**Correlation Id** 01000000-6216-728C-081C-08DD73AC9DC7

| <br> | **Result** | **Error** | **Request Data** | **Reason** | **Error Analysis** | **Fix** |
| --- | --- | --- | --- | --- | --- | --- |
| CreatePlanIdInArk | Error | <br>Error: Establish plan has failed with the following error: System.NullReferenceException: Object reference not set to an instance of an object. at Onboarding.Setup.Plan.ResourceAccess.PlanDefaults DataAccess.BuildRowWhereClause(DefaultTableRow row, String genPlanIDSys) in /src/Onboarding.Setup.Plan/Source/Onboarding.S etup.Plan/ResourceAccess/PlanDefaultsDataAccess.cs:line 131 at Onboarding.Setup.Plan.ResourceAccess .PlanDefaultsDataAccess.MaintainRecord(DefaultTableRow row, String genPlanIDSys)<br> | <br>{  <br>    "PlanID": "283811",  <br>    "Product": "ARKPlan4One",  <br>    "ProductOffering": "AscensusDailyFBIk",  <br>    "PlanData": {  <br>        "achAccountABAContribution": "091304760",  <br>        "achAccountBankNameContribution": "FIRST INTERNATIONAL BANK \u0026 TRUST",  <br>        "businessNameDisplay": "ADFBLLC",  <br>        "businessEIN": "22-2222222",  <br>        "businessEstablishmentDate": "01/01/2001",  <br>        "businessNAICSCode": "123456",  <br>        "businessTaxYearEnd": "30-Apr",  <br>        "businessType": "S Corporation",  <br>        "installationType": "Startup",  <br>        "priorYearTaxStatus": "no",  <br>        "taxFilingExtension": "no",  <br>        "planEffectiveDateOriginal": "2020-12-12T00:00:00.000Z",  <br>        "planSequenceNumber": "111",  <br>        "planEffectiveDateNew": "05/01/2024",  <br>        "planAgeRequirement": "21",  <br>        "planSvcRequirement": "12",  <br>        "planSuccessorShortcut": "",  <br>        "successorPAEmailAddress": "anitha.moturi@[ascensus.com](http://ascensus.com)",  <br>        "successorPAFirstName": "SuccessorPAF",  <br>        "successorPALastName": "SuccessorPAL",  <br>        "automaticFundingCtbnAmt": "21",  <br>        "automaticFundingElection": "yes",  <br>        "recordkeepingEffectiveDate": "2025/04/02",  <br>        "recordkeepingFeePaymentElection": "invoice",  <br>        "textComments": "",  <br>        "onboardingId": "ffb4bb45-c759-439d-9982-909dce0ac161",  <br>         "participant1FirstName": "SponsorADFBF",  <br>        "participant1LastName": "SponsorADFBL",  <br>        "participant1EmailAddress": "teamwhitedevelopers@[ascensus.com](http://ascensus.com)",  <br>        "participant1SSN": "123456789",  <br>        "participant1DOB": "2001-01-01",  <br>        "participant1AddressLine1": "19 Derek Ct",  <br>        "participant1AddressLine2": "Suite 600",  <br>        "participant1City": "Princeton",  <br>        "participant1State": "NJ",  <br>        "participant1ZipCode": "08540",  <br>        "participant1AcctNum": "123456789",  <br>        "participant1RothAcctNum": "123456789"  <br>    },  <br>    "Funds": [],  <br>    "DefaultFund": null,  <br>    "MockEndpointBehaviour": 0  <br>}<br> | Missing businessName proeprty in Sponsor blob / Missing Advisor blob | <br> | <br> |
| InitializeRKSystem | <br> | <br> | <br> | <br> | <br> | <br> |
| InitializeRKPlanDefaults | <br> | <br> | <br> | <br> | <br> | <br> |
| EstablishPlan | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateAuditDocument | <br> | <br> | <br> | <br> | <br> | <br> |
| SendDocumentsToCliff | <br> | <br> | <br> | <br> | <br> | <br> |
| CreateChorusWorkItem | <br> | <br> | <br> | <br> | <br> | <br> |
