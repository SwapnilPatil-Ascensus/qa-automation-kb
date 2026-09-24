#!/usr/bin/env python3
"""Generate self-contained SharePoint Copilot prompts for the Unite MSC site.

Copilot cannot read local files, so every prompt carries its own page content,
design system, and guardrails. Prompts longer than PROMPT_LIMIT are split into
Part 1 (create page) and Part 2 (append to the same page).
"""

from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "copilot"
COMBINED = ROOT / "ALL-COPILOT-PROMPTS.md"

PROMPT_LIMIT = 4000

PARENT_PAGE = "Unite MSC API Automation"
HUB = "API Testing Documentation Hub"

GITLAB_REPO = "https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation"
GITLAB_MOBILE = f"{GITLAB_REPO}/-/tree/main/mobile?ref_type=heads"
GITLAB_BRUNO = (
    f"{GITLAB_REPO}/-/tree/main/bruno/Mobile/mobile-msc/"
    "Unite-MSC-Bruno_collection?ref_type=heads"
)
QTEST_MANUAL = (
    "https://ascensus.qtestnet.com/p/118829/portal/project"
    "#id=69212334&object=0&tab=testdesign"
)
JIRA_EPIC = "https://ascensuscollegesavings.atlassian.net/browse/QA-796"

DESIGN = """DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art."""

RULES = """RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages."""


def hub_links() -> str:
    return """| I need to… | Open |
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
| Add a scenario safely | 11 Extend the Automation |"""


def site_map() -> str:
    return """Render the site map as a Quick Links web part in tile or grid layout, then repeat the same eleven children in a table so the page still reads if tiles cannot be linked yet.

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
| 11 Extend the Automation | How to add a scenario, AI prompt pattern, and definition of done |"""


PAGES = [
    {
        "num": "00",
        "title": "Unite MSC API Automation",
        "slug": "unite-msc-api-automation",
        "is_parent": True,
        "purpose": "Parent hub for Unite MSC API automation. Anyone who needs to support, run, or extend Mobile 1, Mobile 2, or Enrollment starts here and opens the matching child page.",
        "prev": None,
        "next": "01 KT and Onboarding",
        "sections": [
            (
                "What this hub is",
                """This is the parent page for Unite MSC API automation on the API Testing Documentation Hub.

It covers three modules: Mobile 1, Mobile 2, and Enrollment. Canonical automation is Java 17, Maven, TestNG, and Rest Assured in GitLab api-test-automation. This SharePoint page is the published operating guide. It is not the executable source of truth.

Informational callout: child pages 01 through 11 live under this parent. Do not create extra pages for individual endpoints, suites, SQL files, or Jira stories.""",
            ),
            (
                "Site map",
                site_map(),
            ),
            (
                "Start here",
                "Render this set as a second Quick Links web part in tile or grid layout.\n\n" + hub_links(),
            ),
            (
                "Who should use this hub",
                """| Audience | Use this hub to |
|---|---|
| New engineer or receiving team | Complete KT, get access, run one safe suite |
| Day-to-day support | Run a suite, read a report, classify a failure |
| Module owner | Confirm Mobile 1, Mobile 2, or Enrollment scope and exclusions |
| Lead or reviewer | Find sign-off, coverage, and the L1-L4 completion bar |""",
            ),
            (
                "Current scope",
                """| Module | Current documented scope | Primary plants | Child page |
|---|---|---|---|
| Mobile 1 | 26 coded endpoint operations | OK Direct; NM Direct on applicable auth/IDP flows | 05 Mobile 1 Automation |
| Mobile 2 | 24 in-scope business APIs; harness excluded | OK Direct, New York; selected NM Direct smoke | 06 Mobile 2 Automation |
| Enrollment | 25 automated of 28 catalog rows; 3 partner APIs deferred | OK Direct, New York | 07 Enrollment Automation |

Enrollment deferred items are partner submit, Upromise account, and OAuth token. They are exclusions, not missing coding in the signed-off MSC happy path.""",
            ),
            (
                "Environments",
                """| Environment | Use | Caveat |
|---|---|---|
| Stage1 | Primary regression and sign-off evidence | Refresh can invalidate users and data |
| QC4 | Integration and environment proof | Stability, IDP/reverse proxy, and refresh dependencies can block runs |
| Localhost examples | Development templates only | Not CI evidence |

Caution callout: QC4 is not a substitute for Stage1 sign-off evidence. After any database refresh, use page 10 before classifying a product defect.""",
            ),
            (
                "Validation and sign-off bar",
                """| Layer | Meaning | Sign-off |
|---|---|---|
| L1 | HTTP status and transport | Required |
| L2 | Contract and response shape | Required |
| L3 | Schema and typed payload | Required where supported |
| L4 | Business assertions | Required |
| L5 | API-to-database field reconciliation | Optional enhancement; not the completion gate |

Leadership directed that L5 SQL field reconciliation is not the completion gate. Do not claim L5 is implemented.""",
            ),
            (
                "Authoritative project links",
                f"""Render these as a prominent Quick Links web part using labeled tiles.

| Resource | Purpose | URL |
|---|---|---|
| API Test Automation repository | Canonical automation repository | {GITLAB_REPO} |
| Mobile automation folder | Mobile 1, Mobile 2, Enrollment, and reporting code | {GITLAB_MOBILE} |
| Unite MSC Bruno collection | Manual API exploration and testing collection | {GITLAB_BRUNO} |
| qTest Test Design | Manual Unite MSC test cases and traceability | {QTEST_MANUAL} |
| Unite MSC Epic QA-796 | Jira delivery scope and related stories | {JIRA_EPIC} |

Informational callout: the manual test cases are in qTest Test Design, not Confluence. SharePoint provides navigation and operating guidance. qTest is the manual-test system of record. Jira is the delivery system of record. GitLab is the executable system of record.""",
            ),
            (
                "Source-of-truth and security",
                f"""Informational callout: SharePoint explains how to use and support the automation. GitLab remains the source of truth for Java, suite XML, Maven profiles, Bruno, Postman, SQL, and pipeline configuration.

Repository: {GITLAB_REPO}
Mobile code: {GITLAB_MOBILE}
Published documentation: this parent page and its eleven child pages on the API Testing Documentation Hub.

Prohibition callout: never paste passwords, JWT, SSN, certificates, host properties, environment JSON, database connection strings, or raw PII onto this page or any child page.""",
            ),
        ],
    },
    {
        "num": "01",
        "title": "KT and Onboarding",
        "slug": "kt-and-onboarding",
        "purpose": "A receiving engineer can find the code, run one safe suite, locate a report, and know where to ask for help.",
        "prev": "Unite MSC API Automation",
        "next": "02 Architecture and Ownership",
        "sections": [
            (
                "First-week path",
                """| Day | Task | Evidence |
|---|---|---|
| 1 | Confirm GitLab, Jira, VPN, Java 17, Maven 3.9+, and approved DB access | Access checklist complete |
| 2 | Clone api-test-automation; build the mobile parent with tests skipped | Successful Maven build |
| 3 | Run one smoke profile using a local gitignored host overlay | HTML/Surefire report |
| 4 | Trace one endpoint from CSV to Java class to suite XML to report | Review notes |
| 5 | Shadow failure triage and DB-refresh preparation | KT sign-off |""",
            ),
            (
                "What to read, in order",
                f"""1. 02 Architecture and Ownership
2. 03 Access, Setup and Environments
3. 04 Daily Run Playbook
4. The applicable module page: 05, 06, or 07
5. 09 Reporting and Troubleshooting
6. 10 Test Data, DB Refresh and Security
7. Review the Unite MSC Epic: {JIRA_EPIC}
8. Review manual cases in qTest Test Design: {QTEST_MANUAL}
9. Open the manual API collection in Bruno: {GITLAB_BRUNO}""",
            ),
            (
                "KT demonstration",
                """The engineer must demonstrate each of these live:
- Find a test class from an endpoint ID in the coverage register.
- Show which XML suite and Maven profile execute it.
- Run a non-destructive smoke or targeted test.
- Find the generated report and classify one sample failure.
- Explain what changes after a Stage1 or QC4 database refresh.
- Explain the L1-L4 validation boundary and why L5 SQL is not the completion gate.""",
            ),
            (
                "Completion checklist",
                """- [ ] Engineer can run without copying another person's host file.
- [ ] Engineer knows credentials, JWT, SSN, and environment JSON never go in SharePoint or Git.
- [ ] Engineer can distinguish environment, data, automation, and product failures.
- [ ] Engineer knows Mobile 1, Mobile 2, and Enrollment ownership boundaries.
- [ ] KT reviewer records open questions and owners rather than inventing answers.""",
            ),
        ],
    },
    {
        "num": "02",
        "title": "Architecture and Ownership",
        "slug": "architecture-and-ownership",
        "purpose": "How the canonical automation is built, which repository owns what, and where the validation boundary sits.",
        "prev": "01 KT and Onboarding",
        "next": "03 Access, Setup and Environments",
        "sections": [
            (
                "Runtime model",
                """Render as a preformatted code block:

TestNG test class
  -> module base test / shared jsonapi framework
  -> Rest Assured request and L1-L4 assertions
  -> Unite MSC BFF endpoint
  -> downstream account, profile, bank, metadata, transaction, auth services

The canonical automation is Java 17, Maven, TestNG, and Rest Assured. It is not the legacy Cucumber implementation.""",
            ),
            (
                "Repository map",
                f"""Mobile root: {GITLAB_MOBILE}

| Area | GitLab path | Purpose |
|---|---|---|
| Mobile parent | mobile/pom.xml | Shared module build |
| Mobile 1 | mobile/mobile1/ | Authentication, profile, device, biometric, session APIs |
| Mobile 2 | mobile/mobile2/ | Dashboard, bank, contribution, activity, plans, performance APIs |
| Enrollment | mobile/enrollment/ | Encrypted enrollment wizard and subsequent enrollment |
| Shared reporting | mobile/reporting/ or module report wiring | HTML and test evidence |
| Manual API testing | {GITLAB_BRUNO} | Unite MSC Bruno collection |""",
            ),
            (
                "Validation boundary",
                """| Layer | Meaning | Sign-off |
|---|---|---|
| L1 | HTTP status and transport | Required |
| L2 | Contract and response shape | Required |
| L3 | Schema and typed payload | Required where supported |
| L4 | Business assertions | Required |
| L5 | API-to-database field reconciliation | Optional enhancement; not the completion gate |""",
            ),
            (
                "Ownership",
                """- QA Automation owns framework patterns, TestNG tests, suite XML, reports, and coverage registers.
- DevOps owns or partners on runners, schedules, secure files, and pipeline hard gates.
- Product and development SMEs own service behavior and approve unknown API-to-database mappings.
- The receiving team owns steady-state runs, triage, test-data upkeep, and approved enhancements after handoff.

Caution callout: named approvers remain required wherever sign-off documents still contain [NEED_INPUT].""",
            ),
        ],
    },
    {
        "num": "03",
        "title": "Access, Setup and Environments",
        "slug": "access-setup-and-environments",
        "purpose": "Everything needed to get access, build locally, and choose the correct environment.",
        "prev": "02 Architecture and Ownership",
        "next": "04 Daily Run Playbook",
        "sections": [
            (
                "Prerequisites",
                """| Need | Route |
|---|---|
| GitLab project access | Approved GitLab access request |
| Java and Maven | Java 17 and Maven 3.9+ |
| VPN and internal endpoints | Corporate VPN |
| Linux or runner access | Freshservice Linux User Account Creation |
| GitLab access changes | Freshservice Gitlab_Users |
| Frogger / DB relay | Freshservice gwtpsshrelay01 |
| Jira and qTest | Team-approved project access |""",
            ),
            (
                "Local setup",
                f"""Render the commands as a preformatted code block:

git clone {GITLAB_REPO}.git
cd api-test-automation
mvn -f mobile/pom.xml clean install -DskipTests

Prohibition callout: create only a personal, gitignored host overlay under the applicable module test resources. Never upload it to SharePoint and never copy another engineer's credentials.""",
            ),
            (
                "Environment use",
                """| Environment | Use | Caveat |
|---|---|---|
| Stage1 | Primary regression and sign-off evidence | Refresh can invalidate users and data |
| QC4 | Integration and environment proof | Stability, IDP/reverse proxy, and refresh dependencies can block runs |
| Localhost examples | Development templates only | Not CI evidence |

Enrollment uses the cloud Enrollment BFF. Mobile login may use a different BFF; do not swap base URIs. Enrollment POST bodies are encrypted; GET calls may be plain.""",
            ),
            (
                "Setup verification",
                """- [ ] Maven parent build succeeds.
- [ ] Personal host overlay is ignored by Git.
- [ ] One safe smoke profile starts and reaches the expected environment.
- [ ] Report directory is created.
- [ ] No token, password, SSN, or private endpoint is pasted into a ticket or SharePoint.""",
            ),
        ],
    },
    {
        "num": "04",
        "title": "Daily Run Playbook",
        "slug": "daily-run-playbook",
        "purpose": "The day-to-day procedure for running a suite and handling the result.",
        "prev": "03 Access, Setup and Environments",
        "next": "05 Mobile 1 Automation",
        "sections": [
            (
                "Before every run",
                """1. Confirm the intended module, plant, environment, and suite.
2. Confirm VPN or Frogger connectivity and environment health.
3. Check whether a database refresh occurred.
4. Use automation-owned data; do not select arbitrary customer-like records.
5. Ensure the local host overlay is present and gitignored.""",
            ),
            (
                "Enrollment run examples",
                """Render as a preformatted code block:

# Stage1 smoke
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=<YOUR_HOST_FILE>"

# Stage1 regression: OK Direct and New York
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-regression,acceptance-stage1" "-Dhost.properties=<YOUR_HOST_FILE>"

# QC4 integration
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-integration,acceptance-qc4" "-Denvironment.properties=qc4.properties" "-Dhost.properties=<APPROVED_QC4_FILE>"

For Mobile 1 and Mobile 2, use the Maven profiles documented in their module POM and suite XML. Do not guess a profile from an old Confluence page.""",
            ),
            (
                "After every run",
                """| Result | Action |
|---|---|
| Green | Save the run URL or report when evidence is required |
| Environment failure | Record endpoint, environment, timestamp, and dependency |
| Data failure | Refresh only automation-owned fixtures |
| Automation failure | Reproduce targeted; link class and suite |
| Product failure | Follow the automation bug lifecycle with sanitized evidence |""",
            ),
            (
                "Run discipline",
                """Prohibition callout:
- Do not silently remove classes from XML to make a run green.
- Quarantine only with a visible tag or exclusion and a linked follow-up.
- Do not commit target/.
- Do not attach raw request or response payloads containing PII or JWT.""",
            ),
        ],
    },
    {
        "num": "05",
        "title": "Mobile 1 Automation",
        "slug": "mobile-1-automation",
        "purpose": "Scope, plants, artifacts, and known considerations for Mobile 1 API automation.",
        "prev": "04 Daily Run Playbook",
        "next": "06 Mobile 2 Automation",
        "sections": [
            (
                "Scope",
                """Code: api-test-automation/mobile/mobile1/

Mobile 1 documents 26 coded operations covering member session and authentication, username, owner and profile, beneficiary and account closure, routing information, biometric, phone authentication, device and push tokens, password, CSR-as-member, IDP token exchange, session lookup, biometric validation, and session PIN.""",
            ),
            (
                "Plants and suites",
                """- OK Direct is the primary non-IDP path.
- NM Direct is used on applicable authentication and IDP paths.
- Destructive updates and deletes belong in smoke or targeted suites, not an unattended master run unless explicitly designed.""",
            ),
            (
                "Support files",
                """| Artifact | Use |
|---|---|
| Mobile 1 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile1-endpoint-current-state.csv | Endpoint to class to suite mapping |
| mobile1-signoff-summary.md | Quick status |
| Coverage chart image | Optional visual |""",
            ),
            (
                "Known considerations",
                """Caution callout:
- IDP token tests exist in canonical TestNG; legacy Cucumber did not cover the IDP feature.
- QC4 automation JWT behavior can produce environment-dependent 401 responses.
- PATCH logout remains an enhancement candidate.
- L5 SQL analysis is not implemented as the completion gate.

When a case fails, record endpoint ID, class, method, plant, environment, and report - not only a screenshot.""",
            ),
        ],
    },
    {
        "num": "06",
        "title": "Mobile 2 Automation",
        "slug": "mobile-2-automation",
        "purpose": "Scope, coverage position, artifacts, and known considerations for Mobile 2 API automation.",
        "prev": "05 Mobile 1 Automation",
        "next": "07 Enrollment Automation",
        "sections": [
            (
                "Scope",
                """Code: api-test-automation/mobile/mobile2/

Mobile 2 covers activity, transaction history, investments, banks, content, plans, contributions, dashboard and YTD summary, balance trend, performance, stackup, and UGift.""",
            ),
            (
                "Coverage position",
                """| Item | Position |
|---|---|
| Documented rows | 25, including one acceptance harness endpoint |
| Business APIs in sign-off numerator | 24 |
| Intentional exclusion | GET mobilemembers/{planId}/{username} harness |
| Primary master-regression plants | OK Direct and New York |
| Additional smoke plant | NM Direct on selected stackup coverage |""",
            ),
            (
                "Support files",
                """| Artifact | Use |
|---|---|
| Mobile 2 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile2-endpoint-current-state.csv | Endpoint to class to suite mapping |
| unite-msc-endpoint-summary.csv | Compact evidence register |
| Coverage chart image | Optional visual |""",
            ),
            (
                "Known considerations",
                """Caution callout:
- Bank PUT and DELETE, and contribution DELETE, are destructive and intentionally separated from master coverage.
- Dynamic contribution fixtures can be environment-sensitive.
- POST mobilebanks with planId=upromise is a Postman-only enhancement candidate.
- Mobile 2 has the mature nightly pattern to reuse when adding other module jobs.

Use the current GitLab suite XML and POM for commands. SharePoint does not replace executable configuration.""",
            ),
        ],
    },
    {
        "num": "07",
        "title": "Enrollment Automation",
        "slug": "enrollment-automation",
        "purpose": "Scope, wizard flow, suites, and operational notes for Enrollment API automation handed over under QA-893.",
        "prev": "06 Mobile 2 Automation",
        "next": "08 Coverage, Traceability and Sign-off",
        "sections": [
            (
                "Scope and status",
                """Code: api-test-automation/mobile/enrollment/ | Handoff: Jira QA-893

| Metric | Position |
|---|---|
| Catalog rows | 28 |
| Automated | 25 |
| Deferred | 3 |
| Core wizard | 15 of 15 documented happy-path steps |
| Primary plants | OK Direct, New York |
| Local-only plant | NM Direct example; not CI sign-off |

Deferred items are partner submit, Upromise account, and OAuth token. They are exclusions, not missing coding in the signed-off MSC happy path.""",
            ),
            (
                "Wizard flow",
                """Certificate, prospect, enrollment started, owner, address, beneficiary, routing and bank, recurring contribution, allocations, review-confirm, then subsequent enrollment cases.

Prohibition callout: Enrollment POST bodies use encryption. Never paste plaintext sensitive payloads, certificate material, JWT, SSN, or environment JSON into SharePoint.""",
            ),
            (
                "Suites",
                """| Profile | Purpose |
|---|---|
| mobile-ms-enrollment-smoke | Stage1 bootstrap and health |
| mobile-ms-enrollment-regression | Stage1 OK Direct and New York |
| mobile-ms-enrollment-integration | QC4 integration |""",
            ),
            (
                "Operational notes",
                """- QC4 can be blocked by refresh, IDP or reverse proxy, plan metadata, or account and MFA prerequisites.
- The GitLab Enrollment nightly remains a follow-up unless it has since been implemented and verified.
- After a database refresh, use page 10 before classifying a product defect.""",
            ),
        ],
    },
    {
        "num": "08",
        "title": "Coverage, Traceability and Sign-off",
        "slug": "coverage-traceability-and-sign-off",
        "purpose": "Where coverage lives, how to trace an endpoint to evidence, and what the sign-off boundary means.",
        "prev": "07 Enrollment Automation",
        "next": "09 Reporting and Troubleshooting",
        "sections": [
            (
                "Coverage sources",
                f"""| Source | System of record |
|---|---|
| Mobile 1 | mobile1-endpoint-current-state.csv |
| Mobile 2 | mobile2-endpoint-current-state.csv |
| Enrollment | enrollment-endpoint-current-state.csv and the coverage workbook |
| Legacy to canonical | legacy-to-canonical-traceability.csv |
| Automated implementation | {GITLAB_MOBILE} |
| Manual API collection | {GITLAB_BRUNO} |
| Manual test cases | {QTEST_MANUAL} |
| Delivery scope and stories | {JIRA_EPIC} |""",
            ),
            (
                "How to trace an endpoint",
                f"""1. Pick the endpoint ID in the module register.
2. Open the canonical Java class and method.
3. Confirm its suite XML and Maven profile.
4. Confirm the manual request in the Unite MSC Bruno collection where one exists: {GITLAB_BRUNO}
5. Confirm the manual case in qTest Test Design: {QTEST_MANUAL}
6. Link the case to the appropriate story under Unite MSC Epic QA-796: {JIRA_EPIC}
7. Open the sign-off document for scope and exclusion context.
8. Link execution evidence; code presence alone is not a fresh green run.""",
            ),
            (
                "Sign-off boundary",
                """- Mobile 1 and Mobile 2 have formal Word sign-off packs.
- Enrollment has a formal QA-893 sign-off and handoff pack.
- L1-L4 is the approved completion boundary.
- L5 SQL is documented as analysis and future enhancement, not implemented completion.
- Approvals marked [NEED_INPUT] remain open until names and dates are provided.""",
            ),
            (
                "Legacy improvements and open enhancements",
                """Canonical TestNG added or improved IDP, encryption, dynamic data, lean assertions, multi-plan execution, and several Enrollment subsequent APIs not present in the original Excel catalog.

Open enhancement categories: broaden Bruno coverage where gaps remain, complete qTest-to-Jira traceability, Enrollment nightly, NM Direct Enrollment CI, selected partner APIs, negative cases, PATCH logout, and optional SQL field reconciliation.""",
            ),
        ],
    },
    {
        "num": "09",
        "title": "Reporting and Troubleshooting",
        "slug": "reporting-and-troubleshooting",
        "purpose": "Where to find evidence and how to classify a failure before escalating it.",
        "prev": "08 Coverage, Traceability and Sign-off",
        "next": "10 Test Data, DB Refresh and Security",
        "sections": [
            (
                "Where to look",
                """| Evidence | Use |
|---|---|
| Surefire and TestNG output | Class and assertion failure |
| Module HTML report | Shareable sanitized run summary |
| GitLab job log and artifacts | CI environment and command |
| Jira or bug evidence folder | Product or recurring automation defect |""",
            ),
            (
                "First-failure classification",
                """| Symptom | Likely class | First action |
|---|---|---|
| 401 or IDP token error | Auth, environment, or data | Confirm plant, account, token path, IDP availability |
| Enrollment decrypt error | Encryption or session | New certificate and prospect; avoid double encryption |
| 426 | App-version metadata | Confirm approved x-app-version |
| Oracle timeout | Access or environment | Confirm VPN, Frogger, and port |
| Empty SQL fixture | Data refresh | Recreate approved automation data |
| Class never ran | Suite or group wiring | Check XML, profile, groups, exclusions |
| 404 or 503 across tests | Environment or routing | Check service health before editing tests |""",
            ),
            (
                "Triage steps",
                """1. Preserve timestamp, environment, plant, endpoint, class, and report.
2. Re-run targeted once only when safe.
3. Compare with service health and any recent refresh or deploy.
4. Classify as environment, data, automation, product, or expected exclusion.
5. For defects, use the automation bug lifecycle with sanitized evidence.""",
            ),
            (
                "Evidence rules",
                """Prohibition callout: never attach bearer tokens, passwords, SSN, raw personal payloads, host properties, Postman environment JSON, or database credentials. Redact account identifiers unless the approved internal process requires them.""",
            ),
        ],
    },
    {
        "num": "10",
        "title": "Test Data, DB Refresh and Security",
        "slug": "test-data-db-refresh-and-security",
        "purpose": "How to keep automation data valid, what to do after a refresh, and what must never reach SharePoint.",
        "prev": "09 Reporting and Troubleshooting",
        "next": "11 Extend the Automation",
        "sections": [
            (
                "Test-data principles",
                """- Use automation-owned users and accounts, for example approved QAAUTOTEST patterns.
- Generate unique data where the flow supports it.
- Do not mutate arbitrary records returned by broad random SQL.
- Record plant and environment with evidence.""",
            ),
            (
                "After a database refresh",
                """1. Confirm environment restoration is complete.
2. Restore or recreate approved automation accounts.
3. Confirm MFA and IDP prerequisites for the selected plants.
4. Confirm plan metadata, app version, routing, and fund fixtures.
5. Validate VPN, Frogger, and database connectivity.
6. Run the smallest smoke suite.
7. Run targeted module regression only after smoke is green.
8. Record remaining environment gaps in RAID or Jira.""",
            ),
            (
                "SQL boundary",
                """Enrollment SQL in Git supports test-data setup and post-account verification. Mobile 1 and Mobile 2 field-level SQL analysis exists for future work. Leadership approved L1-L4 as the completion bar; do not claim L5 is implemented.""",
            ),
            (
                "Never upload to SharePoint",
                """Prohibition callout:
- Postman environment JSON.
- Local host or property overlays.
- Passwords, tokens, certificates, private keys, SSN, or raw PII.
- Database connection strings.
- Raw SQL exports containing customer-like data.
- target/ reports that include unsanitized payloads.

SharePoint links to controlled Git paths and ticketing processes. It is not a secret store or an executable configuration source.""",
            ),
        ],
    },
    {
        "num": "11",
        "title": "Extend the Automation",
        "slug": "extend-the-automation",
        "purpose": "How to add a scenario safely, including AI-assisted authoring and the definition of done.",
        "prev": "10 Test Data, DB Refresh and Security",
        "next": None,
        "sections": [
            (
                "Add a scenario from an existing pattern",
                f"""1. Identify the endpoint row and nearest canonical TestNG class in {GITLAB_MOBILE}
2. Confirm method, path, and plant behavior with approved source evidence.
3. Review the matching manual request in {GITLAB_BRUNO}
4. Review or create the manual case in {QTEST_MANUAL}
5. Link the manual and automated coverage to the delivering story under {JIRA_EPIC}
6. Reuse the module base test and framework helpers.
7. Use encrypted POST handling for Enrollment.
8. Add lean L1-L4 assertions; do not dump full PII responses.
9. Wire the class into every intended XML and Maven profile.
10. Update the module coverage register.
11. Run targeted, module, and applicable master suites.
12. Attach sanitized evidence and obtain review.""",
            ),
            (
                "AI-assisted prompt pattern",
                """Render as a preformatted code block:

Add a TestNG case for {METHOD} {PATH} in {MODULE}.
Follow {EXISTING_CLASS}; do not change shared framework APIs.
Do not log JWT, password, SSN, or full personal payloads.
Add lean status and key business assertions.
Wire only the approved plants and suite XMLs.
Update the endpoint coverage register.

Caution callout: human review is mandatory. AI must not invent endpoints, expected values, SQL mappings, plants, or credentials.""",
            ),
            (
                "Definition of done",
                """- [ ] Code review complete and pipeline green.
- [ ] Test is wired to the intended suite, not merely present.
- [ ] Existing module and master suites show no unintended regression.
- [ ] Coverage and traceability register updated.
- [ ] Secrets scan clean.
- [ ] Operational documentation updated when commands, environments, or ownership change.""",
            ),
            (
                "Reference downloads",
                f"""Use the page library for approved sign-off, coverage, and traceability attachments.

- Automated code and configuration: {GITLAB_REPO}
- Mobile implementation: {GITLAB_MOBILE}
- Manual API testing in Bruno: {GITLAB_BRUNO}
- Manual test cases in qTest Test Design: {QTEST_MANUAL}
- Unite MSC Jira Epic and related stories: {JIRA_EPIC}""",
            ),
        ],
    },
]


def is_parent(page: dict) -> bool:
    return bool(page.get("is_parent"))


def display_title(page: dict) -> str:
    if is_parent(page):
        return page["title"]
    return f"{page['num']} {page['title']}"


def placement(page: dict) -> str:
    if is_parent(page):
        return (
            f'Site: {HUB}. This IS the parent page. Create it at the hub root titled '
            f'"{PARENT_PAGE}". Do not nest it under another Unite MSC page. '
            "Do not create the eleven child pages from this prompt; those have their own prompts."
        )
    return (
        f'Site: {HUB}. Publish it under the parent page "{PARENT_PAGE}", not at the hub root.'
    )


def closing_line(page: dict) -> str:
    if is_parent(page):
        return (
            f'After generating, verify the page title is exactly "{PARENT_PAGE}" with no "00" prefix, '
            "the breadcrumb, the site-map quick links, and the Source and ownership band, then publish at the hub root."
        )
    return (
        f'After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "{PARENT_PAGE}".'
    )


def design_for(page: dict) -> str:
    if is_parent(page):
        return DESIGN.replace(
            "API Testing Documentation Hub > Unite MSC API Automation > this page.",
            "API Testing Documentation Hub > Unite MSC API Automation (parent; no third segment).",
        )
    return DESIGN


def nav_line(page: dict) -> str:
    if is_parent(page):
        return (
            "This is the parent. Next: 01 KT and Onboarding. "
            "Child pages 01 through 11 are listed in the site map. "
            "Link them after those pages exist; until then keep the titles as text tiles."
        )
    parts = [f"Parent: {PARENT_PAGE}"]
    if page["prev"]:
        parts.append(f"Previous: {page['prev']}")
    if page["next"]:
        parts.append(f"Next: {page['next']}")
    return " | ".join(parts)


def render_sections(sections: list) -> str:
    return "\n\n".join(f"## {heading}\n{body}" for heading, body in sections)


def build_single(page: dict) -> str:
    title = display_title(page)
    return f"""Create a modern, visually polished SharePoint Site Page titled "{title}".

{placement(page)}

{design_for(page)}

Quick links row for this page: {nav_line(page)}

{RULES}

PAGE CONTENT — build the page from exactly this material:

# {title}
Purpose: {page['purpose']}

{render_sections(page['sections'])}

{closing_line(page)}
"""


def build_part_one(page: dict, sections: list, total_parts: int) -> str:
    title = display_title(page)
    publish = (
        f'Publish at the {HUB} root as "{PARENT_PAGE}", then continue with Part B.'
        if is_parent(page)
        else f'Publish under "{PARENT_PAGE}", then continue with Part B.'
    )
    return f"""PART A of {total_parts}. Create a polished SharePoint Site Page titled "{title}".

{placement(page)}

{design_for(page)}

Quick links row for this page: {nav_line(page)}

{RULES}
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# {title}
Purpose: {page['purpose']}

{render_sections(sections)}

{publish}
"""


def build_part_two(page: dict, sections: list, part_index: int, total_parts: int) -> str:
    title = display_title(page)
    letter = chr(64 + part_index)
    closing = (
        "Finish with the gray Source and ownership band below."
        if part_index == total_parts
        else "Leave the page open for the next part."
    )
    return f"""PART {letter} of {total_parts}. Edit the existing SharePoint page "{title}" on {HUB}.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

{closing}

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

{RULES}

APPEND EXACTLY:

{render_sections(sections)}

Republish the page when finished.
"""


def partition(sections: list, cuts: tuple) -> list:
    points = (0, *cuts, len(sections))
    return [sections[points[i] : points[i + 1]] for i in range(len(points) - 1)]


def paste_ready_parts(page: dict) -> list:
    """Return the fewest contiguous prompt parts that each fit Copilot."""
    single = build_single(page)
    if clipboard_length(single) <= PROMPT_LIMIT:
        return [single]

    sections = page["sections"]
    for count in range(2, len(sections) + 1):
        candidates = []
        for cuts in combinations(range(1, len(sections)), count - 1):
            groups = partition(sections, cuts)
            prompts = [build_part_one(page, groups[0], count)]
            prompts.extend(
                build_part_two(page, group, index, count)
                for index, group in enumerate(groups[1:], start=2)
            )
            maximum = max(map(clipboard_length, prompts))
            if maximum <= PROMPT_LIMIT:
                candidates.append((maximum, prompts))
        if candidates:
            return min(candidates, key=lambda item: item[0])[1]

    raise ValueError(f"Cannot split {display_title(page)} below {PROMPT_LIMIT} characters")


def block(label: str, text: str) -> list:
    return [f"## {label}", f"Characters: {clipboard_length(text)}", "", "```text", text.rstrip(), "```", ""]


def clipboard_length(text: str) -> int:
    """Count Windows CRLF as two characters, matching Copilot's counter."""
    return len(text) + text.count("\n")


def main() -> None:
    PROMPTS.mkdir(parents=True, exist_ok=True)
    for stale in PROMPTS.glob("*.md"):
        stale.unlink()
    stale_fallback = ROOT / "SPLIT-FALLBACK-PROMPTS.md"
    if stale_fallback.exists():
        stale_fallback.unlink()

    combined = [
        "# Unite MSC - paste-ready SharePoint Copilot prompts",
        "",
        "Every prompt below is 4,000 characters or fewer. Paste in filename order.",
        f"Create the parent at the {HUB} root, then children 01–11 under it.",
        "For A/B/C pages, paste A first and each later part against the same page.",
        "",
    ]

    written = []
    for page in PAGES:
        title = f"{page['num']} {page['title']}"
        prompts = paste_ready_parts(page)
        for index, text in enumerate(prompts):
            suffix = "" if len(prompts) == 1 else chr(65 + index)
            name = f"{page['num']}{suffix}-{page['slug']}-prompt.md"
            label = title if not suffix else f"{title} - Part {suffix}"
            (PROMPTS / name).write_text(text, encoding="utf-8")
            combined.extend(block(label, text))
            written.append((name, clipboard_length(text)))

    COMBINED.write_text("\n".join(combined), encoding="utf-8")
    for name, size in written:
        print(f"{name}: {size} chars")
    print(f"\nWrote {len(written)} paste-ready prompts; maximum {max(s for _, s in written)} chars")


if __name__ == "__main__":
    main()
