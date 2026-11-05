# Metrics Catalog

## Purpose

This document catalogs all metrics tracked for QA automation, including definitions, targets, and tracking methods.

## Test Execution Metrics

### Pass Rate
- **Definition**: Percentage of tests that pass
- **Formula**: (Passed Tests / Total Tests) × 100
- **Target**: >95%
- **Frequency**: Daily, Weekly, Monthly
- **Tracking**: Test execution reports

### Failure Rate
- **Definition**: Percentage of tests that fail
- **Formula**: (Failed Tests / Total Tests) × 100
- **Target**: <5%
- **Frequency**: Daily, Weekly, Monthly
- **Tracking**: Test execution reports

### Flakiness Rate
- **Definition**: Percentage of tests that are flaky (inconsistent results)
- **Formula**: (Flaky Tests / Total Tests) × 100
- **Target**: <5%
- **Frequency**: Weekly, Monthly
- **Tracking**: Test execution history analysis

### Execution Time
- **Definition**: Time taken to execute test suite
- **Target**: [Target time, e.g., <3 hours for daily regression]
- **Frequency**: Per execution
- **Tracking**: CI/CD logs, execution reports

### Test Coverage
- **Definition**: Percentage of functionality covered by tests
- **Formula**: (Tested Features / Total Features) × 100
- **Target**: [Target percentage, e.g., >80%]
- **Frequency**: Monthly
- **Tracking**: Coverage reports, test matrix

## Defect Metrics

### Defect Detection Rate
- **Definition**: Number of defects found per time period
- **Target**: [Target based on release size]
- **Frequency**: Weekly, Per Release
- **Tracking**: Jira, defect reports

### Defect Resolution Time
- **Definition**: Average time to resolve defects
- **Target**: Meet SLA (Critical: 4 hours, High: 1 day, etc.)
- **Frequency**: Weekly, Monthly
- **Tracking**: Jira, defect reports

### Defect Reopen Rate
- **Definition**: Percentage of defects that are reopened
- **Formula**: (Reopened Defects / Total Defects) × 100
- **Target**: <5%
- **Frequency**: Monthly
- **Tracking**: Jira

### Defect Leakage
- **Definition**: Defects found in production that should have been caught in testing
- **Target**: Minimize (target: 0 critical/high)
- **Frequency**: Per Release
- **Tracking**: Production defect tracking

### Defect Density
- **Definition**: Defects per test case or per feature
- **Formula**: Total Defects / Number of Test Cases
- **Target**: [Target based on historical data]
- **Frequency**: Per Release
- **Tracking**: Defect and test case data

## Quality Metrics

### Test Stability
- **Definition**: Consistency of test results over time
- **Target**: High stability (low flakiness)
- **Frequency**: Weekly, Monthly
- **Tracking**: Test execution history

### Test Maintenance Effort
- **Definition**: Time spent maintaining tests vs. developing new tests
- **Target**: [Target ratio, e.g., <30% maintenance]
- **Frequency**: Monthly
- **Tracking**: Time tracking, effort logs

### Automation Coverage
- **Definition**: Percentage of tests that are automated
- **Formula**: (Automated Tests / Total Tests) × 100
- **Target**: [Target, e.g., >80%]
- **Frequency**: Monthly
- **Tracking**: Test inventory

## Efficiency Metrics

### Test Execution Efficiency
- **Definition**: Tests executed per unit of time
- **Target**: [Target based on infrastructure]
- **Frequency**: Weekly
- **Tracking**: Execution logs

### Time to Feedback
- **Definition**: Time from code commit to test results
- **Target**: [Target, e.g., <30 minutes]
- **Frequency**: Per execution
- **Tracking**: CI/CD pipeline metrics

### Test Development Velocity
- **Definition**: Tests developed per sprint/time period
- **Target**: [Target based on team capacity]
- **Frequency**: Per Sprint
- **Tracking**: Sprint tracking, test inventory

## Process Metrics

### Triage Time
- **Definition**: Time to triage defects
- **Target**: <4 hours for critical, <1 day for others
- **Frequency**: Weekly
- **Tracking**: Jira, defect logs

### RCA Completion Rate
- **Definition**: Percentage of required RCAs completed
- **Target**: 100% for mandatory RCAs
- **Frequency**: Monthly
- **Tracking**: RCA tracking

### Documentation Currency
- **Definition**: Percentage of documentation that is up to date
- **Target**: >90%
- **Frequency**: Quarterly
- **Tracking**: Documentation review

## Team Metrics

### Team Velocity
- **Definition**: Story points or tasks completed per sprint
- **Target**: [Target based on team capacity]
- **Frequency**: Per Sprint
- **Tracking**: Sprint tracking

### Team Availability
- **Definition**: Percentage of planned time team is available
- **Target**: >90%
- **Frequency**: Monthly
- **Tracking**: Time tracking, attendance

## Reporting

### Metric Reports
- **Daily**: Test execution metrics
- **Weekly**: Defect metrics, execution summary
- **Monthly**: Comprehensive metrics report
- **Per Release**: Release-specific metrics

### Dashboards
- **Test Execution Dashboard**: Real-time test status
- **Quality Dashboard**: Quality metrics trends
- **Defect Dashboard**: Defect metrics and trends

## Metric Targets Summary

| Metric | Target | Frequency |
|--------|--------|-----------|
| Pass Rate | >95% | Daily/Weekly |
| Flakiness Rate | <5% | Weekly |
| Defect Reopen Rate | <5% | Monthly |
| Test Coverage | >80% | Monthly |
| Automation Coverage | >80% | Monthly |

## Related Documents

- `07_GOVERNANCE_VISIBILITY/DASHBOARD_REQUIREMENTS.md` - Dashboard specifications
- `07_GOVERNANCE_VISIBILITY/STATUS_RULES.md` - Status reporting rules

## Notes

[Any additional metrics or tracking information]
