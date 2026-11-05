-- Step 04: GET /enrollmentapi/v1/plans/{planId}
-- Downstream: unite-metadata → PlanService.getPlan()
-- Tables: TU_TRAUNCH, TU_TRAUNCH_FUND, TU_FUNDS
-- Captures: enrollment.fundId (first active fund for allocations)

-- Plan detail
SELECT t.traunch_id,
       t.branding,
       t.name,
       t.prefix,
       t.voucher_prefix,
       t.min_init_contrib,
       t.min_rec_contrib,
       t.shell_sequence
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND t.mobile_enabled = 1
  AND UPPER(t.branding) = UPPER('hawaii');

-- Active funds for plan (mirrors GET /plans/{id} fund list)
-- Source: FundTableDao.getStaticFundsByPlan (fund_type = 'S')
SELECT f.fund_id,
       f.fund_name,
       f.fund_type,
       f.web_status,
       f.back_status,
       f.display_order,
       t.branding AS plan_id
FROM tu_traunch t
INNER JOIN tu_traunch_fund tf ON tf.traunch_id = t.traunch_id
INNER JOIN tu_funds f ON f.fund_id = tf.fund_id
WHERE t.ctl_rec_stat = 'A'
  AND tf.ctl_rec_stat = 'A'
  AND tf.state = 'Y'
  AND f.ctl_rec_stat = 'A'
  AND f.web_status = 'A'
  AND f.back_status = 'A'
  AND UPPER(t.branding) = UPPER('hawaii')
ORDER BY f.display_order;

-- RECOMMENDED: pick first fund for enrollment.fundId
SELECT f.fund_id
FROM tu_traunch t
INNER JOIN tu_traunch_fund tf ON tf.traunch_id = t.traunch_id
INNER JOIN tu_funds f ON f.fund_id = tf.fund_id
WHERE t.ctl_rec_stat = 'A'
  AND tf.ctl_rec_stat = 'A'
  AND tf.state = 'Y'
  AND f.ctl_rec_stat = 'A'
  AND f.web_status = 'A'
  AND f.back_status = 'A'
  AND UPPER(t.branding) = UPPER('hawaii')
ORDER BY f.display_order
FETCH FIRST 1 ROW ONLY;
