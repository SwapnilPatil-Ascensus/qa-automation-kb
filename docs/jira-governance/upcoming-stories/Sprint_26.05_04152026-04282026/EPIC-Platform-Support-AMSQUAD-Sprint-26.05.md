# Epic (draft) — Platform Support · AMSQUAD Sprint 26.05 (4/15–4/28)

**Sprint name:** AMSQUAD Sprint 26.05 4/15–4/28  
**Sprint window:** 15 Apr 2026 – 28 Apr 2026  
**Epic type (Jira):** Epic (or Initiative — match your Jira project)  
**Template reference:** Prior “Platform Support” sprint epic pattern (e.g. INNO Q3 Sprint layout: title, roster, scoped bullets, risks).

**Child work (this repo):** Link Stories/Spikes from [SPRINT-26.05-JIRA-STORIES.md](SPRINT-26.05-JIRA-STORIES.md) after they are filed in Jira.

---

## Copy — Jira Epic Summary

```
Platform Support — AMSQUAD Sprint 26.05 (4/15–4/28)
```

---

## Copy — Description

```markdown
## Purpose
Reserve capacity during **AMSQUAD Sprint 26.05** for **platform and production-adjacent support** so delivery work (V2/V3 automation, perf, pipelines) is not derailed by unplanned fires, release checkpoints, or cross-team asks.

*This epic mirrors the structure of historical “Platform Support” sprint epics (roster + scoped support bullets + risks), adapted to **QA Automation / AMS** context.*

## Support roster (fill before sprint start)
| Role | Name | Notes |
|------|------|--------|
| **Primary** | _Assign (QA Lead)_ | First-line triage: nightly failures, pipeline blockers, urgent re-runs |
| **Secondary** | _Assign_ | Backup when primary unavailable |
| **Escalation** | _QA Lead / Manager_ | Sev1, prod-impacting defects, scope conflicts |

*Do **not** copy INNO-specific names (e.g. from other teams’ epics) unless your program explicitly assigns those individuals to AMS this sprint.*

## Scope — in sprint (representative; adjust with QA Lead)
- **Regression & pipeline health:** Triage and coordinate **V2 Jenkins** and **V3 GitLab/Maven** scheduled runs (e.g. nightly / `scheduled_regression_job` style jobs — confirm live names in `prime-test-automation` CI config; KB only references the pattern in `docs/jira-governance/data/jira-export.csv`).
- **Environment / release alignment:** Support **Stage 5 / CAT** smoke and credential gaps called out in KB (`docs/jira-governance/backlog/stories.md` **QA-S-PLAT-002**, `gaps-analysis.md` Stage 5 / CAT).
- **ENVP / Universal Enrollment gate support:** Time-boxed help for Epic **QA-600** / ACS-5289 alignment (UE integration suite, flake triage) per `docs/jira-governance/upcoming-stories/Env-Pipeline_project/README.md`.
- **Cross-team unblock:** qTest linkage, Confluence doc touchpoints (hub pattern `pageId=315559619` in `jira-export.csv`), Selenium/report links — **no new scope** beyond clarification / routing.
- **Design or test-architecture reviews:** Short sessions for pipeline tagging, smoke vs integration boundaries, or perf package shape when requested by sprint Stories (e.g. **S2605-08**–**12**, perf **S2605-18**–**21**).

## Scope — out
- Full feature development for unrelated product teams (log separate Story).
- Long-running refactors that belong under dedicated epics (e.g. full ENVP program outside this sprint’s committed stories).

## Links
- Sprint story pack: `docs/jira-governance/upcoming-stories/Sprint_26.05_04152026-04282026/SPRINT-26.05-JIRA-STORIES.md`
- ENVP drafts: `docs/jira-governance/upcoming-stories/Env-Pipeline_project/`
```

---

## Risks (paste under Description or separate field)

```markdown
| Risk | Mitigation |
|------|------------|
| Platform hours consumed by one product fire | Cap **% of sprint** with QA Lead; escalate if cap exceeded |
| Nightly flakes mask real defects | Time-box triage; link to stabilization Stories (e.g. backlog **QA-S-V3-001** IDP, UE stability) |
| Stage 5 / CAT access or data drift | Track under gap analysis; do not silently “fix” env in automation without Infra/SME |
| ENVP expectations exceed sprint capacity | Align with Epic QA-600 owners; defer net-new gates to next sprint |
```

---

## Definition of Done (Epic level)

- [ ] Roster table completed in Jira at sprint start.  
- [ ] Weekly (or agreed) note in Epic comment: **support hours used**, **top 3 interrupts**, **any carry-over**.  
- [ ] Linked Stories for committed sprint delivery (**S2605-01** … **S2605-21**) remain visible; platform work is **labeled** (e.g. `platform-support`, `amsquad-sprint-26.05`) so it does not vanish in reporting.

---

## Suggested Jira labels

`platform-support`, `amsquad`, `sprint-26.05`, `automation`, `qa-board-view`

---

## Optional — map to INNO-style bullets (for Confluence table)

| INNO-style theme (from template) | AMS automation equivalent (this sprint) |
|----------------------------------|----------------------------------------|
| Support the Entity release | Support **release/regression checkpoints** for modules touched in Sprint 26.05 (exchange, maintenance, smoke, UE, perf). |
| Design review (Sub Bene & Save Points) | **Lightweight design / alignment** on smoke composition, pipeline gates, perf package boundaries (**S2605-08**–**12**, **18**–**21**). |
| Vanguard Support in CAT | **Stage 5 / CAT smoke & env support** (QA-S-PLAT-002, gaps doc). |
| UE Production Support — Primary | **UE + ENVP pipeline** triage and coordination (QA-600 / ACS-5289, UEPIPE drafts). |
| Google Tags / Team Infinity | **Cross-team tooling** (qTest, Confluence, report URLs) — **rename** to actual partner team when known. |

*Rename the last row in Jira to the real internal team you support (do not invent team names).*

---

*Draft version 1.0 — KB only; create the Epic in Jira and paste Summary + Description.*
