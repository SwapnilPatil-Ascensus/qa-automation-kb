# Gamma slide deck prompt — Unite MSC Leadership Update

**Date:** 2026-07-17  
**Deck length:** 10–12 slides max  
**Audience:** Rajiv/Rajib, Henry, Kevin — executive leadership

---

## Generation instructions for Gamma

Create a **premium executive** presentation: **dark navy background**, **white text**, **green** for complete/positive metrics, **amber** for in-progress/risks. **Low text per slide** — chart-heavy. Use Ascensus-adjacent professional styling (no cluttered bullets).

---

## Slide 1 — Title

**Unite MSC Automation Program**  
Weekly Leadership Update · July 17, 2026  
QA Automation · AMSQUAD

Visual: Subtle gradient navy header, program logo placeholder.

---

## Slide 2 — Executive summary

**Headline:** From legacy fragments to a scalable automation platform.

| Pillar | One-line status |
|--------|-----------------|
| Mobile 2 API | Baseline complete — sign-off path |
| Mobile 1 API | Active sprint — auth done |
| Performance | Foundation live — expanding |
| Pipeline | GHA slice done — nightly pending |
| V2/V3 UI | Stable nightly + daily triage |

Visual: 5-icon row with RAG dots (Green/Amber).

---

## Slide 3 — Program metrics snapshot

**Chart: Horizontal bar — Mobile 2 endpoint coverage**

| Label | Value |
|-------|------:|
| Documented endpoints | 25 |
| Automated (verified 07-14) | 22 |
| Coverage | 88% |
| Projected post-merge | TBD ≥96% |

**Chart: Donut — Mobile 1**

- Automated: 1
- Remaining: 26
- Auth foundation: Complete

Footnote: "Endpoint automation coverage — not code coverage."

Visual: Bar chart + small donut side by side.

---

## Slide 4 — Mobile 2: sign-off path

**Message:** Functionally complete — pending MR merge + env evidence.

| Done | Open |
|------|------|
| 19 test classes | GitLab nightly |
| Master OKD+NMD | Stage 1 fixture |
| IDP new capability | Formal sign-off |

Visual: Checklist with green checks; amber items on right.

---

## Slide 5 — Mobile 1: active sprint

**Message:** Authentication foundation on `main` — business endpoints now.

**Roadmap mini-timeline:**
- Now: Non-IDP baseline
- Next sprint: IDP hardening
- End next sprint: M1+M2 IDP/non-IDP target

Visual: 3-step timeline arrow.

---

## Slide 6 — Pipeline status

**Flow diagram:**

```text
Code → Nexus Archive → GHA (Dashboard ✓) → Module suites (in progress)
                                              ↓
                                    GitLab Nightly (NOT YET)
```

| Status | Item |
|--------|------|
| ✅ | Dashboard vertical slice |
| 🔄 | All module integration suites |
| ⏳ | GitLab nightly (DevOps story) |

Visual: Left-to-right pipeline flow with RAG table below.

---

## Slide 7 — Performance regression

| Metric | Value |
|--------|------:|
| MSC Jenkins jobs | 1 live |
| Non-IDP login→Dashboard | Done |
| IDP MSC login | In progress |
| Nightly scheduled | Not yet |

**Next flows:** Contribution · Banks · Activity · Mobile 1

Visual: Progress bar "Foundation → Flow expansion → Nightly"

---

## Slide 8 — V2/V3 UI regression

- Nightly regression: Stable
- Morning validation: 15–20 min (clean days)
- Defects: Daily triage — automation vs app team
- Gaps: Continuously closed from release regression

Visual: Simple status table — **TBD** cells for latest pass rate.

---

## Slide 9 — Team & kudos

**Snapshot table (no ranking):**

| Name | Focus | Highlight |
|------|-------|-----------|
| Swapnil | Program / master suite | Auth SQL, sign-off pack |
| Dinesh | Dashboard, plans, YTD | Plans MR, YTD |
| Venkatesh | Contribution, balance | CRUD contribution |
| Sunil | Banks, investments | Banks baseline |
| Priti | Performance | MSC Jenkins job |

**Callout:** Priti — fast ramp on auth/performance complexity.

Visual: 5-card grid with initials.

---

## Slide 10 — Risks & dependencies

| Risk | Severity |
|------|----------|
| No GitLab nightly | High |
| Test data Stage 1/5/2 | Medium |
| Enrollment encryption | Medium |
| Reporting load | Medium |

Visual: RAG heatmap 2×2.

---

## Slide 11 — Leadership asks

1. Approve GitLab nightly DevOps story  
2. Confirm M2 sign-off after evidence refresh  
3. Confirm M1 sprint priority  
4. Pipeline + environment support  
5. Structured intake for new asks  
6. BA/Scrum support (30–40%) for metrics cadence  

Visual: Numbered list with icons.

---

## Slide 12 — Next 2 sprints

| Sprint | Mobile 2 | Mobile 1 | Perf | Pipeline |
|--------|----------|----------|------|----------|
| **26.11 (now)** | Sign-off | Non-IDP baseline | IDP script | Module GHA |
| **26.12** | Sustain | IDP + hardening | Flow expansion | GitLab nightly |

**Horizon:** Enrollment API (multi-sprint)

Visual: Gantt-style 2-sprint roadmap.

---

## Visual asset recommendations

1. **Coverage bar chart** — M2 88% verified + projected arrow  
2. **Roadmap timeline** — M1/M2/Enrollment  
3. **RAG status table** — all tracks  
4. **Pipeline flow** — Nexus → GHA → GitLab  
5. **Team contribution cards** — 5 names  

## Data caveats for presenter

- Say "88% verified July 14" — not "100%"  
- Post-merge endpoint count is **TBD** until matrix refresh  
- V2/V3 nightly pass rate **TBD** unless export obtained before meeting  
