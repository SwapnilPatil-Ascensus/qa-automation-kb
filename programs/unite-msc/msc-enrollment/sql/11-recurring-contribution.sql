-- Step 11: POST /enrollments/enrollment/recurring-contribution-entered (OPTIONAL)
-- Downstream: unite-bank → bank instruction verify (recurring)
-- Tables: TU_TRAUNCH (min amounts), TU_BNK_INFO (routing)

-- This step can be skipped with "skipped": true in payload.

-- ---------------------------------------------------------------------------
-- 1) Minimum recurring contribution for plan
-- ---------------------------------------------------------------------------
SELECT t.branding,
       t.min_rec_contrib,
       t.min_init_contrib
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND UPPER(t.branding) = UPPER('hawaii');

-- ---------------------------------------------------------------------------
-- 2) Valid routing (reuse step 09/10)
-- ---------------------------------------------------------------------------
SELECT b.routing_num, b.bnk_name
FROM tu_bnk_info b
WHERE b.ctl_rec_stat = 'A'
  AND b.routing_num = '071000013';

-- Domain rules (no SQL):
--   beginDate >= 3 business days from today
--   frequency: valid code (e.g. monthly)
--   amount >= min_rec_contrib from query above
