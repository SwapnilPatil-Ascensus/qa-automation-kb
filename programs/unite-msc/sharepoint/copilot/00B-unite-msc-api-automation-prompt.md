PART B of 4. Edit the existing SharePoint page "Unite MSC API Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Keep each diagram in one full-width monospace block, character for character; never redraw it.

APPEND EXACTLY:

## Site map
Render the site map as a Quick Links web part in tile or grid layout, then repeat the same eleven children in a table so the page still reads if tiles cannot be linked yet.

Unite MSC API Automation
├── 01 KT and Onboarding
├── 02 Architecture and Ownership
├── 03 Access, Setup and Environments
├── 04 Daily Run Playbook
├── 05 Mobile 1 Automation
├── 06 Mobile 2 Automation
├── 07 Enrollment Automation
├── 08 Coverage, Traceability and Sign-off
├── 09 Reporting and Troubleshooting
├── 10 Test Data, DB Refresh and Security
└── 11 Extend the Automation

| Page | What it is for |
|---|---|
| 01 KT and Onboarding | Install, clone, IDE, Oracle overlay, profiles, first runs, Bruno, standards |
| 02 Architecture and Ownership | Framework, inheritance, config layers, reporting, L1-L5 boundary |
| 03 Access, Setup and Environments | Access routes, secure local config, environment selection and proof |
| 04 Daily Run Playbook | Choose/run a suite, inspect report, classify and preserve evidence |
| 05 Mobile 1 Automation | 26/26 operations, auth/data model, suite split, execution and evidence |
| 06 Mobile 2 Automation | 24/25 business coverage, fixtures, suite split, execution and evidence |
| 07 Enrollment Automation | 25/28 catalog, encrypted ordered wizard and subsequent enrollment |
| 08 Coverage, Traceability and Sign-off | 75 operations, 83-row legacy comparison, evidence and exclusions |
| 09 Reporting and Troubleshooting | Portal/Surefire outputs, first-failure classifier, safe reruns |
| 10 Test Data, DB Refresh and Security | Oracle fixtures, refresh recovery, L5 boundary and security |
| 11 Extend the Automation | New-endpoint implementation playbook and reusable prompt library |

## Platform at a glance
Render this diagram as a full-width monospace block, exactly as written:

            Unite MSC API automation (one canonical platform)
                                |
        +-----------------+-----+-----------+
        |                 |                 |
    Mobile 1          Mobile 2          Enrollment
  auth + session    account exp.    encrypted wizard
        |                 |                 |
        +--------+--------+--------+--------+
                 |                 |
        jsonapi-core framework   Oracle test data
                 |
   TestNG suite XML -> branding: okdirect | newyork | nmdirect
                 |
   HTML reporting portal -> evidence for triage and sign-off

Mobile 2 reuses Mobile 1 authentication. Enrollment adds certificate-based encryption and an ordered session chain. Page 02 shows how each module reaches the BFF and the downstream services behind it.

Republish the page when finished.
