# JIRA Story — SYN-443 Barcode API Performance Testing (QC4)

**Epic:** [SYN-443](https://ascensuscollegesavings.atlassian.net/browse/SYN-443) — Returned Mail Barcode Cost Saving Enhancement  
**Assignee:** Kriti  
**Reporter:** Swapnil Patil  
**Sprint:** Current (start 2026-07-27)  
**Target complete:** 2026-07-31 EOD  
**KB module:** `qa-automation-kb/BarcodeProject/`  
**Labels (suggested):** `syn-443`, `barcode`, `performance`, `qc4`, `kofax`, `able`, `529`

---

## JIRA — Summary (title)

```
[SYN-443][Perf] Barcode returned-mail GET API — QC4 baseline load test (single endpoint)
```

---

## JIRA — Description (copy below)

Paste into Jira Description field (visual editor — **not** a code block). Use **Markdown** headings (`##`).

---

**DESCRIPTION — copy below** ↓

## Context

Epic **SYN-443** delivers a barcode enhancement to automate the **Mailstop** process for returned mail across **529 and ABLE** plans. ODS/Kofax scans a barcode; the scan hits a **Unite GET API** that returns customer/mail details.

Performance testing was not completed before release planning. QA Automation is delivering a **lightweight QC4 baseline** (one endpoint) by **2026-07-31**, using the existing JMeter/Blaze perf toolchain. Synergy dev team (Suresh Mahto) owns the API; Rajib Akhter must confirm **QC4 vs Stage** test strategy before results are treated as release evidence.

**KB / artifacts:** `qa-automation-kb/BarcodeProject/`

## User outcome

As a **performance engineer**, I want a **validated Postman request and JMeter baseline** for the barcode lookup GET API in QC4, so that Synergy can prove the endpoint meets agreed load/latency targets before production release.

## Scope

**In:**

- Convert dev-provided **curl** → Postman collection (QC4 environment)
- Configure **client certificate** for QC4 Postman calls (wildcard `*.localdev.acs529.com` — credentials via private channel, not in repo)
- Validate **HTTP 200** and response schema with sample `barcode_id` from QC4 `tu_sent_mail`
- Author **JMeter** (or Blaze/Taurus) script for single GET endpoint
- Run baseline load test in QC4 per agreed profile (see KB `docs/03-load-profile.md`)
- Document setup, results, limitations (QC4 auth bypass vs Stage/Prod cert path)
- Daily status to Brenda; environment decision recorded after Rajib approval

**Out:**

- Stage/Prod perf runs (blocked: cert + DevOps passcode policy unless Rajib approves alternate path)
- UI / Kofax scanner testing
- Functional regression of Mailstop business workflow beyond API response
- Full perf framework refactor (only lightweight project folder under BarcodeProject)

## API summary (from 2026-07-24 dev call)

| Attribute | Detail |
|-----------|--------|
| Method | **GET** (single endpoint) |
| Trigger | Kofax/ODS barcode scan → Unite server |
| Response | Customer / mail details for Mailstop processing |
| Test data (QC4) | `select barcode_id, a.* from tu_sent_mail a;` |
| Authoritative curl | **Pending from Suresh** — update `BarcodeProject/api/curl-from-suresh.md` |

`[NEED_INPUT]` — Paste exact URL, path params, query params, and headers once Suresh shares curl.

## Environment strategy (decision pending)

| Environment | Auth / cert | Perf test this sprint? |
|-------------|-------------|------------------------|
| **QC4** | Wildcard cert `*.localdev.acs529.com`; partner auth bypassed on JBoss | **Proposed** — pending Rajib approval |
| **Stage** | `kofaxapi.stage.acs529.com` client cert; plaintext passcodes not shared with external teams | **Blocked** unless DevOps exception |
| **Prod** | `kofaxapi.prod.acs529.com` | **Out of scope** |

**Risk to document in test report:** QC4 results measure **application throughput** but may **not** include Stage/Prod certificate handshake and partner-auth overhead.

## Dependencies

| Dependency | Owner | Needed by |
|------------|-------|-----------|
| Authoritative curl + sample barcode_id | Suresh Mahto | Day 1 (2026-07-27) |
| QC4 cert + passphrase (private) | Suresh / Rajib | Day 1 |
| Rajib approval — QC4 acceptable for perf sign-off | Rajib Akhter | Day 1 |
| Production-like load targets (TPS / daily volume / peak) | Rajib + Brenda + Kaden ops | Day 1–2 |
| JMeter/Blaze runner access to QC4 | Swapnil / DevOps | Day 2 |

## Links

| Resource | Location |
|----------|----------|
| Epic | https://ascensuscollegesavings.atlassian.net/browse/SYN-443 |
| KB README | `qa-automation-kb/BarcodeProject/README.md` |
| Postman collection | `BarcodeProject/postman/SYN-443-Barcode-API.postman_collection.json` |
| Curl → Postman guide | `BarcodeProject/docs/01-setup-curl-to-postman.md` |
| Environment strategy | `BarcodeProject/docs/02-environment-strategy.md` |
| Load profile draft | `BarcodeProject/docs/03-load-profile.md` |
| Kickoff transcript | `BarcodeProject/Call with Dattatraya and 4 others.docx` |

## Execution steps

### Phase 1 — Postman smoke (Day 1)

1. Import collection + QC4 environment from `BarcodeProject/postman/`.
2. Paste Suresh curl into `api/curl-from-suresh.md`; align collection URL, method, headers, params.
3. Configure Postman **Settings → Certificates** with QC4 wildcard cert (from private ping).
4. Run GET with a valid `barcode_id` from `tu_sent_mail`; confirm **200** and expected JSON fields.
5. Export updated collection if curl differs from template.

### Phase 2 — JMeter baseline (Day 2–3)

1. Record Postman request as HAR or manually build JMeter HTTP Sampler (match headers/cert).
2. Parameterize `barcode_id` from CSV (multiple rows from QC4 SQL).
3. Run smoke (1 user, 1 iteration) then stepped load per `docs/03-load-profile.md`.
4. Capture: throughput, p95/p99 latency, error rate, QC4 server metrics if available.

### Phase 3 — Report & handoff (Day 4–5)

1. Summary doc in `BarcodeProject/` (results markdown + screenshots).
2. KT note for Synergy on how to re-run and extend.
3. Log limitations (QC4 auth path) and recommend Stage follow-up if required for release gate.

## Known failure modes

| Symptom | Likely cause | Owner |
|---------|--------------|-------|
| SSL / cert handshake failure | Wrong cert or expired `*.localdev.acs529.com` | Suresh / Rajib |
| 401 / 403 | Missing header or wrong barcode_id | Dev + Kriti |
| 404 | Invalid test data in QC4 | Suresh — refresh SQL sample |
| Connection timeout from JMeter agent | Network / firewall to QC4 | DevOps |
| Results rejected for release | QC4 auth not representative of Stage | Rajib — escalate Stage cert path |

**DESCRIPTION — copy above** ↑

---

## Acceptance criteria

### Postman / connectivity

- [ ] Rajib (or delegate) **documents approval** of QC4 perf approach OR alternate Stage plan
- [ ] Authoritative curl captured in `api/curl-from-suresh.md`
- [ ] Postman GET returns **HTTP 200** for at least **one** valid QC4 `barcode_id`
- [ ] Response contains expected customer/mail fields (list fields in test report once known)

### Performance baseline

- [ ] JMeter (or Blaze) script runs from agreed agent against QC4
- [ ] Load profile executed per signed-off targets in `docs/03-load-profile.md`
- [ ] Results report includes: users, duration, throughput, p95 latency, error %
- [ ] Report explicitly states **QC4 auth limitation** vs Stage/Prod cert path

### Documentation & comms

- [ ] KB `BarcodeProject/` updated with final collection, script path, and results link
- [ ] Daily status sent to Brenda through **2026-07-31**
- [ ] Handoff note for Synergy on re-running tests

---

## Sub-tasks (suggested)

| # | Task | Assignee |
|---|------|----------|
| 1 | Obtain curl + sample barcode_id from Suresh | Kriti / Swapnil |
| 2 | Rajib approval email sent and decision recorded | Swapnil |
| 3 | Postman QC4 smoke green | Kriti |
| 4 | Confirm load targets with Rajib/Brenda | Swapnil |
| 5 | JMeter baseline script | Kriti |
| 6 | Execute load test + results markdown | Kriti |
| 7 | Create JIRA story in SYN project and link Epic | Swapnil |

---

## JIRA fields checklist

| Field | Value |
|-------|-------|
| Issue Type | Story |
| Epic Link | SYN-443 |
| Priority | High |
| Component | `[NEED_INPUT]` — Synergy / Performance |
| AGS Scrum Team | Synergy |
| Story Points | `[NEED_INPUT]` — suggest 3–5 after refinement |
| Fix Version | `[NEED_INPUT]` |

---

**Author:** Swapnil Patil  
**Last updated:** 2026-07-27
