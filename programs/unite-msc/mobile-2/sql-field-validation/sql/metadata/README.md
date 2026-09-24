# unite-metadata SQL reference

| KB file | Source | Type |
|---------|--------|------|
| `get-plan-by-traunch.sql` | `TraunchTable` / `PlanService` | ORM `tu_traunch` |
| `get-fund-prices.sql` | `PriceTableDao` + gateway | explicit + joins |
| `get-traunch-stackup.sql` | `TraunchStackupDataTableDao.xml` | explicit |

## Repo paths

- DAO XML: `src/main/resources/com/cs529/metadata/repository/`
- DDL: `persistence/src/metadataDatastore.sql`

## JDBC

Use **metadata** datasource.

## Plan id vs traunch id

- Cucumber `Plans` table: `deprecatedId` = `traunch_id` (100001), `id` = `branding` (upromise).
- BFF `dashboard.planId` = branding.
- Fund price joins use branding on `tu_traunch.branding`.
