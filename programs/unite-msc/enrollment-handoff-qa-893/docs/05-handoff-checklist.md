# Enrollment — post database-refresh handoff checklist

**QA-893 / QA-2044**

Run this after Stage1 / QC4 DB refresh **before** claiming Enrollment regression is green.

## Before refresh (if you control timing)

- [ ] Note last green GitLab/local run (date, plant, suite)
- [ ] Confirm no one is mid-wizard on shared automation accounts

## After refresh

| # | Task | Done |
|---|------|------|
| 1 | VPN + Frogger/PuTTY tunnel up (`gwtpsshrelay01`, Stage1 DB localhost:41521) | |
| 2 | Confirm `qc4.properties` / host file still points at live hosts (do not commit secrets) | |
| 3 | Recreate or verify `QAAUTOTEST%` (or current automation username pattern) | |
| 4 | MFA / SMS / email OTP: if enrollment or mobile login needs a device, re-enroll **test** devices only | |
| 5 | GET `/enrollmentapi/v1/certificate` — new cert after env rebuild | |
| 6 | Smoke: `mobile-ms-enrollment-smoke` on okdirect | |
| 7 | Regression: wizard through review-confirm on okdirect + newyork | |
| 8 | If mobile session step is used: Mobile1 session user still exists | |
| 9 | Allocation funds GET or SQL fund ids still valid | |
| 10 | File a Freshservice ticket if Linux/DB access was wiped — not RT | |

## Account and MFA

- Do not use production member accounts.
- Do not store OTPs or passwords in this KB or SharePoint.
- If IDP plants are added later (nmdirect), session/MFA rules follow IDP KT — not this MSC happy path.

## Who to ping

| Blocker | Path |
|---------|------|
| DB tunnel / Linux | Freshservice Linux / UII access (mirror `swpatil` if still valid) |
| BFF 500 after refresh | Platform / env owner |
| Suite red after data wipe | Receiving ACM + this checklist |

## Sign-off after refresh

A green smoke + one wizard regression on okdirect is the minimum to call the env usable. Full two-plant regression is the sustainment bar.
