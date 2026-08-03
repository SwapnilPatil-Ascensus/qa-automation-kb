## Scenario: Trust: Member with one beneficiary gets Mobile dashboard

**Tags:** @integration @component @mobileDashboard @md1

**Feature:** `mobiledashboard.feature:6`

**Setup steps:** delete Positions/Accounts/Members/Owners/Beneficiaries/Plans/Funds/Prices → create Plans (upromise/100001), Funds (C6), Prices (11.23 @ 2019-07-31), Beneficiaries, Owners (James Jones), Members (ssgauser01), Accounts (A90800208-01 Trust), Positions (2000 units C6)

### API Call

- **Endpoint:** `GET /mobile2api/v1/mobiledashboard`
- **Auth:** JWT member from `mobilemembers/upromise/ssgauser01`, verified factors PASSWORD + SMS
- **Test user:** planId=`upromise`, username=`ssgauser01`, traunchId=`100001`

### API Response Fields to Validate

| JSON path | Expected (from feature) | DB query file | DB column | Transform/notes |
|-----------|--------------------------|---------------|-----------|-----------------|
| ownerFirstName | James | profile/get-owner-by-id.sql | first_name | :seqPersonId=1245 |
| ownerLastName | Jones | profile/get-owner-by-id.sql | last_name | |
| totalBalance | 22460.00 | composite/mobiledashboard/total-balance-calculation.sql | total_balance | 2000×11.23, scale 2 |
| asOfDate | 07/31/2019 | metadata/get-plan-by-traunch.sql | asof_date | MM/dd/yyyy |
| mobileAccounts[0].beneFirstName | Bene1 FName | profile/get-beneficiary-by-id.sql | first_name | via seq_bene_id |
| mobileAccounts[0].beneLastName | Bene1 LName | profile/get-beneficiary-by-id.sql | last_name | |
| mobileAccounts[0].acctBalance | 22460.00 | composite/.../total-balance-calculation.sql | acct_balance | |
| mobileAccounts[0].prefix | A90800208 | account/get-accounts-by-member.sql | uii_acct_id | |
| mobileAccounts[0].ext | 01 | account/get-accounts-by-member.sql | uii_acct_ext | |
| mobileAccounts[0].regType | Trust | account/get-accounts-by-member.sql | reg_type | T → Trust display |
| mobileAccounts[0].traunchId | 100001 | account/get-accounts-by-member.sql | traunch_id | |
| mobileAccounts[0].acctState | 91 | account/get-accounts-by-member.sql | acct_state | |

### SQL Execution Order

1. `account/resolve-member-by-username.sql` — `:username=ssgauser01`, `:traunchId=100001` → `:memberId`
2. `metadata/get-plan-by-traunch.sql` — `:traunchId=100001` → `:planId=upromise`, `:asofDate=2019-07-31`
3. `account/get-accounts-by-member.sql` — `:memberId`
4. `profile/get-beneficiary-by-id.sql` — `:seqBeneId` from account row
5. `profile/get-owner-by-id.sql` — `:seqPersonId=1245`
6. `composite/mobiledashboard/total-balance-calculation.sql` — `:memberId`, `:planId`, `:asofDate`

### Bind variable cheat sheet

| Variable | Value |
|----------|-------|
| :username | ssgauser01 |
| :traunchId | 100001 |
| :planId | upromise |
| :asofDate | 2019-07-31 |
| :uiiAcctId | A90800208 |
| :ext | 01 |
| :fundUnits | 2000 |
| :fundPrice | 11.23 |

### Skip / N/A

- `mobileBanks[]` — not seeded; on-prem only
- `mobileUgifts[]` — validate from account assembly (optional secondary pass)
- On-prem withdrawal / matching grant fields

### Stepdef assertions reference

From `MobileDashboardStepdefs`:

- `I have Mobile dashboard` — ownerFirstName, ownerLastName, totalBalance, asOfDate
- `I have Mobile Accounts` — bene names, acctBalance, prefix, ext, regType, traunchId, acctState, seq IDs not null
