# SharePoint — Enrollment module prompts (QA-893)

These four prompts are the original Enrollment-only draft. The complete parent/child site, upload manifest, KT, daily playbook, Mobile 1, Mobile 2, coverage, troubleshooting, and extension pages now live at:

[`programs/unite-msc/sharepoint/README.md`](../../sharepoint/README.md)

Use the complete pack for publication. Keep these prompts only as source history for QA-893; do not create a second Enrollment mini-site.

## Original module pages

| Order | SharePoint title | Prompt (paste, under 4k) | Attach |
|-------|------------------|--------------------------|--------|
| 0 | Enrollment API — Home | [copilot/00-hub-prompt.md](./copilot/00-hub-prompt.md) | Optional: `../docs/00-index.md` |
| 1 | How to run Enrollment | [copilot/01-run-prompt.md](./copilot/01-run-prompt.md) | `../docs/02-execution-troubleshooting.md` |
| 2 | Enrollment sign-off | [copilot/02-signoff-prompt.md](./copilot/02-signoff-prompt.md) | **DOCX** `Enrollment-API-Automation-Sign-Off.docx` |
| 3 | After DB refresh | [copilot/03-handoff-prompt.md](./copilot/03-handoff-prompt.md) | `../docs/05-handoff-checklist.md` |

Their content is incorporated into pages 07, 09, 10, and 11 of the complete Unite MSC site.

## Rules for Copilot

- No emoji, no stock photos, Calibri-style tables.
- Do not invent coverage %, Jenkins URLs, or passwords.
- Link to GitLab `api-test-automation` — do not paste Java.
