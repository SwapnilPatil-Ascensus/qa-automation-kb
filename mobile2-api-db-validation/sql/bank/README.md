# unite-bank SQL reference

| KB file | Source | Type |
|---------|--------|------|
| `get-banks-by-member.sql` | `BankTableDao.xml` | explicit |
| `get-bank-instructions-by-ext.sql` | `BankInstructionTableDao.xml` | explicit |

## Repo paths

- DAO XML: `src/main/resources/com/cs529/bank/repository/`
- DDL: `persistence/src/bankDatastore.sql`

## JDBC

Use **bank** datasource.

## mobiledashboard note

`MobileDashboardService.loadBanks` reads from **on-prem** account, not unite-bank. Use these queries for `mobilebank.feature` validation.
