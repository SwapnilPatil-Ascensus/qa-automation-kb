# ORM vs explicit SQL

UniteMSC microservices use two patterns for database access. Validation SQL must mirror the **effective** query, not always the XML file.

## Pattern 1: ORM `findByCriteria`

**Mechanism:** `@Table` entity + `@Column` fields → framework generates SELECT.

**Example:** `AccountDao.getAccountsByMemberId`

```java
AccountTable accountCriteria = new AccountTable();
accountCriteria.setUiiMemberId(memberId);
accountCriteria.select("seqAcctId", "seqPartId", ...);
return findByCriteria(accountCriteria);
```

**Entity:** `AccountTable.java` → `@Table("tu_acct")`

**KB approach:** Write equivalent SQL with `WHERE uii_member_id = :memberId AND ctl_rec_stat = 'A'`.

**Also used for:**

- `OwnerService.getById` → `tu_person` by `seq_person_id`
- `BeneficiaryService.getById` → `tu_bene` by `seq_bene_id`
- `PlanService.getByTraunchId` → `tu_traunch` by `traunch_id`
- Fund balance views → join `tu_fund_balance` + `tu_acct` via view criteria

## Pattern 2: Explicit XML queries

**Mechanism:** `*TableDao.xml` entry keys referenced by `findByQuery("queryName", params)`.

**Examples:**

| Query name | File | Purpose |
|------------|------|---------|
| `getAccountsByUsername` | AccountTableDao.xml | Login + traunch → accounts |
| `getBeneSsnByAcctIdAndExt` | AccountTableDao.xml | Bene SSN encrypted fields |
| `getMemberByLoginId` | MemberTableDao.xml | Member by login |
| `getJETTContributionSummary` | StatementBalanceTableDao.xml | YTD contributions JETT backend |
| `getOMNIContributionSummary` | StatementBalanceTableDao.xml | YTD OMNI backend |
| `getENVContributionSummary` | StatementBalanceTableDao.xml | YTD Envision backend |

**KB approach:** Copy/adapt SQL from XML; cite source entry key in file header.

## Pattern 3: Hybrid (ORM + gateway)

`FundPositionService.getPositionsByMemberId`:

1. ORM: accounts by member, fund balances by view join.
2. HTTP: metadata `getFundPrices(planId, asofDate)`.
3. Java: match `fundId` to price `deprecatedId`, multiply units × price.

Validation requires **account + metadata** queries or composite SQL.

## Oracle vs Postgres

Some DAOs branch on `isOracle()` (e.g. `generateUgiftId`). Integration tests typically target one DB; document dialect variants in SQL Notes when XML differs.

## Header documentation

Every KB `.sql` file must state:

- `ORM-generated` or `explicit: {queryKey}`
- Source Java method
- Tables touched

See `sql/_templates/validation-query.template.sql`.

## When XML is empty

`FundBalanceTableDao.xml` only has `findAll` — balance reads use ORM on `FundBalanceTable` / views. Derive SQL from entity columns and `FundPositionService` join logic.
