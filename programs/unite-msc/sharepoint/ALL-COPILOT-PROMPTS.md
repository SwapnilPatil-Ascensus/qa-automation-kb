# Unite MSC - paste-ready SharePoint Copilot prompts

Every prompt below is 4,000 characters or fewer. Paste in filename order.
Create the parent at the API Testing Documentation Hub root, then children 01–11 under it.
For A/B/C pages, paste A first and each later part against the same page.

## 00 Unite MSC API Automation - Part A
Characters: 2646

```text
PART A of 4. Create a polished SharePoint Site Page titled "Unite MSC API Automation".

Site: API Testing Documentation Hub. This IS the parent page. Create it at the hub root titled "Unite MSC API Automation". Do not nest it under another Unite MSC page. Do not create the eleven child pages from this prompt; those have their own prompts.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation (parent; no third segment).
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: This is the parent. Next: 01 KT and Onboarding. Child pages 01 through 11 are listed in the site map. Link them after those pages exist; until then keep the titles as text tiles.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# Unite MSC API Automation
Purpose: Parent hub for Unite MSC API automation. Anyone who needs to support, run, or extend Mobile 1, Mobile 2, or Enrollment starts here and opens the matching child page.

## What this hub is
This is the parent page for Unite MSC API automation on the API Testing Documentation Hub.

It covers three modules: Mobile 1, Mobile 2, and Enrollment. Canonical automation is Java 17, Maven, TestNG, and Rest Assured in GitLab api-test-automation. This SharePoint page is the published operating guide. It is not the executable source of truth.

Informational callout: child pages 01 through 11 live under this parent. Do not create extra pages for individual endpoints, suites, SQL files, or Jira stories.

Publish at the API Testing Documentation Hub root as "Unite MSC API Automation", then continue with Part B.
```

## 00 Unite MSC API Automation - Part B
Characters: 3439

```text
PART B of 4. Edit the existing SharePoint page "Unite MSC API Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

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
| 01 KT and Onboarding | First-week path, KT demonstration, and completion checklist |
| 02 Architecture and Ownership | Runtime model, GitLab folders, L1-L4 boundary, and who owns what |
| 03 Access, Setup and Environments | Access tickets, local Maven setup, Stage1 vs QC4 vs localhost |
| 04 Daily Run Playbook | Before-run checks, Maven examples, and after-run actions |
| 05 Mobile 1 Automation | Mobile 1 scope, plants, sign-off artifacts, and known considerations |
| 06 Mobile 2 Automation | Mobile 2 scope, coverage position, artifacts, and known considerations |
| 07 Enrollment Automation | Enrollment wizard, suites, deferred partner APIs, and QC4 notes |
| 08 Coverage, Traceability and Sign-off | Registers, endpoint tracing, sign-off bar, and enhancement backlog |
| 09 Reporting and Troubleshooting | Where reports live and how to classify a first failure |
| 10 Test Data, DB Refresh and Security | Refresh steps, SQL boundary, and what must never reach SharePoint |
| 11 Extend the Automation | How to add a scenario, AI prompt pattern, and definition of done |

## Start here
Render this set as a second Quick Links web part in tile or grid layout.

| I need to… | Open |
|---|---|
| Join or take over support | 01 KT and Onboarding |
| Understand components and ownership | 02 Architecture and Ownership |
| Get access and configure an environment | 03 Access, Setup and Environments |
| Run a suite today | 04 Daily Run Playbook |
| Check Mobile 1 | 05 Mobile 1 Automation |
| Check Mobile 2 | 06 Mobile 2 Automation |
| Check Enrollment | 07 Enrollment Automation |
| Review coverage or sign-off | 08 Coverage, Traceability and Sign-off |
| Diagnose a failure | 09 Reporting and Troubleshooting |
| Prepare data after a refresh | 10 Test Data, DB Refresh and Security |
| Add a scenario safely | 11 Extend the Automation |

Republish the page when finished.
```

## 00 Unite MSC API Automation - Part C
Characters: 2966

```text
PART C of 4. Edit the existing SharePoint page "Unite MSC API Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## Who should use this hub
| Audience | Use this hub to |
|---|---|
| New engineer or receiving team | Complete KT, get access, run one safe suite |
| Day-to-day support | Run a suite, read a report, classify a failure |
| Module owner | Confirm Mobile 1, Mobile 2, or Enrollment scope and exclusions |
| Lead or reviewer | Find sign-off, coverage, and the L1-L4 completion bar |

## Current scope
| Module | Current documented scope | Primary plants | Child page |
|---|---|---|---|
| Mobile 1 | 26 coded endpoint operations | OK Direct; NM Direct on applicable auth/IDP flows | 05 Mobile 1 Automation |
| Mobile 2 | 24 in-scope business APIs; harness excluded | OK Direct, New York; selected NM Direct smoke | 06 Mobile 2 Automation |
| Enrollment | 25 automated of 28 catalog rows; 3 partner APIs deferred | OK Direct, New York | 07 Enrollment Automation |

Enrollment deferred items are partner submit, Upromise account, and OAuth token. They are exclusions, not missing coding in the signed-off MSC happy path.

## Environments
| Environment | Use | Caveat |
|---|---|---|
| Stage1 | Primary regression and sign-off evidence | Refresh can invalidate users and data |
| QC4 | Integration and environment proof | Stability, IDP/reverse proxy, and refresh dependencies can block runs |
| Localhost examples | Development templates only | Not CI evidence |

Caution callout: QC4 is not a substitute for Stage1 sign-off evidence. After any database refresh, use page 10 before classifying a product defect.

## Validation and sign-off bar
| Layer | Meaning | Sign-off |
|---|---|---|
| L1 | HTTP status and transport | Required |
| L2 | Contract and response shape | Required |
| L3 | Schema and typed payload | Required where supported |
| L4 | Business assertions | Required |
| L5 | API-to-database field reconciliation | Optional enhancement; not the completion gate |

Leadership directed that L5 SQL field reconciliation is not the completion gate. Do not claim L5 is implemented.

Republish the page when finished.
```

## 00 Unite MSC API Automation - Part D
Characters: 3011

```text
PART D of 4. Edit the existing SharePoint page "Unite MSC API Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## Authoritative project links
Render these as a prominent Quick Links web part using labeled tiles.

| Resource | Purpose | URL |
|---|---|---|
| API Test Automation repository | Canonical automation repository | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation |
| Mobile automation folder | Mobile 1, Mobile 2, Enrollment, and reporting code | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads |
| Unite MSC Bruno collection | Manual API exploration and testing collection | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads |
| qTest Test Design | Manual Unite MSC test cases and traceability | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| Unite MSC Epic QA-796 | Jira delivery scope and related stories | https://ascensuscollegesavings.atlassian.net/browse/QA-796 |

Informational callout: the manual test cases are in qTest Test Design, not Confluence. SharePoint provides navigation and operating guidance. qTest is the manual-test system of record. Jira is the delivery system of record. GitLab is the executable system of record.

## Source-of-truth and security
Informational callout: SharePoint explains how to use and support the automation. GitLab remains the source of truth for Java, suite XML, Maven profiles, Bruno, Postman, SQL, and pipeline configuration.

Repository: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation
Mobile code: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads
Published documentation: this parent page and its eleven child pages on the API Testing Documentation Hub.

Prohibition callout: never paste passwords, JWT, SSN, certificates, host properties, environment JSON, database connection strings, or raw PII onto this page or any child page.

Republish the page when finished.
```

## 01 KT and Onboarding
Characters: 3923

```text
Create a modern, visually polished SharePoint Site Page titled "01 KT and Onboarding".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: Unite MSC API Automation | Next: 02 Architecture and Ownership

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 01 KT and Onboarding
Purpose: A receiving engineer can find the code, run one safe suite, locate a report, and know where to ask for help.

## First-week path
| Day | Task | Evidence |
|---|---|---|
| 1 | Confirm GitLab, Jira, VPN, Java 17, Maven 3.9+, and approved DB access | Access checklist complete |
| 2 | Clone api-test-automation; build the mobile parent with tests skipped | Successful Maven build |
| 3 | Run one smoke profile using a local gitignored host overlay | HTML/Surefire report |
| 4 | Trace one endpoint from CSV to Java class to suite XML to report | Review notes |
| 5 | Shadow failure triage and DB-refresh preparation | KT sign-off |

## What to read, in order
1. 02 Architecture and Ownership
2. 03 Access, Setup and Environments
3. 04 Daily Run Playbook
4. The applicable module page: 05, 06, or 07
5. 09 Reporting and Troubleshooting
6. 10 Test Data, DB Refresh and Security
7. Review the Unite MSC Epic: https://ascensuscollegesavings.atlassian.net/browse/QA-796
8. Review manual cases in qTest Test Design: https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign
9. Open the manual API collection in Bruno: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads

## KT demonstration
The engineer must demonstrate each of these live:
- Find a test class from an endpoint ID in the coverage register.
- Show which XML suite and Maven profile execute it.
- Run a non-destructive smoke or targeted test.
- Find the generated report and classify one sample failure.
- Explain what changes after a Stage1 or QC4 database refresh.
- Explain the L1-L4 validation boundary and why L5 SQL is not the completion gate.

## Completion checklist
- [ ] Engineer can run without copying another person's host file.
- [ ] Engineer knows credentials, JWT, SSN, and environment JSON never go in SharePoint or Git.
- [ ] Engineer can distinguish environment, data, automation, and product failures.
- [ ] Engineer knows Mobile 1, Mobile 2, and Enrollment ownership boundaries.
- [ ] KT reviewer records open questions and owners rather than inventing answers.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
```

## 02 Architecture and Ownership
Characters: 3975

```text
Create a modern, visually polished SharePoint Site Page titled "02 Architecture and Ownership".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 01 KT and Onboarding | Next: 03 Access, Setup and Environments

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 02 Architecture and Ownership
Purpose: How the canonical automation is built, which repository owns what, and where the validation boundary sits.

## Runtime model
Render as a preformatted code block:

TestNG test class
  -> module base test / shared jsonapi framework
  -> Rest Assured request and L1-L4 assertions
  -> Unite MSC BFF endpoint
  -> downstream account, profile, bank, metadata, transaction, auth services

The canonical automation is Java 17, Maven, TestNG, and Rest Assured. It is not the legacy Cucumber implementation.

## Repository map
Mobile root: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads

| Area | GitLab path | Purpose |
|---|---|---|
| Mobile parent | mobile/pom.xml | Shared module build |
| Mobile 1 | mobile/mobile1/ | Authentication, profile, device, biometric, session APIs |
| Mobile 2 | mobile/mobile2/ | Dashboard, bank, contribution, activity, plans, performance APIs |
| Enrollment | mobile/enrollment/ | Encrypted enrollment wizard and subsequent enrollment |
| Shared reporting | mobile/reporting/ or module report wiring | HTML and test evidence |
| Manual API testing | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads | Unite MSC Bruno collection |

## Validation boundary
| Layer | Meaning | Sign-off |
|---|---|---|
| L1 | HTTP status and transport | Required |
| L2 | Contract and response shape | Required |
| L3 | Schema and typed payload | Required where supported |
| L4 | Business assertions | Required |
| L5 | API-to-database field reconciliation | Optional enhancement; not the completion gate |

## Ownership
- QA Automation owns framework patterns, TestNG tests, suite XML, reports, and coverage registers.
- DevOps owns or partners on runners, schedules, secure files, and pipeline hard gates.
- Product and development SMEs own service behavior and approve unknown API-to-database mappings.
- The receiving team owns steady-state runs, triage, test-data upkeep, and approved enhancements after handoff.

Caution callout: named approvers remain required wherever sign-off documents still contain [NEED_INPUT].

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
```

## 03 Access, Setup and Environments
Characters: 3513

```text
Create a modern, visually polished SharePoint Site Page titled "03 Access, Setup and Environments".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 02 Architecture and Ownership | Next: 04 Daily Run Playbook

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 03 Access, Setup and Environments
Purpose: Everything needed to get access, build locally, and choose the correct environment.

## Prerequisites
| Need | Route |
|---|---|
| GitLab project access | Approved GitLab access request |
| Java and Maven | Java 17 and Maven 3.9+ |
| VPN and internal endpoints | Corporate VPN |
| Linux or runner access | Freshservice Linux User Account Creation |
| GitLab access changes | Freshservice Gitlab_Users |
| Frogger / DB relay | Freshservice gwtpsshrelay01 |
| Jira and qTest | Team-approved project access |

## Local setup
Render the commands as a preformatted code block:

git clone https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation.git
cd api-test-automation
mvn -f mobile/pom.xml clean install -DskipTests

Prohibition callout: create only a personal, gitignored host overlay under the applicable module test resources. Never upload it to SharePoint and never copy another engineer's credentials.

## Environment use
| Environment | Use | Caveat |
|---|---|---|
| Stage1 | Primary regression and sign-off evidence | Refresh can invalidate users and data |
| QC4 | Integration and environment proof | Stability, IDP/reverse proxy, and refresh dependencies can block runs |
| Localhost examples | Development templates only | Not CI evidence |

Enrollment uses the cloud Enrollment BFF. Mobile login may use a different BFF; do not swap base URIs. Enrollment POST bodies are encrypted; GET calls may be plain.

## Setup verification
- [ ] Maven parent build succeeds.
- [ ] Personal host overlay is ignored by Git.
- [ ] One safe smoke profile starts and reaches the expected environment.
- [ ] Report directory is created.
- [ ] No token, password, SSN, or private endpoint is pasted into a ticket or SharePoint.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
```

## 04 Daily Run Playbook
Characters: 3547

```text
Create a modern, visually polished SharePoint Site Page titled "04 Daily Run Playbook".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 03 Access, Setup and Environments | Next: 05 Mobile 1 Automation

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 04 Daily Run Playbook
Purpose: The day-to-day procedure for running a suite and handling the result.

## Before every run
1. Confirm the intended module, plant, environment, and suite.
2. Confirm VPN or Frogger connectivity and environment health.
3. Check whether a database refresh occurred.
4. Use automation-owned data; do not select arbitrary customer-like records.
5. Ensure the local host overlay is present and gitignored.

## Enrollment run examples
Render as a preformatted code block:

# Stage1 smoke
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=<YOUR_HOST_FILE>"

# Stage1 regression: OK Direct and New York
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-regression,acceptance-stage1" "-Dhost.properties=<YOUR_HOST_FILE>"

# QC4 integration
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-integration,acceptance-qc4" "-Denvironment.properties=qc4.properties" "-Dhost.properties=<APPROVED_QC4_FILE>"

For Mobile 1 and Mobile 2, use the Maven profiles documented in their module POM and suite XML. Do not guess a profile from an old Confluence page.

## After every run
| Result | Action |
|---|---|
| Green | Save the run URL or report when evidence is required |
| Environment failure | Record endpoint, environment, timestamp, and dependency |
| Data failure | Refresh only automation-owned fixtures |
| Automation failure | Reproduce targeted; link class and suite |
| Product failure | Follow the automation bug lifecycle with sanitized evidence |

## Run discipline
Prohibition callout:
- Do not silently remove classes from XML to make a run green.
- Quarantine only with a visible tag or exclusion and a linked follow-up.
- Do not commit target/.
- Do not attach raw request or response payloads containing PII or JWT.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
```

## 05 Mobile 1 Automation
Characters: 3168

```text
Create a modern, visually polished SharePoint Site Page titled "05 Mobile 1 Automation".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 04 Daily Run Playbook | Next: 06 Mobile 2 Automation

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 05 Mobile 1 Automation
Purpose: Scope, plants, artifacts, and known considerations for Mobile 1 API automation.

## Scope
Code: api-test-automation/mobile/mobile1/

Mobile 1 documents 26 coded operations covering member session and authentication, username, owner and profile, beneficiary and account closure, routing information, biometric, phone authentication, device and push tokens, password, CSR-as-member, IDP token exchange, session lookup, biometric validation, and session PIN.

## Plants and suites
- OK Direct is the primary non-IDP path.
- NM Direct is used on applicable authentication and IDP paths.
- Destructive updates and deletes belong in smoke or targeted suites, not an unattended master run unless explicitly designed.

## Support files
| Artifact | Use |
|---|---|
| Mobile 1 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile1-endpoint-current-state.csv | Endpoint to class to suite mapping |
| mobile1-signoff-summary.md | Quick status |
| Coverage chart image | Optional visual |

## Known considerations
Caution callout:
- IDP token tests exist in canonical TestNG; legacy Cucumber did not cover the IDP feature.
- QC4 automation JWT behavior can produce environment-dependent 401 responses.
- PATCH logout remains an enhancement candidate.
- L5 SQL analysis is not implemented as the completion gate.

When a case fails, record endpoint ID, class, method, plant, environment, and report - not only a screenshot.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
```

## 06 Mobile 2 Automation
Characters: 3225

```text
Create a modern, visually polished SharePoint Site Page titled "06 Mobile 2 Automation".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 05 Mobile 1 Automation | Next: 07 Enrollment Automation

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 06 Mobile 2 Automation
Purpose: Scope, coverage position, artifacts, and known considerations for Mobile 2 API automation.

## Scope
Code: api-test-automation/mobile/mobile2/

Mobile 2 covers activity, transaction history, investments, banks, content, plans, contributions, dashboard and YTD summary, balance trend, performance, stackup, and UGift.

## Coverage position
| Item | Position |
|---|---|
| Documented rows | 25, including one acceptance harness endpoint |
| Business APIs in sign-off numerator | 24 |
| Intentional exclusion | GET mobilemembers/{planId}/{username} harness |
| Primary master-regression plants | OK Direct and New York |
| Additional smoke plant | NM Direct on selected stackup coverage |

## Support files
| Artifact | Use |
|---|---|
| Mobile 2 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile2-endpoint-current-state.csv | Endpoint to class to suite mapping |
| unite-msc-endpoint-summary.csv | Compact evidence register |
| Coverage chart image | Optional visual |

## Known considerations
Caution callout:
- Bank PUT and DELETE, and contribution DELETE, are destructive and intentionally separated from master coverage.
- Dynamic contribution fixtures can be environment-sensitive.
- POST mobilebanks with planId=upromise is a Postman-only enhancement candidate.
- Mobile 2 has the mature nightly pattern to reuse when adding other module jobs.

Use the current GitLab suite XML and POM for commands. SharePoint does not replace executable configuration.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
```

## 07 Enrollment Automation
Characters: 3239

```text
Create a modern, visually polished SharePoint Site Page titled "07 Enrollment Automation".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 06 Mobile 2 Automation | Next: 08 Coverage, Traceability and Sign-off

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 07 Enrollment Automation
Purpose: Scope, wizard flow, suites, and operational notes for Enrollment API automation handed over under QA-893.

## Scope and status
Code: api-test-automation/mobile/enrollment/ | Handoff: Jira QA-893

| Metric | Position |
|---|---|
| Catalog rows | 28 |
| Automated | 25 |
| Deferred | 3 |
| Core wizard | 15 of 15 documented happy-path steps |
| Primary plants | OK Direct, New York |
| Local-only plant | NM Direct example; not CI sign-off |

Deferred items are partner submit, Upromise account, and OAuth token. They are exclusions, not missing coding in the signed-off MSC happy path.

## Wizard flow
Certificate, prospect, enrollment started, owner, address, beneficiary, routing and bank, recurring contribution, allocations, review-confirm, then subsequent enrollment cases.

Prohibition callout: Enrollment POST bodies use encryption. Never paste plaintext sensitive payloads, certificate material, JWT, SSN, or environment JSON into SharePoint.

## Suites
| Profile | Purpose |
|---|---|
| mobile-ms-enrollment-smoke | Stage1 bootstrap and health |
| mobile-ms-enrollment-regression | Stage1 OK Direct and New York |
| mobile-ms-enrollment-integration | QC4 integration |

## Operational notes
- QC4 can be blocked by refresh, IDP or reverse proxy, plan metadata, or account and MFA prerequisites.
- The GitLab Enrollment nightly remains a follow-up unless it has since been implemented and verified.
- After a database refresh, use page 10 before classifying a product defect.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
```

## 08 Coverage, Traceability and Sign-off - Part A
Characters: 2668

```text
PART A of 2. Create a polished SharePoint Site Page titled "08 Coverage, Traceability and Sign-off".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 07 Enrollment Automation | Next: 09 Reporting and Troubleshooting

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 08 Coverage, Traceability and Sign-off
Purpose: Where coverage lives, how to trace an endpoint to evidence, and what the sign-off boundary means.

## Coverage sources
| Source | System of record |
|---|---|
| Mobile 1 | mobile1-endpoint-current-state.csv |
| Mobile 2 | mobile2-endpoint-current-state.csv |
| Enrollment | enrollment-endpoint-current-state.csv and the coverage workbook |
| Legacy to canonical | legacy-to-canonical-traceability.csv |
| Automated implementation | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads |
| Manual API collection | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads |
| Manual test cases | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| Delivery scope and stories | https://ascensuscollegesavings.atlassian.net/browse/QA-796 |

Publish under "Unite MSC API Automation", then continue with Part B.
```

## 08 Coverage, Traceability and Sign-off - Part B
Characters: 2634

```text
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
```

## 09 Reporting and Troubleshooting
Characters: 3464

```text
Create a modern, visually polished SharePoint Site Page titled "09 Reporting and Troubleshooting".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 08 Coverage, Traceability and Sign-off | Next: 10 Test Data, DB Refresh and Security

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 09 Reporting and Troubleshooting
Purpose: Where to find evidence and how to classify a failure before escalating it.

## Where to look
| Evidence | Use |
|---|---|
| Surefire and TestNG output | Class and assertion failure |
| Module HTML report | Shareable sanitized run summary |
| GitLab job log and artifacts | CI environment and command |
| Jira or bug evidence folder | Product or recurring automation defect |

## First-failure classification
| Symptom | Likely class | First action |
|---|---|---|
| 401 or IDP token error | Auth, environment, or data | Confirm plant, account, token path, IDP availability |
| Enrollment decrypt error | Encryption or session | New certificate and prospect; avoid double encryption |
| 426 | App-version metadata | Confirm approved x-app-version |
| Oracle timeout | Access or environment | Confirm VPN, Frogger, and port |
| Empty SQL fixture | Data refresh | Recreate approved automation data |
| Class never ran | Suite or group wiring | Check XML, profile, groups, exclusions |
| 404 or 503 across tests | Environment or routing | Check service health before editing tests |

## Triage steps
1. Preserve timestamp, environment, plant, endpoint, class, and report.
2. Re-run targeted once only when safe.
3. Compare with service health and any recent refresh or deploy.
4. Classify as environment, data, automation, product, or expected exclusion.
5. For defects, use the automation bug lifecycle with sanitized evidence.

## Evidence rules
Prohibition callout: never attach bearer tokens, passwords, SSN, raw personal payloads, host properties, Postman environment JSON, or database credentials. Redact account identifiers unless the approved internal process requires them.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
```

## 10 Test Data, DB Refresh and Security
Characters: 3301

```text
Create a modern, visually polished SharePoint Site Page titled "10 Test Data, DB Refresh and Security".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 09 Reporting and Troubleshooting | Next: 11 Extend the Automation

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 10 Test Data, DB Refresh and Security
Purpose: How to keep automation data valid, what to do after a refresh, and what must never reach SharePoint.

## Test-data principles
- Use automation-owned users and accounts, for example approved QAAUTOTEST patterns.
- Generate unique data where the flow supports it.
- Do not mutate arbitrary records returned by broad random SQL.
- Record plant and environment with evidence.

## After a database refresh
1. Confirm environment restoration is complete.
2. Restore or recreate approved automation accounts.
3. Confirm MFA and IDP prerequisites for the selected plants.
4. Confirm plan metadata, app version, routing, and fund fixtures.
5. Validate VPN, Frogger, and database connectivity.
6. Run the smallest smoke suite.
7. Run targeted module regression only after smoke is green.
8. Record remaining environment gaps in RAID or Jira.

## SQL boundary
Enrollment SQL in Git supports test-data setup and post-account verification. Mobile 1 and Mobile 2 field-level SQL analysis exists for future work. Leadership approved L1-L4 as the completion bar; do not claim L5 is implemented.

## Never upload to SharePoint
Prohibition callout:
- Postman environment JSON.
- Local host or property overlays.
- Passwords, tokens, certificates, private keys, SSN, or raw PII.
- Database connection strings.
- Raw SQL exports containing customer-like data.
- target/ reports that include unsanitized payloads.

SharePoint links to controlled Git paths and ticketing processes. It is not a secret store or an executable configuration source.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
```

## 11 Extend the Automation - Part A
Characters: 2892

```text
PART A of 2. Create a polished SharePoint Site Page titled "11 Extend the Automation".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 10 Test Data, DB Refresh and Security

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 11 Extend the Automation
Purpose: How to add a scenario safely, including AI-assisted authoring and the definition of done.

## Add a scenario from an existing pattern
1. Identify the endpoint row and nearest canonical TestNG class in https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads
2. Confirm method, path, and plant behavior with approved source evidence.
3. Review the matching manual request in https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads
4. Review or create the manual case in https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign
5. Link the manual and automated coverage to the delivering story under https://ascensuscollegesavings.atlassian.net/browse/QA-796
6. Reuse the module base test and framework helpers.
7. Use encrypted POST handling for Enrollment.
8. Add lean L1-L4 assertions; do not dump full PII responses.
9. Wire the class into every intended XML and Maven profile.
10. Update the module coverage register.
11. Run targeted, module, and applicable master suites.
12. Attach sanitized evidence and obtain review.

Publish under "Unite MSC API Automation", then continue with Part B.
```

## 11 Extend the Automation - Part B
Characters: 2642

```text
PART B of 2. Edit the existing SharePoint page "11 Extend the Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## AI-assisted prompt pattern
Render as a preformatted code block:

Add a TestNG case for {METHOD} {PATH} in {MODULE}.
Follow {EXISTING_CLASS}; do not change shared framework APIs.
Do not log JWT, password, SSN, or full personal payloads.
Add lean status and key business assertions.
Wire only the approved plants and suite XMLs.
Update the endpoint coverage register.

Caution callout: human review is mandatory. AI must not invent endpoints, expected values, SQL mappings, plants, or credentials.

## Definition of done
- [ ] Code review complete and pipeline green.
- [ ] Test is wired to the intended suite, not merely present.
- [ ] Existing module and master suites show no unintended regression.
- [ ] Coverage and traceability register updated.
- [ ] Secrets scan clean.
- [ ] Operational documentation updated when commands, environments, or ownership change.

## Reference downloads
Use the page library for approved sign-off, coverage, and traceability attachments.

- Automated code and configuration: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation
- Mobile implementation: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads
- Manual API testing in Bruno: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads
- Manual test cases in qTest Test Design: https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign
- Unite MSC Jira Epic and related stories: https://ascensuscollegesavings.atlassian.net/browse/QA-796

Republish the page when finished.
```
