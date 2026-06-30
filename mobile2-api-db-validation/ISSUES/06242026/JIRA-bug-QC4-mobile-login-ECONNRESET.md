# JIRA Bug — QC4 Mobile Login Failure (`mobilemembersession` ECONNRESET)

**Issue folder:** `mobile2-api-db-validation/ISSUES/06242026`  
**Date reported:** June 24, 2026  
**RT:** [514351](https://rt.acs529.com/Ticket/Display.html?id=514351)  
**DevOps channel:** DevOps Request (posted same day)

| Field | Value |
|-------|--------|
| **JIRA key** | _[QA-XXX — fill after create]_ |
| **Issue type** | Bug |
| **Priority** | High |
| **Environment** | QC4 |
| **Component** | unite-mobile1 BFF / Mobile Auth |
| **Status** | _Open → Done (close with RCA below)_ |
| **Affects** | Mobile login, Mobile1/Mobile2 QC4 automation |

---

## How to paste in Jira Cloud (read this first)

Your Jira uses the **new visual editor** (toolbar with **Tt**, **B**, lists, **</>**). It does **not** render old wiki markup (`h2.`, `{code}`, `{{monospace}}`) when pasted.

**What went wrong in your screenshot:** the whole description was pasted inside a **code block** (`</>`). Code blocks show raw text only — no headings or bullets.

### Do this

1. Click in the **Description** field (empty area — **not** the `</>` code button first).
2. Copy **only** the text inside the box labeled **“DESCRIPTION — copy below”** in the next section.
3. Paste with **Ctrl+V**. Jira should auto-format `##` headings, `**bold**`, and lists.
4. For the JSON body **only**: select those lines → toolbar **</>** → language **JSON**.

### Do not use

| Avoid | Why |
|-------|-----|
| `h2.`, `{code}`, `{{}}` | Legacy wiki markup — not supported in visual editor |
| Pasting into a code block first | Entire bug shows as monospace with line numbers |
| “Select language” for whole description | That dropdown is **only** for a small code snippet (JSON) |

### If auto-format does not apply after paste

Use toolbar manually: **Tt → Heading 2** for section titles, **B** for bold, bullet/number list icons for lists.

### Language dropdown (`Select language`)

Use **JSON** only for the request body snippet. Leave the rest of the description as normal rich text.

---

## 1. JIRA — copy/paste fields

### Summary (title)

Copy this into the **Summary** field:

```
[QC4][Mobile] Member login failing — POST mobilemembersession returns ECONNRESET
```

### Description — copy below

Copy everything inside the fence (from `## Environment` through the last bullet). **Do not** copy the fence lines themselves.

---

**DESCRIPTION — copy below** ↓

## Environment

- QC4

## Problem

Mobile member login is not working in QC4. Both the mobile app and Postman fail at authentication.

**Endpoint:** POST /mobile1api/v1/mobilemembersession

**URL:** https://mobileapi.qc4.acs529.com/mobile1api/v1/mobilemembersession

**Alternate app BFF host:** https://unite-bff-wtn.qc4.unite529.com/mobile1api/v1/

**Error (Postman):** `Error: write ECONNRESET`

Connection reset before any HTTP status is returned.

## Steps to reproduce

1. Open Postman (Desktop Agent).
2. POST to https://mobileapi.qc4.acs529.com/mobile1api/v1/mobilemembersession
3. Headers: Content-Type: application/json, Authorization: Bearer [acceptance JWT] (if required by collection)
4. Body (JSON):

```
{
  "planId": "upromise",
  "username": "<QC4 test member>",
  "password": "<password>"
}
```

5. Send request.

*(Optional: select only the JSON lines above → toolbar </> → language JSON.)*

## Expected

- HTTP 200 with MobileMemberSession (session id + JWT), OR documented 401/403 JSON error
- Mobile app login succeeds in QC4

## Actual

- Transport failure — no HTTP response
- write ECONNRESET
- Mobile app login fails (see attachment)

## Impact

- Blocks Mobile1 auth smoke and member-session-dependent Mobile2 flows in QC4
- Blocks QC4 mobile regression / deployment gate validation

## Related tickets / comms

- RT: https://rt.acs529.com/Ticket/Display.html?id=514351
- DevOps Request channel — 2026-06-24
- KB: qa-automation-kb/mobile2-api-db-validation/ISSUES/06242026/

## Evidence

- MobileAuth Login failed - QC4.png
- Postman failing on auth endpoint.png

## Technical reference

- unite-mobile1: MobileMemberSessionStepdefs → POST mobilemembersession
- unite-accountowner: auth.service.ts → mobile1dataServiceUrl + mobilemembersession
- QC4 config: environment.qc4.ts → unite-bff-wtn.qc4.unite529.com/mobile1api/v1/

**DESCRIPTION — copy above** ↑

---

### Description — plain text fallback (if Markdown paste fails)

If headings still do not format, paste this version instead (no special syntax):

```
ENVIRONMENT
QC4

PROBLEM
Mobile member login is not working in QC4. Both the mobile app and Postman fail at authentication.

Endpoint: POST /mobile1api/v1/mobilemembersession
URL: https://mobileapi.qc4.acs529.com/mobile1api/v1/mobilemembersession
Alternate app BFF host: https://unite-bff-wtn.qc4.unite529.com/mobile1api/v1/
Error (Postman): Error: write ECONNRESET
Connection reset before any HTTP status is returned.

STEPS TO REPRODUCE
1. Open Postman (Desktop Agent).
2. POST to https://mobileapi.qc4.acs529.com/mobile1api/v1/mobilemembersession
3. Headers: Content-Type: application/json, Authorization: Bearer [acceptance JWT]
4. Body JSON: planId=upromise, username=<QC4 test member>, password=<password>
5. Send request.

EXPECTED
- HTTP 200 with session/JWT, or valid 401/403 JSON error
- Mobile app login succeeds in QC4

ACTUAL
- No HTTP response; write ECONNRESET
- Mobile app login fails

IMPACT
- Blocks Mobile1 auth smoke and Mobile2 QC4 automation

RELATED
- RT: https://rt.acs529.com/Ticket/Display.html?id=514351
- DevOps Request channel — 2026-06-24

EVIDENCE
- MobileAuth Login failed - QC4.png
- Postman failing on auth endpoint.png
```

### Labels (suggested)

`QC4`, `mobile`, `mobile1`, `auth`, `ECONNRESET`, `regression-blocker`, `unite-mobile1`

### Linked issues

| Link type | Ticket |
|-----------|--------|
| Relates to | RT 514351 |
| Blocks | _[Mobile QC4 automation stories — optional]_ |

---

## 2. Acceptance criteria (for closure)

- [ ] `POST /mobile1api/v1/mobilemembersession` returns HTTP response (200 or valid auth error) — not ECONNRESET
- [ ] Mobile app login succeeds in QC4 with standard test member
- [ ] Postman collection auth step passes
- [ ] RCA section below completed and reviewed
- [ ] JIRA resolution comment references RT 514351 + this file

---

## 3. Impact

| Area | Impact |
|------|--------|
| **Mobile app (QC4)** | High — login unavailable |
| **Postman / API smoke** | High — auth entry point unreachable |
| **Automation** | High — `MobileMemberSessionStepdefs`, Mobile2 flows needing member JWT |
| **Other regions** | _[Confirm DEV/QC1/Stage1 unaffected — fill after check]_ |

---

## 4. Resolution (fill when DevOps confirms fix)

| Item | Value |
|------|--------|
| **Resolved date** | _YYYY-MM-DD_ |
| **Resolved by** | _DevOps / Platform — name_ |
| **Fix summary** | _One line — e.g. restarted unite-mobile1 pods / corrected ingress backend pool / renewed cert_ |
| **Verification** | _Postman 200 on mobilemembersession; mobile login OK; optional automation job ID_ |
| **Post-fix job / run** | _[GitLab job or manual test reference]_ |

---

## 5. RCA — complete before closing JIRA

> **Do not close on “works again” alone.** Update this section with DevOps/RT findings, then set JIRA **Done** with resolution *Fixed* or *Done* and link RT 514351.

| Item | Value |
|------|--------|
| **RCA owner** | _DevOps / Platform — [name]_ |
| **RCA date** | _YYYY-MM-DD_ |
| **Detection** | QA reported ECONNRESET on mobilemembersession; RT 514351 opened; DevOps Request posted |
| **Timeline** | _Reported 2026-06-24 → [investigation] → [fix applied] → [verified]_ |

### Root cause (final — replace draft)

_Draft below is a placeholder for common ECONNRESET patterns on QC4 BFF ingress. **Replace with confirmed wording from RT 514351 / DevOps** before closing._

**Draft (pending DevOps confirmation):**

QC4 requests to `mobileapi.qc4.acs529.com` for `POST /mobile1api/v1/mobilemembersession` were failing at the **TCP/TLS layer** with `ECONNRESET` because **[unite-mobile1 BFF had no healthy backend behind the QC4 load balancer / ingress — e.g. pod crash loop, deployment rollback gap, or backend pool drained after a release]**. The client never received an HTTP response, which presented as a mobile login outage and blocked auth-dependent automation. **[Optional: upstream auth/account dependency timeout causing the BFF to drop connections — only if confirmed in logs.]**

**Confirmed root cause (paste from DevOps):**

```
[REPLACE WITH RT 514351 RESOLUTION TEXT]
```

### Contributing factors

| Factor | Notes |
|--------|--------|
| _Deployment / release timing_ | _e.g. mobile1 deploy without successful health check on QC4 ingress_ |
| _Monitoring gap_ | _ECONNRESET may not surface as 5xx in app dashboards if connection never reaches app_ |
| _Dual hostname routing_ | _mobileapi.qc4.acs529.com vs unite-bff-wtn.qc4.unite529.com — confirm which path was broken_ |
| _Other_ | _fill_ |

### Evidence

| Source | Reference |
|--------|-----------|
| RT ticket | https://rt.acs529.com/Ticket/Display.html?id=514351 |
| Postman screenshot | `Postman failing on auth endpoint.png` |
| Mobile app screenshot | `MobileAuth Login failed - QC4.png` |
| Splunk / pod logs | _[link or summary from DevOps]_ |
| Ingress / LB check | _[e.g. no healthy targets for mobile1 backend pool]_ |

### Corrective action (what fixed it)

```
[REPLACE — e.g. Restarted unite-mobile1 deployment in QC4 / Re-applied ingress config /
 Re-pointed mobileapi.qc4 backend pool to healthy pods / Rolled back bad release]
```

### Preventive action

| Action | Owner | Target date |
|--------|-------|-------------|
| Add/post-deploy smoke for `POST mobilemembersession` on QC4 | QA / DevOps | _TBD_ |
| Ensure LB health checks cover mobile1 BFF before marking deploy complete | DevOps | _TBD_ |
| Document authoritative QC4 mobile hostname for Postman vs app | QA KB | _Done — ISSUES/06242026_ |
| _Other from RT_ | | |

### Sign-off

- [ ] RCA text confirmed with **DevOps** (RT 514351 resolution)
- [ ] Post-fix verification recorded (Postman + app)
- [ ] JIRA **Comment** includes RCA summary + link to this file
- [ ] JIRA **Resolution:** Fixed / Done

---

## 6. JIRA closure comment (copy/paste when closing)

```
Verified fixed in QC4.

RT: https://rt.acs529.com/Ticket/Display.html?id=514351

Endpoint POST /mobile1api/v1/mobilemembersession — no longer ECONNRESET; returns expected session response.

Mobile login: OK in QC4 app.

RCA: [One paragraph from section 5 — Confirmed root cause]

Corrective action: [From DevOps]

KB: qa-automation-kb/mobile2-api-db-validation/ISSUES/06242026/JIRA-bug-QC4-mobile-login-ECONNRESET.md
```

---

## 7. Attachments (same folder)

| File | Use in JIRA |
|------|-------------|
| `MobileAuth Login failed - QC4.png` | Attach to bug |
| `Postman failing on auth endpoint.png` | Attach to bug |
| `RT-draft-mobile-login-qc4.md` | Reference / link only |
| `JIRA-bug-QC4-mobile-login-ECONNRESET.md` | This file |

---

**Reported by:** [Your Name]  
**Team:** QA Automation / Mobile QA  
**Last updated:** June 24, 2026 (Jira paste format — visual editor / Markdown, not wiki markup)
