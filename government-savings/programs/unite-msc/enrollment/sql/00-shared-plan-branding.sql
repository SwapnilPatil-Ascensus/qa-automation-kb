-- Shared plan / branding lookup (used by steps 03–13)
-- Downstream: unite-metadata → PlanService → TU_TRAUNCH
-- Source: api-test-automation/mobile/enrollment/sql/plan.sql → unite_branding_properties
-- Use BEFORE test run to populate enrollment.planId, planDeprecatedId, account.prefix

-- ---------------------------------------------------------------------------
-- 1) Core plan properties by branding (enrollment.planId)
-- ---------------------------------------------------------------------------
SELECT t.traunch_id          AS plan_deprecated_id,
       t.branding            AS plan_id,
       t.voucher_prefix      AS plan_prefix,
       t.prefix              AS account_number_prefix,
       t.shell_sequence      AS shell_sequence,
       t.state               AS plan_state,
       t.uuid_traunch_id     AS plan_uuid,
       t.product_type        AS plan_type,
       t.backend_type        AS plan_backend,
       t.name                AS plan_name,
       t.min_init_contrib    AS min_init_contrib,
       t.min_rec_contrib     AS min_rec_contrib,
       t.min_epay_contrib    AS min_epay_contrib,
       t.mobile_enabled      AS mobile_enabled,
       t.allow_enrollments   AS allow_enrollments
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND UPPER(t.branding) = UPPER('hawaii');   -- bind :branding

-- ---------------------------------------------------------------------------
-- 2) Plan metadata (allocation rules, UI config)
-- Downstream: unite-metadata → TraunchMetadataTableDao
-- ---------------------------------------------------------------------------
SELECT m.attribute_key,
       m.attribute_value
FROM tu_traunch_metadata m
INNER JOIN tu_traunch t ON t.traunch_id = m.traunch_id
WHERE m.ctl_rec_stat = 'A'
  AND t.ctl_rec_stat = 'A'
  AND UPPER(t.branding) = UPPER('hawaii')
  AND m.attribute_key IN (
      'MAX_NUMBER_OF_FUNDS',
      'MIN_ALLOCATION_PERCENTAGE'
  );

-- ---------------------------------------------------------------------------
-- 3) List mobile-enabled plans (GET /plans filter)
-- ---------------------------------------------------------------------------
SELECT t.branding,
       t.traunch_id,
       t.name,
       t.mobile_enabled,
       t.allow_enrollments
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND t.mobile_enabled = 1
ORDER BY t.branding;
