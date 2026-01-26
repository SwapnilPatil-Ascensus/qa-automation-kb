# Raw Imports

## Purpose

This folder contains raw imported content that will be processed and organized into the knowledge base.

## Structure

### confluence_exports/
Raw exports from Confluence pages. These will be converted to Markdown and organized into appropriate folders.

### chats_exports/
Exports from chat conversations (Slack, Teams, etc.). Important decisions and information will be extracted.

### meeting_transcripts/
Meeting transcripts and notes. Key decisions will be extracted to `09_DECISIONS_WORKLOG/DECISIONS.md`.

### misc/
Other documents, emails, or content to be processed.

## Import Process

1. **Place Content**: Place raw content in appropriate subfolder
2. **Review**: Review content for important information
3. **Extract**: Extract key information
4. **Convert**: Convert to Markdown (if needed)
5. **Organize**: Move to appropriate numbered folder (00-11)
6. **Update**: Update `00_SYSTEM/SOURCES.md` with import details
7. **Archive**: Keep original in this folder for reference

## Guidelines

- **Don't Delete**: Keep original imports for reference
- **Document**: Update SOURCES.md when importing
- **Organize**: Move processed content to appropriate folders
- **Clean Up**: Periodically review and archive old imports

## Notes

Raw imports are preserved here for reference. Processed content becomes the source of truth in the numbered folders (00-11).
