PART A of 3. Create a polished SharePoint Site Page titled "03 Access, Setup and Environments".

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
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 03 Access, Setup and Environments
Purpose: Access routes and secure configuration reference: tools, GitLab, Oracle, local overlay, environment/profile precedence, Bruno/qTest/Jira, and setup proof.

## 1. Access and tools
| Need | Route |
|---|---|
| GitLab project access | Approved GitLab access request |
| Java and Maven | JDK 17; Maven 3.6.3+, 3.8+ recommended |
| IDE | Eclipse, IntelliJ, VS Code, or Cursor with Lombok and TestNG |
| Oracle test-data access | Freshservice request; used by the SQL fixtures |
| Linux or runner access | Freshservice Linux User Account Creation |
| GitLab access changes | Freshservice Gitlab_Users |
| Oracle DB relay | Team-approved Freshservice relay-access request |
| Jira and qTest | Team-approved project access |

## 2. Repository and first build
Render the commands as a preformatted code block:

git clone https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation.git
cd api-test-automation
mvn -f mobile/pom.xml clean install -DskipTests

The build populates src/test/resources/config/ by unpacking the shared jsonapi-lib resource artifact; that folder is empty in a fresh clone and every *.properties file in it is gitignored. After the build, copy config.properties to <COMPUTERNAME>.properties and fill UNITEDATABASEURL, UNITEUSERNAME, and UNITEPASSWORD. The environment files unpacked beside it are stage1, qc4, qc1, stage5, and cat.

Prohibition callout: the host overlay is personal and gitignored. Never upload it to SharePoint and never copy another engineer's credentials.

Publish under "Unite MSC API Automation", then continue with Part B.
