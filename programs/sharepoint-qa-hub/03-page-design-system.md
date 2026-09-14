# 03 — Page design system (SharePoint modern)

Copilot will invent chrome if you let it. Constrain it.

## Look (what “latest product UX” means here)

SharePoint is not Figma. Aim for **Microsoft 365 Fluent**: lots of whitespace, short headings, cards, and one accent. Not Confluence panels stacked 20 high.

| Element | Rule |
|---------|------|
| Title | `NN Short name` — no emoji, no “DRAFT”, no “📘” |
| Hero | Image or color block + **one** sentence + **one** primary button |
| Width | Full-width hero; body in **two-thirds + one-third** (main + “On this page / Owners”) |
| Sections | At most **five** H2s per page |
| Tables | Preferred over paragraphs (matches KB role) |
| Callouts | One info, one warning max |
| Footer | Owner, last reviewed, source path in this Git repo |

## Web parts (allowed)

- Text
- Quick links (compact or button)
- Callout / Markdown (if enabled)
- People (owners)
- Divider
- Highlighted content (hub only)
- Document library (Archive 99 only)
- Embed (Jenkins/GitLab **behind SSO** — optional; never embed secrets)

Do **not** use: Countdown, Yammer dump, random stock photos of laptops, emoji heading spam.

## Status chips (text, not labels if labels are messy)

Use the same words as the old CI/CD doc: **Active**, **Legacy**, **In progress**, **Blocked**, **Needs review**.

## Page skeleton (every child)

See [templates/sharepoint-page-template.md](./templates/sharepoint-page-template.md).

1. Title + one-line purpose  
2. **Start in 2 minutes** (3 bullets or a 3-row table)  
3. **Standard** (the real content)  
4. **If it fails** (links to 05 / 10)  
5. **Source** (Git path + old PDF name for traceability)

## Accessibility

- No information in emoji only.
- Link text is the page name, not “click here”.
- Tables have a header row.

## Tone

Execution-ready. No generic QA theory. Same as `qa-knowledge-base/00_SYSTEM/ROLE.md`.
