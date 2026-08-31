# Test Data — IDP Login Performance

## CSV file

| Environment | File |
|-------------|------|
| stage1 (Jenkins default) | `idp-login-stage1.csv` |
| qc4 | `idp-login-qc4.csv` |

Path: `performance/universal-platform/idp/jmeter/`

## Schema

```csv
plan-prefix,username,password,account
nyd,testuser1,Newton@123,34456611501
```

| Column | Description |
|--------|-------------|
| plan-prefix | 3-letter plan code (lowercase) |
| username | Login username (plaintext when Jenkins `encrypted=false`) |
| password | Login password |
| account | Account number validated on overview page ("My Accounts") |

## Target plans (stakeholder list)

| plan-prefix | stage1 domain | plan-tpl | Accounts in CSV |
|-------------|---------------|----------|-----------------|
| njd | njd.stage1.acs529.com | /njtpl | 114 |
| nyd | nyd.stage1.acs529.com | /nytpl | 216 |
| idd | idd.stage1.acs529.com | /idtpl | 108 |
| iad | iad.stage1.acs529.com | /iatpl | 72 |
| mdd | mdd.stage1.acs529.com | /mdtpl | 108 |
| nmd | nmd.stage1.acs529.com | /nmdtpl | 228 |
| mod | mod.stage1.acs529.com | /motpl | 174 |

**Total across 7 plans:** 1,020 accounts

### plan-tpl mapping rule (from JMeter Domain Setup)

```groovy
// 2-character template prefix for these plans:
mod, iad, idd  →  /motpl, /iatpl, /idtpl

// All others use full prefix:
njd → /njtpl, nyd → /nytpl, mdd → /mdtpl, nmd → /nmdtpl
```

## User requirements

- **MFP disabled** — MFA steps exist in script but must not block login
- Users must have valid accounts on stage1
- Password encryption: controlled by Jenkins `encrypted` param + `decryption.jmx` key file

## Suggested 50-user / 5-plan split

Pick 5 plans with enough accounts (~10 users each):

| Plan | Available | Suggested users |
|------|-----------|-----------------|
| nyd | 216 | 10 |
| nmd | 228 | 10 |
| njd | 114 | 10 |
| idd | 108 | 10 |
| mod | 174 | 10 |

**Total: 50 users.** Adjust plan selection with Arun if specific plans are required.

## Filtering CSV for a targeted run

To test only specific plans, either:

1. Create a filtered CSV (e.g. `idp-login-stage1-banner-test.csv`) with only the 5 plans, or
2. Use JMeter CSV with `shareMode` and a preprocessor filter (not currently in script)

For Jenkins, simplest approach: temporary CSV swap or duplicate job with filtered file.

## Credentials note

CSV contains real test credentials. Do not commit modified CSVs with production passwords to public repos. Jenkins runs with `encrypted=false` and `stage1.properties` env file on the agent.

## Sample users for manual validation

See [VALIDATION_TEST_USERS.md](../guides/VALIDATION_TEST_USERS.md) for ready-to-use stage1 login URLs, usernames, and passwords per plan.
