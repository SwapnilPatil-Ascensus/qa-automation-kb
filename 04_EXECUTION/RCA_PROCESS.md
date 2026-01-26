# Root Cause Analysis (RCA) Process

## Purpose

This document describes the process for conducting root cause analysis (RCA) for test failures and defects.

## Overview

RCA is a systematic process to identify the underlying cause of problems, not just symptoms, to prevent recurrence.

## When to Perform RCA

### Mandatory RCA
- Critical/high-priority defects
- Production incidents
- Recurring failures
- Flaky tests (see `04_EXECUTION/FLAKINESS_PLAYBOOK.md`)
- Test framework issues

### Optional RCA
- Medium-priority defects (if pattern emerges)
- Low-priority defects (if frequent)
- Performance issues
- Environment issues

## RCA Process

### Step 1: Problem Identification

#### Document the Problem
- **What**: Clear description of the problem
- **When**: When it occurred
- **Where**: Environment, component, area
- **Impact**: Severity and impact
- **Frequency**: How often it occurs

#### Gather Initial Information
- Test execution logs
- Screenshots/videos
- Error messages
- Stack traces
- Test data used
- Environment details

### Step 2: Data Collection

#### Collect Evidence
- **Logs**: Application logs, test logs, system logs
- **Screenshots**: Failure screenshots, UI state
- **Test Data**: Data used in test
- **Configuration**: Environment config, test config
- **History**: Previous occurrences, similar issues

#### Tools and Resources
- Log aggregation tools
- Monitoring dashboards
- Test execution reports
- Defect tracking system
- Team knowledge

### Step 3: Analysis

#### Ask "Why" Five Times
1. Why did the test fail? → [Answer]
2. Why did [Answer] happen? → [Answer]
3. Why did [Answer] happen? → [Answer]
4. Why did [Answer] happen? → [Answer]
5. Why did [Answer] happen? → [Root Cause]

#### Analysis Techniques

**Timeline Analysis**
- Create timeline of events
- Identify sequence of failures
- Look for patterns

**Pattern Analysis**
- Compare with similar failures
- Identify common factors
- Look for trends

**Component Analysis**
- Identify affected components
- Check dependencies
- Verify integration points

**Data Analysis**
- Analyze test data
- Check data state
- Verify data flow

### Step 4: Root Cause Identification

#### Root Cause Categories

**Application Defect**
- Bug in application code
- Logic error
- Data handling issue
- Integration issue

**Test Issue**
- Test script error
- Incorrect assertion
- Test data issue
- Timing issue

**Environment Issue**
- Environment configuration
- Service unavailability
- Data state issue
- Network issue

**Framework Issue**
- Framework bug
- Configuration issue
- Tool version issue
- Dependency issue

**External Dependency**
- Third-party service issue
- External API issue
- Database issue
- Infrastructure issue

### Step 5: Solution Development

#### Immediate Actions
- Fix the issue (if application defect)
- Fix the test (if test issue)
- Resolve environment issue
- Workaround (if needed)

#### Preventive Actions
- Update test to prevent recurrence
- Add monitoring/alerting
- Improve test data management
- Enhance error handling
- Update documentation

#### Long-term Improvements
- Process improvements
- Tool improvements
- Training needs
- Best practices updates

### Step 6: Documentation

#### RCA Report
Use `06_TEMPLATES/RCA_TEMPLATE.md` to document:
- Problem description
- Timeline
- Analysis findings
- Root cause
- Solutions
- Action items
- Lessons learned

#### Update Knowledge Base
- Document in appropriate folder
- Update playbooks if needed
- Share with team
- Archive for reference

## RCA Template Usage

See `06_TEMPLATES/RCA_TEMPLATE.md` for detailed template.

### Key Sections
1. **Problem Summary**: What happened
2. **Timeline**: When it happened
3. **Impact**: Who/what was affected
4. **Investigation**: What was investigated
5. **Root Cause**: Why it happened
6. **Solution**: How to fix
7. **Prevention**: How to prevent
8. **Action Items**: What needs to be done

## Best Practices

1. **Be Systematic**: Follow the process
2. **Be Thorough**: Don't stop at symptoms
3. **Be Objective**: Focus on facts, not blame
4. **Document Everything**: Record findings
5. **Involve Right People**: Get necessary expertise
6. **Think Prevention**: Focus on preventing recurrence
7. **Share Learnings**: Help team learn from issues

## Common Root Causes

### Test Failures
- Timing issues (waits)
- Test data problems
- Environment instability
- Flaky application behavior
- Test script errors

### Application Defects
- Logic errors
- Data handling issues
- Integration problems
- Configuration errors
- Performance issues

### Framework Issues
- Version incompatibilities
- Configuration problems
- Resource limitations
- Tool bugs
- Dependency issues

## Tools and Resources

### Analysis Tools
- Log analysis tools
- Monitoring dashboards
- Debugging tools
- Test execution reports

### Documentation
- RCA template
- Previous RCA reports
- Knowledge base
- Team documentation

## Related Documents

- `06_TEMPLATES/RCA_TEMPLATE.md` - RCA template
- `04_EXECUTION/FLAKINESS_PLAYBOOK.md` - Flakiness investigation
- `09_DECISIONS_WORKLOG/DECISIONS.md` - Document decisions

## Notes

[Any additional RCA process information]
