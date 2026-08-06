-- Step 03: GET /enrollmentapi/v1/plans
-- Downstream: unite-metadata → PlanService.getPlans()
-- Tables: TU_TRAUNCH (ORM findByCriteria, mobile_enabled = 1 filter in API layer)

-- List plans available for mobile enrollment
SELECT t.branding            AS plan_id,
       t.traunch_id          AS deprecated_id,
       t.name                AS plan_name,
       t.description         AS plan_description,
       t.mobile_enabled,
       t.allow_enrollments,
       t.state               AS plan_state,
       t.product_url,
       t.csr_phone
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND t.mobile_enabled = 1
  AND t.allow_enrollments = 'Y'
ORDER BY t.branding;

-- Verify a specific plan is enrollable (pre-run check)
SELECT t.branding,
       t.traunch_id,
       t.allow_enrollments,
       t.mobile_enabled
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND UPPER(t.branding) = UPPER('hawaii');
