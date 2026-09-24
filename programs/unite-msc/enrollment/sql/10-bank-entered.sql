-- Step 10: POST /enrollments/enrollment/bank-entered
-- Downstream:
--   unite-bank → CloudBankInstructionService (routing + duplicate bank check)
--   unite-metadata → plan min contribution (TU_TRAUNCH)
-- Tables: TU_BNK_INFO, TU_BANK, TU_TRAUNCH, TU_CODES

-- ---------------------------------------------------------------------------
-- 1) Valid routing number (same as step 09)
-- ---------------------------------------------------------------------------
SELECT b.routing_num,
       b.bnk_name
FROM tu_bnk_info b
WHERE b.ctl_rec_stat = 'A'
  AND b.routing_num = '071000013';

-- ---------------------------------------------------------------------------
-- 2) Plan minimum contribution amounts (for one-time / ePay validation)
-- Source: unite-metadata → PlanService.getPlan() → TU_TRAUNCH columns
-- ---------------------------------------------------------------------------
SELECT t.branding,
       t.min_init_contrib,
       t.min_rec_contrib,
       t.min_epay_contrib,
       t.min_payroll_contrib
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND UPPER(t.branding) = UPPER('hawaii');

-- ---------------------------------------------------------------------------
-- 3) Duplicate bank check (subsequent enrollment — skip for first enrollment)
-- Source: BankTableDao ORM on TU_BANK
-- ---------------------------------------------------------------------------
SELECT b.seq_bnk_id,
       b.routing_num,
       b.acct_num,
       b.acct_type,
       b.uii_member_id
FROM tu_bank b
WHERE b.ctl_rec_stat = 'A'
  AND b.routing_num = '071000013'
  AND b.acct_num = '654321'
  AND b.acct_type = 'S'
  AND b.uii_member_id = :uii_member_id;   -- only for subsequent enrollment

-- ---------------------------------------------------------------------------
-- 4) Bank verification status code (used at review-confirm)
-- Source: unite-metadata → getCodesByTypeAndId('BANK_VERF_STATUS', 'PENDING')
-- ---------------------------------------------------------------------------
SELECT c.code_id,
       c.description,
       c.type
FROM tu_codes c
WHERE c.ctl_rec_stat = 'A'
  AND c.type = 'BANK_VERF_STATUS'
  AND c.code_id = 'PENDING';
