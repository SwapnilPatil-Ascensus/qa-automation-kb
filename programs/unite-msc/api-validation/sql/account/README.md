# unite-account SQL reference

Validation queries mirroring `unite-account` DAO and service logic.

| KB file | Source | Type |
|---------|--------|------|
| `get-accounts-by-member.sql` | `AccountDao.getAccountsByMemberId` | ORM `tu_acct` |
| `resolve-member-by-username.sql` | `AccountTableDao.getAccountsByUsername` join pattern | explicit XML |
| `get-fund-positions-by-member.sql` | `FundPositionService.getPositionsByMemberId` | ORM view + `tu_fund_balance` |
| `get-bene-ssn-by-acct.sql` | `AccountTableDao.getBeneSsnByAcctIdAndExt` | explicit XML |

## Repo paths

- DAO XML: `src/main/resources/com/cs529/account/repository/`
- Entities: `src/main/java/com/cs529/account/repository/*Table.java`
- DDL: `persistence/src/accountDatastore.sql`

## JDBC

Use **account** datasource.

## Related closed-account queries

For scenarios with closed accounts (`@md4`, `@md5`): see `AccountClosedTableDao.xml` → `tu_acct_closed` (not yet in KB).
