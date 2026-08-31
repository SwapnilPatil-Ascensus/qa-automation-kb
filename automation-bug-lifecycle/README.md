# Automation Bug Lifecycle

**QA Automation operating standard** — regression failure triage through resolution.

Use this module for day-to-day bug handling and for the **Persistent demo**: drop real failure artifacts into `evidence/regression-reports/MMDDYYYY/` and let Cursor + Prompt H produce JIRA, email, Teams, and change-set investigation in ~15 minutes.

## Layout (flat — one layer to find things)

| Path | Purpose |
|------|---------|
| `evidence/regression-reports/` | **Drop zone** — dated folders per failure (`MMDDYYYY/`) |
| `evidence/program-issues-unite-msc/` | Program-specific issue bundles (not daily regression) |
| `prompts/` | Cursor prompts 01–05 (triage, Prompt H, change set, resolution, rollup) |
| `templates/` | Bug doc, triage worksheet, JIRA/RCA templates |
| `process/` | Triage rules, flakiness, defect lifecycle, RCA, daily regression |
| `scripts/` | `new-evidence-folder.ps1` / `.sh` — bootstrap evidence folder |
| `cursor-kit/` | Cursor skill + JIRA formatting rule (copy to `.cursor/`) |
| `reference/` | Confluence Bug Handling PDFs, GitLab PM setup |
| `deliverables/` | Playbook DOCX, standard PPTX (presentation) |
| `assets/` | Workflow charts, GitLab PM screenshots |
| `WORKFLOW.md` | **End-to-end shell guide** — detect through resolution |
| `tools/` | `generate_deliverables.py` — rebuild DOCX/PPTX |

## Quick start

1. **One-time:** copy `cursor-kit/SKILL.md` → `.cursor/skills/automation-bug-lifecycle/`
2. **Per failure:** `scripts/new-evidence-folder.ps1 -Date MMDDYYYY -Feature FeatureName`
3. **Triage:** `prompts/01-triage-regression-failure.md`
4. **Defect:** `prompts/02-bug-report-prompt-h.md` (also in `qa-knowledge-base/00_SYSTEM/PROMPTS.md` § H)
5. **Change set:** GitLab Project Manager — `reference/gitlab-project-manager-setup.md`

Checklist: [`QUICK-START.md`](QUICK-START.md) · Workflow: [`WORKFLOW.md`](WORKFLOW.md) · Setup: [`SETUP-GUIDE.md`](SETUP-GUIDE.md)

## Deliverables (presentation)

| File | Purpose |
|------|---------|
| `deliverables/Automation-Bug-Lifecycle-Standard.pptx` | Team / leadership walkthrough deck |
| `deliverables/Automation-Bug-Lifecycle-Playbook.docx` | Detailed reference playbook |
| `WORKFLOW.md` | Shell guide — how to run the full flow |
| `deliverables/archive/` | Superseded versions |

```bash
python automation-bug-lifecycle/tools/generate_deliverables.py
```

Requires: `python-docx`, `python-pptx`, `matplotlib`, `Pillow`

## KB cross-references

| Topic | Location |
|-------|----------|
| Prompt library | `qa-knowledge-base/00_SYSTEM/PROMPTS.md` |
| Repetitive tasks how-to | `qa-knowledge-base/05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` |
| Bug reporting SOP | `evidence/regression-reports/BUG_REPORTING_PROCESS.md` |
| Constraints / no PII | `qa-knowledge-base/00_SYSTEM/CONSTRAINTS.md` |

## Related programs (not in this module)

| Program | Location |
|---------|----------|
| SYN-443 Barcode | `programs/barcode-syn-443/` |
| Unite MSC coordination | `programs/unite-msc/leadership/jira/` |
