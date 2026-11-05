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
QTEST_BASE = "https://ascensus.qtestnet.com/p/118829/portal/project"
QTEST_UNITE_MSC = f"{QTEST_BASE}#id=69212334&object=0&tab=testdesign"
QTEST_ENROLLMENT = f"{QTEST_BASE}#id=69212335&object=0&tab=testdesign"
QTEST_MOBILE1 = f"{QTEST_BASE}#id=69212337&object=0&tab=testdesign"
QTEST_MOBILE2 = f"{QTEST_BASE}#id=69233940&object=0&tab=testdesign"
# Parent Unite-MSC module (backward-compatible alias used where a single link is enough)
QTEST_MANUAL = QTEST_UNITE_MSC
JIRA_EPIC = "https://ascensuscollegesavings.atlassian.net/browse/QA-796"


def qtest_modules_table() -> str:
    """Four qTest Test Design modules for Unite MSC manual cases."""
    return f"""| Module | qTest Test Design |
|---|---|
| Unite-MSC (parent) | {QTEST_UNITE_MSC} |
| MSC-Enrollment | {QTEST_ENROLLMENT} |
| MSC-Mobile1 | {QTEST_MOBILE1} |
| MSC-Mobile2 | {QTEST_MOBILE2} |"""

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

DIAGRAM_RULE = (
    "- Keep each diagram in one full-width monospace block, character for character; never redraw it."
)

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
| 11 Extend the Automation | New-endpoint implementation playbook and reusable prompt library |"""


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

It covers three modules: Mobile 1, Mobile 2, and Enrollment. Canonical automation is JDK 17, Maven, TestNG, Rest Assured, Oracle-backed test data, mobile encryption, and a reusable HTML reporting portal in GitLab api-test-automation. This SharePoint page is the published operating guide, not executable source.

Informational callout: child pages 01 through 11 live under this parent. Do not create extra pages for individual endpoints, suites, SQL files, or Jira stories.""",
            ),
            (
                "Site map",
                site_map(),
            ),
            (
                "Platform at a glance",
                """Render this diagram as a full-width monospace block, exactly as written:

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

Mobile 2 reuses Mobile 1 authentication. Enrollment adds certificate-based encryption and an ordered session chain. Page 02 shows how each module reaches the BFF and the downstream services behind it.""",
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
                "Program accomplishment",
                """| Measure | Result |
|---|---:|
| Catalog rows reviewed | 79 |
| Automated business operations | 75 |
| Overall catalog coverage | 94.9% |
| Mobile 1 | 26/26 = 100% |
| Mobile 2 | 24/25 = 96.0% |
| Enrollment | 25/28 = 89.3% |
| Legacy traceability rows improved/new | 69 of 83 |

The result is a canonical, multi-plan TestNG platform—not a one-time script conversion. It includes IDP flows, encrypted Enrollment, dynamic Oracle fixtures, safe destructive-suite separation, Bruno manual collections, endpoint registers, formal sign-off packs, and a reusable reporting portal.""",
            ),
            (
                "Current scope",
                """| Module | Current documented scope | Primary plants | Child page |
|---|---|---|---|
| Mobile 1 | 26/26 endpoint operations | Current XML: OK Direct, New York, NM Direct | 05 Mobile 1 Automation |
| Mobile 2 | 24/25 business operations; harness excluded | Current XML: OK Direct, New York, NM Direct | 06 Mobile 2 Automation |
| Enrollment | 25/28 catalog rows; 3 partner APIs deferred | Current XML: OK Direct, New York, NM Direct | 07 Enrollment Automation |

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
| Unite MSC Epic QA-796 | Jira delivery scope and related stories | {JIRA_EPIC} |

### Manual test cases (qTest Test Design)
{qtest_modules_table()}

Informational callout: the manual test cases live in these four qTest modules, not Confluence. SharePoint provides navigation and operating guidance. qTest is the manual-test system of record. Jira is the delivery system of record. GitLab is the executable system of record.""",
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
        "purpose": "Everything a new engineer needs on day one: install, clone, build, open in an IDE, configure the host overlay, run Mobile 1, Mobile 2, or Enrollment, and find the report.",
        "prev": "Unite MSC API Automation",
        "next": "02 Architecture and Ownership",
        "sections": [
            (
                "1. Install and access",
                """| Need | Detail |
|---|---|
| JDK | JDK 17. The modules compile to Java 17 bytecode. Verify with java -version |
| Maven | 3.6+, 3.8+ recommended. Verify with mvn -version |
| Git | Clone access to api-test-automation |
| IDE | Eclipse, IntelliJ IDEA, VS Code, or Cursor with Maven support |
| IDE plugins | Lombok (POJOs use it) and TestNG |
| Oracle access | Read access for test-data SQL; request via Freshservice |
| Network | Corporate network reach to Stage1 and QC4 service endpoints |
| Tracking | Jira Epic QA-796 and qTest modules Unite-MSC / MSC-Enrollment / MSC-Mobile1 / MSC-Mobile2 |

Stack: Java, Maven, TestNG, and Rest Assured on the shared jsonapi-core framework. Test data comes from Oracle. HTML reporting comes from jsonapi-mobile-reporting.""",
            ),
            (
                "2. Clone and build",
                f"""Run once, from the repository root:

git clone {GITLAB_REPO}.git
cd api-test-automation
mvn -f mobile/pom.xml clean install -DskipTests

mobile/pom.xml builds four modules: reporting, enrollment, mobile1, mobile2.

Information callout: after this first build use mvn test, not mvn clean test, unless stale stubs remain.""",
            ),
            (
                "3. Open it in your IDE",
                """1. Import api-test-automation as an existing Maven project.
2. Install the Lombok plugin and enable annotation processing; the POJOs will not compile without it.
3. Install TestNG support so you can run a single class.
4. In VS Code or Cursor, open the repo folder, add the Java and Maven extensions, and run suites from the integrated terminal.
5. Maven compiles to target/maven-compile, deliberately separate from the IDE's own output, so IDE auto-build cannot overwrite Maven classes mid-run.""",
            ),
            (
                "4. Create your host overlay (one time)",
                """Each engineer needs a personal, gitignored host file. Never copy another engineer's file.

1. Build first. The config folder is empty in a fresh clone.
2. Open src/test/resources/config/ in the module you will run.
3. Copy config.properties to <COMPUTERNAME>.properties.
4. Fill in the three keys: UNITEDATABASEURL, UNITEUSERNAME, UNITEPASSWORD.
5. Pass it on every run with -Dhost.properties=<COMPUTERNAME>.properties

Why the folder looks empty before a build: config.properties and the environment files stage1, qc4, qc1, stage5, and cat are not committed in the module. Maven unpacks them from the shared jsonapi-lib resource artifact during generate-resources, and the module gitignore excludes every *.properties file in that folder. Do not try to commit them.

Name the file after your machine. The build derives the default host file from your COMPUTERNAME on Windows or HOSTNAME on Linux, which is why the convention exists; passing -Dhost.properties explicitly overrides that default.

Prohibition callout: the host overlay holds database credentials. It stays local. Never commit it, attach it, or paste its contents into SharePoint, Jira, or Teams.""",
            ),
            (
                "5. Maven profiles you will actually use",
                """| Module | Suite profiles | Suite XML folder |
|---|---|---|
| mobile1 | mobile1-regression, mobile1-integration, mobile1-smoke, mobile1-localhost | mobile/mobile1/testsuites/ |
| mobile2 | mobile2-regression, mobile2-integration, mobile2-smoke, mobile2-localhost | mobile/mobile2/testsuites/ |
| enrollment | mobile-ms-enrollment-regression, mobile-ms-enrollment-integration, mobile-ms-enrollment-smoke, mobile-ms-enrollment-localhost | mobile/enrollment/testsuites/ |
| Environment overlay | acceptance-stage1, acceptance-qc4 | Applies to all three modules |

Caution callout: list the environment profile LAST in -P. It overrides the environment.properties set by the suite profile. mobile1-smoke, mobile2-smoke, and Enrollment suite profiles default to qc4.properties; append acceptance-stage1 to run them against Stage1.""",
            ),
            (
                "6. Run your first suite",
                """Start with the Enrollment smoke suite; it is the least destructive. Replace <COMPUTERNAME> with your own overlay name.

mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

mvn -f mobile/mobile1/pom.xml test "-Pmobile1-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

mvn -f mobile/mobile2/pom.xml test "-Pmobile2-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

For ad-hoc local work, copy the example suite first, then use the localhost profile:

copy mobile\\mobile1\\testsuites\\localhost-testng.xml.example mobile\\mobile1\\testsuites\\localhost-testng.xml
mvn -f mobile/mobile1/pom.xml test "-Pmobile1-localhost,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties"

Swap acceptance-stage1 for acceptance-qc4 to target QC4.""",
            ),
            (
                "7. Find your report",
                """| Output | Path |
|---|---|
| HTML report | <module>/target/mobile-ms-report/index.html |
| TestNG and Surefire output | <module>/target/surefire-reports/ |

Open it directly, for example: start mobile\\enrollment\\target\\mobile-ms-report\\index.html

Plans run as a TestNG branding parameter: okdirect, newyork, nmdirect.""",
            ),
            (
                "8. Manual API testing: Bruno and Postman",
                f"""Use these to explore an endpoint before writing or debugging a TestNG case.

| Tool | Location | Contents |
|---|---|---|
| Bruno | bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection | Folders 01 - Enrollment, 02 - Mobile1, 03 - Mobile2 |
| Bruno environments | Same collection, environments/ | Env-Enrollment-Stage1.yml, Env-Mobile1-Stage1.yml, Env-Mobile2-Stage1.yml |
| Postman | postman/mobile | Mobile Endpoints (w/ IDP Session) for PKCE, member session, and token exchange |

Bruno collection: {GITLAB_BRUNO}

Manual test cases (qTest):
{qtest_modules_table()}

Prohibition callout: treat populated Bruno/Postman environment files as sensitive operational material. Do not paste their values into SharePoint, Jira, Teams, or prompts; use a stripped local demo environment.""",
            ),
            (
                "9. Branching, merge requests, and standards",
                """| Standard | Rule |
|---|---|
| Base branch | main |
| Branch name | feature/QA-####-short-description, matching the Jira key |
| Merge request | Use the repo template: Summary, Related, Test plan, Risks |
| Review gate | Local or CI checks pass; new scenarios executed in a test environment; no unintended API or config changes |
| Never commit | target/, your host overlay, credentials, tokens, certificates, or PII |

Track work under Epic QA-796 and link the Jira key in both the branch name and the merge request.""",
            ),
            (
                "10. Definition of done for onboarding",
                """- [ ] JDK, Maven, Git, and IDE plugins installed and verified.
- [ ] Parent build mvn -f mobile/pom.xml clean install -DskipTests succeeds.
- [ ] Personal host overlay created and confirmed gitignored.
- [ ] One Enrollment smoke run completed against Stage1.
- [ ] One Mobile 1 and one Mobile 2 suite run completed.
- [ ] HTML report located and one failure classified as environment, data, automation, or product.
- [ ] Bruno collection opened and one request executed manually.
- [ ] Branch and merge request standards understood; Epic QA-796 reviewed.""",
            ),
            (
                "11. First-day troubleshooting",
                """| Symptom | Fix |
|---|---|
| Surefire reports Unresolved compilation problems | Delete that module's target/maven-compile and rerun |
| Tests hit the wrong environment | Move acceptance-stage1 or acceptance-qc4 to the END of -P |
| Lombok or POJO compile errors in the IDE | Install the Lombok plugin and enable annotation processing |
| No tests ran | Confirm the suite profile name and that the suite XML exists in testsuites/ |
| Local suite not found | Copy localhost-testng.xml.example to localhost-testng.xml first |

Do not use src/test/resources/user/*.json for login data; authentication users are resolved from SQL at runtime.""",
            ),
        ],
    },
    {
        "num": "02",
        "title": "Architecture and Ownership",
        "slug": "architecture-and-ownership",
        "purpose": "A practical map of the canonical TestNG architecture, shared framework, module inheritance, test data, reporting, legacy references, and ownership.",
        "prev": "01 KT and Onboarding",
        "next": "03 Access, Setup and Environments",
        "sections": [
            (
                "1. Canonical runtime flow",
                """Render this diagram as a full-width monospace block, exactly as written:

  [ mvn -P<suite-profile>,<environment-profile> ]
                    |
                    v
  [ TestNG suite XML ] -- branding parameter: okdirect | newyork | nmdirect
                    |
                    v
  [ module test class ]  mobile1 | mobile2 | enrollment
                    |
                    v
  [ module base class ] MobileBaseRequestTest | EnrollmentBaseTest
       |                                   |
       |                                   +-- Enrollment only:
       +-- Oracle: automation user,             GET certificate, AES key,
           app version, routing, fund,          @MobileEncrypt payloads
           contribution fixtures
                    |
                    v
  [ jsonapi-core BaseRequestTest + Rest Assured client ]
                    |
                    v
  [ Unite MSC BFF route ] <- environment.properties + host overlay
                    |
                    v
  [ downstream MSC services ] -> [ Oracle ]
                    |
                    v
  [ L1-L4 assertions ] -> [ HTML portal + Surefire ]

The canonical stack is JDK 17, Maven, TestNG, Rest Assured, jsonapi-core, Oracle-backed test data, and Extent-based HTML reporting. It replaces the legacy Cucumber implementation; do not add new API coverage to the V2 or V3 UI repositories.""",
            ),
            (
                "2. Service communication map",
                """Render this diagram as a full-width monospace block, exactly as written:

   mobile app  |  Bruno request  |  Rest Assured test
                        |
        +---------------+-------------------+
        |                                   |
  [ Mobile BFF route ]              [ Enrollment BFF route ]
   /mobile1api  /mobile2api              /enrollmentapi
        |                                   |
  unite-mobile1 / unite-mobile2      unite-enrollment (gateway)
        |                                   |
        +---------------+-------------------+
                        |
   +---------+----------+---------+----------+-----------+
   |         |          |         |          |           |
  Auth    Account    Profile   Metadata    Bank    Transaction
 unite-   unite-     unite-    unite-     unite-    gateway
  auth    account    profile   metadata    bank    (YTD, history)
   |         |          |         |          |           |
   +---------+----------+----+----+----------+-----------+
                             |
                    [ Oracle schemas ]
             TA_LOGIN  TU_ACCT  TU_MEMBER  TU_PERSON
             TU_BENE  TU_BANK  TU_TRAUNCH  TU_FUNDS

A test never calls a downstream service directly. It calls the BFF route for its module; the BFF fans out to the services that own each piece of data.

| Service | Owns |
|---|---|
| Auth | prospect and member token issuance |
| Account | prospects, accounts, balances, allocations, account creation |
| Profile | owner and beneficiary identity, address lookup |
| Metadata | plans, funds, prices, states, countries, codes, app version |
| Bank | routing verification and bank instructions |
| Transaction | activity and history by plan backend type |

Informational callout: some dashboard bank and withdrawal fields are served by an on-prem account gateway rather than the Oracle MSC tables. That is one reason a universal API-to-database comparison was not adopted as the sign-off gate.""",
            ),
            (
                "3. Repository and module map",
                f"""Mobile root: {GITLAB_MOBILE}

| Area | GitLab path | Purpose |
|---|---|---|
| Root parent | pom.xml | Builds jsonapi, universal, astro, mobile |
| Mobile parent | mobile/pom.xml | Builds reporting, enrollment, mobile1, mobile2 |
| Shared framework | jsonapi/jsonapi-core | BaseRequestTest, resource loading, SQL, Rest Assured |
| Mobile 1 | mobile/mobile1 | Authentication/session and member-profile capabilities |
| Mobile 2 | mobile/mobile2 | Account experience; reuses Mobile 1 auth base |
| Enrollment | mobile/enrollment | Encrypted wizard + subsequent enrollment |
| Reporting | mobile/reporting | Static portal + Extent detail + sanitization |
| Manual API testing | {GITLAB_BRUNO} | Unite MSC Bruno collection |""",
            ),
            (
                "4. Module inheritance and shared behavior",
                """| Module | Base and shared behavior |
|---|---|
| Mobile 1 | MobileBaseRequestTest extends BaseRequestTest; loads mobile.sql, selects an Oracle-backed automation user, resolves minimum app version, configures mobile/IDP auth |
| Mobile 2 | Reuses Mobile 1 authentication and account context rather than duplicating login endpoints |
| Enrollment | EnrollmentBaseTest owns encryption, prospect/member session context, JSON fixtures, and ordered wizard state |

TestNG passes branding as okdirect, newyork, or nmdirect. SQL and JSON placeholders are resolved for that branding. IDP-enabled plans probe for a login-capable automation user; the framework can fall back to mobile-session auth where designed.""",
            ),
            (
                "5. Related automation estates",
                """| Estate | Technology | Relationship |
|---|---|---|
| Canonical API automation | Maven, TestNG, Rest Assured | Extend for Unite MSC API endpoints |
| Legacy Unite API/mobile reference | Cucumber features and older endpoint flows | Traceability/reference only; do not extend |
| V2 Unite UI automation | Ant, Selenium, Cucumber | UI regression; not API source of truth |
| V3 Unite / Universal Enrollment UI | Maven, Selenium/Cucumber | UI journey coverage; complements API tests |
| Performance automation | JMeter/Taurus performance suites | Load/performance concern; separate from functional L1-L4 |

Do not confuse UI page objects or performance scripts with canonical API coverage. Cross-reference them only when a business journey or pipeline needs layered proof.""",
            ),
            (
                "6. Configuration layers",
                """| Layer | Example | Responsibility |
|---|---|---|
| Suite profile | mobile1-regression | Selects TestNG XML and groups |
| Environment profile | acceptance-stage1 / acceptance-qc4 | Overrides environment.properties; must be last in -P |
| Environment file | stage1.properties / qc4.properties | Service routes and non-secret environment behavior |
| Host overlay | <COMPUTERNAME>.properties | Personal Oracle URL/user/password; local and gitignored |
| Suite XML | testsuites/*-testng.xml | Branding blocks, class order, listeners |

The suite XML is executable truth for what runs. A Java class not wired into the intended XML does not count as executed coverage.""",
            ),
            (
                "7. Validation boundary",
                """| Layer | Meaning | Sign-off |
|---|---|---|
| L1 | HTTP status and transport | Required |
| L2 | Contract and response shape | Required |
| L3 | Schema and typed payload | Required where supported |
| L4 | Business assertions | Required |
| L5 | API-to-database field reconciliation | Analysis/future enhancement; not the completion gate |

Oracle is actively used for test-data selection, minimum mobile version, routing/fund/contribution fixtures, and Enrollment post-account verification. That is different from universal field-by-field API-to-DB reconciliation, which leadership did not require for sign-off.""",
            ),
            (
                "8. Reporting architecture",
                """MobileMsHtmlReportListener is registered in suite XML. It creates:

- target/mobile-ms-report/index.html — leadership-friendly portal.
- target/mobile-ms-report/extent/detail.html — Extent test detail.
- pages for test details, categories, logs, history, and about.
- data/summary.json and data/history.json.
- target/surefire-reports/ — TestNG/JUnit execution detail.

SensitiveDataSanitizer redacts bearer tokens, JWT-like values, passwords, client secrets, and signing keys from report text. Sanitization is a defense, not permission to log secrets.""",
            ),
            (
                "9. Ownership and source-of-truth",
                """| Area | Owner / source |
|---|---|
| Java, POM, TestNG XML, SQL, reporting | GitLab api-test-automation; QA Automation |
| Manual API requests | Unite MSC Bruno collection |
| Manual test cases | qTest: Unite-MSC, MSC-Enrollment, MSC-Mobile1, MSC-Mobile2 |
| Delivery scope and stories | Jira Epic QA-796 |
| Runner, schedule, secure files, hard gates | DevOps + QA Automation |
| Service behavior and unknown DB mappings | Product/development SME |
| Day-to-day run, triage, data upkeep | Receiving automation team after handoff |

Caution callout: named approvers remain required wherever sign-off documents still contain [NEED_INPUT].""",
            ),
        ],
    },
    {
        "num": "03",
        "title": "Access, Setup and Environments",
        "slug": "access-setup-and-environments",
        "purpose": "Access routes and secure configuration reference: tools, GitLab, Oracle, local overlay, environment/profile precedence, Bruno/qTest/Jira, and setup proof.",
        "prev": "02 Architecture and Ownership",
        "next": "04 Daily Run Playbook",
        "sections": [
            (
                "1. Access and tools",
                """| Need | Route |
|---|---|
| GitLab project access | Approved GitLab access request |
| Java and Maven | JDK 17; Maven 3.6.3+, 3.8+ recommended |
| IDE | Eclipse, IntelliJ, VS Code, or Cursor with Lombok and TestNG |
| Oracle test-data access | Freshservice request; used by the SQL fixtures |
| Linux or runner access | Freshservice Linux User Account Creation |
| GitLab access changes | Freshservice Gitlab_Users |
| Oracle DB relay | Team-approved Freshservice relay-access request |
| Jira and qTest | Team-approved project access |""",
            ),
            (
                "2. Repository and first build",
                f"""Render the commands as a preformatted code block:

git clone {GITLAB_REPO}.git
cd api-test-automation
mvn -f mobile/pom.xml clean install -DskipTests

The build populates src/test/resources/config/ by unpacking the shared jsonapi-lib resource artifact; that folder is empty in a fresh clone and every *.properties file in it is gitignored. After the build, copy config.properties to <COMPUTERNAME>.properties and fill UNITEDATABASEURL, UNITEUSERNAME, and UNITEPASSWORD. The environment files unpacked beside it are stage1, qc4, qc1, stage5, and cat.

Prohibition callout: the host overlay is personal and gitignored. Never upload it to SharePoint and never copy another engineer's credentials.""",
            ),
            (
                "3. How a run resolves its target",
                """Render this diagram as a full-width monospace block, exactly as written:

  mvn -f mobile/<module>/pom.xml test
      "-P<suite-profile>,<environment-profile>"
      "-Dhost.properties=<COMPUTERNAME>.properties"
                 |
      +----------+-----------+-------------------+
      |          |           |                   |
  suite       environment   host overlay     report label
  profile      profile      (personal)      -Dmobile.ms.
      |          |           |               report.environment
      v          v           v
  which       stage1 or    Oracle URL,
  testsuites  qc4 .props   user, password
  XML + groups (LAST -P
      |        wins)
      v
  suite XML branding parameter
  okdirect | newyork | nmdirect
      |
      v
  service route from the environment file
  Mobile BFF (/mobile1api, /mobile2api) or Enrollment BFF (/enrollmentapi)

Caution callout: the environment profile must be last in -P. If it is listed first, the suite profile overwrites it and the run silently targets the wrong environment.""",
            ),
            (
                "4. Configuration precedence",
                """| Input | Selected by | Example |
|---|---|---|
| TestNG suite | Module suite profile | mobile2-regression |
| Environment properties | Environment profile listed last | acceptance-stage1 |
| Oracle connection | -Dhost.properties | <COMPUTERNAME>.properties |
| Report label | System property | -Dmobile.ms.report.environment=Stage1 |
| Branding | TestNG XML parameter | okdirect/newyork/nmdirect |

Example: "-Pmobile2-regression,acceptance-stage1" means use Mobile 2 regression XML, then force stage1.properties. Reversing profile order can target the wrong environment.""",
            ),
            (
                "5. Environment use",
                """| Environment | Use | Caveat |
|---|---|---|
| Stage1 | Primary regression and sign-off evidence | Refresh can invalidate users and data |
| QC4 | Integration and environment proof | Stability, IDP/reverse proxy, and refresh dependencies can block runs |
| Localhost suite | Narrow local class/branding selection | Still points to chosen Stage1/QC4 services unless a local service URI is configured |

Enrollment uses the cloud Enrollment BFF. Mobile login may use a different BFF; do not swap base URIs. Enrollment POST bodies are encrypted; GET calls may be plain.""",
            ),
            (
                "6. Manual-tool environments",
                f"""| Tool | Setup |
|---|---|
| Bruno | Open Unite-MSC-Bruno_collection; choose Enrollment, Mobile1, or Mobile2 folder |
| Bruno Stage1 environments | Env-Enrollment-Stage1.yml, Env-Mobile1-Stage1.yml, Env-Mobile2-Stage1.yml; treat populated values as sensitive |
| Postman | Use approved Mobile collection for IDP/mobile token exploration |
| qTest | Open the matching module folder under Test Design |

Bruno: {GITLAB_BRUNO}

qTest modules:
{qtest_modules_table()}

Use request folders to explore contracts. Do not paste Bruno/Postman environment contents into SharePoint, Jira, or Teams. Prefer a local stripped environment for demonstrations; treat committed Stage1 environment YAML as sensitive operational material.""",
            ),
            (
                "7. Setup verification",
                """- [ ] Maven parent build succeeds.
- [ ] java -version and mvn -version meet repo requirements.
- [ ] Personal host overlay is outside git status.
- [ ] acceptance-stage1 / acceptance-qc4 is last in the Maven profile list.
- [ ] Enrollment smoke reaches the intended environment.
- [ ] target/mobile-ms-report/index.html opens.
- [ ] Bruno collection and correct Stage1 environment open.
- [ ] No token, password, SSN, or private endpoint is pasted into a ticket or SharePoint.""",
            ),
        ],
    },
    {
        "num": "04",
        "title": "Daily Run Playbook",
        "slug": "daily-run-playbook",
        "purpose": "Repeatable daily workflow: choose the safe suite, verify data/environment, run the correct profile, inspect the portal, classify failures, and preserve evidence.",
        "prev": "03 Access, Setup and Environments",
        "next": "05 Mobile 1 Automation",
        "sections": [
            (
                "1. The daily loop",
                """Render this diagram as a full-width monospace block, exactly as written:

              what do you need today?
                        |
   +---------+----------+-----------+-------------+
   |         |          |           |             |
 is the    broad      proof in   mutating or   debugging
 service   module     selected     strict      one class
 healthy?  proof      environment  checks          |
   |         |          |           |              |
Enrollment regression integration  smoke     gitignored
  smoke    (Stage1)    (QC4)     (check owned localhost
                                  state first)    XML
   +---------+----------+-----------+-------------+
                        |
                        v
   mvn -f mobile/<module>/pom.xml test
       "-P<suite>,<environment LAST>"
                        |
                        v
   <module>/target/mobile-ms-report/index.html
                        |
                 earliest failure
                        |
   +--------+-----------+----------+-----------+
   |        |           |          |           |
 green  environment   data    automation    product
record   no code    restore    fix class   bug lifecycle
         change     fixtures   or wiring    + evidence

Work top to bottom every day. Pick the suite first, gate the run second, then read the report before changing a single line of test code.""",
            ),
            (
                "2. Choose the suite",
                """| Goal | Suite |
|---|---|
| Service/bootstrap health | Enrollment smoke |
| Broad read/non-destructive module coverage | regression |
| Integration proof in selected environment | integration |
| Mutating/destructive or strict checks | smoke |
| One class/branding while developing | gitignored localhost XML |

Mobile 1/2 smoke includes mutations; Enrollment smoke is health/reference GETs. Read the module page before treating every smoke suite as harmless.""",
            ),
            (
                "3. Pre-run gate",
                """1. Pull main and inspect the relevant module README/POM/XML.
2. Confirm module, suite, branding set, and Stage1 or QC4.
3. Confirm your personal host overlay exists and is not in git status.
4. Ask whether an Oracle refresh or service deployment occurred.
5. Confirm automation-owned auth/data prerequisites.
6. Put acceptance-stage1 or acceptance-qc4 LAST in -P.
7. For destructive smoke, inspect current owned state before running.""",
            ),
            (
                "4. Run commands by module",
                """Render as a preformatted code block. Replace <COMPUTERNAME> with your own host overlay.

# Enrollment
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-integration,acceptance-qc4" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=QC4"

# Mobile 1
mvn -f mobile/mobile1/pom.xml test "-Pmobile1-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"
mvn -f mobile/mobile1/pom.xml test "-Pmobile1-integration,acceptance-qc4" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=QC4"
mvn -f mobile/mobile1/pom.xml test "-Pmobile1-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

# Mobile 2
mvn -f mobile/mobile2/pom.xml test "-Pmobile2-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"
mvn -f mobile/mobile2/pom.xml test "-Pmobile2-integration,acceptance-qc4" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=QC4"
mvn -f mobile/mobile2/pom.xml test "-Pmobile2-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

The environment profile must stay LAST in -P. M1/M2 smoke and Enrollment suite profiles default to QC4 unless an acceptance overlay overrides them.""",
            ),
            (
                "5. Local targeted workflow",
                """1. Copy testsuites/localhost-testng.xml.example to localhost-testng.xml.
2. Keep one intended branding block and the required setup/target classes.
3. Never edit shared regression XML merely to debug locally.
4. For Enrollment, preserve the ordered prerequisite chain through the failing step.
5. Run the module localhost profile with the environment profile last.
6. Restore or discard only your gitignored localhost file after diagnosis.""",
            ),
            (
                "6. Read the result",
                """1. Open <module>/target/mobile-ms-report/index.html.
2. Confirm suite/module/environment labels.
3. Review pass/fail/skip totals and earliest failure.
4. Open extent/detail.html for test detail.
5. Use target/surefire-reports only for compile/setup stack traces or JUnit XML.
6. In an ordered Enrollment chain, fix the first failure before treating later skips as defects.""",
            ),
            (
                "7. Classify and act",
                """| Result | Action |
|---|---|
| Green | Record command, environment, branding, commit, report artifact |
| Environment/service | Record timestamp/status/dependency; do not edit tests |
| Oracle/test data | Restore only approved automation fixtures |
| Automation | Reproduce targeted; fix class/XML/profile/reporting wiring |
| Product/contract | Follow automation bug lifecycle with sanitized evidence |
| Expected exclusion | Link sign-off/backlog; do not report as missing coverage |""",
            ),
            (
                "8. Run record",
                """Minimum evidence:
- module and profile command;
- environment and branding;
- commit SHA and run timestamp;
- passed/failed/skipped counts;
- first failure class/method and endpoint ID;
- sanitized portal/Surefire or GitLab artifact;
- classification and Jira link.

Code presence is not fresh execution evidence.""",
            ),
            (
                "9. Run discipline",
                """Prohibition callout:
- Do not silently remove classes from XML to make a run green.
- Quarantine only with a visible tag or exclusion and a linked follow-up.
- Do not commit target/.
- Do not loop-retry an environment-wide failure.
- Do not rerun destructive tests against unknown records.
- Do not attach raw request or response payloads containing PII or JWT.""",
            ),
        ],
    },
    {
        "num": "05",
        "title": "Mobile 1 Automation",
        "slug": "mobile-1-automation",
        "purpose": "Complete operating guide for Mobile 1: delivered coverage, endpoint families, authentication/data model, suite design, execution, evidence, and safe extension.",
        "prev": "04 Daily Run Playbook",
        "next": "06 Mobile 2 Automation",
        "sections": [
            (
                "1. What was delivered",
                """| Metric | Delivered |
|---|---|
| Endpoint operations automated | 26 of 26 documented |
| TestNG @Test methods | 27 |
| Validation | L1-L4 lean assertions |
| Branding in current regression/integration XML | okdirect, newyork, nmdirect |
| Sign-off | COMPLETE |

This is a full canonical migration, not a wrapper around legacy Cucumber. It adds current TestNG, SQL-driven automation users, mobile/IDP authentication, multi-plan XML execution, and the shared HTML reporting portal.""",
            ),
            (
                "2. Endpoint families",
                """| Family | Coverage |
|---|---|
| Authentication | member session, username, CSR-as-member, IDP exchange, IDP-to-member token |
| Profile and beneficiary | owner/profile menus, owner update, beneficiary lookup, close-account checks |
| Security and device | biometric POST/GET/DELETE, phone authentication, devices, push tokens |
| Session | session by ID, biometric-token validation, session PIN |
| Account utility | routing-number bank info, password change and re-login |

The register assigns stable IDs M1-01 through M1-26 so an endpoint can be traced from sign-off CSV to Java method, suite, evidence, qTest, and Jira.""",
            ),
            (
                "3. Suite strategy",
                """| Suite | Current XML shape | Intent |
|---|---|---|
| mobile1-regression-testng.xml | 16 classes per plan; all 3 plans | Broad read/non-destructive coverage |
| mobile1-integration-testng.xml | Same 16 classes per plan | Environment/integration validation |
| mobile1-smoke-testng.xml | 5 OKD; 6 NY; 6 NMD classes | Mutating/targeted flows |
| localhost-testng.xml.example | 16 classes per plan | Gitignored local ad-hoc copy |

Smoke holds owner PUT, actual account close, biometric DELETE, session lookup/biometric validation, and password rotation where applicable. Never move a destructive class into unattended regression merely to increase the count.""",
            ),
            (
                "4. Authentication and IDP token flow",
                """Render this diagram as a full-width monospace block, exactly as written:

  [ Oracle: automation login user for this branding ]
                    |
                    v
  [ POST /mobile1api/v1/mobilemembersession ]  public, plaintext login
                    |
             member JWT
                    |
        +-----------+-------------------------+
        |                                     |
        v                                     v
  [ Mobile 1 endpoints ]              IDP-enabled branding only
  [ Mobile 2 endpoints ]                      |
   Bearer member JWT                          v
                        [ POST /mobile1api/v1/idptokenexchange ]
                                              |
                                   IDP access token
                                              |
                                              v
                        [ POST /mobile1api/v1/mobilememberidptoken ]
                                              |
                                              v
                               [ member session for the IDP user ]

Non-IDP plans stop at the first member JWT. IDP plans continue through exchange and token-to-session. The automation exchange token is often rejected by the final step by design; a real PKCE token can be supplied with -Duse-pkce-idp-token=true, otherwise the test validates the contract fallback and the upstream steps.""",
            ),
            (
                "5. Test data resolution",
                """MobileBaseRequestTest loads mobile.sql before the suite:

1. Selects an active automation-owned member for the current branding.
2. Requires the approved MFA-skip condition.
3. Resolves account extension, member ID, minimum app version, and routing/fixture data from Oracle.
4. Configures mobile session auth or IDP auth based on plan metadata.
5. Probes several candidate users for IDP-enabled plans and caches a working user.

Do not hardcode a customer, password, account extension, app version, or src/test/resources/user JSON into a new test.""",
            ),
            (
                "6. Run and read the result",
                """Regression command:

mvn -f mobile/mobile1/pom.xml test "-Pmobile1-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

Other suite profiles: mobile1-integration, mobile1-smoke, mobile1-localhost. Keep acceptance-stage1 or acceptance-qc4 LAST.

Open target/mobile-ms-report/index.html for the portal and target/surefire-reports/ for TestNG detail.""",
            ),
            (
                "7. Evidence and downloads",
                f"""| Artifact | Use |
|---|---|
| Mobile 1 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile1-endpoint-current-state.csv | Endpoint to class to suite mapping |
| mobile1-signoff-summary.md | Quick status |
| Coverage chart | Optional executive visual |
| GitLab mobile/mobile1 | Executable source of truth |
| Bruno 02 - Mobile1 | Manual request exploration |
| qTest MSC-Mobile1 | Manual test cases: {QTEST_MOBILE1} |""",
            ),
            (
                "8. Known boundaries and first checks",
                """Caution callout:
- Canonical TestNG includes IDP token exchange that legacy Cucumber did not.
- A QC4 401 can be an environment/IDP automation-JWT issue, not a missing class.
- PATCH logout remains an enhancement; do not count it as delivered.
- L5 field-by-field SQL reconciliation was analyzed but is not the sign-off gate.

When a case fails, capture endpoint ID, Java class/method, suite, branding, environment, HTTP status, and sanitized report link—not only a screenshot.""",
            ),
        ],
    },
    {
        "num": "06",
        "title": "Mobile 2 Automation",
        "slug": "mobile-2-automation",
        "purpose": "Complete Mobile 2 guide: 96% signed-off business coverage, endpoint families, Mobile 1 reuse, suite separation, dynamic fixtures, execution, and evidence.",
        "prev": "05 Mobile 1 Automation",
        "next": "07 Enrollment Automation",
        "sections": [
            (
                "1. What was delivered",
                """| Metric | Delivered |
|---|---|
| Catalog rows | 25 |
| In-scope business operations automated | 24 |
| Signed-off business coverage | 96.0% |
| Validation | L1-L4 lean assertions |
| Current regression/integration branding | okdirect, newyork, nmdirect |
| Sign-off | COMPLETE |

The only excluded catalog row is the acceptance harness GET mobilemembers/{planId}/{username}; it is not a missing business API. Mobile 2 reuses Mobile 1 authentication instead of duplicating login code.""",
            ),
            (
                "2. Endpoint families",
                """| Family | Coverage |
|---|---|
| Account experience | dashboard, YTD summary, activity, transaction history |
| Portfolio | investments, balance trend, performance, stackup |
| Banks | list/detail, add, update, delete |
| Contributions | options/check/detail, create, update, delete |
| Reference/content | content and plans/list/detail |
| Engagement | UGift page and UGift assignment |

IDs M2-01 through M2-25 trace each row to its TestNG class, method, suite, plants, and legacy/Postman source.""",
            ),
            (
                "3. Suite strategy",
                """| Suite | Current XML shape | Intent |
|---|---|---|
| mobile2-regression-testng.xml | 16 classes per plan; all 3 plans | Broad read/non-destructive coverage |
| mobile2-integration-testng.xml | Same 16 classes per plan | Environment/integration validation |
| mobile2-smoke-testng.xml | 6 classes per plan | Mutating and strict checks |
| localhost-testng.xml.example | 16 classes per plan | Local gitignored copy |

Smoke runs bank mutations, contribution POST/PUT/DELETE, UGift PATCH, and strict stackup. Regression/integration also include the acceptance harness GET mobilemembers/{planId}/{username} for observation; it remains outside the 24/25 business numerator. Its member-JWT 401 is expected until acceptance-harness auth is wired—do not treat that alone as a product or coverage defect.""",
            ),
            (
                "4. Where Mobile 2 data comes from",
                """Render this diagram as a full-width monospace block, exactly as written:

  [ Mobile 2 test ]  auth context inherited from Mobile 1
              |
              v
  [ Mobile BFF /mobile2api ] -> [ unite-mobile2 ]
              |
   +----------+-----------------------------+
   |  Account (unite-account)               |  accounts, balances, YTD
   |  Profile (unite-profile)               |  owner, beneficiary
   |  Metadata (unite-metadata)             |  plans, funds, prices
   |  Bank (unite-bank)                     |  bank list, add, update, delete
   |  Transaction gateway                   |  activity, transaction history
   |  On-prem account gateway               |  dashboard banks, withdrawals
   +----------+-----------------------------+
              |
              v
  [ Oracle MSC schemas ]  +  [ on-prem systems of record ]

Informational callout: dashboard bank and withdrawal fields come from the on-prem gateway, not the Oracle MSC tables, so an Oracle field comparison does not apply to them. Transaction history and YTD depend on the plan's backend type, which is why the same assertion can behave differently across brandings.

Mobile 2 extends MobileBaseRequestTest and gets authentication/account context from Mobile 1. Oracle SQL resolves:

- automation-owned login user and account extension;
- active recurring-contribution fixture ID;
- routing number and bank fixture;
- minimum supported mobile app version.

Contribution DELETE is restricted to automation-owned data. New tests must not hardcode account /01, a bank ID, a contribution ID, a customer username, or a routing number.""",
            ),
            (
                "5. Run and read the result",
                """Regression command:

mvn -f mobile/mobile2/pom.xml test "-Pmobile2-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

Other profiles: mobile2-integration, mobile2-smoke, mobile2-localhost. Keep the environment profile last. If Mobile 2 compilation is stale, delete mobile/mobile2/target/maven-compile; delete Mobile 1's compiled output too if the inherited auth class is stale.

Report: mobile/mobile2/target/mobile-ms-report/index.html.""",
            ),
            (
                "6. Evidence and downloads",
                f"""| Artifact | Use |
|---|---|
| Mobile 2 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile2-endpoint-current-state.csv | Endpoint to class to suite mapping |
| unite-msc-endpoint-summary.csv | Compact evidence register |
| Coverage chart | Optional executive visual |
| GitLab mobile/mobile2 | Executable source of truth |
| Bruno 03 - Mobile2 | Manual request exploration |
| qTest MSC-Mobile2 | Manual test cases: {QTEST_MOBILE2} |""",
            ),
            (
                "7. Known boundaries and enhancements",
                """Caution callout:
- Destructive bank/contribution cases stay separated from broad regression.
- Dynamic fixtures can fail after an Oracle refresh even when the API is healthy.
- POST mobilebanks?planId=upromise is optional enhancement scope, not part of the 24 signed-off business operations.
- Two MobileStackupRequestTest package locations are a cleanup candidate; do not duplicate a third.

Use current GitLab POM/XML as executable truth. Capture row ID, class/method, branding, suite, environment, status, and sanitized report during triage.""",
            ),
        ],
    },
    {
        "num": "07",
        "title": "Enrollment Automation",
        "slug": "enrollment-automation",
        "purpose": "End-to-end Enrollment operating guide: delivered coverage, ordered encrypted wizard, subsequent enrollment, suite/plants, data/session design, execution, and handoff evidence.",
        "prev": "06 Mobile 2 Automation",
        "next": "08 Coverage, Traceability and Sign-off",
        "sections": [
            (
                "1. What was delivered",
                """Handoff: Jira QA-893

| Metric | Position |
|---|---|
| Catalog rows | 28 |
| Automated | 25 |
| Deferred | 3 |
| Catalog coverage | 89.3% |
| Ordered regression/integration chain | 17 classes per plant |
| Current plants in XML | okdirect, newyork, nmdirect |
| Validation | L1-L4 + targeted post-account SQL verification |

Deferred partner submit, Upromise account, and OAuth token are explicit scope decisions tied to QA-1808/QA-1807—not missing MSC happy-path coding.""",
            ),
            (
                "2. Ordered first-enrollment wizard",
                """Render this diagram as a full-width monospace block, exactly as written:

  [ 1 prospects ]            POST enrollments/prospects     public
        | issues prospect JWT -> ProspectSessionContext
        v
  [ 2 enrollment-started ]   public, same username
        v
  [ 3 content ]              GET, Bearer prospect JWT
        v
  [ 4 owner-entered ] ----------------+
        v                             |  carried forward
  [ 5 owner-address-entered ]         |  through every
        v                             |  later step:
  [ 6 beneficiary-entered ] ----------+   prospect JWT
        v                             |   username + branding
  [ 7 verify/routingnumber ]          |   AES key + encAesKey
        v                             |   eventId, correlationId,
  [ 8 bank-entered ] ----------------+    seqNum
        | stores bank on session      |   owner, beneficiary,
        v                             |   bank objects
  [ 9 recurring-contribution ] ------+
        | keeps the recurring ciphertext as-is
        v
  [ 10 enrollmentallocationfunds/get ]   returns fundIds
        v
  [ 11 allocations-entered ]
        v
  [ 12 review-confirm-entered ]  + GET plans/{branding}
        |                          for prefix + deprecatedId
        v
  [ 529 account created ]  ext=01
        v
  optional post-submit SQL verify: account, login, member rows

Every step depends on state produced earlier, so the chain runs sequentially, never in parallel. A failure at step 4 makes steps 5-12 skip; fix the earliest failure first. Review-confirm logs only sanitized identifiers.""",
            ),
            (
                "3. How Enrollment reaches account services",
                """Render this diagram as a full-width monospace block, exactly as written:

  [ enrollment test ]
        |
        v
  [ Enrollment BFF /enrollmentapi ]
        |
        v
  [ unite-enrollment gateway ] -- calls the owning service per step
        |
   +----+-------+---------+----------+--------+
   |    |       |         |          |        |
  Auth Account Profile  Metadata   Bank   (per step)
        |
        v
  [ Oracle schemas ]

| Wizard step | Downstream service | Main tables |
|---|---|---|
| prospects | Auth (token), Account, Metadata | login, fraud-block, traunch |
| owner, owner address | Profile, Account | person, address, account |
| beneficiary | Profile, Account | beneficiary, fraud-block |
| verify routing | Bank | bank info |
| bank, recurring | Bank, Metadata | bank info, bank, traunch |
| allocation funds, allocations | Metadata, Account | traunch fund, funds, metadata |
| review-confirm | Account, Metadata | account, login, member, codes |
| plans, states, country | Metadata | traunch, country, codes |

The test never calls Account or Profile directly; it always goes through the Enrollment BFF and gateway. That is why a single downstream outage, for example the gateway failing to reach prospect verification in Account, surfaces as a failure on one specific wizard step rather than as a broad automation defect.

Informational callout: SQL is used to prepare fixtures before the run and to verify the created account afterwards. Mid-wizard steps assert the HTTP response only.""",
            ),
            (
                "4. Subsequent enrollment for an existing member",
                """Render this diagram as a full-width monospace block, exactly as written:

  [ Oracle: existing automation member for this branding ]
        |
        v
  [ POST /mobile1api/v1/mobilemembersession ]  public plaintext login
        | member JWT  (kept separate from the prospect session)
        v
  [ GET subsequentenrollment/banks ]
        v
  [ subsequentenrollment/beneficiary-entered ]
        v
  [ subsequentenrollment/bank-entered ]
        v
  [ subsequentenrollment/recurring-contribution-entered ]
        v
  [ subsequentenrollment/review-confirm-entered ]  ext=02

Subsequent enrollment adds another account extension for a member who already exists, so it authenticates through the Mobile 1 session endpoint rather than the prospect flow. The prospect context from first enrollment must not be overwritten while this chain runs.""",
            ),
            (
                "5. Encryption and session architecture",
                """Render this diagram as a full-width monospace block, exactly as written:

  [ GET /enrollmentapi/v1/certificate ]  -> public key
        v
  [ generate one AES key for the whole wizard ]
        | RSA-wrapped as encAesKey
        v
  [ fields marked @MobileEncrypt ] -> encrypted request payload
        v
  [ review-confirm ]
     encrypted : owner, beneficiary, bank, member
     plaintext : account (prefix, ext, planId, state), terms accepted
     spliced   : recurring ciphertext from step 9, never re-encrypted

Double-encrypting a payload that is already ciphertext is the most common cause of a decrypt or session error on review-confirm.

- Prospect POST creates the JWT and stores it in ProspectSessionContext.
- Later steps reuse the JWT, plan, username, AES key, event IDs, and prior business objects.
- Sensitive POJO fields use @MobileEncrypt; requests go through EnrollmentBaseTest encryption helpers.
- Review-confirm splices existing recurring ciphertext instead of encrypting ciphertext again.
- JSON fixtures use generated usernames/SSNs; there is no Enrollment delete API.

Prohibition callout: never paste plaintext payloads, certificate material, AES data, JWT, SSN, bank numbers, or environment JSON into SharePoint or Jira.""",
            ),
            (
                "6. Suites and profiles",
                """| Profile | Current XML | Purpose |
|---|---|
| mobile-ms-enrollment-smoke | 5 OK Direct classes | ping, certificate, US states, country, plans |
| mobile-ms-enrollment-regression | 17 classes x 3 plants | Full first + subsequent enrollment |
| mobile-ms-enrollment-integration | 17 classes x 3 plants | Same chain for integration validation |
| mobile-ms-enrollment-localhost | localhost XML copy | Local ad-hoc chain |

The wizard is sequential, not parallel: each class depends on state produced by prior steps. New steps must be inserted in correct order in every branding block.""",
            ),
            (
                "7. Run and report",
                """Smoke:
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

Full regression:
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

Report: mobile/enrollment/target/mobile-ms-report/index.html.

Start with smoke after a refresh. Do not run the full wizard until certificate, metadata, plan, fund, routing, and authentication prerequisites are healthy.""",
            ),
            (
                "8. Evidence, handoff, and boundaries",
                f"""| Artifact | Use |
|---|---|
| Enrollment API Automation Sign-Off | Scope, exclusions, acceptance |
| Enrollment coverage matrix/workbook | 28-row catalog and 25 automated rows |
| enrollment-endpoint-current-state.csv | Endpoint/class/suite/plant register |
| Architecture and Execution guides | Setup, run, troubleshoot |
| DB Refresh Checklist | Restore data after refresh |
| AI Scenario Guide | Extend the ordered wizard |
| Bruno 01 - Enrollment | Manual endpoint exploration |
| qTest MSC-Enrollment | Manual test cases: {QTEST_ENROLLMENT} |

Caution callout: QC4 instability, IDP/reverse-proxy behavior, plan metadata, or refreshed data can block proof without indicating an automation defect. Enrollment nightly remains separate delivery scope until a verified job exists.""",
            ),
            (
                "9. Current-vs-historical source rule",
                """Current executable truth is mobile/enrollment/pom.xml and the current TestNG XML, which contain okdirect, newyork, and nmdirect blocks. Prefer mobile/enrollment/README.md for current commands.

If an older Architecture, Sign-Off, coverage file, or enhancement backlog says Enrollment has only two regression plants, NM Direct is localhost-only, Bruno is missing, or a nightly is live, treat that statement as historical until the attachment is refreshed. Do not claim a GitLab nightly without a verified CI job.""",
            ),
        ],
    },
    {
        "num": "08",
        "title": "Coverage, Traceability and Sign-off",
        "slug": "coverage-traceability-and-sign-off",
        "purpose": "Executive coverage story and reviewer drill-down: what was automated, how much improved over legacy, where every endpoint maps, and what COMPLETE means.",
        "prev": "07 Enrollment Automation",
        "next": "09 Reporting and Troubleshooting",
        "sections": [
            (
                "1. Coverage at a glance",
                """| Module | Catalog | Automated business operations | Coverage | Sign-off |
|---|---:|---:|---:|---|
| Mobile 1 | 26 | 26 | 100% | COMPLETE |
| Mobile 2 | 25 | 24 | 96.0% | COMPLETE; one harness excluded |
| Enrollment | 28 | 25 | 89.3% | COMPLETE for MSC scope; 3 partner APIs deferred |
| Total | 79 | 75 | 94.9% | L1-L4 completion boundary |

This is 75 canonical business API operations across Mobile 1, Mobile 2, and Enrollment—not merely converted scripts. The work adds multi-plan suites, SQL-driven data, IDP paths, mobile encryption, subsequent enrollment, lean assertions, and reusable reporting.""",
            ),
            (
                "2. Legacy-to-canonical scorecard",
                """| Delta in the 83-row traceability matrix | Rows |
|---|---:|
| Improved | 47 |
| Newly added | 22 |
| Unchanged | 6 |
| Explicitly excluded | 6 |
| Missing/backlog | 2 |

69 of 83 traced rows are improved or newly added. Improvements include IDP token flows absent from legacy Cucumber, encrypted Enrollment requests, dynamic Oracle fixtures, multi-plan execution, dashboard consolidation from eight scenarios to one lean test, and subsequent Enrollment APIs missing from the early spreadsheet.""",
            ),
            (
                "3. What COMPLETE means",
                """- Every in-scope operation has a canonical Java class/method and stable endpoint ID.
- The class is wired into an intended TestNG suite/profile and branding block.
- L1 HTTP, L2 contract, L3 typed/schema where supported, and L4 business assertions are present.
- Coverage registers and formal sign-off packs record exclusions and enhancement scope.
- Code presence is not a current green run; execution evidence remains run-specific.
- L5 universal API-to-DB reconciliation is documented analysis, not the approved completion gate.""",
            ),
            (
                "4. Coverage sources",
                f"""| Source | System of record |
|---|---|
| Mobile 1 | mobile1-endpoint-current-state.csv |
| Mobile 2 | mobile2-endpoint-current-state.csv |
| Enrollment | enrollment-endpoint-current-state.csv and the coverage workbook |
| Legacy to canonical | legacy-to-canonical-traceability.csv |
| Automated implementation | {GITLAB_MOBILE} |
| Manual API collection | {GITLAB_BRUNO} |
| Delivery scope and stories | {JIRA_EPIC} |

Manual test cases (qTest):
{qtest_modules_table()}""",
            ),
            (
                "5. Trace one endpoint end to end",
                f"""1. Pick the endpoint ID in the module register.
2. Confirm method/path, feature area, migration status, validation layers, and branding.
3. Open the canonical Java class/method in {GITLAB_MOBILE}
4. Confirm its suite XML, Maven profile, groups, and every intended branding block.
5. Confirm the manual Bruno request where one exists: {GITLAB_BRUNO}
6. Confirm or create the qTest manual case in the matching module folder (Unite-MSC, MSC-Enrollment, MSC-Mobile1, or MSC-Mobile2).
7. Link the case and automation evidence to the delivering Jira story under {JIRA_EPIC}
8. Open the formal sign-off pack for exclusions/approvals.
9. Attach a sanitized report or job artifact; never use code presence as run evidence.

qTest modules:
{qtest_modules_table()}""",
            ),
            (
                "6. Evidence package",
                """| Evidence | Reviewer use |
|---|---|
| Three formal sign-off documents | Scope, metrics, exclusions, approval |
| Three endpoint current-state registers | Row-level class/method/suite/plant mapping |
| Enrollment coverage workbook/catalog | Original catalog vs delivered status |
| Legacy-to-canonical DOCX + CSV | 83-row comparison and improvements |
| Enhancement backlog | Deferred/non-defect next-layer scope |
| HTML portal + Surefire/GitLab artifacts | Actual execution result |

Approvals marked [NEED_INPUT] remain open until names/dates are supplied. Never manufacture an approval.""",
            ),
            (
                "7. Explicit exclusions and next layer",
                """Not missing business coverage:
- Mobile 2 acceptance harness GET mobilemembers/{planId}/{username}.
- Operations health/OpenAPI utilities outside the business API numerator.
- Enrollment partner submit, Upromise, and OAuth deferred under separate scope.

Enhancement backlog:
- PATCH logout session and optional Upromise bank variant.
- Broader negative/contract tests.
- qTest-to-Jira linkage completion.
- Verified Enrollment nightly job.
- Optional L5 SQL field reconciliation only if leadership reopens it.

The original traceability snapshot said no Bruno files existed. The current GitLab repository now contains the Unite MSC Bruno collection; use the current repo, not that historical gap statement.""",
            ),
            (
                "8. Source freshness rule",
                """For executable behavior and plants, current POM/TestNG XML wins. Some historical sign-off/coverage attachments predate three-plan XML and the Bruno collection. Until refreshed, do not use an older CSV plant column to dispute current okdirect/newyork/nmdirect XML.

Current .gitlab-ci.yml does not prove a Mobile 2 or Enrollment nightly. Describe nightly enablement as unverified/follow-up unless an actual current job and schedule are reviewed.""",
            ),
        ],
    },
    {
        "num": "09",
        "title": "Reporting and Troubleshooting",
        "slug": "reporting-and-troubleshooting",
        "purpose": "How to read the generated reporting portal, isolate the first real failure, distinguish environment/data/automation/product issues, rerun safely, and capture useful evidence.",
        "prev": "08 Coverage, Traceability and Sign-off",
        "next": "10 Test Data, DB Refresh and Security",
        "sections": [
            (
                "1. Reporting outputs",
                """| Output | Location | Use |
|---|---|
| Portal landing page | <module>/target/mobile-ms-report/index.html | Overall status, counts, suite/module/environment |
| Extent detail | target/mobile-ms-report/extent/detail.html | Per-test steps, duration, sanitized failure |
| Portal pages | target/mobile-ms-report/pages/ | details, categories, logs, history, about |
| Summary/history JSON | target/mobile-ms-report/data/ | machine-readable run and trend data |
| Surefire/TestNG | <module>/target/surefire-reports/ | stack trace, skipped dependency, JUnit XML |
| GitLab job log and artifacts | CI environment and command |
| Jira or bug evidence folder | Product or recurring automation defect |""",
            ),
            (
                "2. Read the run in this order",
                """1. Confirm module, suite, environment, and branding are what you intended.
2. Check passed/failed/skipped counts in index.html.
3. Open the earliest failed class in the ordered chain.
4. Read the HTTP status, assertion, sanitized failure reason, and duration.
5. Treat later Enrollment skips as downstream symptoms until the first failed wizard step is resolved.
6. Cross-check Surefire only when the portal lacks the compile/setup stack trace.
7. Check recent deployment or database-refresh timing before changing code.""",
            ),
            (
                "3. Triage decision tree",
                """Render this diagram as a full-width monospace block, exactly as written:

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

Classification decides who acts next. Never change test code to silence a failure you have not classified.""",
            ),
            (
                "4. First-failure classifier",
                """| Symptom | Likely class | First action |
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
| One stable L4 assertion fails | Product or changed contract | Reproduce targeted and compare approved expectation |""",
            ),
            (
                "5. Safe rerun strategy",
                """| Failure type | Rerun |
|---|---|
| Enrollment wizard step | Rerun the full ordered plan chain; do not start at a dependent middle step |
| Read-only Mobile 1/2 class | Use a gitignored localhost XML containing setup + target class |
| Destructive smoke test | Inspect existing state first; rerun only with automation-owned data |
| Multi-plan failure | Reproduce only the failed branding locally, then restore full XML |
| Environment-wide failure | Do not loop retries; wait for confirmed dependency recovery |

Never delete a class from shared regression XML to create a green result. Any temporary local narrowing stays in a gitignored localhost suite.""",
            ),
            (
                "6. Minimum evidence for escalation",
                """Capture:
- Jira story/bug and endpoint ID.
- Timestamp, environment, branding, suite/profile, commit SHA.
- Java class/method and HTTP method/path.
- Expected vs actual status/business assertion.
- Portal/Surefire artifact and whether targeted rerun reproduced.
- Recent deploy/refresh/dependency context.
- Classification: environment, data, automation, product, or expected exclusion.

Use the automation bug lifecycle for product/recurring automation defects.""",
            ),
            (
                "7. Security and report sanitization",
                """SensitiveDataSanitizer masks bearer tokens, JWT-like strings, passwords, client secrets, and signing keys in report text.

Prohibition callout: sanitization is defense in depth. Never deliberately log or attach passwords, tokens, SSN, bank data, certificates, host overlays, environment JSON, DB credentials/URLs, or raw personal payloads. Redact account identifiers unless the approved internal process requires them.""",
            ),
        ],
    },
    {
        "num": "10",
        "title": "Test Data, DB Refresh and Security",
        "slug": "test-data-db-refresh-and-security",
        "purpose": "Oracle-backed automation data, post-refresh recovery, safe fixture ownership, targeted SQL use, the L5 boundary, and strict secret/PII handling.",
        "prev": "09 Reporting and Troubleshooting",
        "next": "11 Extend the Automation",
        "sections": [
            (
                "1. What Oracle is used for",
                """| Use | Modules |
|---|---|
| Select approved automation member/account and IDP metadata | Mobile 1, Mobile 2, subsequent Enrollment |
| Resolve minimum supported app version | All mobile modules |
| Resolve account extension, member ID, routing/bank | Mobile 1 and Mobile 2 |
| Resolve recurring-contribution fixture ID | Mobile 2 |
| Resolve active fund/plan data and verify created account | Enrollment |

SQL is a controlled fixture/provider layer. It is not permission to browse or mutate arbitrary customer-like data.""",
            ),
            (
                "2. Data rules",
                """- Use only approved automation-owned member/account patterns.
- Generate unique Enrollment username and SSN values through framework placeholders.
- Never hardcode a password, account extension, member ID, bank/contribution ID, routing number, fund ID, or app version in Java.
- Mutating/delete cases must prove they own the record.
- Keep SQL in the module SQL file with a named key and branding placeholder.
- Record environment and branding with evidence; never publish returned rows.""",
            ),
            (
                "3. After a database refresh",
                """Render this diagram as a full-width monospace block, exactly as written:

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
9. Record unresolved data/environment gaps in Jira; do not weaken assertions to pass.""",
            ),
            (
                "4. Host overlay and configuration",
                """The personal <COMPUTERNAME>.properties file supplies UNITEDATABASEURL, UNITEUSERNAME, and UNITEPASSWORD. It lives under the module's src/test/resources/config/ path and is passed with -Dhost.properties.

Environment files such as stage1.properties and qc4.properties select service behavior; Maven acceptance-stage1/acceptance-qc4 profiles select which file wins.

Prohibition callout: never copy another engineer's host overlay or store one in SharePoint, Jira, Teams, qTest, Bruno, Postman, or Git.""",
            ),
            (
                "5. SQL validation boundary",
                """| Level | Status |
|---|---|
| SQL for fixture selection/setup | Implemented and used |
| Enrollment account-created verification | Implemented targeted validation |
| L1-L4 API validation | Approved sign-off requirement |
| Universal API-field to DB-field reconciliation (L5) | Analysis/SQL handoff only; not implemented completion gate |

Rajib and Henry directed the team not to make L5 universal reconciliation mandatory because mappings require developer/SME involvement and are costly to sustain. Mobile 1/2 analysis and candidate SQL remain a future-team handoff, not a failed deliverable.""",
            ),
            (
                "6. Never upload or log",
                """Prohibition callout:
- Postman environment JSON.
- Local host/property overlays or DB URLs.
- Passwords, tokens, cookies, certificates, private keys, SSN, bank data, or raw PII.
- Database connection strings.
- Raw SQL exports containing customer-like data.
- target/ reports that include unsanitized payloads.
- Screenshots showing credentials, tokens, or personal records.

SharePoint links to controlled Git paths and ticketing processes. It is not a secret store or an executable configuration source.""",
            ),
            (
                "7. Refresh-ready definition of done",
                """- [ ] Automation users exist for all required brandings and satisfy auth prerequisites.
- [ ] Minimum version, plan/fund, bank/routing, and contribution queries return approved fixtures.
- [ ] Enrollment health smoke is green.
- [ ] One read-only Mobile 1 and Mobile 2 path is green.
- [ ] Full ordered Enrollment chain completes before broad sign-off.
- [ ] No credentials/PII appear in logs, reports, tickets, or SharePoint.
- [ ] Remaining environment/data dependency has a Jira owner and evidence.""",
            ),
        ],
    },
    {
        "num": "11",
        "title": "Extend the Automation",
        "slug": "extend-the-automation",
        "purpose": "New-endpoint playbook and prompt library: discovery, TestNG implementation, encryption/data, suite wiring, Bruno/qTest/Jira traceability, verification, review, and documentation.",
        "prev": "10 Test Data, DB Refresh and Security",
        "next": None,
        "sections": [
            (
                "1. The new-endpoint workflow",
                """Render this diagram as a full-width monospace block, exactly as written:

  [ intake ]     contract, auth, branding, data, safety, suites
        v
  [ discovery ]  reference class, POM, suite XML, fixtures,
                 Bruno request, qTest case
        v
  [ implement ]  POJO -> base-class auth -> request -> L1-L4
        v
  [ wire ]       group -> every branding block -> suite XML
                 -> Maven profile -> report listener
        v
  [ verify ]     compile -> targeted -> one branding
                 -> all brandings -> impacted regression
        v
  [ trace ]      Bruno request -> qTest case -> Jira link
                 -> coverage register
        v
  [ review ]     merge request: Summary, Related, Test plan, Risks
        v
  [ done ]       wired, evidenced, registers updated

Skipping the wire step is the most common failure: the code compiles and passes locally but never runs in any suite, so it is not delivered coverage.""",
            ),
            (
                "2. Intake before coding",
                f"""Capture in the Jira story:

| Field | Required answer |
|---|---|
| Module | Mobile 1, Mobile 2, or Enrollment |
| Contract | method, path, headers, parameters, request/response shape |
| Auth | public, mobile JWT, IDP, prospect JWT, or member JWT |
| Branding | okdirect, newyork, nmdirect differences |
| Data | Oracle query, generated fixture, or prior-step context |
| Safety | read-only, creates owned data, mutates/deletes |
| Suites | regression, integration, smoke, localhost |
| Assertions | L1-L4 expected behavior |

Sources: canonical code {GITLAB_MOBILE}, Bruno {GITLAB_BRUNO}, qTest modules (Unite-MSC / MSC-Enrollment / MSC-Mobile1 / MSC-Mobile2), and the delivering story under {JIRA_EPIC}. Do not code from a screenshot or memory.

qTest:
{qtest_modules_table()}""",
            ),
            (
                "3. Choose the module pattern",
                """| Endpoint type | Extend/reuse |
|---|---|
| Mobile 1 auth/profile/session/device | MobileBaseRequestTest + nearest mobile1 class |
| Mobile 2 account experience | Existing Mobile 2 class; reuse Mobile 1 auth/account context |
| Enrollment wizard POST | EnrollmentBaseTest + ProspectSessionContext + encryption helpers |
| Enrollment subsequent POST | Existing-member context + encrypted payload |
| HAL list GET | Existing GenericEmbeddedPOJO pattern; avoid one-off wrappers |

Follow the nearest working endpoint in the same module. Do not change shared framework APIs or unrelated POJOs merely to make one endpoint compile.""",
            ),
            (
                "4. Implement the TestNG case",
                """1. Add/reuse one request/response POJO per file following Lombok/Jackson conventions.
2. Put endpoint path and fixture name in the test class.
3. Use framework loaders/placeholders, not hardcoded IDs or personal data.
4. Configure auth through the module base class.
5. Build the request with the framework Rest Assured client.
6. Assert L1 status, L2 contract, L3 typed/schema where useful, and L4 business outcome.
7. Keep assertions lean and diagnostic; do not dump full bodies.
8. For mutation/delete, prove the record is automation-owned and leave deterministic state.""",
            ),
            (
                "5. Enrollment-specific rules",
                """- Extend EnrollmentBaseTest, not BaseRequestTest directly.
- Load fixture -> apply branding/session data -> encrypt once.
- Mark encrypted API fields with @MobileEncrypt.
- Steps after prospect use ProspectSessionContext JWT.
- Insert the class in business order after its prerequisite.
- Add it to every intended branding block in regression, integration, and localhost XML.
- Do not create a new suite XML for one wizard step.
- Rerun the full chain; a dependent middle step is not standalone proof.""",
            ),
            (
                "6. Wire execution correctly",
                """| Check | Required |
|---|---|
| Test group | Matches suite include: regression, integration, or functional |
| Suite XML | Class added to every intended branding block |
| Maven profile | Existing POM profile points to that XML |
| Local XML | Example updated when local coverage is intended |
| Reporting | MobileMsHtmlReportListener remains registered |
| Environment | acceptance-stage1 / acceptance-qc4 stays last in -P |

A Java test not wired into the intended XML is coded but not delivered coverage.""",
            ),
            (
                "7. Manual and management traceability",
                f"""1. Add/update the request under the correct Bruno module folder.
2. Use variables/environment files; strip credentials and personal data.
3. Create/update the qTest manual case in the matching module folder with preconditions, steps, and expected result.
4. Link qTest and automation evidence to the delivering Jira story.
5. Add endpoint ID/class/method/profile/plants to the coverage register; copy plants from the XML branding blocks you changed, not an older CSV value.
6. Update sign-off/traceability if scope or exclusions changed.

Bruno: {GITLAB_BRUNO}
Epic: {JIRA_EPIC}

qTest modules:
{qtest_modules_table()}""",
            ),
            (
                "8. Prompt library — discovery",
                """Render as a copyable preformatted template:

Analyze {METHOD} {PATH} for {MODULE}. Read {REFERENCE_CLASS}, module POM, suite XML, SQL/JSON fixtures, and matching Bruno request. Return auth, branding, data prerequisites, encryption, POJO needs, L1-L4 assertions, safe suite placement, affected files, and risks. Do not edit. Do not invent fields, IDs, SQL mappings, plants, or credentials.""",
            ),
            (
                "9. Prompt library — implementation",
                """Render as a copyable preformatted template:

Implement {METHOD} {PATH} in {MODULE} for Jira {KEY}. Follow {REFERENCE_CLASS} and existing base classes. Do not change shared framework APIs without evidence. Use dynamic approved data and lean L1-L4 assertions. Never log JWT, password, SSN, bank data, host properties, or full payloads. Wire every approved branding block and existing suite profile. Update the coverage register and list exact verification commands.""",
            ),
            (
                "10. Prompt library — review and documentation",
                """Render as two copyable templates:

REVIEW:
Review this endpoint change against Jira AC, nearest module pattern, XML/POM wiring, all branding blocks, dynamic data, encryption, L1-L4 assertions, report sanitization, mutation safety, and regression impact. Report gaps with file/line evidence.

DOCUMENT:
Update endpoint ID, method/path, class/method, profiles, plants, validation layers, Bruno request, qTest case, Jira link, exclusions, and sanitized run evidence. Recalculate source registers before changing metrics.""",
            ),
            (
                "11. Verification ladder",
                """1. Parent/module compile with tests skipped.
2. Targeted local test or gitignored localhost suite.
3. Intended module suite for one branding.
4. Full suite across all approved brandings.
5. Impacted master regression when shared code changed.
6. Inspect HTML portal failures/skips/sanitization.
7. Review git diff for config, target/, secrets, and unrelated changes.
8. Record command, environment, commit, result, and artifact in Jira.""",
            ),
            (
                "12. Definition of done",
                """- [ ] Jira scope and contract evidence are clear.
- [ ] Correct base/helper and approved dynamic data are used.
- [ ] L1-L4 assertions are meaningful and sanitized.
- [ ] Mutation/delete is automation-owned and safe.
- [ ] Every intended XML/group/branding/profile is wired.
- [ ] Bruno, qTest, Jira, coverage, and traceability are linked.
- [ ] Targeted + module + impacted regression pass with report evidence.
- [ ] MR has Summary, Related, Test plan, Risks.
- [ ] Review/secrets checks pass; no unrelated files changed.""",
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
    if page["prev"] and page["prev"] != PARENT_PAGE:
        parts.append(f"Previous: {page['prev']}")
    if page["next"]:
        parts.append(f"Next: {page['next']}")
    return " | ".join(parts)


def render_sections(sections: list) -> str:
    return "\n\n".join(f"## {heading}\n{body}" for heading, body in sections)


def rules_for(sections: list) -> str:
    """Add the diagram rule only to parts that actually carry a diagram."""
    if any("Render this diagram" in body for _, body in sections):
        return f"{RULES}\n{DIAGRAM_RULE}"
    return RULES


def build_single(page: dict) -> str:
    title = display_title(page)
    return f"""Create a modern, visually polished SharePoint Site Page titled "{title}".

{placement(page)}

{design_for(page)}

Quick links row for this page: {nav_line(page)}

{rules_for(page['sections'])}

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

{rules_for(sections)}
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

{rules_for(sections)}

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
