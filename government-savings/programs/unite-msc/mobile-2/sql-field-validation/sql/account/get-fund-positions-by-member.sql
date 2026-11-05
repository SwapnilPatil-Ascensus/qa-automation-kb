-- ============================================================================
-- Query: get-fund-positions-by-member
-- Feature: mobiledashboard, mobilePerformance, investment
-- BFF Endpoint: GET /mobile2api/v1/mobiledashboard
-- Downstream API: GET accountapi/v1/accounts?includeFundPositions=true
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-account\
-- Source file: src/main/java/com/cs529/account/service/FundPositionService.java
-- Source method: getPositionsByMemberId
-- DB tables: tu_acct, tu_fund_balance (+ metadata tu_funds, tu_fund_price via join)
-- Parameters: :memberId
-- Returns: per-account fund units; join prices in metadata query or composite SQL
-- Notes: ORM fundBalanceViewDao; units > 0 only in service layer
-- ============================================================================

SELECT
    a.uii_acct_id       AS prefix,
    a.uii_acct_ext      AS ext,
    a.seq_acct_id       AS seq_acct_id,
    fb.fund_id          AS fund_id,
    fb.total_units      AS fund_units
FROM tu_acct a
JOIN tu_fund_balance fb ON fb.seq_acct_id = a.seq_acct_id
WHERE a.uii_member_id = :memberId
  AND a.ctl_rec_stat = 'A'
  AND fb.ctl_rec_stat = 'A'
  AND fb.total_units > 0
ORDER BY a.uii_acct_id, a.uii_acct_ext, fb.fund_id;
