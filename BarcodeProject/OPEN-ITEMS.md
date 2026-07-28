# OPEN ITEMS — SYN-443 Barcode Perf Testing

**Last updated:** 2026-07-28

| # | Item | Owner | Status | Due |
|---|------|-------|--------|-----|
| 1 | **Rajib approval** — Is QC4 perf testing acceptable for release evidence, given Stage cert/auth differs? | Swapnil → Rajib | **Open** | 2026-07-27 |
| 2 | **Authoritative curl** from Suresh (URL, headers, params) | Suresh Mahto | **Done** | 2026-07-27 |
| 2b | **`returnmail-body.json`** contents | Suresh Mahto | **Open** | 2026-07-27 |
| 2c | **Hosted QC4 URL** (not localdev) — dev team committed deploy to QC4 but only shared local URL | Suresh Mahto | **Open** | 2026-07-28 |
| 2d | **Local proxy/JBoss on 443** — localdev DNS points to 127.0.0.1; **QA will not use local setup** | N/A — blocked | **Won't do** | — |
| 3 | **Sample barcode_id** rows from QC4 `tu_sent_mail` | Suresh Mahto | Partial (SQL known) | 2026-07-27 |
| 4 | **QC4 cert + passphrase** for Postman (private channel only) | Suresh / Rajib | In progress per Channel 2 | 2026-07-27 |
| 5 | **Production-like load targets** (TPS, peak, duration) | Rajib + Brenda + ops | **Open** | 2026-07-28 |
| 6 | **Create JIRA Story** in SYN project, link SYN-443, assign Kriti | Swapnil | Draft ready | 2026-07-27 |
| 7 | **JMeter agent** network path to QC4 API host | DevOps / Swapnil | **Open** | 2026-07-28 |
| 8 | Stage cert path / DevOps exception (if Rajib rejects QC4-only) | Rajib + DevOps | **Contingency** | TBD |

---

## Decisions log

| Date | Decision | Approver | Notes |
|------|----------|----------|-------|
| 2026-07-24 | Perf testing owned by QA Automation (Kriti); not Synergy QA team | Brenda / Swapnil | Teams chat |
| 2026-07-24 | Target ETA Friday 2026-07-31 | Brenda | Channel Discussion 1 |
| — | QC4 vs Stage for perf | **Pending** | Rajib raised valid auth concern |

---

## Risks

1. **QC4 auth bypass** — Results may not reflect Stage/Prod certificate + partner-auth latency.
2. **Missing curl** — Blocks Postman and JMeter until Suresh provides it.
3. **Tight timeline** — 1 endpoint is achievable; cert/network issues could consume Day 1.
4. **Load assumptions** — Epic cites ~55k returned mail/year; peak busy-season rate needs ops input.
