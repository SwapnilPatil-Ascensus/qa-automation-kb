# Prompt Library

## Purpose

This document provides a quick index of Cursor instructions and prompts for common QA automation tasks.

## How to Use

When working with Cursor, reference these prompts to get consistent, high-quality assistance for QA automation tasks.

## Prompt Categories

### Test Development

#### Create Page Object
```
Create a Page Object class for [page name] following POM pattern.
Include:
- WebElement locators
- Action methods
- Verification methods
- Follow naming conventions from 02_STANDARDS/NAMING_CONVENTIONS.md
```

#### Create Test Scenario
```
Create a Cucumber test scenario for [feature/functionality].
Follow BDD best practices and use Gherkin syntax.
Include:
- Given/When/Then steps
- Test data considerations
- Expected validations
```

#### Create API Test
```
Create a REST Assured API test for [endpoint].
Include:
- Request setup
- Response validation
- Error handling
- Test data management
```

### Test Execution

#### Analyze Test Results
```
Analyze the test execution results and identify:
- Failed tests and root causes
- Flaky tests
- Performance issues
- Recommendations for fixes
```

#### Generate Execution Report
```
Generate a test execution report using 06_TEMPLATES/EXEC_REPORT_TEMPLATE.md.
Include:
- Execution summary
- Pass/fail statistics
- Failed test details
- Recommendations
```

### Debugging

#### Investigate Flaky Test
```
Investigate the flaky test [test name].
Follow the process in 04_EXECUTION/FLAKINESS_PLAYBOOK.md.
Identify:
- Root cause
- Fix recommendations
- Prevention strategies
```

#### Root Cause Analysis
```
Perform RCA for [issue/defect] using 06_TEMPLATES/RCA_TEMPLATE.md.
Include:
- Problem description
- Timeline
- Root cause
- Action items
```

### Documentation

#### Create Confluence Page
```
Create a Confluence page using 06_TEMPLATES/CONFLUENCE_PAGE_TEMPLATE.md.
Topic: [topic]
Include relevant sections from the knowledge base.
```

#### Create Jira Ticket
```
Create a Jira ticket using 06_TEMPLATES/JIRA_TICKET_TEMPLATE.md.
Type: [Bug/Story/Task]
Include all required fields and acceptance criteria.
```

### Onboarding

#### Setup Instructions
```
Provide setup instructions for a new team member following 05_ONBOARDING/LOCAL_SETUP.md.
Include:
- Prerequisites
- Step-by-step setup
- Verification steps
- Common issues and solutions
```

## Context-Aware Prompts

When using Cursor, always reference the knowledge base:

```
Using the QA automation knowledge base in this repo, [your request].
Reference relevant standards from 02_STANDARDS/ and architecture from 03_ARCHITECTURE/.
```

## Best Practices

1. **Be specific**: Include context about what you're working on
2. **Reference standards**: Always mention relevant standards documents
3. **Request templates**: Ask for templates when creating new documents
4. **Maintain consistency**: Use established patterns and conventions

## Custom Prompts

Add your own frequently used prompts here as you discover them.
