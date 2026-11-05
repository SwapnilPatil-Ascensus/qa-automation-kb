-- Step 12: POST /enrollments/enrollment/allocations-entered
-- Downstream:
--   unite-account → CloudAllocationService → AllocationValidator
--   unite-metadata  → getFundByDeprecatedId, getAllocationMinPercentByPlan
-- Tables: TU_TRAUNCH, TU_TRAUNCH_FUND, TU_FUNDS, TU_TRAUNCH_METADATA
-- Source: FundTableDao.getStaticFundsByPlan, plan.sql → unite_funding_properties

-- Use BEFORE test run to set enrollment.fundId.
-- Not a mid-wizard validation query — see docs/05-validation-strategy.md.

-- ---------------------------------------------------------------------------
-- 1) Resolve TRAUNCH_ID from plan branding
-- ---------------------------------------------------------------------------
SELECT t.traunch_id,
       t.branding
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND UPPER(t.branding) = UPPER('hawaii');

-- ---------------------------------------------------------------------------
-- 2) RECOMMENDED — active fund for branding (set enrollment.fundId)
-- Mirrors: unite_funding_properties + FundTableDao.getStaticFundsByPlan
-- ---------------------------------------------------------------------------
SELECT f.fund_id,
       f.fund_name,
       f.fund_type,
       tf.traunch_id,
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
  AND UPPER(t.branding) = UPPER('hawaii')
ORDER BY f.display_order;

-- Pick first fund (automation default)
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

-- ---------------------------------------------------------------------------
-- 3) Allocation rules for plan (percentAlloc must sum to 100)
-- Source: TraunchMetadata — MAX_NUMBER_OF_FUNDS, MIN_ALLOCATION_PERCENTAGE
-- ---------------------------------------------------------------------------
SELECT m.attribute_key,
       m.attribute_value
FROM tu_traunch_metadata m
INNER JOIN tu_traunch t ON t.traunch_id = m.traunch_id
WHERE m.ctl_rec_stat = 'A'
  AND UPPER(t.branding) = UPPER('hawaii')
  AND m.attribute_key IN ('MAX_NUMBER_OF_FUNDS', 'MIN_ALLOCATION_PERCENTAGE');

-- ---------------------------------------------------------------------------
-- 4) Semicolon-separated fund list (framework token $$random_fund_id$$)
-- From api-test-automation plan.sql → unite_funding_properties
-- ---------------------------------------------------------------------------
SELECT LISTAGG(f.fund_id, ';') WITHIN GROUP (ORDER BY f.fund_id) AS funds
FROM tu_traunch_fund tf
INNER JOIN tu_funds f ON tf.fund_id = f.fund_id
INNER JOIN tu_traunch t ON t.traunch_id = tf.traunch_id
WHERE t.branding = 'hawaii'
  AND tf.ctl_rec_stat = 'A'
  AND f.ctl_rec_stat = 'A'
  AND f.back_status = 'A'
  AND f.web_status = 'A';

-- Payload: enrollmentAllocations = [{ "fundId": "<from query>", "percentAlloc": "100" }]
