# Smoke test results — Return Mail API

**Last tested:** 2026-07-28  
**Environment:** QC4 (hosted)  
**Target:** `PUT https://api.qc4.acs529.com/api/v1/plans/unite/returnmail/UNT13649678458`

---

## Result: PASSED (QC4 hosted)

| Check | Result |
|-------|--------|
| Host | `api.qc4.acs529.com` — reachable |
| HTTP method | **PUT** |
| Body | `{"SCAN_RESULT_CODE":"RETURNED"}` |
| Client cert | **Not required** (QC4 auth bypass) |
| HTTP response | **200** |
| Response time | **~233 ms** |
| `success` field | `true` |

### Sample response (truncated)

```json
{
  "success": true,
  "status": "PASS-APPLIED",
  "statusMessage": "Document was already scanned",
  "BARCODE_ID": "UNT13649678458",
  "SCAN_RESULT_CODE": "RETURNED",
  "FIRST_NAME": "Ann",
  "LAST_NAME": "Knapp"
}
```

Full response in `api/curl-from-suresh.md` and Postman collection example.

---

## Previous failure (2026-07-27) — localdev only

`api.localdev.acs529.com` → 127.0.0.1, connection refused. **Do not use localdev.** Use hosted QC4 above.

---

## Postman setup

1. Import `postman/SYN-443-Barcode-API.postman_collection.json`
2. Import `postman/SYN-443-Barcode-API-QC4.postman_environment.json`
3. Select environment **SYN-443 Barcode API — QC4**
4. If SSL error: Postman → Settings → disable **SSL certificate verification** (matches curl `-k`)
5. Send **QC4 → Return Mail — Apply Scan Result (PUT)**

### Environment variables

| Variable | Value |
|----------|-------|
| `barcode.host` | `api.qc4.acs529.com` |
| `barcode.id` | `UNT13649678458` |
| `barcode.requestBody` | `{"SCAN_RESULT_CODE":"RETURNED"}` |
