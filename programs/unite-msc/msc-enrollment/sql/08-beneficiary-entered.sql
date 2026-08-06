-- Step 08: POST /enrollments/enrollment/beneficiary-entered
-- Downstream:
--   unite-profile → CloudBeneficiaryService.verifyBeneficiaryInfo()
--   unite-account → RootAccountService.postVerifyRootBeneficiaryAccounts()
-- Tables: TU_FRAUD_BLOCK_INFO, TU_BENE (duplicate check mostly commented out in service)

-- ---------------------------------------------------------------------------
-- 1) Beneficiary SSN not fraud-blocked (must return 0 rows)
-- Source: FraudBlockInfoTableDao.findBySsn
-- ---------------------------------------------------------------------------
SELECT f.seq_fraud_block_info_id,
       f.ssn_h,
       f.permanent_flag
FROM tu_fraud_block_info f
WHERE f.ctl_rec_stat IN ('A', 'R')
  AND (f.permanent_flag = 'Y'
       OR (f.temp_block_flag = 'Y' AND f.temp_block_endtime > SYSDATE))
  AND f.ssn_h = :beneficiary_ssn_hash;

-- ---------------------------------------------------------------------------
-- 2) Beneficiary SSN must differ from owner SSN — enforced in test data builder
-- Use unique SSNs: owner 9{MMDD}{RR}0, bene 8{MMDD}{RR}1
-- ---------------------------------------------------------------------------

-- ---------------------------------------------------------------------------
-- 3) Valid beneficiary fields (no SQL — domain rules)
--   isCtznOrResalien = 'Y'
--   countryCode = '0' (US)
--   dob: must be future college beneficiary (typically < 18 years old for 529)
--   Address: same zip/state validation as owner — see 07-owner-address-entered.sql
