# Unite MSC Leadership Update — 2026-07-17

**Meeting:** Friday 9 AM leadership sync (Rajiv/Rajib, Henry, Kevin)  
**Prepared:** 2026-07-17  
**Reporting hub:** `qa-automation-kb/leadership-updates/unite-msc/2026-07-17-leadership-update/`  
**Primary program:** Unite MSC API automation (Mobile 1 + Mobile 2), performance regression, pipeline readiness, V2/V3 UI support

---

## Execution plan (how this pack was built)

| Step | Action | Source |
|------|--------|--------|
| 1 | Inventory Mobile 2 canonical tests, suites, Maven profiles | `api-test-automation/mobile/mobile2` |
| 2 | Pull verified endpoint coverage metrics | `project-documents/local-mobile-api-audit/16-mobile2-coverage-matrix.md`, `17-mobile2-api-automation-signoff.md` |
| 3 | Cross-check Mobile 1 scope and auth baseline | `03-document-postman-coverage-matrix.md`, `mobile/mobile1` |
| 4 | Pipeline / Nexus / DevOps status | `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md`, `15-devops-mobile2-integration-pipeline-guide.md` |
| 5 | Performance regression | `mobile2-api-db-validation/docs/01-shared/unite-msc-performance-testing-tracker.md` |
| 6 | V2/V3 UI context | `universal-platform-coverage/`, `10_IMPORTS_RAW/regression_reports/` |
| 7 | Team contributions | `git log` on `api-test-automation` (author-filtered) |
| 8 | Flag unverified / stale metrics | `metrics-verification-checklist.md` |

**Rule:** No invented numbers. Metrics dated **2026-07-14** or earlier are cited with date; post-07-14 deltas are marked **TBD / requires verification**.

---

## Deliverables in this folder

| # | File | Purpose |
|---|------|---------|
| 1 | [README.md](./README.md) | Index and execution plan |
| 2 | [source-map.md](./source-map.md) | Evidence → claim mapping |
| 3 | [repo-reference-map.md](./repo-reference-map.md) | Repo paths and owners |
| 4 | [mobile-coverage-map.md](./mobile-coverage-map.md) | M1/M2 endpoint coverage tables |
| 5 | [leadership-update-detailed.md](./leadership-update-detailed.md) | Full narrative for leadership |
| 6 | [leadership-meeting-pointers.md](./leadership-meeting-pointers.md) | 9 AM talking points |
| 7 | [gamma-slide-prompt.md](./gamma-slide-prompt.md) | Deck prompt (10–12 slides) |
| 8 | [weekly-status-email.md](./weekly-status-email.md) | Email draft |
| 9 | [jira-story-mobile2-nightly-gitlab.md](./jira-story-mobile2-nightly-gitlab.md) | DevOps story — **includes Prime V3 reference CI + proposed Mobile 2 YAML** |
| 10 | [team-contribution-summary.md](./team-contribution-summary.md) | Per-person summary |
| 11 | [metrics-verification-checklist.md](./metrics-verification-checklist.md) | TBD items + commands |
| 12 | [generated-docx-source.md](./generated-docx-source.md) | Word-export source + regen instructions |
| 13 | [generate_leadership_docx.py](./generate_leadership_docx.py) | Python generator (charts, RAG, header/footer) |
| 14 | `Unite-MSC-Leadership-Update-2026-07-17.docx` | Professional leadership Word document |

---

## Main message (one line)

Unite MSC automation has moved from fragmented legacy Cucumber into a **reusable, scalable canonical framework** across Mobile APIs, UI regression, performance testing, and pipeline readiness — **Mobile 2 baseline is ready for formal sign-off pending final MR merge and refreshed env evidence**; **Mobile 1 is the active sprint focus**.

---

## Reuse for future weeks

1. Copy folder → `YYYY-MM-DD-leadership-update/`
2. Re-run `metrics-verification-checklist.md` commands
3. Update `mobile-coverage-map.md` from latest sign-off matrix
4. Refresh `team-contribution-summary.md` from `git log`
5. Regenerate DOCX from `generated-docx-source.md`
