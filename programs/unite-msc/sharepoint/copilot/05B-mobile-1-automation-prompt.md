PART B of 3. Edit the existing SharePoint page "05 Mobile 1 Automation" on API Testing Documentation Hub.

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

## 3. Suite strategy
| Suite | Current XML shape | Intent |
|---|---|---|
| mobile1-regression-testng.xml | 16 classes per plan; all 3 plans | Broad read/non-destructive coverage |
| mobile1-integration-testng.xml | Same 16 classes per plan | Environment/integration validation |
| mobile1-smoke-testng.xml | 5 OKD; 6 NY; 6 NMD classes | Mutating/targeted flows |
| localhost-testng.xml.example | 16 classes per plan | Gitignored local ad-hoc copy |

Smoke holds owner PUT, actual account close, biometric DELETE, session lookup/biometric validation, and password rotation where applicable. Never move a destructive class into unattended regression merely to increase the count.

## 4. Authentication and IDP token flow
Render this diagram as a full-width monospace block, exactly as written:

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

Non-IDP plans stop at the first member JWT. IDP plans continue through exchange and token-to-session. The automation exchange token is often rejected by the final step by design; a real PKCE token can be supplied with -Duse-pkce-idp-token=true, otherwise the test validates the contract fallback and the upstream steps.

Republish the page when finished.
