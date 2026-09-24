PART B of 2. Edit the existing SharePoint page "08 Coverage, Traceability and Sign-off" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## How to trace an endpoint
1. Pick the endpoint ID in the module register.
2. Open the canonical Java class and method.
3. Confirm its suite XML and Maven profile.
4. Confirm the manual request in the Unite MSC Bruno collection where one exists: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads
5. Confirm the manual case in qTest Test Design: https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign
6. Link the case to the appropriate story under Unite MSC Epic QA-796: https://ascensuscollegesavings.atlassian.net/browse/QA-796
7. Open the sign-off document for scope and exclusion context.
8. Link execution evidence; code presence alone is not a fresh green run.

## Sign-off boundary
- Mobile 1 and Mobile 2 have formal Word sign-off packs.
- Enrollment has a formal QA-893 sign-off and handoff pack.
- L1-L4 is the approved completion boundary.
- L5 SQL is documented as analysis and future enhancement, not implemented completion.
- Approvals marked [NEED_INPUT] remain open until names and dates are provided.

## Legacy improvements and open enhancements
Canonical TestNG added or improved IDP, encryption, dynamic data, lean assertions, multi-plan execution, and several Enrollment subsequent APIs not present in the original Excel catalog.

Open enhancement categories: broaden Bruno coverage where gaps remain, complete qTest-to-Jira traceability, Enrollment nightly, NM Direct Enrollment CI, selected partner APIs, negative cases, PATCH logout, and optional SQL field reconciliation.

Republish the page when finished.
