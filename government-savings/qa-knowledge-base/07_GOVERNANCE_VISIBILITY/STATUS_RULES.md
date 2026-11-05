# Status Rules

## Purpose

This document defines rules for status reporting to ensure consistent and meaningful status updates.

## Status Definitions

### Test Execution Status

#### ✅ PASS
- **Definition**: All tests passed or only non-critical tests failed
- **Criteria**:
  - Pass rate ≥ [Target, e.g., 95%]
  - No critical/high priority failures
  - Flakiness rate < [Target, e.g., 5%]

#### ⚠️ PASS WITH ISSUES
- **Definition**: Tests passed but with some issues
- **Criteria**:
  - Pass rate ≥ [Target, e.g., 90%] but < [Target, e.g., 95%]
  - Some non-critical failures
  - Issues are documented and tracked

#### ❌ FAIL
- **Definition**: Critical failures or low pass rate
- **Criteria**:
  - Pass rate < [Target, e.g., 90%]
  - Critical/high priority failures
  - Blocking issues present

### Release Status

#### 🟢 GREEN (Go)
- **Definition**: Ready for release
- **Criteria**:
  - All critical tests passed
  - No blocking defects
  - Test coverage met
  - Stakeholder approval

#### 🟡 YELLOW (At Risk)
- **Definition**: Release at risk, issues need attention
- **Criteria**:
  - Some issues present but manageable
  - Non-blocking defects
  - Mitigation plan in place

#### 🔴 RED (No-Go)
- **Definition**: Not ready for release
- **Criteria**:
  - Critical failures
  - Blocking defects
  - Test coverage not met
  - High risk identified

### Defect Status

#### OPEN
- **Definition**: Defect is open and being worked on
- **Sub-statuses**: New, Assigned, In Progress

#### RESOLVED
- **Definition**: Defect has been fixed
- **Sub-statuses**: Fixed, Verified

#### CLOSED
- **Definition**: Defect is closed
- **Sub-statuses**: Closed, Duplicate, Rejected, Deferred

## Status Reporting Rules

### Daily Status Updates

#### When
- During release testing
- When critical issues occur
- As requested by management

#### Content
- Test execution summary
- Pass/fail counts
- Critical issues
- Blockers
- Next steps

#### Format
- Brief (1-2 paragraphs)
- Bullet points for key items
- Clear status indicator
- Action items

#### Recipients
- Team members
- Development team
- Management (if critical)

### Weekly Status Updates

#### When
- Every week (typically Friday)
- Or as scheduled

#### Content
- Week summary
- Test execution metrics
- Defect summary
- Achievements
- Challenges
- Next week plans

#### Format
- Structured format (see `06_TEMPLATES/LEADERSHIP_UPDATE_TEMPLATE.md`)
- Metrics included
- Clear status

#### Recipients
- Team members
- Management
- Stakeholders

### Release Status Updates

#### When
- During release testing
- Before release decision
- After release

#### Content
- Release testing summary
- Test results
- Defect status
- Risk assessment
- Go/No-Go recommendation

#### Format
- Comprehensive report
- Use `06_TEMPLATES/EXEC_REPORT_TEMPLATE.md`
- Clear recommendation

#### Recipients
- Management
- Stakeholders
- Release team

## Status Escalation

### Escalation Triggers

#### Immediate Escalation
- Critical defects found
- Production issues
- Environment down
- Security issues

#### Standard Escalation
- High-priority defects
- Test execution failures
- Resource constraints
- Timeline risks

### Escalation Path

1. **Level 1**: Team Lead
   - First point of escalation
   - For team-level issues

2. **Level 2**: QA Manager
   - For process or resource issues
   - For cross-team issues

3. **Level 3**: Director/VP
   - For strategic issues
   - For critical business impact

## Status Communication Channels

### Daily Updates
- **Channel**: [Email, Chat, Standup]
- **Format**: Brief update
- **Timing**: [Time, e.g., End of day]

### Weekly Updates
- **Channel**: [Email, Confluence, Meeting]
- **Format**: Structured report
- **Timing**: [Day, e.g., Friday]

### Critical Updates
- **Channel**: [Immediate - Email, Phone, Chat]
- **Format**: Alert format
- **Timing**: Immediately

## Status Indicators

### Color Coding
- 🟢 **Green**: Good, on track
- 🟡 **Yellow**: Warning, needs attention
- 🔴 **Red**: Critical, action required
- ⚪ **Gray**: Not applicable, pending

### Status Icons
- ✅ Pass/Success
- ❌ Fail/Error
- ⚠️ Warning/Issue
- ⏳ In Progress
- 📊 Metrics/Data

## Best Practices

1. **Be Consistent**: Use standard status definitions
2. **Be Timely**: Report status promptly
3. **Be Clear**: Use clear language and indicators
4. **Be Actionable**: Include next steps
5. **Be Honest**: Report actual status, not desired status
6. **Be Complete**: Include all relevant information
7. **Be Concise**: Keep updates focused and brief

## Status Templates

### Daily Status Template
```
Status: [GREEN/YELLOW/RED]

Summary: [1-2 sentences]

Key Points:
- [Point 1]
- [Point 2]

Issues:
- [Issue 1]
- [Issue 2]

Next Steps:
- [Action 1]
- [Action 2]
```

### Weekly Status Template
See `06_TEMPLATES/LEADERSHIP_UPDATE_TEMPLATE.md`

## Related Documents

- `06_TEMPLATES/LEADERSHIP_UPDATE_TEMPLATE.md` - Update template
- `07_GOVERNANCE_VISIBILITY/METRICS_CATALOG.md` - Metrics definitions

## Notes

[Any additional status reporting rules or guidelines]
