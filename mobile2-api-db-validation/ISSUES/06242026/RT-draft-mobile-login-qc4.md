# RT Draft — QC4 Mobile Login Failure (`mobilemembersession` ECONNRESET)

**Issue folder:** `mobile2-api-db-validation/ISSUES/06242026`  
**Date reported:** June 24, 2026  
**Status:** Open — ready to submit via email

---

## Email header

**To:** [RT / Service Desk / Unite Platform Support distribution list]  
**Cc:** [Your manager / Mobile QA team / DevOps]  
**Subject:** [RT Request] QC4 — Mobile member login failing; `POST /mobile1api/v1/mobilemembersession` returns `ECONNRESET`

**Requestor:** [Your Name]  
**Team:** QA Automation / Mobile QA  
**Priority requested:** [High / P2]  
**Environment:** QC4

---

## Summary

Mobile member login is **not working in QC4**. Authentication fails at the member session endpoint. Postman calls to **`/mobile1api/v1/mobilemembersession`** fail before an HTTP response is returned, with:

```
Error: write ECONNRESET
```

This blocks mobile login validation, Postman/API smoke checks, and downstream Mobile1/Mobile2 automation in QC4.

---

## Business impact

- Mobile app login cannot be validated in QC4
- API-level auth smoke for Mobile1 is blocked
- Mobile2 / automation work depending on member session is blocked in QC4
- QC4 is used as a deployment gate for mobile regression

---

## Affected service / endpoint

| Item | Detail |
|------|--------|
| **Service** | unite-mobile1 BFF (Mobile1 API) |
| **Endpoint** | `POST /mobile1api/v1/mobilemembersession` |
| **Purpose** | Create mobile member session (login) — returns JWT/session |
| **QC4 base URL (Postman / automation)** | `https://mobileapi.qc4.acs529.com` |
| **Full URL tested** | `https://mobileapi.qc4.acs529.com/mobile1api/v1/mobilemembersession` |
| **Alternate QC4 BFF URL (app config)** | `https://unite-bff-wtn.qc4.unite529.com/mobile1api/v1/mobilemembersession` |

> Confirm which QC4 hostname/load balancer is authoritative if both are in use.

---

## Steps to reproduce

1. Open Postman (Desktop Agent / Cloud Agent — specify which was used).
2. Send **POST** to:
   ```
   https://mobileapi.qc4.acs529.com/mobile1api/v1/mobilemembersession
   ```
3. **Headers** (typical for mobile1 acceptance flow):
   - `Content-Type: application/json`
   - `Authorization: Bearer [acceptance-test JWT]` *(if collection uses it)*
   - `x-app-version: [app version, if required]`
4. **Body (JSON example):**
   ```json
   {
     "planId": "[planId — e.g. upromise]",
     "username": "[QC4 test username]",
     "password": "[test password]"
   }
   ```
5. Send request.

---

## Expected result

- HTTP **200** (or documented auth error such as 401/403 with JSON body)
- Response includes member session object with session id / JWT token
- Mobile login succeeds in QC4 app

---

## Actual result

- Request fails at transport layer — **no HTTP status code**
- Postman error: **`Error: write ECONNRESET`**
- Connection is reset before a response is received
- Mobile login fails in QC4 (see attachments)

---

## Troubleshooting already performed

- Verified endpoint path: `/mobile1api/v1/mobilemembersession` (Mobile1 member session — login entry point)
- Postman Postbot indicates likely causes:
  - Network / Postman Agent connectivity issue
  - Server abruptly closing the connection
  - Firewall / corporate proxy dropping the connection
- [ ] SSL verification on/off — same result
- [ ] Tested from [office VPN / off VPN / different network]
- [ ] Other QC4 mobile endpoints — e.g. health check, mobile2api
- [ ] Same test in [DEV / QC1 / Stage1] — works / also fails

---

## Error details

| Field | Value |
|-------|--------|
| **Error** | `write ECONNRESET` |
| **Client** | Postman [Desktop Agent / Cloud Agent] |
| **Region** | QC4 |
| **Time of failure (approx.)** | [e.g. June 24, 2026, ~10:30 AM ET] |
| **Frequency** | [100% reproducible / intermittent] |

---

## Attachments (this folder)

| File | Description |
|------|-------------|
| `MobileAuth Login failed - QC4.png` | Mobile login failure in QC4 |
| `Postman failing on auth endpoint.png` | Postman `ECONNRESET` on `mobilemembersession` |

---

## Requested action

Please investigate and restore QC4 mobile authentication:

1. Confirm **unite-mobile1 BFF** and upstream dependencies (auth, account, load balancer/ingress) are healthy in QC4.
2. Check whether the connection reset is caused by **LB/firewall/TLS** or the **application forcibly closing** the socket.
3. Review QC4 logs for `mobilemembersession` around the failure timestamp.
4. Confirm whether **`mobileapi.qc4.acs529.com`** vs **`unite-bff-wtn.qc4.unite529.com`** routing is correct.
5. Provide ETA and root cause once identified.

---

## Technical reference

- **Automation source:** `unite-mobile1` → `MobileMemberSessionStepdefs.java` posts to `mobilemembersession` for session creation.
- **App source:** `unite-accountowner` → `auth.service.ts` calls `mobile1dataServiceUrl + 'mobilemembersession'`.
- **QC4 app config:** `environment.qc4.ts` → `https://unite-bff-wtn.qc4.unite529.com/mobile1api/v1/`

---

## Contact

[Your Name] | [Email] | [Phone/Teams]

---

## Email body (copy/paste)

```
To: [RT distribution list]
Cc: [team]
Subject: [RT Request] QC4 — Mobile member login failing; POST /mobile1api/v1/mobilemembersession returns ECONNRESET

Hi Team,

Mobile member login is not working in QC4. Postman and the mobile app both fail at the authentication step.

Environment: QC4
Endpoint: POST https://mobileapi.qc4.acs529.com/mobile1api/v1/mobilemembersession
Error: Error: write ECONNRESET (connection reset before HTTP response)

Impact: Blocks mobile login validation, Postman auth smoke, and Mobile1/Mobile2 automation in QC4.

Steps to reproduce:
1. POST to /mobile1api/v1/mobilemembersession with planId, username, password JSON body
2. Request fails with ECONNRESET — no HTTP status returned

Expected: HTTP 200 with member session / JWT
Actual: Connection reset (ECONNRESET)

Attachments: MobileAuth Login failed - QC4.png, Postman failing on auth endpoint.png

Please investigate unite-mobile1 BFF, QC4 ingress/LB, and auth dependencies. Confirm routing for mobileapi.qc4.acs529.com vs unite-bff-wtn.qc4.unite529.com.

Thanks,
[Your Name]
[Team]
[Contact]
```
