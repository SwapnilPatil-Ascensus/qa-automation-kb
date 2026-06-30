# Cucumber test data setup steps

Glue packages provide Given steps that seed and tear down database rows before API calls.

## Glue configuration

From `unite-mobile2/src/test/java/mobile2/CucableJavaTemplate.java`:

```java
glue = {"mobile2", "metadata", "account", "profile", "transaction", "bank"}
```

## Common setup pattern (mobiledashboard example)

Typical scenario order:

```
Given I delete Positions
And I delete Accounts
And I delete Members
And I delete Owners
And I delete Beneficiaries
...
And I create Plans
And I create Funds / Prices
And I create Beneficiaries
And I create Owners
And I create Members
And I create Accounts
And I create Positions
```

Deletes run first for isolation; creates build dependency order (plan → funds → people → member → account → positions).

## Step → table mapping

| Cucumber step | Glue package | Primary tables touched |
|---------------|--------------|------------------------|
| `I delete Plans` | metadata | `tu_traunch`, related metadata |
| `I delete Funds` / `Fund Managers` / `Prices` | metadata | `tu_funds`, `tu_fund_price`, `tu_traunch_fund` |
| `I delete Codes` | metadata | `tu_codes` |
| `I delete Beneficiaries` | profile | `tu_bene` |
| `I delete Owners` | profile | `tu_person` |
| `I delete Successors` | profile | successor tables |
| `I delete Members` | account | `tu_member`, `ta_login`, `ta_app_context` |
| `I delete Accounts` | account | `tu_acct` |
| `I delete Positions` | account | `tu_fund_balance` |
| `I create Plans` | metadata | `tu_traunch` (`deprecatedId` = traunch_id e.g. 100001, `id` = branding e.g. upromise) |
| `I create Members` | account | `tu_member`, login tables (`username`, `traunchId`) |
| `I create Accounts` | account | `tu_acct` (`prefix`, `ext`, `regType`, `acctState`, `traunchId`) |
| `I create Positions` | account | `tu_fund_balance` (`fundUnits` → `total_units`) |
| `I create Prices` | metadata | `tu_fund_price` |
| Bank-related create/delete | bank | `tu_bank`, `tu_bnk_instruction` |
| Transaction setup | transaction | txn / stmt balance tables |

## Keys to reuse in validation SQL

Extract from feature DataTables:

| Setup column | Bind variable | Example (@md1) |
|--------------|---------------|----------------|
| Members.username | `:username` | ssgauser01 |
| Members.traunchId | `:traunchId` | 100001 |
| Plans.id (branding) | `:planId` | upromise |
| Accounts.prefix | `:uiiAcctId` | A90800208 |
| Accounts.ext | `:ext` | 01 |
| Positions.id (fund) | `:fundId` | C6 |
| Prices.price | `:fundPrice` | 11.23 |
| Positions.fundUnits | `:fundUnits` | 2000 |

Resolve `:memberId` via `sql/account/resolve-member-by-username.sql` or member session API.

## Implementation locations

| Package | Path |
|---------|------|
| account | `unite-account/src/test/java/account/` |
| profile | `unite-profile/src/test/java/profile/` |
| metadata | `unite-metadata/src/test/java/metadata/` |
| transaction | `unite-transaction/src/test/java/transaction/` |
| bank | `unite-bank/src/test/java/bank/` |

## Validation implication

SQL must filter `ctl_rec_stat = 'A'` where production DAOs do, matching active rows created by glue steps. Soft-deleted rows from prior scenarios should not exist after delete steps.
