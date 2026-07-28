# Authoritative curl — Return Mail API (from Suresh demo)

**Source:** Suresh demo (2026-07-24 call)  
**Status:** Captured 2026-07-27

---

## Curl (PowerShell)

```powershell
curl "https://api.localdev.acs529.com/api/v1/plans/unite/returnmail/UNT13649678458" `
  -H "Host: api.localdev.acs529.com" `
  -H "Content-Type: application/json" `
  --data-binary "@C:\temp\returnmail-body.json"
```

---

## URL breakdown → Postman environment

| Postman variable | Value | Notes |
|------------------|-------|-------|
| `barcode.host` | `api.localdev.acs529.com` | Hostname only — **not** full URL |
| `barcode.id` | `UNT13649678458` | Path segment after `returnmail/` |
| `barcode.requestBody` | contents of `returnmail-body.json` | Paste JSON; `{}` placeholder until Suresh shares |

**Resolved URL:**

```
https://{{barcode.host}}/api/v1/plans/unite/returnmail/{{barcode.id}}
→ https://api.localdev.acs529.com/api/v1/plans/unite/returnmail/UNT13649678458
```

**Smoke test (2026-07-27):** curl failed — `api.localdev.acs529.com` resolves to `127.0.0.1` and nothing listens on port 443. See `docs/04-smoke-test-results.md`.

---

## Headers

| Header | Value | Postman |
|--------|-------|---------|
| `Host` | `api.localdev.acs529.com` | Usually auto-set from URL; add explicitly if needed |
| `Content-Type` | `application/json` | Required |

---

## Request body

Curl uses `--data-binary "@C:\temp\returnmail-body.json"`.

- **Ask Suresh** for the exact JSON inside `returnmail-body.json` and paste into Postman **Body → raw → JSON**.
- Placeholder sample: `postman/returnmail-body.sample.json`

---

## HTTP method note

Curl with `--data-binary` defaults to **POST** unless `-X GET` is specified. Suresh's demo did **not** include `-X GET`. Confirm with Suresh; collection is set to **POST** to match the demo curl.

---

## Certificate

Host `api.localdev.acs529.com` matches wildcard cert `*.localdev.acs529.com`.

Postman → **Settings → Certificates** → Add for host `api.localdev.acs529.com` (CRT + KEY from Suresh; passphrase via private channel).

---

## QC4 test data

```sql
select barcode_id, a.* from tu_sent_mail a;
```

Swap `barcode.id` with other `barcode_id` values from this query.

---

## Verification checklist

- [x] URL mapped to environment variables
- [ ] `returnmail-body.json` contents obtained from Suresh
- [ ] Client cert configured in Postman
- [ ] HTTP 200 smoke test
