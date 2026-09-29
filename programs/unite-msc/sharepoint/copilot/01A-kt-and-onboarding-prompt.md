PART A of 4. Create a polished SharePoint Site Page titled "01 KT and Onboarding".

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

Quick links row for this page: Parent: Unite MSC API Automation | Next: 02 Architecture and Ownership

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 01 KT and Onboarding
Purpose: Everything a new engineer needs on day one: install, clone, build, open in an IDE, configure the host overlay, run Mobile 1, Mobile 2, or Enrollment, and find the report.

## 1. Install and access
| Need | Detail |
|---|---|
| JDK | JDK 17. The modules compile to Java 17 bytecode. Verify with java -version |
| Maven | 3.6+, 3.8+ recommended. Verify with mvn -version |
| Git | Clone access to api-test-automation |
| IDE | Eclipse, IntelliJ IDEA, VS Code, or Cursor with Maven support |
| IDE plugins | Lombok (POJOs use it) and TestNG |
| Oracle access | Read access for test-data SQL; request via Freshservice |
| Network | Corporate network reach to Stage1 and QC4 service endpoints |
| Tracking | Jira Epic QA-796 and qTest modules Unite-MSC / MSC-Enrollment / MSC-Mobile1 / MSC-Mobile2 |

Stack: Java, Maven, TestNG, and Rest Assured on the shared jsonapi-core framework. Test data comes from Oracle. HTML reporting comes from jsonapi-mobile-reporting.

## 2. Clone and build
Run once, from the repository root:

git clone https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation.git
cd api-test-automation
mvn -f mobile/pom.xml clean install -DskipTests

mobile/pom.xml builds four modules: reporting, enrollment, mobile1, mobile2.

Information callout: after this first build use mvn test, not mvn clean test, unless stale stubs remain.

Publish under "Unite MSC API Automation", then continue with Part B.
