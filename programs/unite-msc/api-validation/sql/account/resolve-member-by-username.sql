-- ============================================================================
-- Query: resolve-member-by-username
-- Feature: mobiledashboard (session bootstrap)
-- BFF Endpoint: GET /mobile2api/v1/mobilemembers/{planId}/{username}
-- Downstream API: GET accountapi/v1/members/{planId}/{username}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-account\
-- Source file: src/main/resources/com/cs529/account/repository/AccountTableDao.xml
-- Source method: getAccountsByUsername (join path) + MemberDao
-- DB tables: tu_member, ta_login, ta_app_context, tu_acct
-- Parameters: :username, :traunchId (plan deprecated id / traunch_id)
-- Returns: uii_member_id for use as :memberId
-- Notes: planId in API is branding; member lookup uses traunch on account rows
-- ============================================================================

SELECT DISTINCT
    m.uii_member_id AS member_id,
    m.email         AS email
FROM tu_acct a
JOIN tu_member m ON m.uii_member_id = a.uii_member_id
JOIN ta_app_context ac ON ac.app_member_id = a.uii_member_id AND ac.application_id = 'uii'
JOIN ta_login al ON al.login_id = ac.login_id
WHERE al.username = :username
  AND a.traunch_id = :traunchId
  AND a.ctl_rec_stat = 'A'
  AND m.ctl_rec_stat = 'A';
