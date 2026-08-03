# UniteMSC repository map

Mobile2 validation spans one BFF and five SQL-backed microservices. Auth/security services issue tokens only.

## Repository roles

| Repo | Maven artifact | Role | SQL location | JDBC datasource |
|------|----------------|------|--------------|-----------------|
| **unite-mobile2** | mobile2 BFF | REST orchestration, field assembly, on-prem HTTP | None | N/A |
| **unite-account** | account 2.7.0 | Accounts, members, positions, allocations | `src/main/resources/com/cs529/account/repository/*.xml`, `@Table` entities, `persistence/src/accountDatastore.sql` | account |
| **unite-profile** | profile 2.4.0 | Owners, beneficiaries, persons | `src/main/resources/com/cs529/profile/repository/*.xml`, `persistence/src/profileDatastore.sql` | profile |
| **unite-metadata** | metadata 2.7.0 | Plans (traunches), funds, prices, stackup | `src/main/resources/com/cs529/metadata/repository/*.xml`, `persistence/src/metadataDatastore.sql` | metadata |
| **unite-transaction** | transaction 2.3.0 | Transactions, contribution summaries, balance history | `src/main/resources/com/cs529/transaction/repository/*.xml`, `persistence/src/transactionDatastore.sql` | transaction |
| **unite-bank** | bank 2.9.0 | Banks, bank instructions | `src/main/resources/com/cs529/bank/repository/*.xml`, `persistence/src/bankDatastore.sql` | bank |
| unite-auth | auth 2.7.0 | JWT issuance | Skip DB validation | — |
| unite-security | security 1.3.2 | Security policies | Skip DB validation | — |

## Path reference (read-only)

```
C:\Workspace\GitLab\MobileAutomation\UniteMSC\
├── unite-mobile2\
│   ├── src/main/java/com/cs529/mobile2/
│   │   ├── resource/          RESTApplication.java — resource registration
│   │   ├── service/           *Service.java — orchestration
│   │   └── gateway/           *Gateway.java — HTTP to microservices
│   └── src/test/
│       ├── resources/features/  *.feature
│       └── java/mobile2/        *Stepdefs.java
├── unite-account\ ...
├── unite-profile\ ...
├── unite-metadata\ ...
├── unite-transaction\ ...
└── unite-bank\ ...
```

## BFF gateway → microservice mapping

| Gateway class | Base URL property | Downstream prefix | Target repo |
|---------------|-------------------|-------------------|-------------|
| `AccountGateway` | `ACCOUNT_SERVICE_URL` | `/accountapi/v1/` | unite-account |
| `ProfileGateway` | `PROFILE_SERVICE_URL` | `/profileapi/v1/` | unite-profile |
| `MetadataGateway` | `METADATA_SERVICE_URL` | `/metadataapi/v1/` | unite-metadata |
| `TransactionGateway` | `TRANSACTION_SERVICE_URL` | `/transactionapi/v1/` | unite-transaction |
| `BankGateway` | `BANK_SERVICE_URL` | `/bankapi/v1/` | unite-bank |
| `ContentGateway` | CMS URL | external HTML | no local SQL |
| `OnPremAccountGateway` | on-prem URL | agsup-account-web | external |
| `IdpGateway` | IdP URL | auth | no DB validation |

Gateway base URLs are defined in `BaseGatewayUtil.java`:

```java
ProfileEndPoint    = {PROFILE_SERVICE_URL}/profileapi/v1/
AccountEndPoint    = {ACCOUNT_SERVICE_URL}/accountapi/v1/
TransactionEndPoint= {TRANSACTION_SERVICE_URL}/transactionapi/v1/
BankEndPoint       = {BANK_SERVICE_URL}/bankapi/v1/
```

## Cucumber glue packages

Test data setup steps (`I create Accounts`, `I delete Members`, …) live in service test JARs:

| Glue package | Repo path |
|--------------|-----------|
| `mobile2` | `unite-mobile2/src/test/java/mobile2/` |
| `account` | `unite-account/src/test/java/account/` |
| `profile` | `unite-profile/src/test/java/profile/` |
| `metadata` | `unite-metadata/src/test/java/metadata/` |
| `transaction` | `unite-transaction/src/test/java/transaction/` |
| `bank` | `unite-bank/src/test/java/bank/` |

Configured in `CucableJavaTemplate.java`: `glue = {"mobile2", "metadata", "account", "profile", "transaction", "bank"}`.

## Feature → service coverage matrix

| Feature | Primary SQL repos |
|---------|-------------------|
| mobiledashboard | account, profile, metadata, transaction*, on-prem |
| mobilebank | bank, account, metadata, on-prem |
| mobilecontribution | account, profile, metadata, bank |
| mobileactivity | transaction, account, metadata, bank, CMS |
| mobileTransactionHistory | transaction |
| mobilePerformance | account, transaction |
| mobileBalanceTrend | account, transaction |
| mobileStackup | metadata |
| mobileugift | account |
| investment | account, metadata |
| planselection | metadata |
| contentservice | external CMS only |
| e2e | all |

\* transaction used for YTD summary endpoint on mobiledashboard feature.

## DDL reference

Schema definitions for column names and types:

| Repo | DDL file |
|------|----------|
| account | `unite-account/persistence/src/accountDatastore.sql` |
| profile | `unite-profile/persistence/src/profileDatastore.sql` |
| metadata | `unite-metadata/persistence/src/metadataDatastore.sql` |
| transaction | `unite-transaction/persistence/src/transactionDatastore.sql` |
| bank | `unite-bank/persistence/src/bankDatastore.sql` |
