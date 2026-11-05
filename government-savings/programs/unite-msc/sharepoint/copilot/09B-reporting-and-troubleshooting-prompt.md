PART B of 3. Edit the existing SharePoint page "09 Reporting and Troubleshooting" on API Testing Documentation Hub.

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

## 3. Triage decision tree
Render this diagram as a full-width monospace block, exactly as written:

  [ run failed ]
        |
  did the build fail before TestNG started?
        |-- yes -> local build or stale target/maven-compile
        |
       no
        v
  is this the earliest failure in an ordered chain?
        |-- no  -> fix the earlier step first;
        |          later skips are symptoms, not defects
       yes
        v
  what is the signal?
        |
        +-- 401 on the Mobile 2 mobilemembers harness
        |     -> expected exclusion, record and move on
        +-- 401 elsewhere
        |     -> auth, IDP state, or automation user for that branding
        +-- 426
        |     -> app-version fixture in Oracle
        +-- 404 or 503 across unrelated tests
        |     -> service or route health; check recent deploys
        +-- Oracle error or empty fixture
        |     -> host overlay, access, or post-refresh data
        +-- decrypt or session error in Enrollment
        |     -> restart a fresh full chain; check double encryption
        +-- class never ran
        |     -> suite XML, group, profile, or branding block wiring
        +-- one stable business assertion fails
              -> product or changed contract
        v
  classify: environment | data | automation | product | expected exclusion

Classification decides who acts next. Never change test code to silence a failure you have not classified.

## 4. First-failure classifier
| Symptom | Likely class | First action |
|---|---|---|
| BUILD FAILURE before TestNG | Local build/dependency | Run mobile parent build; inspect Maven cause |
| Unresolved compilation problems | Stale compile output | Delete module target/maven-compile and rerun |
| 401 / IDP token failure | Auth, automation data, or environment | Confirm branding, IDP state, usable automation account |
| 401 only on M2 mobilemembers harness GET | Expected harness design | Record as excluded observation; do not open product/coverage defect |
| 426 | App-version metadata | Verify Oracle MIN_MOBILE_VERSION fixture |
| Oracle connection/empty fixture | Access or refresh/data | Verify host overlay and recreate approved fixtures |
| Enrollment decrypt/session error | Ordered state/encryption | Start a fresh chain; find first failed step; avoid double encryption |
| Class never ran | XML/profile/group wiring | Check selected profile, XML, group, and all branding blocks |
| 404/503 across unrelated tests | Route/service environment | Check service health/deploy before editing tests |
| One stable L4 assertion fails | Product or changed contract | Reproduce targeted and compare approved expectation |

Republish the page when finished.
