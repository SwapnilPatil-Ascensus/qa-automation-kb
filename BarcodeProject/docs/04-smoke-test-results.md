# Smoke test results — Return Mail API

**Tested:** 2026-07-27  
**Tester:** Swapnil Patil (automated curl from dev machine)  
**Target:** `POST https://api.localdev.acs529.com/api/v1/plans/unite/returnmail/UNT13649678458`

---

## Result: FAILED (connectivity — not API logic)

| Check | Result |
|-------|--------|
| DNS | `api.localdev.acs529.com` → **127.0.0.1** |
| Port 443 on 127.0.0.1 | **Connection refused** — nothing listening |
| `C:\temp\returnmail-body.json` | **Not found** on test machine |
| Client cert `*.localdev.acs529.com` | **Not found** on test machine |
| HTTP response | **None** — failed before TLS |

### curl output

```
curl: (7) Failed to connect to api.localdev.acs529.com port 443 after 2084 ms: Could not connect to server
HTTP_CODE:000
```

---

## Why Postman also fails

Two separate issues:

### 1. Infrastructure (primary)

Suresh's demo host resolves to **localhost**. His machine likely had:

- A **local JBoss/API proxy** running on port 443, **or**
- A **hosts/DNS + tunnel** setup active during the demo

Without that stack running, neither curl nor Postman can connect.

### 2. Postman collection URL bug (fixed 2026-07-27)

Previous collection put `https://api.localdev.acs529.com/api/v1` inside the `host` field. Postman requires:

- `host` = `api.localdev.acs529.com` only
- `path` = `api`, `v1`, `plans`, `unite`, `returnmail`, `{barcodeId}`

Re-import `postman/SYN-443-Barcode-API.postman_collection.json` and `SYN-443-Barcode-API-QC4.postman_environment.json`.

---

## What you need from Suresh before retry

| # | Item | Why |
|---|------|-----|
| 1 | Contents of `returnmail-body.json` | Required request body |
| 2 | Client cert + key (private) | TLS client auth for `*.localdev.acs529.com` |
| 3 | What must be **running locally** (proxy/JBoss port 443?) | Explains 127.0.0.1 DNS |
| 4 | Confirm **POST** vs GET | curl uses `--data-binary` → POST |

---

## Retry checklist (your machine)

1. [ ] Ask Suresh: is local proxy/JBoss required? Start it if yes.
2. [ ] Confirm DNS: `ping api.localdev.acs529.com` — if 127.0.0.1, local stack must be up.
3. [ ] Save `returnmail-body.json` to `C:\temp\` (or paste into `barcode.requestBody` env var).
4. [ ] Postman → Settings → Certificates → add cert for `api.localdev.acs529.com`.
5. [ ] Re-import fixed collection + environment.
6. [ ] Send **Return Mail Lookup (POST)**.

### PowerShell retry command

```powershell
curl.exe -v -k `
  "https://api.localdev.acs529.com/api/v1/plans/unite/returnmail/UNT13649678458" `
  -H "Host: api.localdev.acs529.com" `
  -H "Content-Type: application/json" `
  --data-binary "@C:\temp\returnmail-body.json"
```

Add `--cert` and `--key` once Suresh provides them.

---

## Postman environment (current)

| Variable | Value |
|----------|-------|
| `barcode.host` | `api.localdev.acs529.com` |
| `barcode.id` | `UNT13649678458` |
| `barcode.requestBody` | `{}` (replace with real JSON from Suresh) |

**Resolved URL:** `https://api.localdev.acs529.com/api/v1/plans/unite/returnmail/UNT13649678458`
