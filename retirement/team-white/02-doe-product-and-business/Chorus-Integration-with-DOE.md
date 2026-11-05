# Chorus Integration with DOE

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Chorus-Integration-with-DOE-305976180.aspx) | Created: 2025-02-24 | Last modified: 2025-03-13 | Author: Franklin Zabala | Last editor: Shankar Satijani

---

#### **Links:**

- Chorus Workflow Home
  - [https://ascensus0.sharepoint.com/sites/ChorusWorkflow?web=1](https://ascensus0.sharepoint.com/sites/ChorusWorkflow?web=1)
- Concepts
  - Common Terms
    - [Chorus BPM - Definitions of Acronyms and Common Terms.pdf](https://ascensus0.sharepoint.com/:b:/r/sites/ChorusWorkflow/User%20Utilization%20Guides/Chorus%20BPM%20-%20Definitions%20of%20Acronyms%20and%20Common%20Terms.pdf?csf=1&web=1&e=qrG6JC)
  - Business Area
    - [Chorus Business Area Definitions.pdf](https://ascensus0.sharepoint.com/:b:/r/sites/ChorusWorkflow/User%20Utilization%20Guides/Chorus%20Business%20Area%20Definitions.pdf?csf=1&web=1&e=Tj1Ld3)
  - Work Type:
    - [Work Type Inventory](https://ascensus0.sharepoint.com/:x:/r/sites/ChorusWorkflow/_layouts/15/Doc.aspx?sourcedoc=%7b3964D3DB-E5D5-437B-A96D-1B4D59E0549B%7d&file=CHORUS%20WORK%20TYPE%20DEFINITIONS.xlsx&action=default&mobileredirect=true)
  - Status
    - [Status Definitions](https://ascensus0.sharepoint.com/:x:/r/sites/ChorusWorkflow/_layouts/15/Doc.aspx?sourcedoc=%7b3964D3DB-E5D5-437B-A96D-1B4D59E0549B%7d&file=CHORUS%20WORK%20TYPE%20DEFINITIONS.xlsx&action=default&mobileredirect=true)
  - Queue
    - [Queue Definitions](https://ascensus0.sharepoint.com/:x:/r/sites/ChorusWorkflow/Process%20Documents/CHORUS%20WORK%20TYPE%20DEFINITIONS.xlsx?d=w3964d3dbe5d5437ba96d1b4d59e0549b&csf=1&web=1&e=jmlXGL)
- Process Documents:
  - [https://ascensus0.sharepoint.com/sites/ChorusWorkflow/Process%20Documents/Forms/AllItems.aspx](https://ascensus0.sharepoint.com/sites/ChorusWorkflow/Process%20Documents/Forms/AllItems.aspx)
- Learning Materials
  - Introduction to Chorus (30 minutes)
    - [https://360.articulate.com/review/content/6e30238a-2f02-458c-bb1f-0f5350693b66/review](https://360.articulate.com/review/content/6e30238a-2f02-458c-bb1f-0f5350693b66/review)
  - New Micro learning topics:
    - Focus on Chorus: Processor Workspace (10 minutes)
      - This chapter focuses on how to navigate the processor workspace.
      - [https://360.articulate.com/review/content/c6b53832-40ad-440f-84a9-56a70616847c/review](https://360.articulate.com/review/content/c6b53832-40ad-440f-84a9-56a70616847c/review)
    - Focus on Chorus: System Structure and Workflow (10 minutes)
      - This chapter goes into more detail around the system structure and process workflow in Chorus.
      - [https://360.articulate.com/review/content/e08d4246-9dfa-4958-8fe3-54ae5fe1c6aa/review](https://360.articulate.com/review/content/e08d4246-9dfa-4958-8fe3-54ae5fe1c6aa/review)
    - Focus on Chorus: Work Objects (15 minutes)
      - This chapter goes into more detail around the system structure and process workflow in Chorus.
      - [https://360.articulate.com/review/content/b3a323ba-305f-4587-ae17-784db06dc1e1/review](https://360.articulate.com/review/content/b3a323ba-305f-4587-ae17-784db06dc1e1/review)
    - Focus on Chorus: Worklist Card & Document Delivery (15 minutes)
      - This chapter goes into more detail around the system structure and process workflow in Chorus.
      - [https://360.articulate.com/review/content/e22c0c9a-7444-4e9d-adba-be51fd624b7f/review](https://360.articulate.com/review/content/e22c0c9a-7444-4e9d-adba-be51fd624b7f/review)
    - Focus on Chorus: Search Card (15 minutes)
      - This chapter goes into more detail around the system structure and process workflow in Chorus.
      - [https://360.articulate.com/review/content/1a40331d-21e5-4a9e-b1e2-b6ddd9febcd4/review](https://360.articulate.com/review/content/1a40331d-21e5-4a9e-b1e2-b6ddd9febcd4/review)
    - Focus on Chorus: Create Card (25 minutes)
      - This chapter goes into more detail around the system structure and process workflow in Chorus.
      - [https://360.articulate.com/review/content/ec9c5786-e98d-401e-9f39-47cd03b9e760/review](https://360.articulate.com/review/content/ec9c5786-e98d-401e-9f39-47cd03b9e760/review)

##### **Research Findings**

We have found two approaches we can use for integration with Chorus

- Soap API
- RESTful API

We had a discussion with the Chorus Team, and it was discussed that Chorus Integration using RESTfulAPI is the preferred way as this is the latest. Some teams have already implemented for integration with Chorus.
One example we found was for the application **ComplianceTest.ChorusCommunication**  which was developed by Team Spartans.

Git Repo: [http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/ComplianceTest.ChorusCommunication](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/ComplianceTest.ChorusCommunication)

We also found on the confluence a POC which was done by them.

[POC - Chorus Endpoint Implementation And Create Work Item - Team Spartans (Satellite) - Ascensus - Confluence](https://ascensus0.sharepoint.com/sites/TeamSpartansCF/SitePages/STS-POC---Chorus-Endpoint-Implementation-And-Create-Work-Item-273583068.aspx)

We could refer the code of the above-mentioned Git repo and POC and can use it in our DOE integration with Chorus.

Chorus RESTful API Documentation: [https://d12filxzewqx4c.cloudfront.net/chorus-restful/chorus-restful.html](https://d12filxzewqx4c.cloudfront.net/chorus-restful/chorus-restful.html)

**Next Steps**

- Understand the Chorus concepts
  - Case vs WorkItem vs UpdateItem
- We also need to request Chorus Team to create a dedicated user account for Digital Onboarding for test and production environments.
- We will require the values for the following parameters from the Chorus Team to uniquely identify that a particular Chorus Work Item Creation Request is triggered from the DOE
  - API Pass
  - Business Area - Mostly set as "INSTLRTMNT" which represents Institutional Retirement
  - Work Type
  - Status - Status of the Work Item. Example "CREATED"
  - Queue - example: "PRIMARY"
  - Plan ID
  - FieldValues (array)
  - Assignee Information? - Corresponds to user that has the workitem assigned (this can be blank)
  - Install Type?
- We probably need to create new events which will trigger the creation of a new Chorus Item from the DOE, currently the list of events which are mentioned on the below confluence page does not list's any specific event for Onboarding      [ARK to CHORUS API Call for Web Initiated Transactions - Shared Documentation - Ascensus - Confluence](https://ascensus0.sharepoint.com/sites/Confluence-Test4/SitePages/GLOBAL-ARK-to-CHORUS-API-Call-for-Web-Initiated-Transactions-244655770.aspx)

#### Business Questions:

- When to submit **work item**
  - What stage of the Onboarding workflow to submit a work item
    - Create Onboarding Record
    - Submit Advisor Flow Data
    - Submit Sponsor Flow Data
    - Stage Plan Document
    - Initialize Onboarding Workflow
    - ARK Integration (write to ARK)
      - Create Plan ID
      - Initialize Recordkeeping System
      - Initialize Plan Defaults
      - Establish Plan
    - CLIFF Integration (archive Plan Document)
  - Scenarios
    - What onboarding issues are you interested in knowing?
      - Missing CRD?
      - An EIN with an existing ARK plan trying to create a new plan?
      - Investment fund selected during onboarding but is no longer active or available during "write to ark"

#### Tech Questions:

- Integration
  - 2-Way communication? We submit a work item and wait for response and do something with it?
  - Or is it fire and forget?

#### Chorus Links:

- Chorus Training
  - [Chorus Training Resources - RPS-QRP Product - Ascensus - Confluence](https://ascensus0.sharepoint.com/sites/RPS-QRPProduct/SitePages/RPQRP-Chorus-Training-Resources-283908142.aspx)
- Chorus create WorkItems and Get Data
  - [https://confluence.ascensus.com/display/TMSF/Chorus+Data](https://confluence.ascensus.com/display/TMSF/Chorus+Data)
