# Weekly Backoffice Feed Suites (Prime V2)

Purpose: Weekly scheduled backoffice feed processing validation. Runs on specific days (Tuesday, Wednesday).

## Suites

| Suite XML | Suite Name | Schedule | Tests | Coverage |
|-----------|------------|----------|-------|----------|
| tue/unitefeedwts11.xml | Weekly Tuesday | Tuesdays | 5 | Mellon ACH Debit Cycle A/B/B1 Logic, Mellon ACH Debit File, UiiProcess SWP |
| wed/unitefeedwts11.xml | Weekly Wednesday | Wednesdays | 16 | ACI Account Info/Position/Transaction, By All Accounts, Mellon Envision Trade/Late Trade, State Street Cash/Trade/HL Advisor Trade, USAA Customer Info/Position/Transaction, Vanguard Trade |

**Runner:** FeatureRunner (thread count 1). Feature paths under backoffice/.

**XML location:** `suites/v2/weekly/`
