-- POST /enrollmentapi/v1/enrollmentallocationfunds/get
-- Downstream: unite-metadata → AllocationFundsService.getAllFundsAndTraunchMetaDataInfo()
-- Tables: TU_TRAUNCH, TU_TRAUNCH_FUND, TU_FUNDS, TU_RISK_AGE_FUND,
--         TU_AGE_BASED_CLASSIFICATION, TU_RISK_TOLERANCE, TU_FUND_AUTOSELECT
-- Source: FundTableDao.getFundsByPlanIdAndBeneDob, getStaticFundsByPlan, getFundsFromFundAutoSelect

-- Age-based funds (fund_type = 'A') — bind beneficiary age in years
-- Source: FundTableDao.getFundsByPlanIdAndBeneDob
SELECT f.fund_id,
       f.fund_name,
       f.fund_type,
       f.display_order,
       t.branding AS plan_id
FROM tu_traunch t
INNER JOIN tu_traunch_fund tf ON tf.traunch_id = t.traunch_id
INNER JOIN tu_funds f ON f.fund_id = tf.fund_id
INNER JOIN tu_risk_age_fund tr ON tr.fund_id = f.fund_id
INNER JOIN tu_age_based_classification tc ON tr.age_based_id = tc.id
INNER JOIN tu_risk_tolerance tt ON tr.risk_id = tt.id
WHERE t.ctl_rec_stat = 'A'
  AND tf.ctl_rec_stat = 'A'
  AND tf.state = 'Y'
  AND f.ctl_rec_stat = 'A'
  AND f.web_status = 'A'
  AND f.back_status = 'A'
  AND f.fund_type = 'A'
  AND UPPER(t.branding) = UPPER('hawaii')
  AND :bene_age_years BETWEEN tc.years_to_college_start AND tc.years_to_college_end
ORDER BY f.display_order;

-- Static funds (fund_type = 'S') — simpler path for E2E
SELECT f.fund_id,
       f.fund_name,
       f.fund_type,
       t.branding
FROM tu_traunch t
INNER JOIN tu_traunch_fund tf ON tf.traunch_id = t.traunch_id
INNER JOIN tu_funds f ON f.fund_id = tf.fund_id
WHERE t.ctl_rec_stat = 'A'
  AND tf.ctl_rec_stat = 'A'
  AND tf.state = 'Y'
  AND f.ctl_rec_stat = 'A'
  AND f.web_status = 'A'
  AND f.back_status = 'A'
  AND f.fund_type = 'S'
  AND UPPER(t.branding) = UPPER('hawaii')
ORDER BY f.display_order;

-- Allocation metadata for plan
SELECT m.attribute_key,
       m.attribute_value
FROM tu_traunch_metadata m
INNER JOIN tu_traunch t ON t.traunch_id = m.traunch_id
WHERE m.ctl_rec_stat = 'A'
  AND UPPER(t.branding) = UPPER('hawaii')
  AND m.attribute_key IN ('MAX_NUMBER_OF_FUNDS', 'MIN_ALLOCATION_PERCENTAGE');
