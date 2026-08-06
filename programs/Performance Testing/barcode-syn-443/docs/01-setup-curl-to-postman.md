# Setup: curl → Postman (QC4)

## Prerequisites

- Postman Desktop (recommended for client certificates)
- QC4 wildcard cert `*.localdev.acs529.com` + key/passphrase from **Suresh** (private ping — **never commit**)
- Sample `barcode_id` from QC4:

```sql
select barcode_id, a.* from tu_sent_mail a;
```

- Authoritative curl in [../api/curl-from-suresh.md](../api/curl-from-suresh.md)

---

## Step 1 — Import collection

1. Open Postman → **Import**
2. Select:
   - `postman/SYN-443-Barcode-API.postman_collection.json`
   - `postman/SYN-443-Barcode-API-QC4.postman_environment.json`
3. Activate environment **SYN-443 Barcode API — QC4**

---

## Step 2 — Import curl (when received)

### Option A — Postman Import (fastest)

1. Copy Suresh's full curl command
2. Postman → **Import** → **Raw text** → paste curl → **Continue** → **Import**
3. Compare imported request with **Barcode Lookup (GET)** in collection; merge URL, headers, and params
4. Save updated collection

### Option B — Manual mapping

Map curl parts to environment variables:

| curl part | Postman variable |
|-----------|------------------|
| Host / base URL | `barcode.baseUrl` |
| Path (no query) | `barcode.apiPath` |
| barcode query/path value | `barcode.id` |
| `-H` headers | Request Headers tab |
| `--cert` / `--key` | Settings → Certificates (Step 3) |

---

## Step 3 — Client certificate (QC4)

Per Channel Discussion 2 (Suresh / Laxmi):

- Cert CN: `*.localdev.acs529.com`
- Issuer: ACS Internal CA
- Valid: 2022-07-20 → 2027-07-19
- QC4 bypasses JBoss partner authentication (not applicable to Stage)

**Postman configuration:**

1. Save cert `.crt` and key `.key` locally (outside repo)
2. Postman → **Settings** (gear) → **Certificates** → **Add Certificate**
3. **Host:** QC4 API hostname from curl (e.g. `something.qc4.unite529.com` or Kofax QC host)
4. **CRT file** + **KEY file** → enter passphrase if prompted
5. Enable **SSL certificate verification** unless dev instructs otherwise

---

## Step 4 — Smoke test

1. Set `barcode.id` to a known-good QC4 value
2. Send **Barcode Lookup (GET)**
3. Expect:
   - **HTTP 200**
   - JSON body with customer/mail fields
   - Tests tab: 3 smoke assertions pass

---

## Step 5 — Troubleshooting

| Issue | Action |
|-------|--------|
| `SSL Error: CERTIFICATE_VERIFY_FAILED` | Confirm correct host in Certificates tab; cert not expired |
| `401` / `403` | Check headers from curl; confirm barcode_id exists in QC4 |
| `404` | Wrong path or param name — re-sync with Suresh curl |
| `Could not get response` | VPN / network; confirm host reachable from your machine |
| Works in Postman, fails in JMeter | Replicate cert in JMeter Keystore Configuration |

---

## Step 6 — Handoff to JMeter

Once Postman is green:

1. Export request as cURL from Postman (verify matches Suresh)
2. Use JMeter **HTTP Request** sampler with same URL, method, headers
3. Add **Keystore Configuration** for client cert if required
4. Parameterize `barcode_id` via CSV (multiple rows from `tu_sent_mail`)

See [03-load-profile.md](./03-load-profile.md) for load targets.
