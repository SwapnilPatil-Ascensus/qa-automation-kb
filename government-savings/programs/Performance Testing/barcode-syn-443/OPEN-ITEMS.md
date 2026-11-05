# OPEN ITEMS — SYN-443 Barcode Perf Testing

**Last updated:** 2026-07-28

| # | Item | Owner | Status | Due |
|---|------|-------|--------|-----|
| 1 | **Rajib scope sign-off** — QC4 endpoint-only; auth/search/cert out of scope | Swapnil → Rajib | **Open** | ASAP |
| 2 | **Hosted QC4 URL + curl** | Suresh Mahto | **Done** | 2026-07-28 |
| 3 | **Request body** `{"SCAN_RESULT_CODE":"RETURNED"}` | Suresh | **Done** | 2026-07-28 |
| 4 | **QC4 smoke test** (curl + Postman) | QA | **Done** | 2026-07-28 |
| 5 | **barcode_id CSV** for load test (from `tu_sent_mail`) | Suresh / DBA | **Open** | |
| 6 | **Load targets + acceptance criteria** | Rajib + Brenda | **Open** | |
| 7 | **JMeter scripts** | Priti Choudhary | **Next** | |
| 8 | **DevOps RT** — QC4 JAR deploy + exclude from daily redeploy | Suresh | **Done** | |
| 9 | **JIRA Story** — assign Priti | Swapnil | Draft ready | |

---

## Decisions log

| Date | Decision | Approver | Notes |
|------|----------|----------|-------|
| 2026-07-28 | QC4 endpoint-only perf testing | Team meeting | Rajib confirmation still pending |
| 2026-07-28 | QC4 accessible at `api.qc4.acs529.com`, PUT, no client cert | Suresh | Verified HTTP 200 |
| 2026-07-24 | Target ETA Friday 2026-07-31 | Brenda | |

---

## API quick reference (QC4)

```
PUT https://api.qc4.acs529.com/api/v1/plans/unite/returnmail/{barcodeId}
Body: {"SCAN_RESULT_CODE":"RETURNED"}
```

Postman: `postman/SYN-443-Barcode-API.postman_collection.json`
