# Mobile Bank — Overview (stub)

**Status:** Not Started — see `STATUS.md`

| Item | Path |
|------|------|
| Feature | `mobilebank.feature` |
| Stepdefs | `MobileBankStepdefs.java` |
| Service | `MobileBankService.java` |

## BFF endpoints

- `GET /mobile2api/v1/mobilebanks`
- `GET /mobile2api/v1/mobilebanks/{id}`

## Gateways

BankGateway, AccountGateway, MetadataGateway, OnPremAccountGateway

## SQL repos

bank, account, metadata + on-prem for some bank data

## Planned SQL

- `sql/bank/get-banks-by-member.sql`
- `sql/bank/get-bank-instructions-by-ext.sql`

Complete this doc when tracing `MobileBankService` (next priority after mobiledashboard).
