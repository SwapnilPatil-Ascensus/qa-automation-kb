# SharePoint — Enrollment API (QA-893)

Parent: **Automation Squad → API Testing Hub** (or the API documentation project you already started).  
Do not nest under the old Confluence dump. Cursor cannot publish to SharePoint; paste Copilot prompts.

## Pages to create (only these)

| Order | SharePoint title | Prompt (paste, under 4k) | Attach |
|-------|------------------|--------------------------|--------|
| 0 | Enrollment API — Home | [copilot/00-hub-prompt.md](./copilot/00-hub-prompt.md) | Optional: `../docs/00-index.md` |
| 1 | How to run Enrollment | [copilot/01-run-prompt.md](./copilot/01-run-prompt.md) | `../docs/02-execution-troubleshooting.md` |
| 2 | Enrollment sign-off | [copilot/02-signoff-prompt.md](./copilot/02-signoff-prompt.md) | **DOCX** `Enrollment-API-Automation-Sign-Off.docx` |
| 3 | After DB refresh | [copilot/03-handoff-prompt.md](./copilot/03-handoff-prompt.md) | `../docs/05-handoff-checklist.md` |

Copy each attach file into a SharePoint/OneDrive library Copilot can read. Architecture, reporting, and AI guides stay in Git unless support asks for them on the site.

## Rules for Copilot

- No emoji, no stock photos, Calibri-style tables.
- Do not invent coverage %, Jenkins URLs, or passwords.
- Link to GitLab `api-test-automation` — do not paste Java.
