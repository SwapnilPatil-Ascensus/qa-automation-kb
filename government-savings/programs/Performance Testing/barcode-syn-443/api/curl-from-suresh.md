# Authoritative curl — Return Mail API (QC4)

**Source:** Suresh Mahto (2026-07-28)  
**Status:** ✅ Verified — HTTP 200 from QA machine (2026-07-28)

---

## QC4 curl (PowerShell) — use this

```powershell
$json = '{"SCAN_RESULT_CODE":"RETURNED"}'

[System.IO.File]::WriteAllText('C:\temp\returnmail-body.json', $json, (New-Object System.Text.UTF8Encoding $false))

curl.exe -k -s -w "`nHTTP:%{http_code}" -X PUT `
  "https://api.qc4.acs529.com/api/v1/plans/unite/returnmail/UNT13649678458" `
  -H "Host: api.qc4.acs529.com" `
  -H "Content-Type: application/json" `
  --data-binary "@C:\temp\returnmail-body.json"
```

---

## API contract (QC4)

| Field | Value |
|-------|-------|
| **Method** | `PUT` |
| **Host** | `api.qc4.acs529.com` |
| **Path** | `/api/v1/plans/unite/returnmail/{barcodeId}` |
| **Path param** | `barcodeId` — e.g. `UNT13649678458` |
| **Body** | `{"SCAN_RESULT_CODE":"RETURNED"}` |
| **Content-Type** | `application/json` |
| **Client cert** | Not required (QC4 auth bypass via DevOps JAR deploy) |
| **TLS** | curl uses `-k` (skip verify); Postman may need SSL verification off |

---

## Postman environment variables

| Variable | Value |
|----------|-------|
| `barcode.host` | `api.qc4.acs529.com` |
| `barcode.id` | `UNT13649678458` |
| `barcode.requestBody` | `{"SCAN_RESULT_CODE":"RETURNED"}` |

**Resolved URL:** `https://api.qc4.acs529.com/api/v1/plans/unite/returnmail/UNT13649678458`

Import: `postman/SYN-443-Barcode-API.postman_collection.json` + `postman/SYN-443-Barcode-API-QC4.postman_environment.json`

---

## Sample 200 response (2026-07-28)

```json
{
  "success": true,
  "addressMatch": true,
  "ctype": "CAL",
  "stopMailApplied": true,
  "status": "PASS-APPLIED",
  "statusMessage": "Document was already scanned",
  "BARCODE_ID": "UNT13649678458",
  "SEQ_RETURN_MAIL_ID": 32,
  "SEQ_CASE_ID": 1243910,
  "CTL_CSR_ID": 47029,
  "RECIPIENT_TYPE_CODE": "AO",
  "SCAN_RESULT_CODE": "RETURNED",
  "FIRST_NAME": "Ann",
  "MIDDLE_INITIAL": "j",
  "LAST_NAME": "Knapp",
  "ML_ADDLINE1": "UBS",
  "ML_ADDLINE2": "Apartment B",
  "ML_ADDLINE3": "",
  "ML_CITY": "Hartsdale",
  "ML_ZIPCODE": "10530",
  "ML_STATELABEL": "NY"
}
```

**Response time:** ~233 ms (single request, 2026-07-28)

---

## QC4 test data

```sql
select barcode_id, a.* from tu_sent_mail a;
```

Body file in repo: `postman/returnmail-body.qc4.json`

---

## Deprecated — localdev (do not use)

Previous demo URL `api.localdev.acs529.com` (127.0.0.1) is **not** for perf testing. Use hosted QC4 above.

---

## Verification checklist

- [x] Hosted QC4 URL works
- [x] PUT method confirmed
- [x] Request body documented
- [x] Sample 200 response captured
- [x] Postman collection updated
- [ ] Rajib scope sign-off (endpoint-only vs Stage auth path)
- [ ] Load test barcode_id CSV from DB
- [ ] JMeter script (Priti)
