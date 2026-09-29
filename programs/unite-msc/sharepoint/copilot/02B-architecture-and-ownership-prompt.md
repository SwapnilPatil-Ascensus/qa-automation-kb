PART B of 4. Edit the existing SharePoint page "02 Architecture and Ownership" on API Testing Documentation Hub.

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

## 2. Service communication map
Render this diagram as a full-width monospace block, exactly as written:

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

Informational callout: some dashboard bank and withdrawal fields are served by an on-prem account gateway rather than the Oracle MSC tables. That is one reason a universal API-to-database comparison was not adopted as the sign-off gate.

Republish the page when finished.
