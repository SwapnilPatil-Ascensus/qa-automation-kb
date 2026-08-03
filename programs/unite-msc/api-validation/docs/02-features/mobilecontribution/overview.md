# Mobile Contribution — Overview (stub)

**Status:** Not Started | **Scenarios:** 70

| Item | Path |
|------|------|
| Feature | `mobilecontribution.feature` |
| Stepdefs | `MobileContributionStepdefs.java` |
| Service | `MobileContributionService.java` |

## BFF endpoints

- `GET /mobile2api/v1/mobilecontribution`
- `GET /mobile2api/v1/mobilecontributioncheck`
- `GET /mobile2api/v1/mobilecontribution/{ext}/{id}`

## SQL repos

account, profile, metadata, bank

## Notes

High complexity — multiple contribution types and bank instruction paths. See `mappings/endpoint-registry.yaml`.

## Dynamic test fixture (ext / id)

GET/PUT/DELETE use `/mobilecontribution/{ext}/{id}`. Path `{id}` is API `RecurringContribution.id` = `tu_bnk_instruction.seq_pay_id` (not `bnkId` / not transaction summary). See [dynamic-ext-id-fixture.md](./dynamic-ext-id-fixture.md) and `sql/bank/get-mobile-contribution-fixture-by-user.sql`.
