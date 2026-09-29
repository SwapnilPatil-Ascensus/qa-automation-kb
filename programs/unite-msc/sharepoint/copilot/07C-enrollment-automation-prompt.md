PART C of 5. Edit the existing SharePoint page "07 Enrollment Automation" on API Testing Documentation Hub.

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

## 3. How Enrollment reaches account services
Render this diagram as a full-width monospace block, exactly as written:

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

Informational callout: SQL is used to prepare fixtures before the run and to verify the created account afterwards. Mid-wizard steps assert the HTTP response only.

## 4. Subsequent enrollment for an existing member
Render this diagram as a full-width monospace block, exactly as written:

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

Subsequent enrollment adds another account extension for a member who already exists, so it authenticates through the Mobile 1 session endpoint rather than the prospect flow. The prospect context from first enrollment must not be overwritten while this chain runs.

Republish the page when finished.
