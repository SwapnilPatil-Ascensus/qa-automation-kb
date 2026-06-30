-- ============================================================================
-- Query: full-dashboard-validation
-- Feature: mobiledashboard
-- BFF Endpoint: GET /mobile2api/v1/mobiledashboard
-- Downstream API: composite account + profile + metadata
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-mobile2\
-- Source file: MobileDashboardService.getMobileDashboard
-- Source method: full assembly (excluding on-prem)
-- DB tables: tu_acct, tu_fund_balance, tu_person, tu_bene, tu_traunch, tu_fund_price
-- Parameters: :memberId, :planId, :asofDate
-- Returns: dashboard-level row set for object compare
-- Notes: Single-schema variant; split by datasource in multi-DB environments
-- ============================================================================

WITH member_accounts AS (
    SELECT *
    FROM (
        SELECT
            a.seq_acct_id,
            a.seq_part_id,
            a.seq_bene_id,
            a.traunch_id,
            a.uii_acct_id,
            a.uii_acct_ext,
            a.reg_type,
            a.acct_state,
            a.enroll_status,
            ROW_NUMBER() OVER (ORDER BY a.uii_acct_id, a.uii_acct_ext) AS rn
        FROM tu_acct a
        WHERE a.uii_member_id = :memberId
          AND a.ctl_rec_stat = 'A'
    ) q
    WHERE acct_state IS NOT NULL
      AND (enroll_status IS NULL OR enroll_status <> 'R')
),
owner AS (
    SELECT p.first_name, p.last_name, p.dob
    FROM tu_person p
    WHERE p.seq_person_id = (SELECT MAX(seq_part_id) FROM member_accounts WHERE seq_part_id <> 0)
      AND p.ctl_rec_stat = 'A'
),
plan AS (
    SELECT t.branding AS plan_id, t.asof_date
    FROM tu_traunch t
    WHERE t.traunch_id = (SELECT MAX(traunch_id) FROM member_accounts)
      AND t.ctl_rec_stat = 'A'
)
SELECT
    o.first_name        AS owner_first_name,
    o.last_name         AS owner_last_name,
    TO_CHAR(pl.asof_date, 'MM/DD/YYYY') AS as_of_date,
    pl.plan_id          AS plan_id,
    ma.uii_acct_id      AS prefix,
    ma.uii_acct_ext     AS ext,
    b.first_name        AS bene_first_name,
    b.last_name         AS bene_last_name,
    ma.reg_type         AS reg_type_raw,
    ma.traunch_id       AS traunch_id,
    ma.acct_state       AS acct_state
FROM member_accounts ma
JOIN tu_bene b ON b.seq_bene_id = ma.seq_bene_id AND b.ctl_rec_stat = 'A'
CROSS JOIN owner o
CROSS JOIN plan pl
ORDER BY ma.uii_acct_id, ma.uii_acct_ext;

-- Join with total-balance-calculation.sql for acct_balance and total_balance columns
