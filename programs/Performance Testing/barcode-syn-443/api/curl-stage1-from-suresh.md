# Stage 1 curl — Return Mail API (PFX client cert)

**Source:** Suresh / dev team  
**Status:** Endpoint reachable; **401 without cert** (verified 2026-07-28). Full test requires PFX passphrase.

---

## curl (bash)

```bash
curl -k -v --connect-timeout 10 -m 30 -X PUT \
  "https://api.stage1.acs529.com/api/v1/plans/unite/returnmail/UNT96080597642" \
  -H "Host: api.stage1.acs529.com" \
  -H "Content-Type: application/json" \
  --cert-type P12 \
  --cert "C:\Workspace\GitLab\qa-automation-kb\BarcodeProject\Suresh P12\security\kofaxapi.stage.acs529.com.pfx:YOUR_PFX_PASSPHRASE" \
  -d '{"scanResultCode":"RETURNED"}'
```

---

## API contract (Stage 1)

| Field | Value |
|-------|-------|
| **Method** | `PUT` |
| **Host** | `api.stage1.acs529.com` |
| **Path** | `/api/v1/plans/unite/returnmail/{barcodeId}` |
| **Sample barcodeId** | `UNT96080597642` |
| **Body** | `{"scanResultCode":"RETURNED"}` ← **camelCase** (differs from QC4) |
| **Client cert** | `kofaxapi.stage.acs529.com.pfx` (P12/PFX + passphrase) |
| **TLS** | curl uses `-k` |

---

## QC4 vs Stage 1 body field

| Environment | Request body key |
|-------------|------------------|
| QC4 | `SCAN_RESULT_CODE` |
| Stage 1 | `scanResultCode` |

Response still returns uppercase `SCAN_RESULT_CODE` (per QC4 sample).

---

## Connectivity test (no cert)

```
HTTP 401 — {"message":"Invalid client credentials"}
```

Confirms host is reachable; cert is required for 200.

---

## Postman

Import `postman/SYN-443-Barcode-API-Stage1.postman_environment.json` and follow `docs/07-stage1-postman-cert-setup.md`.

---

## Verification checklist

- [x] Hosted Stage 1 URL reachable
- [x] 401 without cert (expected)
- [ ] curl 200 with PFX + passphrase
- [ ] Postman 200 with cert configured
- [ ] Sample Stage 1 response captured
