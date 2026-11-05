# Meeting decisions — 2026-07-28

**Epic:** SYN-443  
**Transcript:** `Performance Testing Requirements – Barcode Feature - Meeting on 07-28-2026.docx`

---

## Executive summary

Performance testing will proceed on the **QC4 API endpoint only** — not the full Stage/Production authentication/search/cert workflow. Swapnil raised that **leadership (Rajib)** must explicitly agree to this scope so future prod issues on auth/search layers are not attributed to incomplete perf coverage.

DevOps updated QC4 (JAR deploy / auth bypass) so the endpoint is reachable **without client certificates**. Suresh provided a working **hosted QC4 curl** on 2026-07-28; QA verified **HTTP 200**.

---

## Key decisions

| # | Decision | Status |
|---|----------|--------|
| 1 | Perf test **API endpoint in QC4** only | ✅ Aligned in meeting |
| 2 | **Rajib scope confirmation** — endpoint-only acceptable; auth/search out of scope | ☐ Pending |
| 3 | DevOps QC4 JAR deploy for auth bypass | ✅ Done (endpoint accessible) |
| 4 | JMeter scripts after QC4 smoke — owner **Priti Choudhary** | ☐ Next |

---

## Action items

| # | Action | Owner | Status |
|---|--------|-------|--------|
| 1 | Leadership scope confirmation with Rajib | Swapnil Patil | Open |
| 2 | DevOps RT for QC4 JAR deploy | Suresh Mahto | Done |
| 3 | Engage DevOps — QC4 config, exclude JARs from daily redeploy | Suresh / Dev | Done |
| 4 | Provide working QC4 endpoint + curl | Suresh | ✅ Done 2026-07-28 |
| 5 | Verify deployment | Dev team | ✅ Verified by QA curl |
| 6 | JMeter perf scripts | Priti Choudhary | Pending |

---

## QC4 endpoint (confirmed working)

```
PUT https://api.qc4.acs529.com/api/v1/plans/unite/returnmail/{barcodeId}
Body: {"SCAN_RESULT_CODE":"RETURNED"}
```

See `api/curl-from-suresh.md` and `postman/SYN-443-Barcode-API.postman_collection.json`.

---

## Risks (documented)

1. **Scope mismatch** — "performance tested" may be interpreted as full prod path including certs/search.
2. **Environment dependency** — QC4 JAR bypass must persist across redeploys.
3. **Timeline** — Limited time before deliverable; QC4 unblocked 2026-07-28.

---

## Out of scope (unless Rajib expands)

- Stage 1 client cert auth (`kofaxapi.stage.acs529.com`)
- Kofax scanner / search workflow
- Production load testing
