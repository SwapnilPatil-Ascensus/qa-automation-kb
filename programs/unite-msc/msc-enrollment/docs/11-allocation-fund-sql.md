# Allocation Fund ID — SQL Lookup

Step **12 `allocations-entered`** and step **13 `review-confirm-entered`** require a valid `fundId` in `enrollmentAllocations`. **Do not hardcode** `fundId` in API automation — resolve it dynamically from Oracle.

---

## Payload reference

| File | Field |
|------|-------|
| `postman/payloads/plain/12-allocations-entered.json` | `enrollmentAllocations[].fundId` → `{{enrollment.fundId}}` |
| `postman/payloads/plain/13-review-confirm-entered.json` | Same `fundId` in review body |

```json
{
  "enrollmentAllocations": [
    { "fundId": "{{enrollment.fundId}}", "percentAlloc": "100" }
  ]
}
```

`percentAlloc` must sum to **100** for a single-fund enrollment.

---

## Tables

| Table | Purpose |
|-------|---------|
| `TU_TRAUNCH` | Plan / branding → `TRAUNCH_ID` |
| `TU_TRAUNCH_FUND` | Active funds per traunch → `FUND_ID` |

### `TU_TRAUNCH` — resolve traunch from branding

```sql
SELECT *
FROM TU_TRAUNCH
WHERE BRANDING = 'hawaii';
```

Use `TRAUNCH_ID` from this result to scope fund lookup. For Stage1 hawaii, verify the row in your environment before running tests.

### `TU_TRAUNCH_FUND` — active funds

```sql
SELECT *
FROM TU_TRAUNCH_FUND
WHERE CTL_REC_STAT = 'A';
```

| Column | Example | Notes |
|--------|---------|-------|
| `TRAUNCH_ID` | `100009` | Links to `TU_TRAUNCH` |
| `FUNDMGR_ID` | `10091` | Fund manager |
| `FUND_ID` | `1009030` | **Use this in allocation payload** |
| `STATE` | `Y` | Prefer `STATE = 'Y'` when multiple rows exist |
| `CTL_REC_STAT` | `A` | Active record only |

---

## Recommended combined query

Use this in **API test setup** (before step 12):

```sql
SELECT tf.FUND_ID,
       tf.TRAUNCH_ID,
       tf.FUNDMGR_ID,
       tf.STATE,
       t.BRANDING
FROM TU_TRAUNCH_FUND tf
INNER JOIN TU_TRAUNCH t ON t.TRAUNCH_ID = tf.TRAUNCH_ID
WHERE tf.CTL_REC_STAT = 'A'
  AND tf.STATE = 'Y'
  AND UPPER(t.BRANDING) = UPPER(:branding)
ORDER BY tf.FUND_ID;
```

- **`:branding`** = `enrollment.planId` (e.g. `hawaii`)
- Take **`FUND_ID`** from the first row (or apply team rule if multiple funds)
- Set test variable `enrollment.fundId` before encrypting payloads 12 and 13

Full script file: [`sql/12-allocations-entered.sql`](../sql/12-allocations-entered.sql) — see also [`sql/README.md`](../sql/README.md) for all endpoint SQL.

---

## Postman vs API automation

| Approach | When | How |
|----------|------|-----|
| **GET `/plans/{planId}`** (step 04) | Postman manual E2E today | Collection script extracts `fundId` from plan response → `enrollment.fundId` |
| **SQL lookup** (this doc) | **API / TestNG implementation** | Query before run; set `enrollment.fundId` in test data builder |
| **Hardcoded env default** | Fallback only | `1001001` in environment — **overwrite** with SQL or GET plan |

For automation (Phase 1+), **SQL is the source of truth** so tests stay valid when fund catalog changes.

---

## API implementation checklist

- [ ] Add `getActiveFundIdForBranding(String branding)` to `EnrollmentTestDataBuilder` (or SQL helper)
- [ ] Run combined query at test start; bind `branding` from config (`hawaii`)
- [ ] Set `fundId` on allocation POJO / JSON fixture before step 12
- [ ] Reuse same `fundId` in step 13 `review-confirm-entered`
- [ ] If query returns 0 rows → fail fast with clear message (no active fund for plan)
- [ ] If multiple rows → document selection rule (`ORDER BY FUND_ID`, first row, or `STATE = 'Y'`)

---

## Validation rules (unchanged)

| Rule | Value |
|------|-------|
| `percentAlloc` | Must total 100% |
| `fundId` | Must be active for plan's traunch |
| Mid-wizard SQL | **Not allowed** for assertion (see `05-validation-strategy.md`) |
| Pre-run SQL for test data | **Allowed** |

---

## Related docs

- [02-endpoint-catalog.md](02-endpoint-catalog.md) — `allocations-entered` API
- [06-test-data-standards.md](06-test-data-standards.md) — `enrollment.fundId`
- [08-implementation-plan.md](08-implementation-plan.md) — Phase 1 SQL task
- [05-validation-strategy.md](05-validation-strategy.md) — no mid-flow SQL assertions
