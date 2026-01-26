# Defect Lifecycle

## Purpose

This document describes the defect lifecycle process from identification to closure.

## Defect States

### New
- **Description**: Defect has been identified and logged
- **Actions**: Initial logging, assignment
- **Next State**: Assigned, Duplicate, Rejected

### Assigned
- **Description**: Defect assigned to developer/team
- **Actions**: Development team reviews
- **Next State**: In Progress, Duplicate, Rejected, Deferred

### In Progress
- **Description**: Defect is being worked on
- **Actions**: Development team fixes defect
- **Next State**: Fixed, Duplicate, Rejected, Deferred

### Fixed
- **Description**: Defect has been fixed
- **Actions**: QA verifies fix
- **Next State**: Verified, Reopened

### Verified
- **Description**: Fix has been verified
- **Actions**: Close defect
- **Next State**: Closed

### Reopened
- **Description**: Defect was not properly fixed
- **Actions**: Reassign, investigate
- **Next State**: Assigned, In Progress

### Duplicate
- **Description**: Defect is duplicate of existing defect
- **Actions**: Link to original, close
- **Next State**: Closed

### Rejected
- **Description**: Defect is not valid (not a bug, by design, etc.)
- **Actions**: Document reason, close
- **Next State**: Closed

### Deferred
- **Description**: Defect deferred to future release
- **Actions**: Document deferral reason, update priority
- **Next State**: Assigned (when picked up)

### Closed
- **Description**: Defect is resolved and closed
- **Actions**: Archive, no further action
- **Next State**: N/A (final state)

## Defect Priority

### Critical (P1)
- **Definition**: Blocks critical functionality, production down
- **SLA**: Fix within [time, e.g., 4 hours]
- **Examples**: Application crash, data loss, security breach

### High (P2)
- **Definition**: Major functionality broken, significant impact
- **SLA**: Fix within [time, e.g., 1 business day]
- **Examples**: Core feature not working, significant data issue

### Medium (P3)
- **Definition**: Moderate impact, workaround available
- **SLA**: Fix within [time, e.g., 1 week]
- **Examples**: Feature partially working, minor data issue

### Low (P4)
- **Definition**: Minor impact, cosmetic issues
- **SLA**: Fix within [time, e.g., next release]
- **Examples**: UI cosmetic issues, minor text errors

## Defect Severity

### Blocker (S1)
- **Definition**: Blocks testing or use of application
- **Impact**: Cannot proceed with testing/use
- **Examples**: Application crash, login not working

### Critical (S2)
- **Definition**: Major functionality broken
- **Impact**: Significant functionality unavailable
- **Examples**: Core feature broken, data corruption

### Major (S3)
- **Definition**: Important functionality broken
- **Impact**: Feature not working as expected
- **Examples**: Feature partially working, incorrect behavior

### Minor (S4)
- **Definition**: Minor functionality issue
- **Impact**: Small impact on functionality
- **Examples**: Minor feature issue, edge case

### Trivial (S5)
- **Definition**: Cosmetic or very minor issue
- **Impact**: Minimal impact
- **Examples**: UI cosmetic, text typo

## Defect Logging

### Required Information

#### Basic Information
- **Title**: Clear, concise summary
- **Description**: Detailed description of issue
- **Steps to Reproduce**: Step-by-step reproduction
- **Expected Result**: What should happen
- **Actual Result**: What actually happens
- **Environment**: Where defect was found
- **Priority**: Critical/High/Medium/Low
- **Severity**: Blocker/Critical/Major/Minor/Trivial

#### Additional Information
- **Screenshots**: Visual evidence
- **Logs**: Relevant log excerpts
- **Test Data**: Data used in test
- **Test Case**: Associated test case
- **Attachments**: Any relevant files
- **Reproducibility**: Always/Sometimes/Rarely

### Defect Template

Use `06_TEMPLATES/JIRA_TICKET_TEMPLATE.md` for defect logging.

## Defect Triage

### Triage Process

1. **Review Defects**
   - Review all new defects
   - Verify defect validity
   - Check for duplicates

2. **Categorize**
   - Assign priority
   - Assign severity
   - Assign to component/team

3. **Assign**
   - Assign to developer/team
   - Set target resolution date
   - Communicate assignment

4. **Track**
   - Monitor defect status
   - Follow up on overdue defects
   - Update stakeholders

### Triage Rules

See `04_EXECUTION/TRIAGE_RULES.md` for detailed triage rules.

## Defect Verification

### Verification Process

1. **Receive Notification**
   - Defect marked as "Fixed"
   - Review fix details
   - Prepare verification

2. **Verify Fix**
   - Reproduce original steps
   - Verify fix works
   - Test related functionality
   - Check for regressions

3. **Update Status**
   - Mark as "Verified" if fixed
   - Reopen if not fixed
   - Update comments

### Verification Checklist
- [ ] Original issue is fixed
- [ ] No regressions introduced
- [ ] Related functionality works
- [ ] Test case passes
- [ ] Documentation updated (if needed)

## Defect Metrics

### Key Metrics
- **Defect Detection Rate**: Defects found per time period
- **Defect Resolution Time**: Time to fix defects
- **Defect Reopen Rate**: % of defects reopened
- **Defect Density**: Defects per test/feature
- **Defect Leakage**: Defects found in production

### Targets
- **Resolution Time**: Meet SLA targets
- **Reopen Rate**: < 5%
- **Defect Leakage**: Minimize production defects

## Best Practices

1. **Log Immediately**: Don't delay defect logging
2. **Be Detailed**: Provide complete information
3. **Include Evidence**: Screenshots, logs, etc.
4. **Follow Up**: Track defect status
5. **Verify Thoroughly**: Complete verification
6. **Document Learnings**: Update knowledge base
7. **Communicate**: Keep stakeholders informed

## Tools

### Defect Tracking
- **Jira**: Primary defect tracking tool
- **Integration**: With test management, CI/CD

### Reporting
- Defect dashboards
- Metrics reports
- Status updates

## Related Documents

- `06_TEMPLATES/JIRA_TICKET_TEMPLATE.md` - Defect template
- `04_EXECUTION/TRIAGE_RULES.md` - Triage rules
- `04_EXECUTION/RCA_PROCESS.md` - Root cause analysis

## Notes

[Any additional defect lifecycle information]
