# Salesforce CRM Integration with DOE

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Salesforce-CRM-Integration-with-DOE-319228471.aspx) | Created: 2025-04-23 | Last modified: 2026-03-31 | Author: Palak Bhatt | Last editor: Palak Bhatt

---

- [Objective](#objective)
- [Data Hierarchy - Why Account → Contact → Opportunity](#data-hierarchy-why-account-%e2%86%92-contact-%e2%86%92-opportunity)
- [Account - Broker Dealer details](#account-broker-dealer-details)
- [Contact - Advisor Dealer details](#contact-advisor-dealer-details)
- [Opportunity - Creating a new opportunity based on Advisor Blob](#opportunity-creating-a-new-opportunity-based-on-advisor-blob)
- [Opportunity - Updating the opportunity based on Sponsor Blob](#opportunity-updating-the-opportunity-based-on-sponsor-blob)
- [Flow Diagram](#flow-diagram)
 [Salesforce Integration for Group-2](#salesforce-integration-for-group-2)
- [Account for Group-2](#account-for-group-2)
- [Contact for Group-2](#contact-for-group-2)
- [Opportunity for Group-2](#opportunity-for-group-2)
  - [Sharebuilder opportunity](#sharebuilder-opportunity)
  - [BAML opportunity](#baml-opportunity)
- [Enhancements for Group 2](#enhancements-for-group-2)
  - [Addition of fields in contact](#addition-of-fields-in-contact)
  - [Addition of fields in opportunity](#addition-of-fields-in-opportunity)
  - [Changes in Opportunity](#changes-in-opportunity)
  [Salesforce Integration for Group 2.2](#salesforce-integration-for-group-2.2)
- [Account for Group 2.2](#account-for-group-2.2)
  - [Account details without Advisor](#account-details-without-advisor)
  - [Accounts with Advisor](#accounts-with-advisor)
- [Contact Creation Process](#contact-creation-process)
- [Opportunity Creation Process](#opportunity-creation-process)
  - [For Products without Advisor both IK and Group](#for-products-without-advisor-both-ik-and-group)

#### **Objective**

To design and implement an efficient digital onboarding experience integrated with Salesforce CRM, enabling seamless opportunity mapping, data accuracy and process automation across various Group-1 IK plans.

#### **Data Hierarchy - Why Account → Contact → Opportunity**

To create an opportunity in salesforce, we need to create an account and contact which will be linked to the opportunity.

Account represents the broker dealer details.

Contact represent the Advisor which are associated with the account i.e. broker dealer.

Opportunity represents the IK workflow, we will send the data when we get the Advisor data and Plan sponsor data.

#### **Account - Broker Dealer details**

- Below is the format for the account details which needs to be stored.
- We will be storing Broker dealer name in Account name field CRD number of the Broker dealer in the CRD field.
- Account Owner and Account ID will always remain the same for DOE.
- Account owner will be "0056S00000EuX3qQAF", based in this we will get the Account ID.

**How do we get the broker dealer details?**

- When we receive the data from the advisor blob, we will check that whether the broker dealer data does exist?
  - There will be two scenarios in this place
    - Broker dealer data does not exist in advisor blob- This will be applicable for Group 1 plans which are Ascensus Balance Forward (w/Advisor), Ameriprise, JP Morgan, Pershing
      - We will look-up for Broker dealer data based on the Advisor CRD which will be available in the advisor blob.
    - Broker dealer data exists in advisor blob - This will be applicable for Group 1 plan which is Ascensus Daily Fee based
      - We will get the broker dealer details directly from "Advisor Flow → Firm Information Section → About Firm Page".

**When do we create a new account in Salesforce?**

- Once we have the broker dealer data, based on the CRD number of the broker dealer, we will check whether the data exists in the Salesforce CRM or not.
- If the broker dealer data exists, then no need to create a new account in the Salesforce CRM.
- If the broker dealer data does not exist, create a new account with the following details mentioned in the below excel.
- Account Owner will always remain the same when creating a new account in Salesforce CRM. Based on the account owner, we will be able to get the Account ID.
- We only need to add
  - Account name - Name of Broker dealer.
  - CRD Number - CRD of Broker dealer.

**What happens when we do not have the Broker Dealer details ?**

- If we do not have the broker dealer details, then we will use the default Broker Dealer which is provided by the Salesforce team.
- The default account ID is 001R700000TtLntIAF (production) and 001Ec00000vUb6aIAC (sandbox)

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** |
| --- | --- | --- | --- | --- |
| **Account** | <br> | **Account** | **Object** | <br> |
| Record Type ID | 012i0000000VCx3AAG | RecordTypeId | Record Type | When creating new account |
| Account Name | Name of broker dealer | Name | Name | When creating new account |
| CRD Number | CRD of BD | CRD_Number__c | Text | To match with existing account, also needs to be added when created |
| Account Owner | 0056S00000EuX3qQAF | OwnerId | Lookup(User) | When creating new account. |
| Account ID | Created automatically for new accounts, needs to be called for existing accounts based on the CRD | AccountID | Lookup(Account) | Called when existing account CRD match is found |
| Default Account ID | 001R700000TtLntIAF (production), 001Ec00000vUb6aIAC (sandbox) | AccountID | Lookup(Account) | Called when we do not have broker dealer CRD. |

#### **Contact - Advisor Dealer details**

- Contact will contain the advisor dealer details.

**How do we get the Advisor dealer details?**

- Below is a table which has the information representing the advisor data which will be received from the Advisor Blob.
  - This table contains from which page of the advisor flow will we receive the data.
- We will receive Advisor data only for
  - Ascensus Balance Forward (w/Advisor)
  - Ameriprise
  - JP Morgan
  - Pershing and
  - Ascensus Daily Fee Based
- For Amundi, State Farm and Daily Fee based, we do not receive the advisor data so we will not be creating advisor contact.

**When do we create a new contact in Salesforce?**

- We will first verify whether the advisor details, along with the broker-dealer mapping received in the advisor blob, exists in the Salesforce CRM.
- If the data exists in the Salesforce CRM, then we can move ahead and create an opportunity.
- If the advisor data does not exist, then we need to create a new contact.
  - This also contains the broker dealer mapping which we will receive based on advisor CRD.

| **Field Name** | **Data Entry** | **Ascensus Balance Forward (w/Advisor)** | **Ameriprise** | **JP Morgan** | **Pershing** | **Ascensus Daily Fee Based** |
| --- | --- | --- | --- | --- | --- | --- |
| Contact | <br> | Not to be fetched from the Advisor Blob |  |  |  |  |
| Contact Record Type | 0120H000001QVtdQAG |  |  |  |  |  |
| First Name | Advisors first name | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page |
| Last Name | Advisors last name | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page | 1)Advisor Flow  <br>2)Get Started Section  <br>3)Landing Page  <br>4)Firm Information Section  <br>5)About business page |
| Account Name | Broker dealer of the advisor. The ID will need to be pulled based on the BDs CRD | <br> | <br> | <br> | <br> | <br> |
| Telephone | Advisors phone number | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page |
| Email | Advisors email | <br>same as above<br>For Street Address we will add Address1 and Address2 in Street Address field.<br> |  |  |  |  |
| Firm Address | Advisors street address |  |  |  |  |  |
| Firm City | Advisors city |  |  |  |  |  |
| Firm State | Advisors state |  |  |  |  |  |
| Firm Zip | Advisors zip |  |  |  |  |  |
| FA CRD Number | Advisors CRD (different than their account CRD, which belongs to their BD) | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page | 1)Advisor Flow  <br>2)Firm Information Section  <br>3)About Business Page |

The database schema for the contact table is as below.

- In here the contact number or the owner Id will always be "0056S00000EuX3qQAF"
- Lead source will always be "Digital Onboarding Experience"

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** |
| --- | --- | --- | --- | --- |
| **Contact** | <br> | **Contact** | **Object** | <br> |
| Contact Record Type | 0120H000001QVtdQAG | RecordTypeId | Record Type | When creating new contact |
| First Name | Advisors first name | FirstName | Text | When creating new contact |
| Last Name | Advisors last name | LastName | Text | When creating new contact |
| Account Name | Broker dealer of the advisor. The ID will need to be pulled based on the BDs CRD | AccountId | Lookup(Account) | When creating new contact |
| Telephone | Advisors phone number | Converted_Lead_Phone__c | Phone | When creating new contact |
| Email | Advisors email | Email | Email | When creating new contact |
| Firm Address | Advisors street address | Firm_address__c | Text | When creating new contact |
| Firm City | Advisors city | Firm_city__c | Text | When creating new contact |
| Firm State | Advisors state | Firm_state__c | Text | When creating new contact |
| Firm Zip | Advisors zip | Firm_ZIP__c | Text | When creating new contact |
| FA CRD Number | Advisors CRD (different than their account CRD, which belongs to their BD) | FA_CRD_Number__c | Text | To match with existing contact, also needs to be added when created |
| Contact Owner | 0056S00000EuX3qQAF | OwnerId | Lookup(User) | When creating new contact |
| Lead Source | Digital Onboarding Experience | LeadSource | Picklist | When creating new contact |

#### Opportunity - Creating a new opportunity based on Advisor Blob

- Once we have the account details ( broker dealer detail) and mapped contact ( advisor dealer detail), we will be able to create an opportunity.
- Below are the details which needs to be added in the opportunity tab
- Opportunity will be created for all the Group-1 plans.

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** | **Data received from Advisor Blob** | **Data received from Sponsor Blob** |
| --- | --- | --- | --- | --- | --- | --- |
| Opportunity | <br> | Opportunity | Object | <br> | <br> | <br> |
| Opportunity Record Type | 0126S000000yvuRQAQ | RecordTypeId | Record Type | When creating new opportunity | <br> | <br> |
| Opportunity Name | Name of company or plan name | Name | Text | When creating new opportunity | 1)Advisor Flow  <br>2)Plan Details Section  <br>3)About client Page as Business name | 1)Sponsor Flow  <br>2) Business Information Section  <br>3)Review business Page as Business Name |
| Sold Date | The go live date would be input here | Sold_Date__c | Date | When creating new or updating existing opportunity | Date to which we receive the Advisor data | Date to which we get the sponsor data |
| Lead Source | Digital Onboarding Experience | LeadSource | Picklist | When creating new opportunity | Will always be "Digital Onboarding Experience" |  |
| Close Date | Current date | CloseDate | Date | When creating new opportunity | Date to which we receive the Advisor data | Date to which we get the sponsor data |
| Total Plan Participants | If gathered, enter total participant count, otherwise default to 1 | Total_Plan_Participants__c | Number | When creating new opportunity | Default to 1 | Count when Plan Sponsor adds the Participant |
| Total Plan Assets | 0 | Total_Plan_Assets__c | Number | When creating new opportunity | Will always be 0 |  |
| Opportunity Owner | 0056S00000EuX3qQAF | OwnerId | Lookup(User) | When creating new opportunity | Will always be the same  i.e. "0056S00000EuX3qQAF" |  |
| Account Name | Broker dealer of the advisor. The ID will need to be pulled based on the BDs CRD. | AccountId | Lookup(Account) | When creating new opportunity | Broker dealer name | Broker dealer name |
| Company ID | Plan ID | Company_ID__c | Text | When creating new or updating existing. Will be used to match existing opportunities based on this unique ID | <br> | <br> |
| Type of Plan | <br>APIs for the different Types of plans below:<br>IKBFAMEX (Ameriprise BF)<br>IKBFOTHER (Ascensus BF)<br>IKBFPERSHING (Pershing BF)<br>IKBFJPMORGAN (JP Morgan BF)<br>IKFEEBASED (Ascensus Fee based Daily)<br>AMUNDIIK (Amundi Daily)<br>STATEFARMIK (State Farm Daily)<br>IKLEVCOMP50 (Level Comp Daily 50)<br> | Type_of_Plan__c | Picklist | When creating new or updating existing opportunity | The only API's we will use are Ameriprise BF, Ascensus BF, Pershing BF, JP Morgan BF and Ascensus Fee based Daily |  |
| Stage | APIs for the different Stages are below: | StageName | Picklist | When creating new or updating existing opportunity | In- Progress | Closed Won |
| [DOE FA First Name](https://pairetirementservices.lightning.force.com/lightning/setup/ObjectManager/Opportunity/FieldsAndRelationships/00NR7000005HrgA/view) | Advisors first name | DOE_FA_First_Name__c | Text(30) | This data will be filled when we do not have the broker dealer CRD/DETAILS for the Advisor CRD. | <br> | <br> |
| [DOE FA Last Name](https://pairetirementservices.lightning.force.com/lightning/setup/ObjectManager/Opportunity/FieldsAndRelationships/00NR7000005Hs2j/view) | Advisors last name | DOE_FA_Last_Name__c | Text(30) | <br> | <br> |  |
| [DOE FA Phone](https://pairetirementservices.lightning.force.com/lightning/setup/ObjectManager/Opportunity/FieldsAndRelationships/00NR7000005Hs5x/view) | Advisors phone number | DOE_FA_Phone__c | Phone | <br> | <br> |  |
| [DOE FA Email](https://pairetirementservices.lightning.force.com/lightning/setup/ObjectManager/Opportunity/FieldsAndRelationships/00NR7000005Hs4L/view) | Advisors email | DOE_FA_Email__c | Email | <br> | <br> |  |

#### Opportunity - Updating the opportunity based on Sponsor Blob

- The data will be updated once we received the data through the Sponsor blob.
- In the above table, details which needs to be updated in the opportunity while we get the sponsor blob are displayed.
- Once we have the Sponsor data, we will update the respective opportunity and close the opportunity.

#### Flow Diagram

The flow diagram is mainly for the plans which have advisor CRD.

For Amundi, State farm and Level comp - we will be directly creating the opportunity

*🚧 Gliffy diagram 'Salesflow CRM flow' replaced by image:*

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Salesforce-CRM-Integration-with-DOE-319228471/Salesflow%20CRM%20flow.png)

### Salesforce Integration for Group-2

For Group-2, we have four products that will be used, which are listed below. However, for all these products, we will not have any broker-dealer or advisor data. We will only have Plan Sponsor data.

- Sharebuilder IK
- Sharebuilder Group
- BAML IK
- BAML Group

Therefore, while integrating with Salesforce, the following data for the account will be hardcoded, and the same account will be used for the opportunity and contact creation.

#### Account for Group-2

**For BAML IK and Group**

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** |
| --- | --- | --- | --- | --- |
| Account | <br> | Account | Object | <br> |
| Default Account ID | 001R700000Vx1fmIAB | AccountID | Lookup(Account) | Used for all new BAML contacts being created through DOE |

**For Sharebuilder IK and Group**

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** |
| --- | --- | --- | --- | --- |
| Account | <br> | Account | Object | <br> |
| Default Account ID | 001R700000Vwj7oIAB | AccountID | Lookup(Account) | Used for all new Sharebuilder contacts being created through DOE |

#### Contact for Group-2

- Once we receive the data till "Tell us About your Business" page, we will have the ability to create a contact as well as opportunity.
- Contact will contain the plan sponsor information.

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** | **Data received when Plan sponsor fills data till "Tell me about your business"** | **Section in Data Dictionary (Column A)** | **UI Wireframe (Column W)** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Contact | <br> | Contact | Object | <br> | <br> | <br> | <br> |
| Contact Record Type | 012i0000000xnrRAAQ | RecordTypeId | Record Type | When creating new contact | <br> | <br> | <br> |
| First Name | Plan sponsors first name | FirstName | Text | When creating new contact | planContactFirstName | Plan Contact Info | Business Information |
| Last Name | Plan sponsors last name | LastName | Text | When creating new contact | planContactLastName | Plan Contact Info | Business Information |
| Account Name | Default Digital Onboarding Account, Call ID 001R700000Vx1fmIAB | AccountId | Lookup(Account) | When creating new contact | will always be the same | <br> | <br> |
| Telephone | Plan Sponsors phone number | Converted_Lead_Phone__c | Phone | When creating new contact | planContactPhoneNumber | Plan Contact Info | Business Information |
| Email | Plan Sponsors email | Email | Email | When creating new contact | planContactEmailAddress | Plan Contact Info | Business Information |
| Address | Plan Sponsors street address | MailingAddress | Address | When creating new contact | businessAddressLine1, businessAddressLine2 | Business Information | Business Information (Provide business information) |
| City | Plan Sponsors city | MailingAddress | Address | When creating new contact | businessAddressCity | Business Information | Business Information (Provide business information) |
| State | Plan Sponsors state | MailingAddress | Address | When creating new contact | businessAddressState | Business Information | Business Information (Provide business information) |
| Zip | Plan Sponsors zip | MailingAddress | Address | When creating new contact | businessAddressZipCode | Business Information | Business Information (Provide business information) |
| Tax number (EIN) | Plan Sponsors Business EIN, this is what will be used as their unique identifier | Tax_number__c | Text (15) | To match with existing contact, also needs to be added when created | businessEIN | Business Information | Business Information (Provide business information) |
| Contact Owner | 0056S00000EuX3qQAF | OwnerId | Lookup(User) | When creating new contact | will always be the same | <br> | <br> |
| Lead Source | Digital Onboarding Experience | LeadSource | Picklist | When creating new contact | will always be the same | <br> | <br> |
| Start Date | Establishment date/effective date | Start_Date__c | Date | When creating new or updating existing contact with new data | when the plan sponsor fills "Tell us about your business" page | <br> | <br> |

#### Opportunity for Group-2

##### Sharebuilder opportunity

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** | **Data received till "Tell Us about your business" Page** | **Data received from Sponsor Blob** | **Section in Unqork Data Dictionary (Column A)** | **UI Wireframe (Column W)** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Opportunity | <br> | Opportunity | Object | <br> | <br> | <br> | <br> | <br> |
| Opportunity Record Type | 0126S000001yS8XQAU | RecordTypeId | Record Type | When creating new opportunity | <br> | <br> | <br> | <br> |
| Opportunity Name | Name of company or plan name | Name | Text | When creating new opportunity (can also be updated if client updates business name) | businessname | businessname | Business Information | Business Information (Provide business information) |
| Sold Date | The go live date would be input here | Sold_Date__c | Date | When updating existing opportunity to sold | Blank | Date to which the sponsor finished the onboarding phase. | <br> | <br> |
| Lead Source | Digital Onboarding Experience | LeadSource | Picklist | When creating new opportunity | Will always be the same | <br> | <br> |  |
| Close Date | Current date | CloseDate | Date | When creating new opportunity | No date | Date to which we get the sponsor data | <br> | <br> |
| Total Plan Participants | Enter total participant count based on provided census | Total_Plan_Participants__c | Number | When creating new opportunity or updating existing (if they select "Skip Now" when first prompted to complete the census) | Default to 1 | Count when Plan Sponsor adds the Participant | <br> | <br> |
| Total Plan Assets | Default to zero if a start up, otherwise enter asset amount if provided for a conversion plan | Total_Plan_Assets__c | Number | When creating new opportunity or updating existing | The discussion for this is still in progress.   <br>If startup then this will be 0  <br>If conversion , Discussion in progress | <br> | <br> |  |
| Opportunity Owner | 0056S00000EuX3qQAF | OwnerId | Lookup(User) | When creating new opportunity | Will always be the same | <br> | <br> |  |
| Contact Name | Employer contact ID will need to be pulled based on the created plan sponsor contact | ContactId | Lookup(Account) | When creating new opportunity | Contact Role will be: Business Owner and Primary will be "True" | Contact Role will be: Business Owner and Primary will be "True" | <br> | <br> |
| Plan ID | Plan ID | Plan_ID__c | Text | When creating new or updating existing. Will be used to match existing opportunities based on this unique ID | Plan ID | Plan ID | Plan Info - General | not applicable |
| Type of Plan | APIs for the different Types of plans below: | Type_of_Plan__c | Picklist | When creating new or updating existing opportunity | <br> | <br> | <br> |  |
| <br> | Sharebuilder | <br> | <br> | <br> | Sharebuilder Group | Sharebuilder Group | <br> | <br> |
| <br> | Sharebuilder Individual(k) | <br> | <br> | <br> | Sharebuilder IK | Sharebuilder IK | <br> | <br> |
| Stage | APIs for the different Stages are below:  <br>In-Progress  <br>Closed Won | StageName | Picklist | When creating new or updating existing opportunity | In- Progress | Closed Won | <br> | <br> |
| Will this plan be Safe Harbor? | Add the appropriate Safe Harbor selection (opps default to Unknown if they haven't answered this yet)  <br>Yes  <br>No  <br>Not applicable | will_this_plan_be_safe_harbor__c | Picklist | When creating new or updating existing opportunity | <br> | For Group - safeHarborContribution  <br>For Ik Plans - "Not applicable" | Plan Info - ER Contributions | Contribution elections |
| Type | Select option based on if this is a new plan or a conversion plan  <br>Startup Plan  <br>Conversion Plan | Type | Picklist | When creating new opportunity | <br> | installationtype | <br> | <br> |
| Current Plan Provider (Other) | Input their current plan provider (only applicable if Conversion Plan) | Current_Plan_Provider_del__c | Test Area(255) | When creating new or updating existing opportunity | We do not have any information from UI to get this value. So we will not be accommodating this. | <br> | <br> |  |
| Account Name | Default Digital Onboarding Account, Call ID 001R700000Vx1fmIAB | AccountId | Lookup(Account) | When creating new opportunity | <br> | <br> | <br> | <br> |

##### BAML opportunity

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** | **Data received till "Tell Us about your business" Page** | **Data received from Sponsor Blob** | **Section in Unqork Data Dictionary (Column A)** | **UI Wireframe (Column W)** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Opportunity | <br> | Opportunity | Object | <br> | <br> | <br> | <br> | <br> |
| Opportunity Record Type | 0120H000001QWkMQAW | RecordTypeId | Record Type | When creating new opportunity | <br> | <br> | <br> | <br> |
| Opportunity Name | Name of company or plan name | Name | Text | When creating new opportunity (can also be updated if client updates business name) | businessname | businessname | Business Information | Business Information (Provide business information) |
| Sold Date | The go live date would be input here | Sold_Date__c | Date | When updating existing opportunity to sold | Blank | Date to which the sponsor finished the onboarding phase. | <br> | <br> |
| Lead Source | Digital Onboarding Experience | LeadSource | Picklist | When creating new opportunity | Will always be the same | <br> | <br> |  |
| Close Date | Current date | CloseDate | Date | When creating new opportunity | No date | Date to which we get the sponsor data | <br> | <br> |
| Total Plan Participants | Enter total participant count based on provided census | Total_Plan_Participants__c | Number | When creating new opportunity or updating existing (if they select "Skip Now" when first prompted to complete the census) | Default to 1 | Count when Plan Sponsor adds the Participant | <br> | <br> |
| Total Plan Assets | Default to zero if a startup plan, otherwise enter asset amount if provided for a conversion plan | Total_Plan_Assets__c | Number | When creating new opportunity or updating existing | The discussion for this is still in progress. | <br> | <br> |  |
| Opportunity Owner | 0056S00000EuX3qQAF | OwnerId | Lookup(User) | When creating new opportunity | Will always be the same | <br> | <br> |  |
| Contact Name | Employer contact ID will need to be pulled based on the created plan sponsor contact | ContactId | Lookup(Account) | When creating new opportunity | Contact Role will be: Business Owner and Primary will be "True" | Contact Role will be: Business Owner and Primary will be "True" | <br> | <br> |
| Plan ID | Plan ID | Plan_ID__c | Text | When creating new or updating existing. Will be used to match existing opportunities based on this unique ID | Plan ID | Plan ID | Plan Info - General | not applicable |
| Type of Plan | APIs for the different Types of plans below: | Type_of_Plan__c | Picklist | When creating new or updating existing opportunity | <br> | <br> | <br> | <br> |
| <br> | BAML Ascensus | <br> | <br> | <br> | BAML Group | BAML Group | <br> | <br> |
| <br> | BAML Ascensus Individual(k) | <br> | <br> | <br> | BAML IK | BAML IK | <br> | <br> |
| Stage | APIs for the different Stages are below:  <br>In-Progress  <br>Closed Won | StageName | Picklist | When creating new or updating existing opportunity | In-Progress | Closed Won | <br> | <br> |
| Marketing Start Date | Current date | Marketing_Start_Date__c | Date | When creating new opportunity | Blank | Date to which the sponsor finished the onboarding phase. | <br> | <br> |
| Merrill Edge FSA Name | If Merrill advisor was listed as a referral, enter their name | Merrill_Edge_FSA_Name__c | Text (25) | When creating new opportunity | The discussion for this is still in progress. | <br> | <br> |  |
| Will this plan be Safe Harbor? | Add the appropriate Safe Harbor selection (opps default to Unknown if they haven't answered this yet)  <br>Yes  <br>No  <br>Not applicable | will_this_plan_be_safe_harbor__c | Picklist | When creating new or updating existing opportunity | <br> | For Group - safeHarborContribution  <br>For Ik Plans - "Not applicable" | <br> | <br> |
| Type | Select option based on if this is a new plan or a conversion plan  <br>Startup Plan  <br>Conversion Plan | Type | Picklist | When creating new opportunity | <br> | installationtype | Plan Info - ER Contributions | Contribution elections |
| Current Plan Provider (Other) | Input their current plan provider (only applicable if Conversion Plan) | Current_Plan_Provider_del__c | Test Area(255) | When creating new or updating existing opportunity | We do not have any information from UI to get this value. So we will not be accommodating this. | <br> | <br> |  |
| Account Name | Default Digital Onboarding Account, Call ID 001R700000Vx1fmIAB | AccountId | Lookup(Account) | When creating new opportunity | Will always be the same | <br> | <br> |  |

#### **Enhancements for Group 2**

There are changes which are made for Contact and opportunity with respect to Group-2. Below are the data for the same.

##### **Addition of fields in contact**

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** | **Data received from blob - Propertyid** | **Section in Unqork Data Dictionary (Column A)** | **UI Wireframe (Column W)** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Auto enrollment | checklist to be provided for a Yes/No option | Auto_Enrollment__c | (checkbox) | This is a checkbox that should be automatically selected based on the Plan Sponsor's response in the UI—either 'Yes' or 'No'.  <br>  <br>The Boolean value needs to send across as a Boolean. True (checked) = Yes, Auto Enrollment, False (unchecked) = No Auto Enrollment. Upon opportunity creation, this will default to “false”, so nothing needs to be passed until the client makes their election. | automaticEnrollment | Plan Info - Auto Enrollment | Auto enrollment |
| Profit sharing selection | Picklist which will have the following data   <br>1. Salary Proportionate (Pro Rata)  <br>2. New Comparability  <br>3. Social Security Integrated  <br>4. Age weighted   <br>5. None | Profit_Sharing__c | picklist | The picklist will be false when the opportunity is created, however when the plan sponsor makes an election, pass the value as selected by the plan sponsor. | profitSharingAllocationFormula | Plan Info - ER Contributions | Contribution elections |

##### Addition of fields in opportunity

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** | **Data received from blob - Propertyid** | **Section in Unqork Data Dictionary (Column A)** | **UI Wireframe (Column W)** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Auto enrollment | checklist to be provided for a Yes/No option | Auto_Enrollment__c | (checkbox) | This is a checkbox that should be automatically selected based on the Plan Sponsor's response in the UI—either 'Yes' or 'No'.  <br>  <br>The Boolean value needs to send across as a Boolean. True (checked) = Yes, Auto Enrollment, False (unchecked) = No Auto Enrollment. Upon opportunity creation, this will default to “false”, so nothing needs to be passed until the client makes their electon. | automaticEnrollment | Plan Info - Auto Enrollment | Auto enrollment |
| Profit sharing selection | Picklist which will have the following data   <br>1. Salary Proportionate (Pro Rata)  <br>2. New Comparability  <br>3. Social Security Integrated  <br>4. Age weighted   <br>5. None | Profit_Sharing__c | picklist | The picklist will be false when the opportunity is created, however when the plan sponsor makes an election, pass the value as selected by the plan sponsor. | profitSharingAllocationFormula | Plan Info - ER Contributions | Contribution elections |

##### **Changes in Opportunity**

| **Field Name** | **Data entry** | **old API** | **New API** | **Field in the DD** |
| --- | --- | --- | --- | --- |
| How did you hear about us ? | List will include  <br>This is a single select field  <br>  <br>Bank/Branch associate  <br>Bank/Branch flyer  <br>[BankOfAmerica.com/MerrillEdge.com](http://BankOfAmerica.com/MerrillEdge.com)  <br>Other | Referred_By__c | Leadsource | salesReferralSource |
| Merrill Edge FSA Name | If the user selects Bank/Branch associate or Other- Plan sponsor will have ability to add name. This is a text field. | Merrill_Edge_FSA_Name__c | Web_Submission_Type__c | <br>If below is selected<br>**Bank/Branch associate** - salesReferralDetailName<br>**Other**  - salesReferralDetailOther<br> |

### **Salesforce Integration for Group 2.2**

For Group 2.2, we have two types of products those are

1. Products without Advisor
  1. Balance Forward
  2. American Funds Employer Direct
  3. Vanguard employer direct
  4. Copilot employer direct
2. Products with Advisor
  1. American Funds Advisor
  2. Copilot Advisor
  3. Raymond James Advisor

For Accounts without Advisor, Salesforce has provided with default accounts which are based on the product type.

#### **Account for Group 2.2**

##### Account details without Advisor

Default account will be provided for Account without advisor.

These defaults will be based on product type.

**For CoPilot Employer Direct and American Funds Employer direct**

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** |
| --- | --- | --- | --- | --- |
| Account | <br> | Account | Object | <br> |
| Default Account ID | 001R700000dKzVWIA0 | AccountID | Lookup(Account) | Used for all new CoPilot Employer and American Funds employer direct contacts being created through DOE |

**For Vanguard Employer Direct**

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** |
| --- | --- | --- | --- | --- |
| Account | <br> | Account | Object | <br> |
| Default Account ID | 001R700000dQ9SbIAK | AccountID | Lookup(Account) | Used for all new Vanguard Employer contacts being created through DOE |

**For Balance Forward**

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** |
| --- | --- | --- | --- | --- |
| Account | <br> | Account | Object | <br> |
| Default Account ID | 001R700000emFVZIA2 | AccountID | Lookup(Account) | Used for all new ER contacts being created through DOE |

##### **Accounts with Advisor**

For product with Advisor, we will be entering the broker dealer information. The data is similar to that we have for Group-1. However the details are as below for the products with Advisor for both IK and Group

These will be for

1. American Funds Advisor
2. Copilot Advisor
3. Raymond James Advisor

| **Field Name** | **Data Entry** | **API** | **Data Type** | **When to use** | **Data received from blob - Propertyid** | **Section in Unqork Data Dictionary (Column A)** | **UI Wireframe (Column W)** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Account | <br> | Account | Object | <br> | <br> | <br> | <br> |
| Record Type ID | 012i0000000VCx3AAG | RecordTypeId | Record Type | When creating new account, | <br> | <br> | <br> |
| Account Name | Name of broker dealer | Name | Name | When creating new account | advisorDealerName | Advisor Information | Advisor Landing Page  <br>Advisor Information Page |
| CRD Number | CRD of BD | CRD_Number__c | Text | To match with existing account, also needs to be added when created | advisorDealerCRDNumber | Advisor Information | Advisor Landing Page  <br>Advisor Information Page |
| Account Owner | 0056S00000EuX3qQAF | OwnerId | Lookup(User) | When creating new account | <br> | <br> | <br> |
| Account ID | Created automatically for new accounts, needs to be called for existing accounts based on the CRD | AccountID | Lookup(Account) | Called when existing account CRD match is found | <br> | <br> | <br> |
| Default Account ID | 001R700000TtLntIAF (production), 001Ec00000vUb6aIAC (sandbox) | AccountID | Lookup(Account) | Called when advisor isn't associated with an Account with a CRD | <br> | <br> | <br> |

#### **Contact Creation Process**

There are two approaches for creating a Contact:

1. **Contact Creation for Products with an Advisor**    When the product includes an assigned Advisor, the Advisor’s information will be added to the Contact record.
2. **Contact Creation for Products without an Advisor**    For products that do not have an Advisor, the Plan Sponsor’s information will be added to the Contact record instead.

**Table for data of Contact Creation without advisor**

The data is similar to what we did for Group 2. It contains the Plan sponsor information.

Please refer to [Contact for Group-2](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Salesforce-CRM-Integration-with-DOE-319228471.aspx)

**Table for data of contact creation with advisor**

The data is similar to what we had for Group-1. It contains the Broker dealer information.

| **Field Name** | **Data Entry** | **API** | **Data Type** | **Data received from blob - Propertyid** | **Section in Unqork Data Dictionary (Column A)** | **UI Wireframe (Column W)** |
| --- | --- | --- | --- | --- | --- | --- |
| Contact | <br> | Contact | Object | <br> | <br> | <br> |
| Contact Record Type | 0120H000001QVtdQAG | RecordTypeId | Record Type | <br> | <br> | <br> |
| First Name | Advisors first name | FirstName | Text | advisorFirstName | Advisor Information | Advisor Landing Page  <br>Advisor Information Page |
| Last Name | Advisors last name | LastName | Text | advisorLastName | Advisor Information | Advisor Landing Page  <br>Advisor Information Page |
| Account Name | Broker dealer of the advisor. The ID will need to be pulled based on the BDs CRD | AccountId | Lookup(Account) | <br> | <br> | <br> |
| Telephone | Advisors phone number | Converted_Lead_Phone__c | Phone | advisorPhoneNumber | Advisor Information | Advisor Landing Page  <br>Advisor Information Page |
| Email | Advisors email | Email | Email | advisorEmailAddress | Advisor Information | Advisor Landing Page  <br>Advisor Information Page |
| Firm Address | Advisors street address | Firm_address__c | Text | advisorPaymentAddress1, advisorPaymentAddress2 | Advisor Information | Advisor Payment Info - Payment Contact info - CHECK IF WE GET THIS IN IK |
| Firm City | Advisors city | Firm_city__c | Text | advisorPaymentCity | Advisor Information | Advisor Payment Info - Payment Contact info - CHECK IF WE GET THIS IN IK |
| Firm State | Advisors state | Firm_state__c | Text | advisorPaymentState | Advisor Information | Advisor Payment Info - Payment Contact info - CHECK IF WE GET THIS IN IK |
| Firm Zip | Advisors zip | Firm_ZIP__c | Text | advisorPaymentZip | Advisor Information | Advisor Payment Info - Payment Contact info - CHECK IF WE GET THIS IN IK |
| FA CRD Number | <br>Advisors CRD (different than their account CRD, which belongs to their BD)<br>To match with existing contact, also needs to be added when created<br> | FA_CRD_Number__c | Text | advisorCRDNumber | <br> | <br> |
| Contact Owner | 0056S00000EuX3qQAF | OwnerId | Lookup(User) | <br> | <br> | <br> |
| Lead Source | Digital Onboarding Experience | LeadSource | Picklist | <br> | <br> | <br> |

#### **Opportunity Creation Process**

**Most of the fields are the same like we had for Group-2. The newly introduced fields or fields where there is an updated are below**

##### **For Products without Advisor both IK and Group**

| **Field Name** | **Data Entry** | **API** | **Data Type** | **Section in Data Dictionary (Column A) with propertyid** | **UI Wireframe (Column W)** | **Data for Copilot** | **American funds** | **Vanguard** | **Direct BF** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Opportunity | <br> | Opportunity | Object | <br> | <br> | <br> | <br> | <br> | <br> |
| Opportunity Record Type | 0126S000000yvuMQAQ | RecordTypeId | Record Type | <br> | <br> | 0126S000000yvuMQAQ | 0126S000001BDFQQA4 | 012R7000002ei4PIAQ | 0126S000000yvuRQAQ |
| Opportunity Name | Name of company or plan name | Name | Text | businessname | businessname | <br> | <br> | <br> | <br> |
| Sold Date | The go live date would be input here | Sold_Date__c | Date | Blank | Date to which the sponsor finished the onboarding phase. | <br> | <br> | <br> | <br> |
| Lead Source | See Sheet 3 | LeadSource | Picklist | <br> | salesReferralSource | See Sheet 3 | See Sheet 3 | Current VG IK Client | See Sheet 3 |
| Secondary Lead Source | Pull in free form data | Web_Submission_Type__c | <br> | <br> | <br> | Pull in free form data | Pull in free form data | NA | Pull in free form data |
| Close Date | Current date | CloseDate | Date | No date | Date to which we finish the onboarding experience | <br> | Current date | <br> | <br> |
| Total Plan Participants | Enter total participant count based on provided census | Total_Plan_Participants__c | Number | Default to 1 | Count when Plan Sponsor adds the Participant | <br> | <br> | <br> | <br> |
| Total Plan Assets | Default to zero if a startup plan, otherwise enter asset amount if provided for a conversion plan | Total_Plan_Assets__c | Number | <br> | <br> | <br> | <br> | <br> | <br> |
| Opportunity Owner | 0056S00000EuX3qQAF | OwnerId | Lookup(User) | <br> | <br> | 0056S00000EuX3qQAF | 0056S00000EuX3qQAF | 0056S00000EuX3qQAF | 0056S00000EuX3qQAF |
| Contact Name | Employer contact ID will need to be pulled based on the created plan sponsor contact | ContactId | Lookup(Account) | <br> | <br> | <br> | <br> | <br> | <br> |
| Plan ID | Plan ID | Plan_ID__c | Text | Plan ID | Plan ID | <br> | <br> | <br> | <br> |
| Type of Plan | APIs for the different Types of plans below: | Type_of_Plan__c | Picklist | <br> | <br> | APIs for the different Types of plans below:  <br>1. CoPilot 0 Hybrid Ascensus  <br>2. CoPilot 0 Passive Ascensus  <br>3. CoPilot 0 Hybrid Ascensus Individual(k)  <br>4. CoPilot 0 Passive Ascensus Individual(k) | American Funds 0 CoPilot Ascensus Individual(k) | ASCESVGRIA (Ascensus featuring Vanguard) | IKBFOTHER (Ascensus BF) |
| Stage | APIs for the different Stages are below:  <br>In-Progress  <br>Waiting for Signature  <br>Closed Won | StageName | Picklist | <br> | <br> | <br> | <br> | <br> | <br> |
| Will this plan be Safe Harbor? | Add the appropriate Safe Harbor selection (opps default to Unknown if they haven't answered this yet)  <br>Yes  <br>No  <br>Not applicable | will_this_plan_be_safe_harbor__c | Picklist | <br> | <br> | <br> | <br> | <br> | <br> |
| Type | Select option based on if this is a new plan or a conversion plan  <br>Startup Plan  <br>Conversion Plan | Type | Picklist | <br> | <br> | <br> | <br> | <br> | <br> |
| Current Plan Provider (Other) | Input their current plan provider (only applicable if Conversion Plan) | Current_Plan_Provider_del__c | Test Area(255) | <br> | <br> | <br> | <br> | Call ID 0016S00003OYdmmQAD | <br> |
| Account Name | Default Digital Onboarding Account, Call ID 001R700000dKzVWIA0 | AccountId | Lookup(Account) | <br> | <br> | Default Digital Onboarding Account, Call ID 001R700000dKzVWIA0 | Default Digital Onboarding Account, Call ID 001R700000dKzVWIA0 | Default Digital Onboarding Account, Call ID 001R700000dQ9SbIAK | Default Digital Onboarding Account, Call ID 001R700000emFVZIA2 |
| Asset summary | Link the URL from Cliff | Asset_Summary__c | URL(255) | <br> | <br> | <br> | <br> | <br> | <br> |
| Auto enrollment | True = Auto Enrollment, False = No Auto Enrollment | Auto_Enrollment__c | Checkbox | <br>automaticEnrollment<br>Plan Info - Auto Enrollment<br> | Auto enrollment | <br> | <br> | <br> | <br> |
| Profit sharing selection | Select the appropriate profit sharing option based on the clients election  <br>Salary Proportionate (Pro Rata)  <br>Social Security Integrated  <br>Age Weighted  <br>New Comparability | Profit_Sharing__c | Picklist | <br>profitSharingAllocationFormula<br>Plan Info - ER Contributions<br> | Contribution elections | <br> | <br> | <br> | <br> |

For leadsource they would be asked

| How did you hear about us? |
| --- |
| Google/Web Search |
| Financial Advisor |
| Financial Institution |
| CPA |
| Publication |
| Payroll Provider |
| Other |
