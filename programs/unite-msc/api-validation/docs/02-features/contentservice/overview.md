# Content Service — Overview

**Status:** Not Started | **Validation:** NO-DB / external only

| Item | Path |
|------|------|
| Feature | `contentservice.feature` |
| Stepdefs | `ContentServiceStepdefs.java` |
| Service | `ContentService.java` |
| Gateway | `ContentGateway` → external CMS |

## BFF endpoint

`GET /mobile2api/v1/content`

## DB validation

**None.** Content is HTML from `content.service.url` (howtosaveforcollege.com / configured CMS).

## Validation approach

- HTTP contract tests (status, content-type)
- Optional snapshot compare against fixture files
- Do not add SQL under `sql/` for this feature

See `docs/00-architecture/external-systems.md`.
