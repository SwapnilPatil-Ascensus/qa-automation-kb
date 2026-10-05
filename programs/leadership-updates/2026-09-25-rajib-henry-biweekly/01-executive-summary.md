# Executive Summary — Rajib / Henry Biweekly (Oct 1, 2026 · 3:00 PM ET)

**Presenter:** Swapnil Patil · **Deck:** `deliverables/AM-Squad-Biweekly-Status-Rajib-Henry-Oct01-2026.pptx`  
**Note:** Rescheduled from Fri Sep 25  
**Sprint scope:** 26.16 closeout + **26.17 (current)**  
**Board:** [QA AMSQUAD](https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/2515)

---

## 30-second opener

> **MSC coding is done. ENVP QA-600 is closed.** SharePoint KT hub is ready to publish. **Perf regression is healthy** — Enrollment MSC perf is the last MSC perf gap. **API GitLab nightly is still pending DevOps** — batch/job/remote mostly ready; need DB files on the server and a named owner (API regression waits on that). **Critical asks today:** (1) Stage1 **MFA / DB update support** for offshore — I’m the only one with update access; (2) **Stage5/CAT** regression takeover — I’ve been running V2+V3 per Brian; (3) **V3 IDP + Universal Enrollment** sustaining owner.

---

## Pulse

| Metric | Value |
|--------|-------|
| MSC coding | **100%** on main |
| ENVP QA-600 | **Closed** |
| SharePoint hub | Parent + 11 children — **publishing** |
| Perf regression | **Healthy** (Enrollment MSC perf remaining) |
| API GitLab nightly | **Pending DevOps** ownership |
| Stage1 / Stage5 | Recovered · CAT regression **running** (needs owner) |

---

## Leadership asks (need names on this call)

1. **Stage1 MFA / DB updates** — offshore has no update access; MFA disable after refresh / new accounts is single-threaded on me. Arrange support.  
2. **Stage5 / CAT regression** — name owner to take over V2 + V3 smoke support.  
3. **V3 IDP + Universal Enrollment** — name sustaining support owner.  
4. **API GitLab nightly** — confirm DevOps owner; copy DB files; turn on job. API regression pending until then.  
5. **Perf** — no ask (healthy). Keep Enrollment MSC perf priority.  
6. **Post-MSC queue** — Atlas vs API suite packaging vs Stage5/V3 support capacity?

---

## Jul–Sep TCs (shared with Dhanashree)

| | Jul | Aug | Sep |
|--|-----|-----|-----|
| V2 | 33 | 8 | 39 |
| V3 | 10 | 8 | 16 |
| Stage5/CAT | — | — | 49 |
| MSC ×3 plans | 99 | 75 | 6 |
| Perf | 12 | 22 | 47 |

---

## If they ask “what’s left on MSC?”

| Done | In flight | Waiting |
|------|-----------|---------|
| Coding M1/M2/Enrollment | SharePoint publish | API GitLab nightly (DevOps) |
| Bruno · qTest links · QA-600 | Enrollment **performance** | API regression schedule |
| Perf regression healthy | | Named support owners (MFA / CAT / V3) |
