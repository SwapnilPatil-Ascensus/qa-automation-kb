# Plain Payload Templates

Encrypt these files with `EncryptHelper` CLI before pasting into Postman POST bodies.

## Usage

```powershell
# 1. Replace {{variables}} with values from Postman environment (or edit directly)
# 2. Encrypt
java -jar jsonapi-encryption.jar -m encrypt -e stage -s enrollment -f 05-prospects.json
# 3. Paste output into Postman request body
```

Reuse the same AES key for all steps in one run:

```powershell
$key = Get-Content aeskey.txt
java -jar jsonapi-encryption.jar -m encrypt -e stage -s enrollment -f 06-owner-entered.json -a $key
```

## Files

| File | Postman step | Auth |
|------|-------------|------|
| `05-prospects.json` | 05 Create Prospect | None |
| `06-owner-entered.json` | 06 owner-entered | Bearer JWT |
| `07-owner-address-entered.json` | 07 owner-address-entered | Bearer JWT |
| `08-beneficiary-entered.json` | 08 beneficiary-entered | Bearer JWT |
| `09-verify-routing.json` | 09 verify routing (optional) | None |
| `10-bank-entered.json` | 10 bank-entered | Bearer JWT |
| `12-allocations-entered.json` | 12 allocations-entered | Bearer JWT |
| `12-allocations-entered.md` | 12 — **fundId SQL lookup notes** | — |
| `13-review-confirm-entered.json` | 13 review-confirm-entered | Bearer JWT |

**Shortcut:** For smoke test, only encrypt `05-prospects.json` and `13-review-confirm-entered.json`.
