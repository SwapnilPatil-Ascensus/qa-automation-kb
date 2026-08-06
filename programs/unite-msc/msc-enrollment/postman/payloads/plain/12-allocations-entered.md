# Step 12 — allocations-entered

Plain payload template. Encrypt before use in Postman.

## Body

See `12-allocations-entered.json`:

```json
[
  {
    "enrollmentAllocations": [
      { "fundId": "{{enrollment.fundId}}", "percentAlloc": "100" }
    ]
  }
]
```

## fundId — do not hardcode

`fundId` must be an **active fund** for the enrollment plan's traunch. Resolve dynamically before this step.

### API / TestNG (recommended)

Query Oracle at test setup:

```sql
SELECT tf.FUND_ID
FROM TU_TRAUNCH_FUND tf
INNER JOIN TU_TRAUNCH t ON t.TRAUNCH_ID = tf.TRAUNCH_ID
WHERE tf.CTL_REC_STAT = 'A'
  AND tf.STATE = 'Y'
  AND UPPER(t.BRANDING) = UPPER('hawaii');
```

Set `enrollment.fundId` from `FUND_ID` (e.g. `1009030` for hawaii on Stage1 — verify in your env).

Full documentation: [`docs/11-allocation-fund-sql.md`](../../../docs/11-allocation-fund-sql.md)  
SQL file: [`sql/allocation-fund-lookup.sql`](../../../sql/allocation-fund-lookup.sql)

### Postman (manual)

1. Run step **04 GET `/plans/hawaii`** — collection extracts `fundId` into `enrollment.fundId`, or  
2. Run SQL above manually and set `enrollment.fundId` in environment before encrypting this payload.

## Also used in

- `13-review-confirm-entered.json` — same `enrollment.fundId` in `enrollmentAllocations`
