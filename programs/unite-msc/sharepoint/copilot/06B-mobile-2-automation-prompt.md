PART B of 3. Edit the existing SharePoint page "06 Mobile 2 Automation" on API Testing Documentation Hub.

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
| mobile2-regression-testng.xml | 16 classes per plan; all 3 plans | Broad read/non-destructive coverage |
| mobile2-integration-testng.xml | Same 16 classes per plan | Environment/integration validation |
| mobile2-smoke-testng.xml | 6 classes per plan | Mutating and strict checks |
| localhost-testng.xml.example | 16 classes per plan | Local gitignored copy |

Smoke runs bank mutations, contribution POST/PUT/DELETE, UGift PATCH, and strict stackup. Regression/integration also include the acceptance harness GET mobilemembers/{planId}/{username} for observation; it remains outside the 24/25 business numerator. Its member-JWT 401 is expected until acceptance-harness auth is wired—do not treat that alone as a product or coverage defect.

## 4. Where Mobile 2 data comes from
Render this diagram as a full-width monospace block, exactly as written:

  [ Mobile 2 test ]  auth context inherited from Mobile 1
              |
              v
  [ Mobile BFF /mobile2api ] -> [ unite-mobile2 ]
              |
   +----------+-----------------------------+
   |  Account (unite-account)               |  accounts, balances, YTD
   |  Profile (unite-profile)               |  owner, beneficiary
   |  Metadata (unite-metadata)             |  plans, funds, prices
   |  Bank (unite-bank)                     |  bank list, add, update, delete
   |  Transaction gateway                   |  activity, transaction history
   |  On-prem account gateway               |  dashboard banks, withdrawals
   +----------+-----------------------------+
              |
              v
  [ Oracle MSC schemas ]  +  [ on-prem systems of record ]

Informational callout: dashboard bank and withdrawal fields come from the on-prem gateway, not the Oracle MSC tables, so an Oracle field comparison does not apply to them. Transaction history and YTD depend on the plan's backend type, which is why the same assertion can behave differently across brandings.

Mobile 2 extends MobileBaseRequestTest and gets authentication/account context from Mobile 1. Oracle SQL resolves:

- automation-owned login user and account extension;
- active recurring-contribution fixture ID;
- routing number and bank fixture;
- minimum supported mobile app version.

Contribution DELETE is restricted to automation-owned data. New tests must not hardcode account /01, a bank ID, a contribution ID, a customer username, or a routing number.

Republish the page when finished.
