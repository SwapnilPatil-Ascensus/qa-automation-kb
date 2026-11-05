# Cliff - Importing Documents

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Cliff---Importing-Documents-294982977.aspx) | Created: 2024-12-09 | Last modified: 2024-12-31 | Author: Franklin Zabala | Last editor: Chris Reynolds

---

Cliff UI:

- DEV: [http://cliff.dev.internal.ascensus.com/edms/login.aspx](http://cliff.dev.internal.ascensus.com/edms/login.aspx)
-
  - Username: brsd\imaging_adm_dev
  - Password: [REDACTED]
- QA: [http://cliff.qa.internal.ascensus.com/edms/login.aspx](http://cliff.qa.internal.ascensus.com/edms/login.aspx)
-
  - Username: brsd\imaging_adm_qa
  - Password: [REDACTED]
- PRO: [https://cliff.internal.ascensus.com/EDMS/Main.aspx?DataSource=EDMS](https://cliff.internal.ascensus.com/EDMS/Main.aspx?DataSource=EDMS)

Cliff has a SOAP service that can be referenced directly by a configured user:

- CLIFF AxServicesInterface:
  - DEV: [http://cliff.dev.internal.ascensus.com/edms/AxServicesInterface.asmx](http://cliff.dev.internal.ascensus.com/edms/AxServicesInterface.asmx)
  - QA: [http://cliff.qa.internal.ascensus.com/edms/AxServicesInterface.asmx](http://cliff.qa.internal.ascensus.com/edms/AxServicesInterface.asmx)
  - PRO: [http://cliff.internal.ascensus.com/edms/AxServicesInterface.asmx](http://cliff.internal.ascensus.com/edms/AxServicesInterface.asmx)

Ascensus has two different services that act as wrappers around the SOAP service:

- [Cliff.DocumentManagement](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Cliff.DocumentManagement) (old)
-
  - The original that most applications reference
  - Swagger
  -
    - DEV: [https://cliff-api-dev.ascensus.com/swagger/index.html](https://cliff-api-dev.ascensus.com/swagger/index.html)
    - QA: [https://cliff-api-qa.ascensus.com/swagger/index.html](https://cliff-api-qa.ascensus.com/swagger/index.html)
    - PRO: [https://cliff-api.ascensus.com/swagger/index.html](https://cliff-api.ascensus.com/swagger/index.html)
- [DocumentManagement.Cliff](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/DocumentManagement.Cliff) (new)
-
  - Team Platinum
  - A clone of the original with enhanced logging
  - Only used by DocumentManagement.Statement currently
  - Swagger
  -
    - DEV: [https://internal-api-dev.ascensus.com/documentmanagement/cliff/swagger/index.html](https://internal-api-dev.ascensus.com/documentmanagement/cliff/swagger/index.html)
    - QA: [https://internal-api-qa.ascensus.com/documentmanagement/cliff/swagger/index.html](https://internal-api-qa.ascensus.com/documentmanagement/cliff/swagger/index.html)
    - PRO: [https://internal-api.ascensus.com/documentmanagement/cliff/swagger/index.html](https://internal-api.ascensus.com/documentmanagement/cliff/swagger/index.html)

When documents are added to Cliff, they are associated with an *application* .  The application determines where the document will be found in Cliff.  The document ID also seems to be unique to the document within an *application* .  The wrapper services have separate controllers for each *application* that they handle.

We may need to add our own controller to the wrapper if we need to use a specific application that is not readily available (for example, "NEW_BUSINESS").  This would likely just be a copy of an existing controller with minor tweaks.  (It sounds like we will be using "DOCUMENT_MANAGEMENT" so may not need to build anything new here)

### Questions

1. Where will the new Onboarding documents that we will be uploading into CLIFF be placed?
  1. Application = "**DOCUMENT_MANAGEMENT** "
2. Are there any other specific attribute values that should be used for the Onboarding documents?
  1. **These will be provided once they are known**
  2. Common properties set in import request:
    1. DocStatus = "INDEX" ?
    2. ReceiptType = "IMPORTED" ?
    3. Department = "INDIVIDUAL K" ?
    4. BusinessUnit = "PSG" ?
    5. TransactionType = "PLAN EST KIT" ?
    6. DocumentType = "PEK" ?
  3. When receiving advisor approved signed document(s)
    1. TBD for specific values
  4. When receiving sponsor approved signed document(s)
    1. TBD for specific values
3. Is anything needed for Chorus to be alerted when our documents are imported?
  1. **Team Gold is working on an API between Chorus and Cliff**  to provide features like directly referencing documents or images.  This could be helpful once we understand more about what we'll need in Chorus.   [https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/602154](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/602154)
