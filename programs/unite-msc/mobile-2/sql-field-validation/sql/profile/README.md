# unite-profile SQL reference

| KB file | Source | Type |
|---------|--------|------|
| `get-owner-by-id.sql` | `OwnerService.getById` | ORM `tu_person` |
| `get-beneficiary-by-id.sql` | `BeneficiaryService.getById` | ORM `tu_bene` |

## Repo paths

- DAO XML: `src/main/resources/com/cs529/profile/repository/PersonTableDao.xml`, `BeneficiaryTableDao.xml`
- DDL: `persistence/src/profileDatastore.sql`

## JDBC

Use **profile** datasource.

## BFF mapping

`MobileDashboardService.loadOwner` / `loadBene` copy profile fields to dashboard root and `mobileAccounts[]`.
