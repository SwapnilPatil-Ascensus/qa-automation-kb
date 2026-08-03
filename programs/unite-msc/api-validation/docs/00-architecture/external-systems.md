# External systems (out of UniteMSC SQL scope)

Fields sourced outside unite-account/profile/metadata/transaction/bank require different validation approaches.

## On-prem account service (agsup-account-web)

**Gateway:** `OnPremAccountGateway.java`  
**Called from:** `MobileDashboardService`, `MobileBankService`, `MobileContributionService`, `MobileActivityService`, and others.

### Data provided

| API field / object | Source | DB validation |
|--------------------|--------|---------------|
| `mobileBanks[]` | On-prem account banks | **Skip** — not in UniteMSC SQL repos |
| `availBalanceForWithdrawal` | On-prem beneficiary | **Skip** or manual on-prem query |
| `isEligibleForWithdrawal` | On-prem beneficiary | **Skip** |
| `fundBalances` map | On-prem fund assets | **Skip** |
| `uuidBeneId` | On-prem beneficiary id | **Skip** |
| Matching grant fields (`mgAccountNumber`, etc.) | On-prem matching grant DTO | **Skip** — validate merge logic separately |
| PATAP `acctBalance` | On-prem fund asset market value | Overrides fund position sum |

### BFF behavior notes

- `getOnPremAccount()` uses first account's prefix + plan branding from metadata.
- PATAP branding uses on-prem `marketValue` instead of `loadPositions()` sum.
- `asOfDate` for PATAP comes from on-prem fund asset, not `tu_traunch.asof_date`.

### Validation approach

1. Mark scenario rows **Skip / N/A** for on-prem fields.
2. For scenarios without on-prem dependency (e.g. `@md1` JETT/upromise), validate all UniteMSC-backed fields fully.
3. Optional: add separate on-prem validation doc if agsup SQL becomes available.

## Content CMS

**Gateway:** `ContentGateway.java`  
**Endpoint:** `GET /mobile2api/v1/content`  
**Target:** `content.service.url` (e.g. howtosaveforcollege.com)

- Returns HTML/content payloads.
- **No DB validation** — compare static fixtures or HTTP contract only.

## Identity Provider (IdP)

**Gateway:** `IdpGateway.java`

- Authentication and token exchange.
- **Skip DB validation.**

## When to document "external only"

In feature `overview.md`, list any scenario that:

- Asserts bank list from dashboard (on-prem).
- Uses PATAP plan branding.
- Calls `/content`.
- Depends on matching grant linkage.

## Feature impact summary

| Feature | External dependency |
|---------|---------------------|
| mobiledashboard | On-prem (banks, withdrawal, PATAP, matching grants) |
| mobilebank | On-prem + bank microservice |
| mobilecontribution | On-prem in some flows |
| mobileactivity | Content CMS + multiple backends |
| contentservice | CMS only |
| planselection, mobileStackup, investment | Primarily metadata/account — minimal external |
