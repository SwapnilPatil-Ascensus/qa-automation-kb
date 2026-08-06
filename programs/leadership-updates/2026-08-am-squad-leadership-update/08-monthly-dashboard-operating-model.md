# Monthly Leadership Dashboard — Operating Model

**Purpose:** Define how AM Squad maintains a **dynamic, auditable leadership dashboard** refreshed monthly across resources, channels, and platforms.  
**Audience:** Swapnil Patil (implementation) · Michael Blake / Dhanashree (consumers)  
**Date:** August 2026

---

## Problem we are solving

Today's leadership pack is **manually assembled** (days of effort per cycle). Michael Blake and VP audience need:

1. **High-level numbers first** — then drill-down on demand  
2. **Value narrative** — not raw test counts alone  
3. **Monthly refresh** — same structure, new data  
4. **Multi-channel view** — V2, V3, API/MSC, perf, pipeline, standards, cross-team  
5. **Per-resource contribution** — who delivered what

---

## Recommended architecture (3 layers)

Industry best practice (VP/board reporting): **operational → strategic → executive** layers with different refresh cadences.

| Layer | Audience | Refresh | Contents |
|-------|----------|---------|----------|
| **L1 — Operational** | Squad lead, engineers | Daily / weekly | Nightly pass rates, open defects, flaky tests, env status |
| **L2 — Strategic** | Directors, Dhanashree | Monthly | MR velocity, coverage by platform, roadmap % complete, emergency hours |
| **L3 — Executive** | VP (Michael Blake) | Monthly / quarterly | 5–7 KPIs, value stories, asks, ETA track record |

**This pack is L3 with L2 appendix.** The dashboard automates L2 → L3 generation.

---

## Target dashboard sections

| Section | Primary data source | Metric examples |
|---------|--------------------|-----------------|
| **Delivery velocity** | GitLab API / MR export | Merged MRs by month, author, repo, area |
| **Regression health** | Jenkins + GitLab CI artifacts | V2 module pass %, V3 suite status, API master suite |
| **Coverage by platform** | Repos + qTest + Jira | M2/M1 endpoints, V3 TestNG inventory, perf scenarios |
| **Release impact** | Historical FTE model + automation % | ~80% automated validations |
| **Cross-team support** | Jira labels + squad log | Emergency count, days absorbed |
| **Roadmap** | Jira epics | % complete, ETA vs actual |
| **AI / efficiency** | Internal tracker | Hours saved, agents used |

---

## Data sources & MCP integration

| System | MCP server | Status (Aug 6, 2026) | Data we need |
|--------|------------|----------------------|--------------|
| **Jira** | `user-jira` | ✅ Connected | QA stories closed, epics, sprint velocity |
| **GitLab** | `user-gitlab` | ⚠️ Blocked (TLS cert chain) | MR counts, pipeline status, schedules |
| **qTest** | `user-qtest` | ⚠️ Fetch failed | Test case inventory by module |
| **Jenkins** | File export / API (future) | Manual export today | Nightly HTML, perf job results |
| **CSV fallbacks** | Repo evidence folder | ✅ Working | `evidence/gitlab/*.csv`, regression snapshots |

**Minimum viable:** Continue CSV exports where API blocked; fix GitLab TLS (`NODE_EXTRA_CA_CERTS` or corporate root CA in MCP Node config) and qTest token for full automation.

---

## Monthly runbook (what you do each month)

### Week 1 — Collect (automated where possible)

```powershell
# 1. Export GitLab MRs (AM Squad repos, merged to main, date range)
#    → evidence/gitlab/merged-work-items-YYYYMM.csv

# 2. Regenerate MR analysis
python programs/leadership-updates/tools/analyze_gitlab_mrs.py

# 3. Regenerate charts
python programs/leadership-updates/tools/generate_leadership_charts.py

# 4. Snapshot regression (Jenkins HTML → CSV)
#    → data/regression-snapshot-YYYY-MM-DD.csv

# 5. (When MCP live) Jira closed stories, qTest module counts
```

### Week 1 — Generate deliverables

```powershell
python programs/leadership-updates/tools/generate_leadership_deliverables.py
```

Outputs:

- `deliverables/AM-Squad-Leadership-Update-YYYYMM.pptx`
- `deliverables/AM-Squad-Leadership-Briefing-YYYYMM.docx`
- `data/team-mr-summary.json` (machine-readable)

### Week 2 — Narrative pass (human, ~2 hours)

1. Update value stories in `06-value-roadmap-and-eta.md`  
2. Refresh roadmap table (Jira epic status)  
3. Update `05-vp-one-pager.md` headline numbers  
4. Send [email draft](./email-draft-to-dhanashree.md) to Dhanashree for VP routing

### Week 3–4 — VP session (optional)

30-minute live walkthrough — framework demo + dashboard review.

---

## Folder structure (maintain monthly)

```
programs/leadership-updates/
  YYYY-MM-am-squad-leadership-update/     ← copy prior month folder
    01-executive-summary.md
    05-vp-one-pager.md
    data/
      team-mr-summary.json
      regression-snapshot-YYYY-MM-DD.csv
      monthly-delivery-metrics.csv
    evidence/
      gitlab/
      jenkins/
    assets/charts/                          ← regenerated PNGs
    deliverables/
      AM-Squad-Leadership-Update-YYYYMM.pptx
      AM-Squad-Leadership-Briefing-YYYYMM.docx
```

**Rule:** If it is not in the folder with evidence, it does not ship to VP.

---

## Build vs buy

| Option | Effort | Recommendation |
|--------|--------|----------------|
| **A — Git repo + Python + MCP** (this plan) | Low; fits existing tooling | ✅ **Start here** — extend `coverage-intelligence` collector |
| **B — Power BI / Grafana** | Medium; needs IT data connectors | Phase 2 if VP wants self-serve clicking |
| **C — Confluence live dashboard** | Medium; manual macros | Fallback for readers who live in Confluence |

Phase 1 deliverable: **static PPTX/DOCX + JSON snapshot** generated monthly.  
Phase 2: **internal HTML dashboard** (`programs/leadership-updates/dashboard/`) reading JSON.  
Phase 3: **Power BI** fed by same JSON warehouse.

---

## 30 / 60 / 90 day plan

| Days | Action | Owner |
|------|--------|-------|
| **0–30** | Fix GitLab MCP TLS + qTest token; document in `09-mcp-validation` | Swapnil |
| **0–30** | Automate `analyze_gitlab_mrs.py` against GitLab API (fallback: CSV) | Swapnil |
| **30–60** | Extend collector: Jenkins nightly CSV ingest | Squad |
| **30–60** | First **automated monthly run** (Sep 2026 pack) | Swapnil |
| **60–90** | Pilot HTML dashboard from `team-mr-summary.json` | Squad |
| **90** | VP review: static deck vs live dashboard preference | Michael Blake |

---

## Success criteria

| Criteria | Target |
|----------|--------|
| Time to produce monthly pack | **< 4 hours** (from ~2 days today) |
| Number provenance | Every headline number traceable to CSV/API |
| VP consumption | One-pager + 15-slide deck; optional live demo |
| Drill-down | Deep dives linked from deck appendix |

---

## Related work already in flight

- `programs/government-savings-assessment/coverage-intelligence/` — GS coverage register pattern  
- `programs/government-savings-assessment/coverage-intelligence/10-leadership/action-item-proposal.md` — AI-06 weekly Python job  
- `automation-bug-lifecycle/tools/generate_deliverables.py` — branded DOCX/PPTX pattern to reuse
