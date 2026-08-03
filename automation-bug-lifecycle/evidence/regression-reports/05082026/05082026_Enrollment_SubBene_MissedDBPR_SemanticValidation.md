# Supplementary note — engineering narrative (MR / DBPR / Teams)

> **Primary QA Automation bug record (create our own JIRA; RCA before close):**  
> **[`05082026_QA_BUG_Stage1_UE_SubBene_SQLFailures.md`](./05082026_QA_BUG_Stage1_UE_SubBene_SQLFailures.md)** · JIRA **[QA-821](https://ascensuscollegesavings.atlassian.net/browse/QA-821)**

This file keeps **optional** context that came from **engineering / Teams** (missed **`PR_107560`**, **MR !1615**, semantic validation, names). **Do not use ODY tickets as our system of record** — they lack detail for QA clone/workflow.

---

## Engineering thread summary (informal)

- **Symptom:** Stage 1 **enrollment** SQL errors and **sub-bene** issues across plans.
- **Direction from eng:** Error tied to a **missed package** used in **semantic validation**; **`PR_107560`** (*Update metrics package with new stored proc*, **EWW-330**) had not been applied on Stage 1.
- **Fix delivery:** **MR !1615** — *Add total balance stored proc* — `uii-releases`, branch `feature/EWW-368-missing` → `main` — adds **`DB_PRs/mod100.0/PR_107560.sql`** (+ release note line).
- **Apply:** **RT** to run approved **DBPR** on Stage 1; **Cristian Cejas** reported apply **without errors**; **enrollment** and **sub-bene** confirmed working afterward.

**MR:** https://ascensus-gs.gitlab.com/products/depot/uii-releases/-/merge_requests/1615

---

## Product tickets (reference only)

ODY-2518 / ODY-2519 — mentioned in chat only; **not** sufficient for our bug package. Link from our **QA-…** ticket under “See also” if needed.

---

**Artifacts:** Same folder — `Bug - Enrollment & Sub Seq enrollment issue.txt`, job **14273272936** links, screenshots.
