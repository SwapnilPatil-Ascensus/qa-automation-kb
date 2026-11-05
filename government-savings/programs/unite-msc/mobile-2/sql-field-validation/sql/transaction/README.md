# unite-transaction SQL reference

| KB file | Source | Type |
|---------|--------|------|
| `get-contribution-summary-jett.sql` | `StatementBalanceTableDao.getJETTContributionSummary` | explicit |
| `get-contribution-summary-omni.sql` | `getOMNIContributionSummary` | explicit |
| `get-transactions-by-ext.sql` | Transaction services | placeholder |
| `get-balance-history.sql` | Statement balance / history | placeholder |

## Additional XML queries (not yet in KB)

- `getENVContributionSummary` — Envision backend (@md14, @md15)
- `getPAGSPContributionSummary` — PA GSP
- `getPreConversionContributionSummary`

## JDBC

Use **transaction** datasource.

## YTD on mobiledashboard

`MobileDashboardService.getCurrentYrContribution` → `TransactionGateway.getContributionSummaryByExt` → backend-specific DAO selected by plan backend type.
