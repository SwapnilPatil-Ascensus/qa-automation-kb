# Email draft — Priti handoff (SYN-443 Barcode perf)

**To:** Priti Choudhary  
**Cc:** Krishna Reddy, Suresh Mahto, Dattatraya Adsul  
**From:** Swapnil Patil  
**Subject:** Barcode API Performance Testing Handoff (SYN-443)

---

## Attachment checklist — you have everything correct ✓

| # | File attached | Purpose | Required? |
|---|---------------|---------|-----------|
| 1 | `SYN-443-Barcode-API.postman_collection.json` | Collection (QC4 + Stage 1 requests) | **Yes** |
| 2 | `SYN-443-Barcode-API-QC4.postman_environment.json` | QC4 environment variables | **Yes** |
| 3 | `SYN-443-Barcode-API-Stage1.postman_environment.json` | Stage 1 environment variables | **Yes** |
| 4 | `PRITI-HANDOFF.md` | Step-by-step instructions | **Yes** |
| 5 | `Suresh P12.zip` | Stage 1 client cert (`kofaxapi.stage.acs529.com.pfx`) | **Yes** (Stage 1 only) |

**You do NOT need to attach:** `returnmail-body.*.json` — body is already in the environment files.

**Unzip `Suresh P12.zip`** → use only `security/kofaxapi.stage.acs529.com.pfx` (ignore `.p12` files for Postman).

---

## Body (copy below)

---

Hi Priti,

Please find attached everything you need to start performance testing for **SYN-443 (Returned Mail Barcode API)**.

**Epic:** https://ascensuscollegesavings.atlassian.net/browse/SYN-443

### Attachments

| File | What to do |
|------|------------|
| `SYN-443-Barcode-API.postman_collection.json` | Postman → **Import** |
| `SYN-443-Barcode-API-QC4.postman_environment.json` | Postman → **Import** |
| `SYN-443-Barcode-API-Stage1.postman_environment.json` | Postman → **Import** |
| `PRITI-HANDOFF.md` | Follow step-by-step (also summarized below) |
| `Suresh P12.zip` | Unzip → use `security/kofaxapi.stage.acs529.com.pfx` for Stage 1 only |

Import all **3 JSON files** into Postman. The collection has **QC4** and **Stage 1** folders — URL, request body, and sample barcode ID are already configured in each environment. You only need to pick the environment from the top-right dropdown.

---

### Step 1 — QC4 smoke (build JMeter here first)

**Primary environment for load test design.** No certificate needed.

1. Environment → **SYN-443 Barcode API — QC4**
2. Request → **QC4 → Return Mail — Apply Scan Result (PUT)**
3. If SSL error: Postman **Settings → General → SSL certificate verification → OFF**
4. Click **Send** → expect **200 OK** and **6/6** tests passed

**Test data (QC4 DB):**

```sql
select barcode_id, a.* from tu_sent_mail a;
```

Export `barcode_id` values for JMeter CSV. You can change `barcode.id` in the environment to test other rows.

---

### Step 2 — Stage 1 smoke (Rajib wants Stage 1 validated too)

Requires client certificate (one-time Postman setup).

1. Unzip **Suresh P12.zip**
2. Postman → **Settings** (gear) → **Certificates** → **Add Certificate**

| Field | Value |
|-------|-------|
| Host | `api.stage1.acs529.com` |
| PFX file | `kofaxapi.stage.acs529.com.pfx` (from zip) |
| Passphrase | `jnx@K=kHH4TyG?UL` |

3. **Settings → General → SSL certificate verification → OFF**
4. Environment → **SYN-443 Barcode API — Stage 1**
5. Request → **Stage 1 → Return Mail — Apply Scan Result (PUT)**
6. Request **Settings** tab → **Enable SSL certificate verification → OFF**
7. Click **Send** → expect **200 OK** and **6/6** tests passed

> **Important:** Do not add the `.p12` files from the zip — only the `.pfx`. If you get `401 Invalid client credentials`, delete the cert and re-add with the passphrase above.

**Stage 1 test data:** Confirm Stage 1 DB access with Suresh/me. Same query pattern on `tu_sent_mail`. Sample barcode in env: `UNT96080597642`.

---

### QC4 vs Stage 1 (for JMeter)

| | QC4 | Stage 1 |
|---|-----|---------|
| Host | `api.qc4.acs529.com` | `api.stage1.acs529.com` |
| Method | PUT | PUT |
| Path | `/api/v1/plans/unite/returnmail/{barcodeId}` | Same |
| Body | `{"SCAN_RESULT_CODE":"RETURNED"}` | `{"scanResultCode":"RETURNED"}` |
| Client cert | No | Yes (PFX + passphrase) |
| Load test focus | **Primary** | Smoke + sign-off |

---

### Step 3 — JMeter (after Postman is green on both)

1. Mirror the Postman request (method, URL, headers, body).
2. QC4: no keystore needed.
3. Stage 1: add JMeter **Keystore Configuration** with same PFX + passphrase.
4. Parameterize `barcodeId` from CSV (DB export).
5. Load targets — I'll confirm with Rajib/Brenda; reach out if you need numbers before running load.

Full troubleshooting and contacts are in **PRITI-HANDOFF.md**.

Please ping me once QC4 and Stage 1 Postman smokes are green, and we can align on load profile before you run the full perf test.

Thanks,  
Swapnil Patil

---

## Notes for sender

- Passphrase is in email body for Priti's convenience — treat as confidential.
- `Suresh P12.zip` should contain the `.pfx`; if Priti only has zip, she unzips locally.
- KB repo path (for reference): `qa-automation-kb/programs/barcode-syn-443/`
