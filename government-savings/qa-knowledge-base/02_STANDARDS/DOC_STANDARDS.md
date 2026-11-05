# Documentation Standards

## Purpose

This document defines standards for writing and formatting documentation in this knowledge base.

## General Principles

1. **Clarity**: Write clearly and concisely
2. **Consistency**: Follow established patterns
3. **Completeness**: Include all necessary information
4. **Currency**: Keep documents updated
5. **Accessibility**: Make documents easy to find and navigate

## Markdown Formatting

### Headers

Use header hierarchy appropriately:
- `#` for document title (H1) - use once per document
- `##` for major sections (H2)
- `###` for subsections (H3)
- `####` for sub-subsections (H4)

### Lists

**Unordered Lists**:
```markdown
- Item 1
- Item 2
  - Nested item
```

**Ordered Lists**:
```markdown
1. First item
2. Second item
   1. Nested item
```

### Tables

Use tables for structured data:
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
```

### Code Blocks

Use code fences with language specification:
````markdown
```java
public class Example {
    // code here
}
```
````

### Emphasis

- **Bold** for important terms or emphasis
- *Italic* for emphasis or foreign terms
- `Code` for inline code, file names, or technical terms

### Links

- Internal links: `[Link Text](relative/path/to/file.md)`
- External links: `[Link Text](https://example.com)`

## Document Structure

### Standard Document Template

```markdown
# Document Title

## Purpose

Brief description of what this document is for.

## [Main Section 1]

Content here.

## [Main Section 2]

Content here.

## Notes

Any additional information.

---

**Last Updated**: [Date]
**Updated By**: [Name]
```

## Naming Conventions

### File Names
- Use `UPPERCASE_WITH_UNDERSCORES.md` for all documentation files
- Be descriptive and consistent
- Examples: `CURRENT_STATE.md`, `TEST_PLAN_TEMPLATE.md`

### Section Headers
- Use Title Case for section headers
- Be specific and descriptive
- Examples: "Test Execution Process", "Environment Configuration"

## Content Guidelines

### Writing Style

1. **Be Direct**: Get to the point quickly
2. **Use Active Voice**: "The test executes" not "The test is executed"
3. **Be Specific**: Avoid vague terms
4. **Use Examples**: Include examples where helpful
5. **Define Acronyms**: Define acronyms on first use

### Technical Content

- Include code examples where relevant
- Provide step-by-step instructions for processes
- Include diagrams or screenshots when helpful (use relative paths)
- Reference related documents

### Tables

- Use tables for comparisons, matrices, or structured data
- Include headers
- Keep tables readable (consider breaking large tables)

## Version Control

### Document Updates

- Update "Last Updated" date when making changes
- Include "Updated By" for significant changes
- Use Git commit messages that describe the change

### Change Log

For significant documents, consider including a change log:
```markdown
## Change Log

- 2026-01-25: Initial version
- 2026-01-26: Added section on [topic]
```

## Templates

Use templates from `06_TEMPLATES/` for:
- Confluence pages
- Jira tickets
- Test plans
- Execution reports
- Leadership updates
- RCA documents

## Review Process

1. **Self-Review**: Check for clarity, completeness, and formatting
2. **Peer Review**: Have a colleague review for accuracy
3. **Update Knowledge Base**: Ensure document is in correct location
4. **Notify Team**: Inform team of significant updates

## Examples

### Good Documentation

```markdown
## Test Execution Process

### Prerequisites
- Environment must be available
- Test data must be prepared
- Credentials must be configured

### Steps
1. Navigate to Jenkins dashboard
2. Select "Daily Regression" job
3. Click "Build with Parameters"
4. Select environment from dropdown
5. Click "Build"
```

### Poor Documentation

```markdown
## Testing

Do the tests. Make sure everything works.
```

## Checklist

Before publishing documentation:

- [ ] Follows document structure template
- [ ] Uses proper Markdown formatting
- [ ] Includes purpose statement
- [ ] Headers are properly nested
- [ ] Tables are formatted correctly
- [ ] Code blocks have language specified
- [ ] Links are working
- [ ] Acronyms are defined
- [ ] Examples are included where helpful
- [ ] Last updated date is current
- [ ] Document is in correct folder

## Notes

[Any additional documentation standards or guidelines]
