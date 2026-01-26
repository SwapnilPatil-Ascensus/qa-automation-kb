# Triage Rules

## Purpose

This document defines rules and guidelines for defect triage to ensure consistent prioritization and assignment.

## Triage Principles

1. **Consistency**: Apply rules consistently
2. **Objectivity**: Base decisions on facts
3. **Impact-Focused**: Prioritize by impact
4. **Timely**: Triage promptly
5. **Documented**: Document decisions

## Priority Assignment Rules

### Critical (P1) - Immediate Attention

**Criteria**:
- Production system down
- Data loss or corruption
- Security breach
- Critical functionality completely broken
- Blocks all testing

**Assignment**: Assign immediately
**SLA**: Fix within [time, e.g., 4 hours]
**Escalation**: Notify management immediately

### High (P2) - Urgent

**Criteria**:
- Major functionality broken
- Significant user impact
- No workaround available
- Blocks release
- Affects critical path

**Assignment**: Assign within [time, e.g., 2 hours]
**SLA**: Fix within [time, e.g., 1 business day]
**Escalation**: Notify team lead

### Medium (P3) - Important

**Criteria**:
- Moderate functionality impact
- Workaround available
- Affects non-critical features
- Some user impact
- Can be deferred if needed

**Assignment**: Assign within [time, e.g., 1 business day]
**SLA**: Fix within [time, e.g., 1 week]
**Escalation**: Normal process

### Low (P4) - Nice to Have

**Criteria**:
- Minor functionality impact
- Cosmetic issues
- Low user impact
- Easy workaround
- Can wait for next release

**Assignment**: Assign within [time, e.g., 1 week]
**SLA**: Fix in next release
**Escalation**: Normal process

## Severity Assignment Rules

### Blocker (S1)

**Criteria**:
- Cannot test/use application
- Blocks all related functionality
- No workaround possible

**Examples**:
- Application crash on startup
- Login completely broken
- Database connection failure

### Critical (S2)

**Criteria**:
- Major functionality broken
- Significant impact on users
- Limited workaround

**Examples**:
- Core feature not working
- Data corruption
- Payment processing broken

### Major (S3)

**Criteria**:
- Important functionality affected
- Moderate user impact
- Workaround available

**Examples**:
- Feature partially working
- Incorrect calculations
- Missing validation

### Minor (S4)

**Criteria**:
- Minor functionality issue
- Low user impact
- Easy workaround

**Examples**:
- Minor feature issue
- Edge case not handled
- Performance degradation

### Trivial (S5)

**Criteria**:
- Cosmetic issue
- Very minor impact
- No functional impact

**Examples**:
- UI alignment issue
- Text typo
- Color inconsistency

## Assignment Rules

### By Component/Area

**Rules**:
- Assign to component owner
- Assign to team responsible for area
- Consider expertise required
- Balance workload

### By Priority

**Rules**:
- Critical/High: Assign immediately
- Medium: Assign within 1 day
- Low: Assign within 1 week

### By Expertise

**Rules**:
- Assign to specialist if needed
- Consider team member expertise
- May require multiple people

## Duplicate Detection

### Duplicate Criteria

**Consider Duplicate If**:
- Same issue already logged
- Same root cause
- Same symptoms
- Same area/component

### Duplicate Handling

1. **Identify Original**: Find original defect
2. **Link Defects**: Link duplicate to original
3. **Close Duplicate**: Mark as duplicate, close
4. **Update Original**: Add information from duplicate if useful
5. **Notify Reporter**: Inform about duplicate

## Rejection Rules

### Valid Rejection Reasons

**By Design**:
- Behavior is intentional
- Matches requirements
- Documented behavior

**Not Reproducible**:
- Cannot reproduce issue
- Insufficient information
- Environment-specific (not reproducible elsewhere)

**Invalid**:
- Not a defect
- User error
- Test error
- Out of scope

### Rejection Process

1. **Review Carefully**: Ensure valid rejection
2. **Document Reason**: Clear explanation
3. **Notify Reporter**: Explain rejection
4. **Close Defect**: Mark as rejected, close

## Deferral Rules

### Deferral Criteria

**Defer If**:
- Low priority
- Can wait for next release
- Resource constraints
- Not critical for current release
- Requires significant effort

### Deferral Process

1. **Assess Impact**: Evaluate deferral impact
2. **Document Reason**: Why deferred
3. **Set Target Release**: When to address
4. **Update Priority**: May adjust priority
5. **Notify Stakeholders**: Inform about deferral

## Triage Meeting

### Frequency
- **Daily**: For critical/high priority defects
- **Weekly**: For all defects
- **Ad-hoc**: As needed

### Participants
- QA Lead
- Development Lead
- Product Owner (if needed)
- Team Members (as needed)

### Agenda
1. Review new defects
2. Assign priority/severity
3. Assign to team members
4. Review overdue defects
5. Discuss blockers
6. Update status

## Escalation Rules

### When to Escalate

**Escalate If**:
- Critical defect not addressed
- SLA not met
- Resource constraints
- Disagreement on priority
- Blocking release

### Escalation Process

1. **Document Issue**: Clear description
2. **Notify Lead**: Inform team lead
3. **Escalate to Management**: If needed
4. **Track Resolution**: Follow up
5. **Document Outcome**: Record resolution

## Metrics and Tracking

### Triage Metrics
- **Triage Time**: Time to triage defects
- **Assignment Accuracy**: Correct assignments
- **SLA Compliance**: Meeting SLA targets
- **Reopen Rate**: Defects reopened

### Targets
- **Triage Time**: < 4 hours for critical, < 1 day for others
- **SLA Compliance**: > 95%
- **Reopen Rate**: < 5%

## Best Practices

1. **Triage Promptly**: Don't delay
2. **Be Consistent**: Apply rules consistently
3. **Document Decisions**: Record rationale
4. **Communicate**: Keep stakeholders informed
5. **Review Regularly**: Update rules as needed
6. **Learn from Patterns**: Identify trends
7. **Balance Workload**: Distribute fairly

## Related Documents

- `04_EXECUTION/DEFECT_LIFECYCLE.md` - Defect lifecycle
- `06_TEMPLATES/JIRA_TICKET_TEMPLATE.md` - Defect template

## Notes

[Any additional triage rules or guidelines]
