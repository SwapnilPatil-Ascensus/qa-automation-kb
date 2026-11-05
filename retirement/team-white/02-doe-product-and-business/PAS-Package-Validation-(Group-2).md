# PAS Package Validation (Group 2)

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-PAS-Package-Validation-(Group-2)-341947634.aspx) | Created: 2025-09-16 | Last modified: 2025-09-19 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

There is logic in place in Onboarding.Messaging.Api (Onboarding.Messaging.Api.Domain.Engine.PasPackageValidationEngine) which will ensure that we have received all documents we expect from PAS.  Document expectations are defined in *appsettings.json*  (*PASExpectedDocuments*  section), using rules as listed in the data dictionary.

Several flags were introduced to aid in testing:

- **EnableValidation**
  - This is essentially a feature flag that can toggle the PAS package validation logic in its entirety.
  - It is expected to be TRUE in production.
- **BypassExceptionFailure**
  - This flag will bypass the exception that is thrown when one or more expected documents are missing but will continue to log the exception as a warning.
  - It is expected to be FALSE in production, which will prevent the documents from being staged into the PASDocument table when one or more expected documents are missing, and will instead set InitializePlanDocumentsCmdState to failed status.

### Document Requirements (as of 9/16/2025)

#### BAMLDailyIKNoAdv

**Required Documents:**

- Adoption Agreement
- Basic Plan Document(s)
- Recordkeeping Service Agreement SA
- Trust-Custodial Agreement - HC

#### ShareBuilderDailyIKNoAdv

**Required Documents:**

- Adoption Agreement
- Basic Plan Document(s)
- Recordkeeping Service Agreement SA
- Custodial Agreement - HC

#### BAMLDailyGroup

**Required Documents:**

- Adoption Agreement
- SPDs & SMMs
- Basic Plan Document(s)
- Automatic Rollover Notice
- Recordkeeping Service Agreement SA
- Trust Agreement - HC

**Optional Documents (may or may not appear, not sure on the condition in PAS):**

- Adoption Agreement - Non-Signature Documents

**Conditionally Required Documents:**

- 401(k) Safe Harbor Contribution Notice
  - Condition Field: *safeHarborContribution*
  - Condition Values: true
- 401(k) Notice of Eligible Automatic Contribution Arrangement (EACA)
  - Condition Field: *automaticEnrollmentType*
  - Condition Values: "EACA"
- 401(k) Notice of Automatic Contribution Arrangement (ACA)
  - Condition Field: *automaticEnrollmentType*
  - Condition Values: "ACA"
- Discretionary Matching Contribution Notice
  - Condition Field: *employerMatchFormulaType*
  - Condition Values: "Discretionary"
- Discretionary Matching Contribution Plan Administrator and Trustee Notice
  - Condition Field: *employerMatchFormulaType*
  - Condition Values: "Discretionary"
- Cross-tested Trustee Contribution Notice
  - Condition Field: *profitSharingAllocationFormula*
  - Condition Values: "New comparability" or "Age weighted"

#### ShareBuilderDailyGroup

**Required Documents:**

- Adoption Agreement
- SPDs & SMMs
- Basic Plan Document(s)
- Automatic Rollover Notice
- Recordkeeping Service Agreement SA
- Custodial Agreement - HC
- Automatic IRA Rollover Service Agreement

**Optional Documents (may or may not appear, not sure on the condition in PAS):**

- Adoption Agreement - Non-Signature Documents

**Conditionally Required Documents:**

- 401(k) Safe Harbor Contribution Notice
  - Condition Field: *safeHarborContribution*
  - Condition Values: true
- 401(k) Notice of Eligible Automatic Contribution Arrangement (EACA)
  - Condition Field: *automaticEnrollmentType*
  - Condition Values: "EACA"
- 401(k) Notice of Automatic Contribution Arrangement (ACA)
  - Condition Field: *automaticEnrollmentType*
  - Condition Values: "ACA"
- Discretionary Matching Contribution Notice
  - Condition Field: *employerMatchFormulaType*
  - Condition Values: "Discretionary"
- Discretionary Matching Contribution Plan Administrator and Trustee Notice
  - Condition Field: *employerMatchFormulaType*
  - Condition Values: "Discretionary"
- Cross-tested Trustee Contribution Notice
  - Condition Field: *profitSharingAllocationFormula*
  - Condition Values: "New comparability" or "Age weighted"
