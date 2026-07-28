# Email draft — Rajib approval (QC4 perf strategy)

**To:** Rajib Akhter  
**Cc:** Brenda Montoya, Suresh Mahto, Krishna Reddy, Laxmi Priya Samala Pandu, Kriti  
**From:** Swapnil Patil  
**Subject:** SYN-443 Barcode API — Request approval: QC4 performance testing approach (ETA 7/31)

---

## Body (copy below)

Hi Rajib,

Following Friday's discussion and our kickoff call with Suresh's team, I'm writing to confirm the performance testing approach for **SYN-443 (Returned Mail Barcode / Mailstop)** before Kriti begins execution this week.

### What we're testing

- **One GET API** on Unite: Kofax/ODS scans a barcode → API returns customer/mail details for the Mailstop process.
- **Scope:** Lightweight QC4 baseline using Postman (smoke) + JMeter (load), organized under `qa-automation-kb/BarcodeProject/`.
- **Target:** Baseline results by **Friday 7/31 EOD** (per Brenda's timeline).

### Why we're proposing QC4

- Suresh confirmed QC4 is viable for perf validation; Stage requires **client certificate auth** (`kofaxapi.stage.acs529.com`) and DevOps has indicated **Stage/Prod passcodes are not shared** with external teams.
- QC4 can use the wildcard cert (`*.localdev.acs529.com`) for Postman/JMeter — Suresh is coordinating cert handoff separately.
- This is a **single endpoint** — we can deliver a meaningful throughput/latency baseline quickly.

### Your concern (and how we'll address it)

You raised a valid point: **QC4 bypasses partner/JBoss authentication** that exists in Stage/Production. We agree that QC4-only results measure **application performance** but may **not** include full production auth overhead.

**We are asking for your approval on one of the following:**

1. **Option A (recommended for 7/31):** Proceed with QC4 baseline; document auth-path limitation in the report; open a follow-up for Stage cert validation if needed for release gate.

2. **Option B:** Hold QC4 load test until Stage cert path is available (likely pushes past 7/31).

3. **Option C (hybrid):** QC4 baseline by 7/31 + Synergy/Kofax runs a small Stage smoke with cert (auth validation only).

### What we need from you

1. **Approval** of Option A, B, or C (or a variant).
2. **Load assumptions** — rough peak scans/hour or concurrent Kofax sessions during busy season (draft profile in KB: `BarcodeProject/docs/03-load-profile.md`).
3. Whether QC4 results are **acceptable evidence** for release, or Stage cert test is a **hard gate**.

### Next steps (pending your reply)

| Step | Owner | When |
|------|-------|------|
| JIRA Story created & assigned to Kriti | Swapnil | Today |
| Curl + sample barcode_id | Suresh | Today |
| Postman smoke in QC4 | Kriti | Day 1 |
| JMeter baseline | Kriti | Day 2–4 |
| Daily status to Brenda | Swapnil / Kriti | Daily EOD |

**Epic:** https://ascensuscollegesavings.atlassian.net/browse/SYN-443  
**KB folder:** `qa-automation-kb/BarcodeProject/` (story draft, Postman collection, environment strategy doc)

Please reply with your preferred option so we can proceed without ambiguity. Happy to jump on a quick call if easier.

Thanks,  
Swapnil Patil  
QA Automation

---

## Follow-up (if no response by EOD 7/27)

Short ping:

> Rajib — gentle follow-up on QC4 vs Stage approval for SYN-443 barcode perf test. Kriti is blocked on environment sign-off. Default plan is Option A unless you prefer otherwise. Thanks.
