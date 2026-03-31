# Gaps analysis — backlog

## 1. Missing inputs from stakeholders

| Gap | Why it blocks | WHO must provide |
|-----|----------------|------------------|
| **Real Jira export** (`data/jira-export.csv`) | Dedup against existing keys; match naming | Jira admin / SM export |
| **Project key & components** | Import mapping | Jira admin |
| **Authoritative plan list** for V2/V3 (which plans in scope) | Avoid over-claiming “all plans” | Product + chapter SME |
| **IDP cutover calendar** | V2 vs V3 ownership of same flow | Platform / program |
| **Performance SLOs** | AC numerically testable | NFR owner / SRE |
| **qTest project & cycle naming** | Perf stories need link targets | QA tooling owner |
| **Stage 5 / CAT hostnames & credentials** | Smoke pipeline stories | Infra |
| **API catalog** for API↔UI mapping | Scope of mapping epic | Tech lead / architect |

---

## 2. Risk areas

| Risk | Mitigation (Story coverage) |
|------|-----------------------------|
| Flaky IDP undermines all V3 signal | QA-S-V3-001 + timeboxed spike if needed |
| Pipeline drift (Entity/Unite) | QA-S-PLAT-001 + monitoring Story |
| Offshore DB/schema permissions | Link AM Troubleshooting KB; separate infra Story if needed |
| Perf tests without stable env | Preeti stories gated on env parity note in AC |
| Governance shelfware | `00-overview/rollout-enforcement-and-leadership.md` — leadership email |

---

## 3. Coverage gaps (test / automation)

| Area | Gap | Proposed follow-up |
|------|-----|-------------------|
| V3 mobile / non-Chrome | Not in current input | Add Story when in scope |
| Accessibility | Not in input | Epic candidate |
| Load on non-IDP endpoints | Partially in perf | Expand after IDP stable |
| Entity suite sync | Mentioned historically in team updates | Add under QA-E-PLAT-INF when confirmed |

---

## 4. Duplicate / merge candidates

Once `jira-export.csv` exists, compare:

- Any existing **IDP** / **UE** / **perf** Stories → merge description into QA-S-* IDs or retire duplicates.
- **“Stabilize”** Stories → ensure one owner metric (e.g., flake rate, consecutive greens).

---

**Version:** 1.0
