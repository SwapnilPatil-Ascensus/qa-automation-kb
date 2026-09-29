PART B of 5. Edit the existing SharePoint page "07 Enrollment Automation" on API Testing Documentation Hub.

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

## 2. Ordered first-enrollment wizard
Render this diagram as a full-width monospace block, exactly as written:

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

Every step depends on state produced earlier, so the chain runs sequentially, never in parallel. A failure at step 4 makes steps 5-12 skip; fix the earliest failure first. Review-confirm logs only sanitized identifiers.

Republish the page when finished.
