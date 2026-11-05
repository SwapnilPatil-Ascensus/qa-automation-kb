# Constraints

## Purpose

This document outlines constraints, limitations, and boundaries that must be respected in QA automation work.

## Technical Constraints

### Environment Access
- Limited access to production environments (read-only where possible)
- Staging environments may have restricted availability windows
- Test data constraints (no production data, limited test data sets)

### Tool Limitations
- Tool licensing constraints
- Version compatibility requirements
- Integration limitations between tools

### Infrastructure
- CI/CD pipeline capacity and execution time limits
- Resource constraints (memory, CPU, network bandwidth)
- Browser/device availability for testing

## Process Constraints

### Timeline
- Release schedules and deadlines
- Maintenance windows
- Sprint cadence and planning cycles

### Resource Constraints
- Team size and availability
- Onshore/offshore coordination time zones
- Budget limitations for tools and infrastructure

## Security Constraints

### ⚠️ Critical Security Rules

> **🚨 DO NOT store secrets, tokens, credentials, or customer PII in this repository.**
>
> **When uncertain about sensitivity, mark as `[REDACT_NEEDED]` and stop.**

#### What Must Never Be Committed
- [ ] Secrets
- [ ] Tokens
- [ ] Credentials
- [ ] Customer PII (Personally Identifiable Information)

#### Redaction Requirements
The following must be redacted before committing:
- [ ] Email addresses
- [ ] Plan participant data
- [ ] Access URLs that are sensitive
- [ ] Internal-only identifiers (if required)

#### Content Standards
- Keep all content **enterprise-safe** and **audit-friendly**
- When uncertain about sensitivity, mark as `[REDACT_NEEDED]` and stop
- Review all content before committing

### Data Handling
- No production data in test environments
- PII/PHI redaction requirements (see `02_STANDARDS/SECURITY_AND_DATA.md`)
- Credential management policies
- **Never commit sensitive data to version control**

### Access Control
- Role-based access restrictions
- Network security policies
- Compliance requirements (SOX, HIPAA, etc.)

### Security Checklist

Before committing any content:
- [ ] No secrets, tokens, or credentials
- [ ] No customer PII
- [ ] Emails redacted (if applicable)
- [ ] Sensitive URLs redacted
- [ ] Internal identifiers redacted (if required)
- [ ] Content is enterprise-safe
- [ ] Content is audit-friendly

## Quality Constraints

### Test Coverage
- Minimum coverage requirements
- Critical path prioritization
- Maintenance overhead limits

### Flakiness Tolerance
- Maximum acceptable flakiness rate
- Retry strategy limitations
- Timeout constraints

## Documentation Constraints

### Format Requirements
- Markdown format for all documentation
- Template adherence (see `06_TEMPLATES/`)
- Version control requirements

### Content Restrictions
- No sensitive data in documentation
- No hardcoded credentials
- Redaction rules compliance

## Communication Constraints

### Update Frequency
- Daily status updates during releases
- Weekly updates during normal operations
- Ad-hoc updates for critical issues

### Channel Usage
- Appropriate channels for different types of communication
- Escalation paths and procedures
