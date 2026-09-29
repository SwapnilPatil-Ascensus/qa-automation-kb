PART B of 3. Edit the existing SharePoint page "03 Access, Setup and Environments" on API Testing Documentation Hub.

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

## 3. How a run resolves its target
Render this diagram as a full-width monospace block, exactly as written:

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

Caution callout: the environment profile must be last in -P. If it is listed first, the suite profile overwrites it and the run silently targets the wrong environment.

## 4. Configuration precedence
| Input | Selected by | Example |
|---|---|---|
| TestNG suite | Module suite profile | mobile2-regression |
| Environment properties | Environment profile listed last | acceptance-stage1 |
| Oracle connection | -Dhost.properties | <COMPUTERNAME>.properties |
| Report label | System property | -Dmobile.ms.report.environment=Stage1 |
| Branding | TestNG XML parameter | okdirect/newyork/nmdirect |

Example: "-Pmobile2-regression,acceptance-stage1" means use Mobile 2 regression XML, then force stage1.properties. Reversing profile order can target the wrong environment.

## 5. Environment use
| Environment | Use | Caveat |
|---|---|---|
| Stage1 | Primary regression and sign-off evidence | Refresh can invalidate users and data |
| QC4 | Integration and environment proof | Stability, IDP/reverse proxy, and refresh dependencies can block runs |
| Localhost suite | Narrow local class/branding selection | Still points to chosen Stage1/QC4 services unless a local service URI is configured |

Enrollment uses the cloud Enrollment BFF. Mobile login may use a different BFF; do not swap base URIs. Enrollment POST bodies are encrypted; GET calls may be plain.

Republish the page when finished.
