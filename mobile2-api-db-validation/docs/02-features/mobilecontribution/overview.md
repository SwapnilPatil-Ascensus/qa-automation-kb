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
