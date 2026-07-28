# Priti — Barcode API Performance Testing Handoff (SYN-443)

**Epic:** SYN-443  
**Your focus:** JMeter perf scripts  
**Postman:** Smoke test first, then script from same API contract  

---

## Files to import (from `BarcodeProject/postman/`)

| # | File | Import as |
|---|------|-----------|
| 1 | `SYN-443-Barcode-API.postman_collection.json` | Collection |
| 2 | `SYN-443-Barcode-API-QC4.postman_environment.json` | Environment |
| 3 | `SYN-443-Barcode-API-Stage1.postman_environment.json` | Environment |

**Postman → Import → drag all 3 files.**

Collection has two folders: **QC4** and **Stage 1**. URL, body, and barcode ID are already in the environment — you only switch the environment dropdown.

**Cert file (Stage 1 only):** get from Swapnil — `Suresh P12/security/kofaxapi.stage.acs529.com.pfx`  
**PFX passphrase (Stage 1 only):** get from Swapnil (private — not in repo).

---

## Part 1 — QC4 smoke (do this first)

**Design perf tests on QC4.** No certificate needed.

1. Top-right environment → **`SYN-443 Barcode API — QC4`**
2. Open **QC4 → Return Mail — Apply Scan Result (PUT)**
3. If SSL error: **Settings → General → SSL certificate verification → OFF**
4. Click **Send**
5. Expect **200 OK** and **6/6** tests passed

**QC4 test data (barcode IDs):**

```sql
select barcode_id, a.* from tu_sent_mail a;
```

Run on **QC4 database**. Export rows for JMeter CSV. Update `barcode.id` in environment to try other IDs.

---

## Part 2 — Stage 1 smoke (Rajib wants Stage 1 coverage)

Same request as QC4, but **client certificate required**.

### One-time: add certificate in Postman

1. **Delete** any existing cert for `api.stage1.acs529.com` (Settings → Certificates → trash)
2. **Add Certificate...**

| Field | Value |
|-------|-------|
| **Host** | `api.stage1.acs529.com` |
| **PFX file** | `kofaxapi.stage.acs529.com.pfx` (path from Swapnil) |
| **Passphrase** | From Swapnil |

3. **Settings → General → SSL certificate verification → OFF**

**Do not add the `.p12` files** — only the `.pfx`.

### Run Stage 1 request

1. Environment → **`SYN-443 Barcode API — Stage 1`**
2. Open **Stage 1 → Return Mail — Apply Scan Result (PUT)**
3. Request **Settings** tab → **Enable SSL certificate verification → OFF**
4. Click **Send**
5. Expect **200 OK** and **6/6** tests passed

**Stage 1 test data:** Confirm Stage 1 DB access with Swapnil/Suresh. Use same pattern — query `tu_sent_mail` for valid `barcode_id` values on Stage 1. Sample ID in env: `UNT96080597642`.

---

## QC4 vs Stage 1 (for JMeter)

| | QC4 | Stage 1 |
|---|-----|---------|
| Host | `api.qc4.acs529.com` | `api.stage1.acs529.com` |
| Method | PUT | PUT |
| Path | `/api/v1/plans/unite/returnmail/{barcodeId}` | Same |
| Body | `{"SCAN_RESULT_CODE":"RETURNED"}` | `{"scanResultCode":"RETURNED"}` |
| Client cert | No | Yes (PFX + passphrase) |
| Primary for load test | **Yes** | Smoke + Rajib sign-off |

---

## JMeter (after Postman green)

1. Mirror Postman request (method, URL, body, headers).
2. QC4: no keystore.
3. Stage 1: add **Keystore Configuration** with same PFX + passphrase.
4. Parameterize `barcodeId` from CSV (DB export).
5. Load targets: see `docs/03-load-profile.md` — confirm with Swapnil/Rajib.

---

## If something fails

| Error | Fix |
|-------|-----|
| QC4 connection / SSL | SSL verification OFF |
| Stage 1 `401 Invalid client credentials` | Re-add PFX **with passphrase** |
| Stage 1 SSL error | SSL verification OFF (global + request Settings) |
| `400 Bad Request` on Stage 1 | Wrong env selected — body keys differ QC4 vs Stage 1 |

---

## Contacts

| Need | Ask |
|------|-----|
| PFX file + passphrase | Swapnil |
| QC4 / Stage 1 DB access | Suresh |
| Load targets + Rajib scope | Swapnil / Brenda |

---

**Repo path:** `qa-automation-kb/BarcodeProject/`
