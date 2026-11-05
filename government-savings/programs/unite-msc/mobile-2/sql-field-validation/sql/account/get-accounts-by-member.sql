-- ============================================================================
-- Query: get-accounts-by-member
-- Feature: mobiledashboard (all mobile2 features using account list)
-- BFF Endpoint: GET /mobile2api/v1/mobiledashboard
-- Downstream API: GET accountapi/v1/accounts?includeFundPositions=true
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-account\
-- Source file: src/main/java/com/cs529/account/repository/AccountDao.java
-- Source method: getAccountsByMemberId
-- DB tables: tu_acct
-- Parameters: :memberId (uii_member_id)
-- Returns: account columns mapped to MobileAccount / Account domain
-- Notes: ORM-generated via findByCriteria on AccountTable; ctl_rec_stat = 'A'
-- ============================================================================

SELECT
    a.seq_acct_id       AS seq_acct_id,
    a.seq_part_id       AS seq_part_id,
    a.seq_bene_id       AS seq_bene_id,
    a.traunch_id        AS traunch_id,
    a.uii_member_id     AS uii_member_id,
    a.uii_acct_id       AS uii_acct_id,
    a.uii_acct_ext      AS uii_acct_ext,
    a.reg_type          AS reg_type,
    a.acct_state        AS acct_state,
    a.enroll_status     AS enroll_status,
    a.ugift_id          AS ugift_id,
    a.ugift_status      AS ugift_status
FROM tu_acct a
WHERE a.uii_member_id = :memberId
  AND a.ctl_rec_stat = 'A'
ORDER BY a.uii_acct_id, a.uii_acct_ext;
