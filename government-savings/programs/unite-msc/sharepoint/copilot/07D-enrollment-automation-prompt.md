PART D of 5. Edit the existing SharePoint page "07 Enrollment Automation" on API Testing Documentation Hub.

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

## 5. Encryption and session architecture
Render this diagram as a full-width monospace block, exactly as written:

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

Prohibition callout: never paste plaintext payloads, certificate material, AES data, JWT, SSN, bank numbers, or environment JSON into SharePoint or Jira.

## 6. Suites and profiles
| Profile | Current XML | Purpose |
|---|---|
| mobile-ms-enrollment-smoke | 5 OK Direct classes | ping, certificate, US states, country, plans |
| mobile-ms-enrollment-regression | 17 classes x 3 plants | Full first + subsequent enrollment |
| mobile-ms-enrollment-integration | 17 classes x 3 plants | Same chain for integration validation |
| mobile-ms-enrollment-localhost | localhost XML copy | Local ad-hoc chain |

The wizard is sequential, not parallel: each class depends on state produced by prior steps. New steps must be inserted in correct order in every branding block.

Republish the page when finished.
