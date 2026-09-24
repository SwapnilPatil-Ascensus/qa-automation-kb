-- Step 13: POST /enrollments/enrollment/review-confirm-entered
-- Downstream:
--   Re-validates all sections (prospect, owner, bene, bank, allocations)
--   unite-account → AccountService.getNewAccount() → account number generation
--   unite-account → CreateAccountService → INSERT TU_ACCT, TU_MEMBER, TA_LOGIN, etc.
--   unite-metadata → plan lookup, BANK_VERF_STATUS code
-- Tables: TU_TRAUNCH, TU_CODES, TU_ACCT (read for subsequent only)

-- ---------------------------------------------------------------------------
-- 1) Plan properties needed for account creation payload
-- ---------------------------------------------------------------------------
SELECT t.traunch_id   AS plan_deprecated_id,   -- account.planId in payload
       t.branding     AS plan_id,
       t.prefix       AS account_number_prefix, -- account.prefix (generated at runtime)
       t.voucher_prefix,
       t.shell_sequence
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND UPPER(t.branding) = UPPER('hawaii');

-- NOTE: account.prefix in payload is a placeholder; service generates real number via
-- Mod10Util529.generateMod10Number(plan.prefix, shell_sequence next val).
-- Postman env default: enrollment.account.prefix = '180004006', ext = '01'

-- ---------------------------------------------------------------------------
-- 2) Bank verification pending status code (set on new bank at create)
-- Source: EnrollmentService.onReviewConfirmEnter → metadata getCodesByTypeAndId
-- ---------------------------------------------------------------------------
SELECT c.code_id,
       c.description
FROM tu_codes c
WHERE c.ctl_rec_stat = 'A'
  AND c.type = 'BANK_VERF_STATUS'
  AND c.code_id = 'PENDING';

-- ---------------------------------------------------------------------------
-- 3) reviewConfirm.tcAccepted = true required (account state 91 vs 90)
-- No SQL — boolean in payload

-- ---------------------------------------------------------------------------
-- 4) All prior step test data must be present in aggregate payload:
--    prospect, owner (with address), beneficiary, member, account, bank, allocations
--    See postman/payloads/plain/13-review-confirm-entered.json
