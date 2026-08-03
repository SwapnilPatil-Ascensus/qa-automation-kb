# Mobile Microservices Automation — Immediate Action Items

**Last updated:** 2026-05-18

---

## Critical (before sprint work)

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| A1 | **Decide pilot module order** — Enrollment first (program brief) vs Mobile 2 first (Nick/Brian estimates) | Leadership | TBD | ☐ Open |
| A2 | **Decide architecture track** — Cucumber migration to API framework vs Path B (`unite-msc/` TestNG) vs hybrid | Architecture + QA | TBD | ☐ Open |
| A3 | Confirm **API Automation Framework** repo URL, branch, and `mobile-automation/` parent path | QA + Dev | TBD | ☐ Open |
| A4 | Obtain **read access** to UniteMSC source repos (`ascensus-gs/products/unitemsc`) | QA / Admin | TBD | ☐ Open |

---

## Discovery (Week 1–2)

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| B1 | Run **legacy inventory** for pilot module: feature files, steps, endpoints, SQL, configs, test data | QA | TBD | ☐ Open |
| B2 | Gather **Infinity team data** for QA-796 epic breakdown (per Brian note) | QA lead | TBD | ☐ Open |
| B3 | Map endpoints to **OpenAPI** specs where available (e.g. `mobile2.yaml`) | QA + Dev | TBD | ☐ Open |
| B4 | Document **IDP / Universal Platform / encryption** blockers per module | QA | TBD | ☐ Open |
| B5 | Populate tracker tables in [05](./05-unite-enrollment-migration-tracker.md) / [06](./06-unite-mobile1-migration-tracker.md) / [07](./07-unite-mobile2-migration-tracker.md) | QA | TBD | ☐ Open |

---

## Design and vertical slice (Week 2–4)

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| C1 | Sign off **target folder structure**, tags, and test data strategy | QA + Dev | TBD | ☐ Open |
| C2 | Select **3–5 vertical slice scenarios** for pilot module | QA | TBD | ☐ Open |
| C3 | Migrate vertical slice to target framework; prove **QC4 execution** | QA | TBD | ☐ Open |
| C4 | **Validate Maven command examples** in [08-regression-suite-and-pipeline-strategy.md](./08-regression-suite-and-pipeline-strategy.md) | QA | TBD | ☐ Open |

---

## Pipeline and DevOps

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| D1 | Align with DevOps on **CI platform** (GitHub Actions vs GitLab) and runner access | DevOps + QA | TBD | ☐ Open |
| D2 | Define **PR gate policy** — hard block vs advisory; smoke vs regression default | Leadership + DevOps | TBD | ☐ Open |
| D3 | Configure QC4/Stage1 **credentials** in pipeline secrets (not in property files) | DevOps | TBD | ☐ Open |
| D4 | Plan env-health probe + quarantine approach before hard-block gate | QA + DevOps | TBD | ☐ Open |

---

## Documentation and governance

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| E1 | **Publish Confluence hub** — copy pages per [README.md](./README.md) order | QA | TBD | ☐ Open |
| E2 | Post first **weekly status** using [10-weekly-status-and-leadership-updates.md](./10-weekly-status-and-leadership-updates.md) template | QA lead | TBD | ☐ Open |
| E3 | Update [09-raid-log.md](./09-raid-log.md) when DEC-1 and DEC-2 are decided | QA lead | TBD | ☐ Open |
| E4 | Import JIRA stories from [jira-stories/06-story-import-table.csv](./jira-stories/06-story-import-table.csv); link to QA-796 | QA | TBD | ☐ Open |

---

## Mobile UI automation (deferred — awareness only)

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| F1 | Create Confluence **placeholder** page for Mobile UI Automation workstream | QA | TBD | ☐ Open |
| F2 | Schedule Nick KT for local BrowserStack setup (separate track) | QA | TBD | ☐ Deferred |

---

## Completed

| # | Action | Completed |
|---|--------|-----------|
| ✓ | Generate Confluence-ready program hub markdown package | 2026-05-18 |
| ✓ | Generate JIRA epics, stories, and import CSV | 2026-05-18 |
