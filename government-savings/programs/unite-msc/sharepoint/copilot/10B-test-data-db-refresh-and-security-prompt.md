PART B of 3. Edit the existing SharePoint page "10 Test Data, DB Refresh and Security" on API Testing Documentation Hub.

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

## 3. After a database refresh
Render this diagram as a full-width monospace block, exactly as written:

  [ refresh declared complete ]
        v
  [ recreate automation members per branding ]
        | MFA-skip condition + IDP metadata
        v
  [ verify fixtures ]
    app version | plan and fund | routing and bank | contribution
        v
  [ Enrollment smoke ]  ping, certificate, states, country, plans
        |-- fails -> environment or data gap:
        |            raise Jira and stop here
       passes
        v
  [ one read-only Mobile 1 auth path ]
        v
  [ one read-only Mobile 2 path ]
        v
  [ targeted module regression ]
        v
  [ full ordered Enrollment chain ]   most dependent, so run it last
        v
  [ record any remaining gap in Jira ]

Work in this order. Running the full Enrollment chain first after a refresh produces a wall of skips that hides the real cause.

1. Confirm database and service restoration is declared complete.
2. Recreate/verify automation-owned members and active accounts for all intended brandings.
3. Confirm MFA-skip and IDP metadata required by authentication.
4. Confirm minimum app version, plan metadata, active fund, routing/bank, and contribution fixtures.
5. Validate your personal Oracle overlay without sharing its values.
6. Run Enrollment smoke: ping, certificate, states, country, plans.
7. Run one read-only Mobile 1 authentication path.
8. Run targeted regression by module; run the full Enrollment chain last.
9. Record unresolved data/environment gaps in Jira; do not weaken assertions to pass.

## 4. Host overlay and configuration
The personal <COMPUTERNAME>.properties file supplies UNITEDATABASEURL, UNITEUSERNAME, and UNITEPASSWORD. It lives under the module's src/test/resources/config/ path and is passed with -Dhost.properties.

Environment files such as stage1.properties and qc4.properties select service behavior; Maven acceptance-stage1/acceptance-qc4 profiles select which file wins.

Prohibition callout: never copy another engineer's host overlay or store one in SharePoint, Jira, Teams, qTest, Bruno, Postman, or Git.

Republish the page when finished.
