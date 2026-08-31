# Data Confidence & Leadership FAQ

**Purpose:** Prepare for VP questions on whether Apr–Aug numbers are real, defensible, and not double-counted against pre-April work.

**Team context:** AMSQUAD formed **Q2 2025**. Most team members hired **Nov 2025 – Mar 2026**. This pack reports a **5-month delivery window** (Apr–Aug 2026) within a **~12-month build**.

---

## Two different metrics — do not add them together

| Metric | What it measures | Apr–Aug example |
|--------|------------------|-----------------|
| **Monthly delivery chart** | New automation coverage **delivered each month** (period velocity) | ~**1,212** estimated test cases across 5 months |
| **Scorecard / nightly snapshots** | **Stage1 primary nightly job** inventory today (Aug 4) | V2 **592** + V3 **442** + Perf **323** |

**If asked:** *"Did you build 592 + 442 test methods in 5 months?"*

**Answer:** No. The squad started building frameworks and suites in **Q2 2025** with ~1–2 resources. The 592 and 442 numbers are **Aug 4 Stage1 nightly snapshots** of inventory accumulated over ~12 months. Apr–Aug is the **reporting window** for delivery velocity, not when the inventory began.

**If asked:** *"Does 592/442 include smoke, Stage 2, Stage 5, integrations?"*

**Answer:** No. Those numbers count **Stage1 primary nightly jobs only**. Additional coverage exists separately: V2 Stage 5/Stage 2 smoke, +33 CSR Actions (pending nightly wire), V3 Stage 5 smoke (UE + IDP), integration XML profiles, and Entity suites still expanding.

---

## Are the monthly numbers real?

**Source:** 225 Jira stories/tasks/spikes resolved Apr–Aug 2026 (AMSQUAD Sprints 26.04–26.12), classified by channel, multiplied by conservative per-story averages:

| Channel | Stories closed | Avg cases/story | Est. cases |
|---------|---------------:|----------------:|-----------:|
| API / Unite MSC | 88 | 4 | 352 |
| V3 Universal Platform | 29 | 8 | 232 |
| Performance Testing | 28 | 12 | 336 |
| V2 Legacy UI | 33 | 6 | 198 |
| Standards / Pipeline | 47 | 2 | 94 |
| **Total** | **225** | — | **~1,212** |

These are **estimates**, not a raw qTest diff. They align with Jira delivery volume and channel effort (MSC sprint peak Jun–Jul).

---

## Why test case counts are higher than "script count"

Leadership should expect **test cases > scripts** when we count correctly:

| Area | How we count | Example |
|------|--------------|---------|
| **Performance** | Transaction label × plan permutation | IDP login: 15 labels × 7 plans = **105** cases |
| **V3 UE** | Scenario × traunch/plan matrix | **303** nightly methods across enrollment plans |
| **API MSC** | Endpoint × branding plan (OKD + NYD/NMD) | 21 master areas × IDP/non-IDP multipliers |
| **V2/V3 UI** | Positive + negative paths, multi-module | CSR, enrollment, login variants per plan |

**Environments:** Stage1 (primary nightly — what 592/442 count), Stage5 smoke, Stage2 smoke, QC4 (API integration) — **not double-counted** in scorecard; reflected as separate jobs/suites.

---

## What existed before April 2026?

Pre-Apr foundation (not in the 5-month delivery chart, but in nightly inventory):

- Framework architecture and canonical repo structure (API, perf, UI)
- V2 baseline nightly suites on Jenkins Stage1
- V3 Universal Enrollment and IDP login suite foundations
- Perf IDP/legacy login baselines and Jenkins scheduling
- qTest master suite design and automation bug lifecycle standard
- Pipeline/DevOps co-design (hub workflow, module switches)

**Apr–Aug highlights (new delivery in period):**

- **Jun–Jul:** MSC API sprint — 48 MRs, M2 25/25, M1 ~86%
- **Apr–Jul:** V2 CSR maintenance modules (fee entry, contributions, authorize agent)
- **May–Jun:** V3 entity registration, withdrawal, web registration stabilization
- **Apr–Aug:** Perf barcode SYN-443, MSC endurance, pipeline API profiles

---

## Anticipated leadership questions

### "Your team is new — how did you deliver this much in 5 months?"

We didn't build from zero in 5 months. The squad has been operating since **Q2 2025**. Apr–Aug is the **reporting window** for this leadership pack. Nightly inventory reflects **~1 year** of build; the monthly chart shows **when** work landed (peak Jun–Jul during MSC).

### "Is 1,212 everything you've ever built?"

No. It's estimated **new coverage delivered in Apr–Aug** from closed Jira work. Pre-April suites (V2 baseline, UE foundation, perf baselines) are in the **592 / 442 / 323** inventory numbers, not re-counted in the monthly bars.

### "Why does performance show 323 but only 4 Jenkins scenarios?"

**323 = test cases** (labels × plans). **4 = scheduled Jenkins job definitions**. One JMeter scenario can execute dozens of plan permutations — same model used for IDP (7 plans), legacy (5 plans), MSC (2 brandings).

### "Can we audit these numbers?"

Yes. Sources: GitLab MR export, Jira AMSQUAD sprint export, Jenkins/GitLab nightly logs, api-test-automation repo inventory. Monthly estimates are derived; inventory snapshots are directly counted from nightly runs.

---

## Recommended slide footnote (use on monthly delivery chart)

> *Period delivery estimate (Apr–Aug 2026) — not cumulative inventory. Nightly totals reflect ~12 months of team build-out since Q2 2025.*
