# Barcode Project Trackr — SYN-443 Performance Testing

**Epic:** [SYN-443 — Returned Mail Barcode Cost Saving Enhancement](https://ascensuscollegesavings.atlassian.net/browse/SYN-443)  
**AHA:** ACS-1696  
**Product:** ASTRO (529 + **ABLE** plans)  
**Priority:** High (last-minute perf testing gap before release)  
**Target ETA:** Friday **2026-07-31** EOD (worst case)  
**Perf engineer:** Kriti (offshore)  
**QA Automation lead:** Swapnil Patil  
**Synergy dev contacts:** Suresh Mahto, Krishna Reddy, Laxmi Priya Samala Pandu  
**PM:** Brenda Montoya  
**Approver / perf strategy:** Rajib Akhter  

---

## What this project is

When mail ops receives **returned mail**, ODS/Kofax scans a **barcode** on the piece. That scan triggers a **single GET API** on the Unite server. The API returns **customer / mail details** needed for the **Mailstop** process (eliminating manual indexing and 2nd-attempt mailers).

Performance testing was missed in the delivery plan. QA Automation is standing up a **lightweight, one-endpoint** perf baseline in **QC4** so Synergy can extend it later.

---

## Folder map

| Path | Purpose |
|------|---------|
| [JIRA-story-SYN-443-barcode-perf-testing.md](./JIRA-story-SYN-443-barcode-perf-testing.md) | **Copy-paste JIRA Story** for Kriti |
| [postman/](./postman/) | Postman collection + QC4 environment |
| [docs/01-setup-curl-to-postman.md](./docs/01-setup-curl-to-postman.md) | Import curl, certs, first successful call |
| [docs/02-environment-strategy.md](./docs/02-environment-strategy.md) | QC4 vs Stage vs Prod — auth & cert decision log |
| [docs/05-dev-team-meeting-agenda.md](./docs/05-dev-team-meeting-agenda.md) | **Dev meeting agenda** — QC4 vs Stage, questions, acceptance criteria |
| [communications/](./communications/) | Email drafts and status update templates |
| [OPEN-ITEMS.md](./OPEN-ITEMS.md) | Blockers, owners, decisions needed |
| [api/curl-from-suresh.md](./api/curl-from-suresh.md) | Paste authoritative curl from dev call |
| `SYN-443.doc` | Epic export |
| `Teams Chat.txt` | Initial Teams thread |
| `Channel Discussion 1.png` / `2.png` | QC4 vs Stage cert thread |
| `Call with Dattatraya and 4 others.docx` | 2026-07-24 kickoff transcript |

---

## Current status (2026-07-27)

| Item | Status |
|------|--------|
| Kickoff call with Synergy devs | Done (2026-07-24) |
| Epic linked | [SYN-443](https://ascensuscollegesavings.atlassian.net/browse/SYN-443) |
| QC4 test data SQL | `select barcode_id, a.* from tu_sent_mail a;` (Suresh) |
| Authoritative curl from Suresh | **Blocked** — meeting ended before curl was shared; see [api/curl-from-suresh.md](./api/curl-from-suresh.md) |
| Rajib approval — QC4 vs Stage | **Pending** — see [communications/email-rajib-qc4-approval-draft.md](./communications/email-rajib-qc4-approval-draft.md) |
| QC4 wildcard cert for Postman | Suresh / Rajib path — cert `*.localdev.acs529.com` (do **not** commit cert or passphrase) |
| JIRA Story created | **Draft ready** — create in JIRA and link to SYN-443 |
| Postman collection | **Template ready** — finalize after curl received |
| JMeter / Blaze baseline script | Not started — Kriti, after Postman green |

---

## Quick start (Kriti)

1. Get **Rajib sign-off** on QC4 approach (or revised Stage plan).
2. Obtain **curl** from Suresh → paste into [api/curl-from-suresh.md](./api/curl-from-suresh.md) and update Postman.
3. Follow [docs/01-setup-curl-to-postman.md](./docs/01-setup-curl-to-postman.md) for cert + first 200.
4. Pick load targets from [docs/03-load-profile.md](./docs/03-load-profile.md) (confirm with Rajib / Brenda).
5. Implement JMeter script (reuse existing perf framework patterns).
6. Post daily status using [communications/status-update-template.md](./communications/status-update-template.md).

---

## Key technical notes

- **One primary GET endpoint** (per Suresh, 2026-07-24 call).
- **QC4:** Partner auth bypassed on JBoss; wildcard cert can be used in Postman locally.
- **Stage:** Requires `kofaxapi.stage.acs529.com` client cert; DevOps policy — no Stage/Prod passcodes to external teams.
- **Prod:** `kofaxapi.prod.acs529.com` cert — out of scope for this sprint.
- **Risk if QC4-only:** Load numbers may be valid but **auth path differs** from Stage/Prod; document explicitly in results.

---

## Stakeholder comms

- **Brenda** — daily EOD progress (per Teams agreement).
- **Rajib** — environment strategy approval + load assumptions.
- **Suresh / Krishna / Laxmi** — API details, QC4 data, cert handoff (private channel only).

---

**Maintainer:** Swapnil Patil  
**Last updated:** 2026-07-27
