# Stage 1 Postman — EXACT setup steps (copy-paste checklist)

**Do this once.** If you added the PFX **without a passphrase**, delete it and start again at Step 3.

---

## Do you need the `.p12` files?

**No — for this API you only need ONE file:**

| File | Add to Postman? |
|------|-----------------|
| `kofaxapi.stage.acs529.com.pfx` | **YES** — this is the client cert |
| `apitest.client.trust.p12` | **NO** — used by .NET/Kofax apps, not Postman |
| `apitest.qa.acs529.com.identity.p12` | **NO** — different identity cert |

The dev curl only uses the `.pfx`. Postman needs the same single PFX + passphrase.

---

## Step 1 — Environment

1. Top-right dropdown → select **`SYN-443 Barcode API — Stage 1`**
2. Click the **eye icon** → confirm:

| Variable | Must be |
|----------|---------|
| `barcode.host` | `api.stage1.acs529.com` |
| `barcode.id` | `UNT96080597642` |
| `barcode.requestBody` | `{"scanResultCode":"RETURNED"}` |

> **Passphrase does NOT go in environment variables.** It goes in Certificates (Step 3).

---

## Step 2 — Request body & headers

Open: **Stage 1 → Return Mail — Apply Scan Result (PUT)**

| Tab | Setting |
|-----|---------|
| Method | `PUT` |
| URL | `https://{{barcode.host}}/api/v1/plans/unite/returnmail/{{barcode.id}}` |
| **Body** | `raw` → `JSON` → `{"scanResultCode":"RETURNED"}` |
| **Headers** | `Content-Type: application/json` (Auto-added is OK) |

---

## Step 3 — Client certificate (THIS IS WHERE PASSPHRASE GOES)

### 3a — Remove the broken entry (you added PFX without passphrase)

1. Click **gear icon** (top right) → **Settings**
2. Tab: **Certificates**
3. Find row: Host = `api.stage1.acs529.com`
4. Click **trash icon** → delete it

### 3b — Add certificate WITH passphrase

1. Click **Add Certificate...**
2. Fill in **exactly**:

| Field | Value |
|-------|-------|
| **Host** | `api.stage1.acs529.com` |
| **PFX file** | Browse → `C:\Workspace\GitLab\qa-automation-kb\BarcodeProject\Suresh P12\security\kofaxapi.stage.acs529.com.pfx` |
| **Passphrase** | Paste your passphrase here (the one Suresh gave you) |

3. Click outside the dialog or confirm to save
4. **Close Settings**

> If there is no Passphrase field visible, click **PFX file** first — Postman shows Passphrase after you select a `.pfx`.

---

## Step 4 — SSL settings (two places)

### 4a — Global (recommended)

1. **Settings** → **General**
2. **SSL certificate verification** → **OFF**

### 4b — Request level (you already did this)

1. On the request → **Settings** tab (next to Cookies)
2. **Enable SSL certificate verification** → **OFF**

**CA certificates** (Settings → Certificates → top toggle): leave **OFF**.

---

## Step 5 — Send

1. Click **Send**
2. Expected: **200 OK**, `success: true`
3. **Test Results** tab should show **6/6** passed

---

## Step 6 — Verify with curl (optional)

PowerShell — passphrase in variable avoids special-character issues:

```powershell
$pfx  = 'C:\Workspace\GitLab\qa-automation-kb\BarcodeProject\Suresh P12\security\kofaxapi.stage.acs529.com.pfx'
$pass = 'PASTE_YOUR_PASSPHRASE_HERE'

curl.exe -k -s -w "`nHTTP:%{http_code}`n" --connect-timeout 15 -m 30 -X PUT `
  'https://api.stage1.acs529.com/api/v1/plans/unite/returnmail/UNT96080597642' `
  -H 'Host: api.stage1.acs529.com' `
  -H 'Content-Type: application/json' `
  --cert-type P12 `
  --cert "${pfx}:${pass}" `
  -d '{"scanResultCode":"RETURNED"}'
```

---

## Troubleshooting

| What you see | Fix |
|--------------|-----|
| `401 Invalid client credentials` | Delete cert → re-add with **passphrase** |
| `Could not send request` / SSL error | SSL verification OFF (Steps 4a + 4b) |
| `400 Bad Request` | Body must be `scanResultCode` (camelCase), not `SCAN_RESULT_CODE` |
| Cert row shows PFX but still 401 | Passphrase was empty — **delete and re-add** |
| Works in QC4, not Stage 1 | Different env selected? Must be **Stage 1** environment |

---

## Security

- **Never commit passphrase** to git or Postman collection JSON
- Passphrase lives **only** in Postman Settings → Certificates
- `.pfx` / `.p12` files are in `.gitignore`

---

## Quick checklist

- [ ] Environment = **SYN-443 Barcode API — Stage 1**
- [ ] Body = `{"scanResultCode":"RETURNED"}`
- [ ] Deleted old cert without passphrase
- [ ] Added `kofaxapi.stage.acs529.com.pfx` **with passphrase**
- [ ] Did **not** add `.p12` files
- [ ] SSL verification OFF (global + request)
- [ ] Send → **200 OK**
