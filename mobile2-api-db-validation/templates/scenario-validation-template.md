# Scenario validation template

Copy to `docs/02-features/{feature}/scenarios/{tag}-{slug}.md`.

---

## Scenario: {name}

**Tags:** @integration @component @...

**Feature:** `{feature}.feature:{line}`

**Setup steps:** I create Accounts, Members, ...

### API Call

- **Endpoint:** `GET /mobile2api/v1/{endpoint}`
- **Auth:** JWT member, verified factors PASSWORD + SMS
- **Test user:** planId=`upromise`, username=`ssgauser01`

### API Response Fields to Validate

| JSON path | Expected (from feature) | DB query file | DB column | Transform/notes |
|-----------|--------------------------|---------------|-----------|-----------------|
| ownerFirstName | James | profile/get-owner-by-id.sql | first_name | |
| totalBalance | 22460.00 | composite/mobiledashboard/total-balance-calculation.sql | SUM(units*price) | scale 2, HALF_UP |

### SQL Execution Order

1. Resolve memberId from login
2. Get accounts
3. Get owner
4. Calculate balance

### Skip / N/A

- `mobileBanks` → on-prem only
- Fields marked computed in `overview.md`
