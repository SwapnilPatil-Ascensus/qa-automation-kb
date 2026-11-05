-- ============================================================================
-- Query: total-balance-calculation
-- Feature: mobiledashboard
-- BFF Endpoint: GET /mobile2api/v1/mobiledashboard
-- Downstream API: composite (account positions + metadata prices)
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-mobile2\
-- Source file: src/main/java/com/cs529/mobile2/service/MobileDashboardService.java
-- Source method: loadPositions + getMobileDashboard (totalBalance sum)
-- DB tables: tu_acct, tu_fund_balance, tu_fund_price, tu_funds, tu_traunch_fund, tu_traunch
-- Parameters: :memberId, :planId (branding), :asofDate
-- Returns: per-account acct_balance, total_balance
-- Notes: Matches loadPositions HALF_UP scale 2; excludes PATAP on-prem override
-- ============================================================================

WITH positions AS (
    SELECT
        a.seq_acct_id,
        a.uii_acct_id,
        a.uii_acct_ext,
        a.acct_state,
        a.enroll_status,
        a.reg_type,
        fb.fund_id,
        fb.total_units AS fund_units
    FROM tu_acct a
    JOIN tu_fund_balance fb ON fb.seq_acct_id = a.seq_acct_id
    WHERE a.uii_member_id = :memberId
      AND a.ctl_rec_stat = 'A'
      AND fb.ctl_rec_stat = 'A'
      AND fb.total_units > 0
),
priced AS (
    SELECT
        p.seq_acct_id,
        p.uii_acct_id,
        p.uii_acct_ext,
        p.acct_state,
        p.enroll_status,
        p.reg_type,
        ROUND(p.fund_units * fp.price, 2) AS fund_value
    FROM positions p
    JOIN tu_funds f ON f.fund_id = p.fund_id
    JOIN tu_fund_price fp ON fp.fund_id = f.fund_id
    JOIN tu_traunch_fund tf ON tf.fund_id = f.fund_id
    JOIN tu_traunch tr ON tr.traunch_id = tf.traunch_id
    WHERE tr.branding = :planId
      AND fp.price_date = :asofDate
      AND fp.ctl_rec_stat = 'A'
      AND f.ctl_rec_stat = 'A'
),
account_balances AS (
    SELECT
        seq_acct_id,
        uii_acct_id AS prefix,
        uii_acct_ext AS ext,
        acct_state,
        enroll_status,
        reg_type,
        SUM(fund_value) AS acct_balance
    FROM priced
    GROUP BY seq_acct_id, uii_acct_id, uii_acct_ext, acct_state, enroll_status, reg_type
)
SELECT
    prefix,
    ext,
    acct_balance,
    SUM(acct_balance) OVER () AS total_balance
FROM account_balances
WHERE acct_state IS NOT NULL
  AND (enroll_status IS NULL OR enroll_status <> 'R')
ORDER BY prefix, ext;

-- Expected @md1: single row ext=01, acct_balance=22460.00 (2000 * 11.23)
