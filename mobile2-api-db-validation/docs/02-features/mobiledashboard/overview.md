# Mobile Dashboard — Overview

Reference implementation for Mobile2 API–DB validation.

## Source references

| Item | Path |
|------|------|
| Feature file | `unite-mobile2/src/test/resources/features/mobiledashboard.feature` |
| Step definitions | `unite-mobile2/src/test/java/mobile2/MobileDashboardStepdefs.java` |
| BFF service | `unite-mobile2/src/main/java/com/cs529/mobile2/service/MobileDashboardService.java` |
| BFF resource | `unite-mobile2/src/main/java/com/cs529/mobile2/resource/MobileDashboardResource.java` |

## Tags

- Feature: `@mobile2`
- Component: `@component @mobileDashboard`
- Scenario tags: `@md1` … `@md15`, `@ytdcontribution` (md15)
- Integration: `@integration` on selected scenarios (md1, md8, md9, md11)

## Scenarios (15)

| Tag | Line | Scenario |
|-----|------|----------|
| @md1 | 6 | Trust: one beneficiary |
| @md2 | 63 | Individual/Matching Grant: two beneficiaries |
| @md3 | 132 | Partnership: active + pending account |
| @md4 | 200 | Forfeiture: active + closed account |
| @md5 | 269 | Non-profit: active + invalid closed account |
| @md6 | 337 | OT Omnibus: active + rejected account |
| @md7 | 405 | Individual/UGMA: two beneficiaries, multiple positions |
| @md8 | 477 | Corporate: Transit state |
| @md9 | 537 | Scholarship: Synced state |
| @md10 | 596 | Individual/UGMA: multiple positions (variant) |
| @md11 | 668 | Balance Rounding: 12 funds |
| @md12 | 757 | Stackup list: active + pending |
| @md13 | 825 | Stackup + YTD contribution (Jett) |
| @md14 | 919 | Stackup + YTD contribution (Envision) |
| @md15 | 1026 | YTD amount when selecting member list (Envision) |

Scenario docs: `scenarios/` ( `@md1` complete; others indexed in `scenarios/README.md`).

## BFF endpoints

| Method | Path | Auth | Query params | Response |
|--------|------|------|--------------|----------|
| GET | `/mobile2api/v1/mobilemembers/{planId}/{username}` | Acceptance JWT | — | `MobileMember` |
| GET | `/mobile2api/v1/mobiledashboard` | Member JWT + verified factors | — | `MobileDashboard` |
| GET | `/mobile2api/v1/mobileytdsummary/{ext}` | Member JWT + verified factors | — | `MobileContriSummary` |

HAL path for assertions: `_embedded.item` via `JsonUtil.EMBEDDED_ITEM`.

## Response domain objects

| Object | Java class | JSON collection |
|--------|------------|-----------------|
| Dashboard root | `MobileDashboard` | — |
| Accounts | `MobileAccount` | `mobileAccounts[]` |
| Ugift summary | `MobileUgift` | `mobileUgifts[]` |
| Banks | `MobileBank` | `mobileBanks[]` (on-prem) |
| YTD | `MobileContriSummary` | `currentYrContribution` |

## Downstream microservice calls

| Order | Gateway | API | SQL repo |
|-------|---------|-----|----------|
| 1 | AccountGateway | `GET accountapi/v1/accounts?includeFundPositions=true` | account |
| 2 | MetadataGateway | `GET metadataapi/v1/plans/traunch/{traunchId}` | metadata |
| 3 | OnPremAccountGateway | on-prem by account prefix + branding | external |
| 4 | ProfileGateway | `GET profileapi/v1/owners/{seqPartId}` | profile |
| 5 | ProfileGateway | `GET profileapi/v1/beneficiaries/{seqBeneId}` | profile |
| 6 | TransactionGateway | `GET transactionapi/v1/contributionsummary/{ext}` (YTD only) | transaction |

## DB tables involved

See `mappings/table-registry.yaml` → `mobiledashboard`.

## SQL files in this KB

| File | Validates |
|------|-----------|
| `sql/account/resolve-member-by-username.sql` | member id for binds |
| `sql/account/get-accounts-by-member.sql` | account list fields |
| `sql/account/get-fund-positions-by-member.sql` | position units |
| `sql/profile/get-owner-by-id.sql` | owner name |
| `sql/profile/get-beneficiary-by-id.sql` | bene name |
| `sql/metadata/get-plan-by-traunch.sql` | planId, asOfDate |
| `sql/metadata/get-fund-prices.sql` | fund prices |
| `sql/composite/mobiledashboard/total-balance-calculation.sql` | balances |
| `sql/composite/mobiledashboard/full-dashboard-validation.sql` | joined dashboard row |
| `sql/transaction/get-contribution-summary-jett.sql` | YTD (@md13) |

## Fields computed in Java (skip direct DB compare)

| Field | Logic |
|-------|--------|
| `totalBalance` | Sum of `mobileAccount.acctBalance` for displayed accounts |
| `mobileUgifts[]` | Assembled from account + bene fields; excludes matching grant reg type |
| `displayInStackup` | `acctState==ACCEPTED_TC` and not matching grant/kids/term distributed |
| Matching grant fields | Copied from MG account to individual via on-prem DTO |
| `regType` display | `MobileAccount.getAccountTypeDisplayLongName` |
| PATAP `acctBalance` | On-prem market value overrides fund sum |

## External systems

| Data | System | Approach |
|------|--------|----------|
| `mobileBanks[]` | agsup-account-web | Skip DB |
| Withdrawal fields | on-prem beneficiary | Skip DB |
| PATAP balances/dates | on-prem | Skip or env-specific |

## Flow diagram

See `flow-diagram.md`.

## Example scenario

Full validation walkthrough: [`scenarios/md1-trust-one-bene.md`](scenarios/md1-trust-one-bene.md).

Expected calculation (@md1):

- Units: 2000 × Price: 11.23 = **22460.00**
- asOfDate from plan: **07/31/2019**
- Owner: **James Jones** from owner id 1245
