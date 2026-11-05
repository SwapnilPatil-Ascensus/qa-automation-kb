-- GET /enrollmentapi/v1/country
-- Downstream: unite-metadata → CountryService → CountryTableDao.findAll
-- Table: TU_COUNTRY
-- Source: CountryTableDao.xml

SELECT c.country_code,
       c.name,
       c.iso_country_code
FROM tu_country c
ORDER BY c.name;

-- For US enrollment test data:
--   beneficiary.isCtznOrResalien = 'Y'
--   beneficiary.countryCode = '0'  (US — not from this table directly)
