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
