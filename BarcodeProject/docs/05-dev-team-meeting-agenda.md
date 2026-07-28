# Dev Team Meeting — SYN-443 Barcode API Performance Testing

**Purpose:** Get everything required to run performance testing **without a local dev setup** — using a **real hosted environment** (QC4 and/or Stage 1).  
**Epic:** [SYN-443](https://ascensuscollegesavings.atlassian.net/browse/SYN-443)  
**Audience:** Suresh Mahto, Krishna Reddy, Laxmi Priya, Rajib Akhter, Brenda Montoya, DevOps  
**QA Automation:** Swapnil Patil, Kriti  
**Meeting date:** `[FILL IN]`  
**Last updated:** 2026-07-28

---

## 1. Our position (open with this)

> We are **not** set up to replicate a developer's local environment (local DNS → 127.0.0.1, local JBoss/proxy on port 443, local cert files). That is not sustainable for performance testing or handoff to the perf team.
>
> **What we need:** A **hosted, reachable URL per environment** (QC4 minimum; Stage 1 if that is the release gate), plus complete API contract, auth details, test data rules, and load/acceptance criteria — so we can run Postman smoke and JMeter load from our standard perf infrastructure.
>
> If **Stage 1 is the organic/production-like path** (certs, Kofax auth, real keys), we support testing there — but we need DevOps/Synergy to **provision access** (certs, network, credentials policy). We should not pretend QC4 local-dev URLs are the same thing.

---

## 2. What we have today vs what is missing

| Item | Status | Notes |
|------|--------|-------|
| Epic / business context | ✅ | SYN-443, Mailstop for 529 + ABLE |
| Demo curl (Suresh) | ⚠️ Partial | Uses **`api.localdev.acs529.com`** — resolves to **127.0.0.1**, not a hosted QC4 URL |
| QC4 hosted URL | ❌ | **Not provided** — blocker #1 |
| Request body (`returnmail-body.json`) | ❌ | Referenced in curl, contents unknown |
| Response schema / sample 200 | ❌ | Not documented |
| HTTP method confirmed | ❌ | Demo curl implies POST (`--data-binary`); call said "GET" |
| Client cert for hosted env | ❌ | Only wildcard `*.localdev.acs529.com` discussed |
| Stage 1 URL + cert path | ❌ | `kofaxapi.stage.acs529.com` — certs "not reading" per team thread |
| Test data SQL (QC4) | ⚠️ Partial | `select barcode_id, a.* from tu_sent_mail a;` |
| Load targets | ❌ | No TPS/concurrency agreement |
| Acceptance criteria per env | ❌ | Not defined |
| Perf runner network access | ❌ | Not confirmed |

**Smoke test result (2026-07-27):** curl to demo URL → `Connection refused` on port 443. See `04-smoke-test-results.md`.

---

## 3. QC4 vs Stage 1 vs Production — what is the difference?

Use this section in the meeting to align everyone.

| Dimension | QC4 (hosted — what we want) | What Suresh demoed (`localdev`) | Stage 1 | Production |
|-----------|----------------------------|----------------------------------|---------|------------|
| **URL type** | Hosted QC4 API gateway / BFF (e.g. `*.qc4.unite529.com` or Kofax QC host) | **Local dev** — DNS → 127.0.0.1 | Hosted Stage | Hosted Prod |
| **Who uses it** | QA / perf / integration | Developer laptop only | Kofax team (per Rajib) | Live ODS/Kofax |
| **Client certificate** | QC cert / wildcard `*.localdev.acs529.com` (if QC path) | Local wildcard cert + local proxy | **`kofaxapi.stage.acs529.com`** cert | **`kofaxapi.prod.acs529.com`** cert |
| **Partner / JBoss auth** | **Bypassed** in QC (per Suresh) | Bypassed locally | **Full Kofax auth path** | **Full Kofax auth path** |
| **Passcodes / secrets** | Dev team can help | Local files | DevOps: **not shared** with external teams (per Suresh) | Not shared |
| **Represents prod behavior** | App logic only — **auth path differs** | Dev-only — **not valid for perf sign-off** | **Highest pre-prod fidelity** | Ground truth |
| **Perf test viable for QA Automation?** | **Yes — if hosted URL + access provided** | **No — we will not support** | **Yes — if certs + network provisioned** | **No** (policy) |

### Why Rajib cares about Stage 1

- Kofax tests in **Stage**, not on a developer's laptop.
- Stage uses **real certificate + auth keys**; QC4/local may **skip** steps that exist in Production.
- If we only test QC4/local, we risk **false confidence** — app may be fast but **prod auth/cert path** could fail or add latency under load.

### Our recommendation to discuss

| Option | Description | When to choose |
|--------|-------------|----------------|
| **A** | **QC4 hosted URL only** (fast) | Friday deadline; Rajib accepts auth-path gap |
| **B** | **Stage 1 only** (organic) | Release gate requires prod-like auth; DevOps grants cert access |
| **C** | **Hybrid** (recommended if time allows) | QC4 load baseline by 7/31 + Stage 1 cert smoke for auth validation |

**Decision needed today:** ☐ A  ☐ B  ☐ C  — Owner: Rajib Akhter

---

## 4. Step-by-step — what must happen for perf test success

Walk through this checklist in the meeting. Capture answers in the **Answer** column.

| Step | Action | Owner | Answer / decision |
|------|--------|-------|-------------------|
| **1** | **Agree target environment(s)** for perf (QC4 hosted, Stage 1, or both) | Rajib + Brenda | |
| **2** | Provide **hosted base URL per environment** (not `localdev`) | Synergy Dev | |
| **3** | Confirm **HTTP method** (GET vs POST) and full path pattern | Synergy Dev | |
| **4** | Provide **complete request contract** (headers, body, path/query params) | Synergy Dev | |
| **5** | Provide **sample request + sample 200 response** (JSON) | Synergy Dev | |
| **6** | Document **authentication** per env (cert, headers, passcodes, keystore) | Dev + DevOps | |
| **7** | Provision **client cert** to perf team OR run Stage smoke internally | DevOps / Rajib | |
| **8** | Confirm **network path** from perf runner/Jenkins to API host | DevOps | |
| **9** | Define **test data rules** (DB barcode_ids, reuse, randomization) | Synergy Dev + DBA | |
| **10** | Define **load profile + acceptance criteria** per environment | Rajib + Ops | |
| **11** | Postman smoke **200** from hosted env | Kriti | |
| **12** | JMeter baseline + report | Kriti | |

---

## 5. Questions for the development team

### 5.1 Environment & URL (ask first — highest priority)

| # | Question | Why we need it | Answer |
|---|----------|----------------|--------|
| E1 | What is the **hosted QC4 URL** for this API? (Not `api.localdev.acs529.com`) | Local URL does not work for perf team | |
| E2 | Is the API deployed to QC4 today? If yes, **exact hostname + path**. | Confirms deploy status | |
| E3 | What is the **Stage 1 URL** for the same endpoint? | Stage 1 thread / organic testing | |
| E4 | Why was the demo done on **localdev** instead of QC4? | Understand gap | |
| E5 | Can Synergy provide a **working curl against hosted QC4** from a network we can reach? | Proof before we script | |
| E6 | Do we need **VPN, jump host, or IP allowlist** to hit QC4/Stage from perf runners? | Network planning | |
| E7 | Which **environment is the release gate** for perf sign-off? QC4, Stage 1, or both? | Drives Option A/B/C | |

### 5.2 API contract (exact technical spec)

| # | Question | Why we need it | Answer |
|---|----------|----------------|--------|
| A1 | **HTTP method** — GET or POST? | Demo curl uses POST body; call said GET | |
| A2 | Full **URL pattern** — is barcode ID a **path param** or **query param**? | JMeter parameterization | |
| A3 | Provide complete **`returnmail-body.json`** contents | Body is required in demo curl | |
| A4 | Which **headers are required**? (Host, Content-Type, Authorization, custom) | Postman/JMeter | |
| A5 | Any **optional** query params or headers? | Coverage / negative tests | |
| A6 | Provide **sample success response** (200 JSON) with field descriptions | Assertions | |
| A7 | Document **error responses** (400, 401, 403, 404, 500) and when they occur | Perf error-rate interpretation | |
| A8 | Is there an **OpenAPI/Swagger** spec or Confluence page? | Single source of truth | |
| A9 | Does the API **write** anything (audit log, mailstop trigger) or read-only lookup? | Side effects under load | |
| A10 | **Timeout** expectations — client vs server? | JMeter timeouts | |

### 5.3 Authentication & certificates ("search keys" / cert keys)

| # | Question | Why we need it | Answer |
|---|----------|----------------|--------|
| C1 | What auth is required on **hosted QC4**? | May differ from localdev | |
| C2 | What auth is required on **Stage 1**? | Organic path | |
| C3 | Stage team said certs/keys are **"not reading"** — what is broken? Who fixes? | Stage blocker | |
| C4 | Provide **cert CN, issuer, expiry** per environment | Keystore setup | |
| C5 | Who provisions **client cert** for perf team on Stage 1? (DevOps ticket?) | Unblocks Option B | |
| C6 | Are **passcodes/passwords** required in addition to cert? How are they injected? | JMeter pre-processor | |
| C7 | Can DevOps make an **exception** to share Stage creds with QA perf, or will Synergy run Stage perf? | Policy decision | |
| C8 | For QC4, is wildcard `*.localdev.acs529.com` only for local, or also for hosted QC4? | Avoid wrong cert | |

### 5.4 Test data & barcode_id behavior

| # | Question | Why we need it | Answer |
|---|----------|----------------|--------|
| D1 | Must `barcode_id` come from **`tu_sent_mail`** in QC4, or can we use any format? | CSV design | |
| D2 | Provide **10–50 valid barcode_ids** per environment (export or SQL) | Load test data pool | |
| D3 | If we send the **same barcode_id 10 times in a row**, what happens? Cache? Lock? Error? | Concurrency model | |
| D4 | If we send the **same barcode_id under load** (100 users), any **rate limit or lock**? | Realistic perf | |
| D5 | Can we **randomize** barcode IDs, or must they exist in DB with specific state? | Data generation | |
| D6 | Are there **plan-specific** barcodes (529 vs ABLE)? Do we need both? | Coverage | |
| D7 | What makes a barcode_id **invalid** for testing 404 path? | Negative test | |
| D8 | Does test data expire or get **consumed** (one-time use)? | Soak test design | |
| D9 | Confirm QC4 SQL: `select barcode_id, a.* from tu_sent_mail a` — still correct? Any filters? | Data query | |
| D10 | Who owns **refreshing test data** if rows are deleted? | Maintenance | |

### 5.5 Load, performance & acceptance criteria

| # | Question | Why we need it | Answer |
|---|----------|----------------|--------|
| L1 | Expected **peak scans per hour** during busy season? | Thread count | |
| L2 | How many **concurrent Kofax scanners** in peak? | Max users | |
| L3 | Target **p95 / p99 latency** (ms) per environment? | Pass/fail | |
| L4 | Max acceptable **error rate** under load? | Pass/fail | |
| L5 | Required **test duration** (smoke 1 min, soak 30 min, etc.)? | Schedule | |
| L6 | Baseline **TPS** from Kofax or ops? | Realistic load | |
| L7 | Any **downstream dependencies** under load (DB, Unite, external)? | Bottleneck analysis | |
| L8 | Acceptance criteria for **QC4** — what numbers sign off release? | Per-env AC | |
| L9 | Acceptance criteria for **Stage 1** — same or stricter? | Per-env AC | |
| L10 | Who **approves** perf results? (Rajib, Brenda, Kaden ops?) | Sign-off | |

### 5.6 Operational & handoff

| # | Question | Why we need it | Answer |
|---|----------|----------------|--------|
| O1 | **SME on call** during perf execution (name, timezone)? | Blocker resolution | |
| O2 | **Maintenance windows** — when not to load test QC4/Stage? | Avoid false failures | |
| O3 | Monitoring available? (APM, logs, server metrics) | Correlate latency | |
| O4 | After perf test, does Synergy want **JMeter scripts in GitLab**? Which repo? | Handoff | |
| O5 | Target date still **2026-07-31** given env blockers? | Reset ETA if needed | |

---

## 6. Acceptance criteria template — fill per environment

Use this in the meeting to get numeric agreement.

### QC4 (hosted)

| Criterion | Target | Agreed? |
|-----------|--------|---------|
| Postman/curl smoke returns **HTTP 200** from **hosted** QC4 URL | Yes | ☐ |
| Sample response matches agreed schema | Yes | ☐ |
| Load: concurrent users | `[ASK]` | ☐ |
| Load: duration | `[ASK]` | ☐ |
| p95 latency | `[ASK] ms` | ☐ |
| Error rate | `< [ASK] %` | ☐ |
| Auth path caveat documented (if QC4 bypasses prod auth) | Yes | ☐ |
| **Sign-off owner** | `[ASK]` | ☐ |

### Stage 1

| Criterion | Target | Agreed? |
|-----------|--------|---------|
| Client cert + auth path works (smoke 200) | Yes | ☐ |
| Same load profile as QC4 or stricter? | `[ASK]` | ☐ |
| p95 latency | `[ASK] ms` | ☐ |
| Error rate | `< [ASK] %` | ☐ |
| Required for **production release gate**? | Yes / No | ☐ |
| **Sign-off owner** | `[ASK]` | ☐ |

---

## 7. Load profile — draft to validate with ops

From SYN-443 epic (~55k returned mail/year). **Dev team must confirm or correct.**

| Scenario | Users | Duration | Purpose |
|----------|-------|----------|---------|
| Smoke | 1 | 1 min | Connectivity + correctness |
| Baseline | `[ASK]` | 10 min | Steady-state |
| Peak | `[ASK]` | 15 min | Busy-season simulation |
| Soak (optional) | `[ASK]` | 30 min | Leaks / stability |

**Data:** Rotate `barcode_id` from CSV (DB export) unless dev confirms reuse is valid.

---

## 8. Meeting agenda (30–45 min)

| Time | Topic | Outcome |
|------|-------|---------|
| 0–5 min | Position: no local dev setup; need hosted QC4/Stage | Alignment |
| 5–10 min | QC4 vs Stage 1 — Rajib's organic testing concern | Pick Option A/B/C |
| 10–20 min | Walk **Section 5.1–5.3** (URL, API, auth) | Fill answer column |
| 20–30 min | Walk **Section 5.4–5.5** (data, load, AC) | Fill answer column |
| 30–35 min | Assign owners + dates for every ❌ in Section 2 | Action list |
| 35–40 min | Confirm ETA still 7/31 or revised | Timeline |
| 40–45 min | Next sync / who sends hosted curl proof | Close |

---

## 9. Action log (fill during meeting)

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| 1 | Provide **hosted QC4 URL** + working curl | Suresh | | ☐ |
| 2 | Provide **returnmail-body.json** + sample 200 response | Suresh | | ☐ |
| 3 | **Stage 1 URL** + cert provisioning plan | DevOps / Suresh | | ☐ |
| 4 | Fix Stage cert "not reading" issue | `[ASK]` | | ☐ |
| 5 | Export **barcode_id** CSV for load test | Suresh / DBA | | ☐ |
| 6 | Confirm **load targets + AC** per env | Rajib + Brenda | | ☐ |
| 7 | Network access for perf runner to QC4/Stage | DevOps | | ☐ |
| 8 | Environment decision (A/B/C) recorded | Rajib | | ☐ |

---

## 10. One-liner summary for Rajib

> **Localdev is not a test environment for us.** Give us a **reachable QC4 or Stage 1 URL**, full API spec, cert access (or Synergy-run Stage smoke), test data rules, and load/acceptance numbers. We can deliver JMeter baseline quickly on **one endpoint** — but only against a **real hosted environment** that matches what you expect in production.

---

## Related docs

- `02-environment-strategy.md` — QC4 vs Stage tradeoffs
- `04-smoke-test-results.md` — why localdev failed
- `api/curl-from-suresh.md` — demo curl (local only)
- `03-load-profile.md` — load draft
- `../communications/email-rajib-qc4-approval-draft.md` — prior email draft
- `../OPEN-ITEMS.md` — blocker tracker
