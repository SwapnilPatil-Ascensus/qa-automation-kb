# Mobile Dashboard — API to DB field mapping

Field-level mapping for `GET /mobile2api/v1/mobiledashboard`. Machine-readable subset in `mappings/json-to-sql-field-map.yaml`.

## Dashboard root

| JSON path | API example | DB source | SQL file | Column / expression | Notes |
|-----------|-------------|-----------|----------|---------------------|-------|
| `ownerFirstName` | James | tu_person | profile/get-owner-by-id.sql | first_name | seq_part_id from displayed account |
| `ownerLastName` | Jones | tu_person | profile/get-owner-by-id.sql | last_name | |
| `ownerDob` | 2018-07-03 … | tu_person | profile/get-owner-by-id.sql | dob | Format `yyyy-MM-dd HH:mm:ss` |
| `totalBalance` | 22460.00 | computed | composite/.../total-balance-calculation.sql | total_balance | SUM acct balances |
| `asOfDate` | 07/31/2019 | tu_traunch | metadata/get-plan-by-traunch.sql | asof_date | MM/dd/yyyy; PATAP uses on-prem |
| `planId` | upromise | tu_traunch | metadata/get-plan-by-traunch.sql | branding | |

## mobileAccounts[]

| JSON path | DB source | SQL file | Column | Notes |
|-----------|-----------|----------|--------|-------|
| `prefix` | tu_acct | account/get-accounts-by-member.sql | uii_acct_id | |
| `ext` | tu_acct | account/get-accounts-by-member.sql | uii_acct_ext | |
| `seqAcctId` | tu_acct | account/get-accounts-by-member.sql | seq_acct_id | |
| `seqBeneId` | tu_acct | account/get-accounts-by-member.sql | seq_bene_id | |
| `seqPersonId` | tu_acct | account/get-accounts-by-member.sql | seq_part_id | |
| `traunchId` | tu_acct | account/get-accounts-by-member.sql | traunch_id | |
| `acctState` | tu_acct | account/get-accounts-by-member.sql | acct_state | e.g. 91 |
| `beneFirstName` | tu_bene | profile/get-beneficiary-by-id.sql | first_name | |
| `beneLastName` | tu_bene | profile/get-beneficiary-by-id.sql | last_name | |
| `acctBalance` | tu_fund_balance × price | composite/.../total-balance-calculation.sql | acct_balance | HALF_UP scale 2 |
| `regType` | tu_acct.reg_type | account/get-accounts-by-member.sql | reg_type | **Transform** to display name |
| `displayInStackup` | — | — | — | **Computed** in BFF |

### regType code → display (@md1)

| tu_acct.reg_type | API regType |
|------------------|-------------|
| T | Trust |
| U | UGMA/UTMA |
| … | See `MobileAccount.getAccountTypeDisplayLongName` |

## mobileUgifts[]

Assembled in BFF from account + bene; not a single table.

| JSON path | Source | Notes |
|-----------|--------|-------|
| `ext`, `seqAcctId` | tu_acct | |
| `beneFirstName`, `beneLastName` | tu_bene via loaded MobileAccount | |
| `ugiftId`, `ugiftStatus` | tu_acct | |
| `isClosedAcct`, `closedDate` | acct state TERM_AND_ASSETS_DISTRIBUTED | |
| `isKidsAcct` | reg_type KIDS_CONTRIB | |

Excluded when `reg_type` = matching grant.

## mobileBanks[] — skip DB

| JSON path | Source |
|-----------|--------|
| `uuidBnkId`, `name`, `routingNum`, … | OnPremAccountGateway |

## On-prem account fields on MobileAccount — skip DB

| JSON path | Source |
|-----------|--------|
| `uuidBeneId` | on-prem beneficiary |
| `availBalanceForWithdrawal` | on-prem |
| `isEligibleForWithdrawal` | on-prem |
| `fundBalances` | on-prem fund assets |
| `hasBankProduct` | on-prem |
| `mgAccountNumber`, `mgAvailableBalance`, … | on-prem matching grant merge |

## mobileytdsummary endpoint

| JSON path | Backend | SQL file |
|-----------|---------|----------|
| `currentYrContribution` | JETT | transaction/get-contribution-summary-jett.sql |
| `currentYrContribution` | OMNI | transaction/get-contribution-summary-omni.sql |
| `currentYrContribution` | ENV | StatementBalanceTableDao getENVContributionSummary (TBD) |

Backend selected in `TransactionSummaryService` from plan `backend_type`.

## Account inclusion filter

Accounts in API must pass BFF filters. SQL composite queries should exclude:

- Accounts failing `MobileAccount.canDisplayToOwner(acctState)`
- `enroll_status = 'R'` (REJECTED)

Scenarios @md3, @md6, @md12 intentionally test partial lists.

## Execution order (validation framework)

1. `resolve-member-by-username.sql` → `:memberId`
2. `get-plan-by-traunch.sql` → `:planId`, `:asofDate`
3. `get-accounts-by-member.sql`
4. Per account: `get-beneficiary-by-id.sql`, balance from `total-balance-calculation.sql`
5. `get-owner-by-id.sql` using max non-zero `seq_part_id` from displayed accounts
6. Compare to API JSON
