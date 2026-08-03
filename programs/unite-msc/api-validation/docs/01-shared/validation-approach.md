# Validation approach

Rules for comparing RestAssured API JSON to JDBC query results.

## Object compare strategy

1. Flatten API response to path → value (e.g. `mobileAccounts[0].acctBalance`).
2. Look up mapping in `mappings/json-to-sql-field-map.yaml`.
3. Execute mapped SQL with scenario bind variables.
4. Apply transform (date format, scale, enum display name).
5. Assert equality or documented tolerance.

## Money

| Rule | Detail |
|------|--------|
| Type | `BigDecimal` |
| Scale | 2 decimal places |
| Rounding | `HALF_UP` |
| BFF utility | `NumberUtil.roundBigDecimal(value, 2)` |
| Per-fund | `fundPrice.multiply(fundUnits).setScale(2, HALF_UP)` in `loadPositions` |

Compare with `compareTo == 0` after normalization, not string equality.

## Dates

| Context | API format | DB | Transform |
|---------|------------|-----|-----------|
| Dashboard asOfDate | `MM/dd/yyyy` | `tu_traunch.asof_date` | `SimpleDateFormat("MM/dd/yyyy")` |
| Owner/bene DOB | `yyyy-MM-dd HH:mm:ss` | `tu_person.dob`, `tu_bene.dob` | Format DB timestamp to API string |
| PATAP asOfDate | `MM/dd/yyyy` | on-prem ISO string | Parsed in BFF — skip or separate |

## Reg type display names

API `regType` on `MobileAccount` uses `MobileAccount.getAccountTypeDisplayLongName(regType, seqSecOwnerId)` — not raw `tu_acct.reg_type` code.

Example: DB `T` → API `Trust`. Validation must apply same mapping table or compare via known scenario expectation only.

## Acct state

API returns numeric/string state codes from account domain (e.g. `91` for accepted T&C in tests). Compare to `tu_acct.acct_state` directly when stepdefs assert raw values.

## Computed fields — validate components

| Field | Do not | Do instead |
|-------|--------|------------|
| `totalBalance` | Single opaque compare when multi-account | SUM filtered `acctBalance` values |
| `mobileUgifts[]` | Full object from DB | Validate from account fields per assembly rules |
| Matching grant merge | DB query | Skip on-prem; verify individual accounts only |
| `displayInStackup` | SQL column | Replicate BFF boolean logic from regType + acctState |

## BFF account filter (mobiledashboard)

Include account in API list only if:

- `MobileAccount.canDisplayToOwner(acctState)` is true
- `enrollStatus != REJECTED`

Exclude from expected counts when scenario creates rejected/pending accounts intentionally.

## Multi-DB execution

| Datasource | Queries |
|------------|---------|
| account | tu_acct, tu_fund_balance, tu_member, login |
| profile | tu_person, tu_bene |
| metadata | tu_traunch, tu_funds, tu_fund_price |
| transaction | contribution summaries, txn history |
| bank | tu_bank, tu_bnk_instruction |

Framework may merge JDBC results in Java when schemas are split.

## Test isolation

Scenarios delete/recreate data — use keys from **current scenario's** DataTables, not hard-coded production IDs except documented fixtures (`ssgauser01`, `100001`).

## Tolerances

| Field type | Tolerance |
|------------|-----------|
| Money | Exact at scale 2 after HALF_UP |
| Strings | Exact match unless whitespace normalization noted |
| Booleans | Exact |
| Dates | Exact after format transform |
| Collections | Same size + ordered compare when BFF sorts (e.g. `MobileAccountComparator`) |

## Skip / N/A documentation

Every scenario doc must list fields skipped (on-prem, CMS, computed-only) with reason.
