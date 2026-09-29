PART C of 3. Edit the existing SharePoint page "09 Reporting and Troubleshooting" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 5. Safe rerun strategy
| Failure type | Rerun |
|---|---|
| Enrollment wizard step | Rerun the full ordered plan chain; do not start at a dependent middle step |
| Read-only Mobile 1/2 class | Use a gitignored localhost XML containing setup + target class |
| Destructive smoke test | Inspect existing state first; rerun only with automation-owned data |
| Multi-plan failure | Reproduce only the failed branding locally, then restore full XML |
| Environment-wide failure | Do not loop retries; wait for confirmed dependency recovery |

Never delete a class from shared regression XML to create a green result. Any temporary local narrowing stays in a gitignored localhost suite.

## 6. Minimum evidence for escalation
Capture:
- Jira story/bug and endpoint ID.
- Timestamp, environment, branding, suite/profile, commit SHA.
- Java class/method and HTTP method/path.
- Expected vs actual status/business assertion.
- Portal/Surefire artifact and whether targeted rerun reproduced.
- Recent deploy/refresh/dependency context.
- Classification: environment, data, automation, product, or expected exclusion.

Use the automation bug lifecycle for product/recurring automation defects.

## 7. Security and report sanitization
SensitiveDataSanitizer masks bearer tokens, JWT-like strings, passwords, client secrets, and signing keys in report text.

Prohibition callout: sanitization is defense in depth. Never deliberately log or attach passwords, tokens, SSN, bank data, certificates, host overlays, environment JSON, DB credentials/URLs, or raw personal payloads. Redact account identifiers unless the approved internal process requires them.

Republish the page when finished.
