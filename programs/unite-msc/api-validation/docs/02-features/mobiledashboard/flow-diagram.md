# Mobile Dashboard — flow diagram

## Sequence: GET mobiledashboard

```mermaid
sequenceDiagram
    autonumber
    participant Test as Cucumber
    participant BFF as MobileDashboardService
    participant Acct as AccountGateway
    participant Meta as MetadataGateway
    participant OnPrem as OnPremAccountGateway
    participant Prof as ProfileGateway
    participant AcctDB as account DB
    participant MetaDB as metadata DB
    participant ProfDB as profile DB

    Test->>BFF: GET /mobiledashboard (member JWT)
    BFF->>Acct: getAccountsByMemberId(includeFundPositions=true)
    Acct->>AcctDB: tu_acct + tu_fund_balance + prices via metadata
    AcctDB-->>Acct: Account[] with FundPosition[]
    Acct-->>BFF: accountList

    BFF->>Meta: getPlanByTraunchId(traunchId)
    Meta->>MetaDB: tu_traunch
    MetaDB-->>Meta: Plan (branding, asofDate)
    Meta-->>BFF: plans[]

    BFF->>OnPrem: getAccountByAccountNumber(prefix, branding)
    Note over OnPrem: external — banks, withdrawal, PATAP
    OnPrem-->>BFF: OnPremMobileAccount

    loop each displayable account
        BFF->>Prof: getBeneficiary(seqBeneId)
        Prof->>ProfDB: tu_bene
        ProfDB-->>Prof: Beneficiary
        Prof-->>BFF: bene fields on MobileAccount
        BFF->>BFF: loadPositions (sum units × price)
    end

    BFF->>Prof: getOwner(seqPersonId)
    Prof->>ProfDB: tu_person
    ProfDB-->>Prof: Owner
    Prof-->>BFF: ownerFirstName/LastName

    BFF->>BFF: merge matching grants, sort, totalBalance
    BFF-->>Test: MobileDashboard JSON
```

## Balance calculation flow

```mermaid
flowchart TD
    A[tu_acct by uii_member_id] --> B[tu_fund_balance units]
    B --> C[tu_traunch.asof_date + branding]
    C --> D[tu_fund_price at asof_date]
    D --> E["fund_value = ROUND(units × price, 2)"]
    E --> F[acct_balance = SUM fund_value per account]
    F --> G[totalBalance = SUM acct_balance displayed accounts]

    H[OnPrem PATAP branding] -.->|overrides| F
```

## YTD summary flow (@md13–@md15)

```mermaid
sequenceDiagram
    participant Test as Cucumber
    participant BFF as MobileDashboardService
    participant Acct as AccountGateway
    participant Txn as TransactionGateway
    participant TxnDB as transaction DB

    Test->>BFF: GET /mobileytdsummary/{ext}
    BFF->>Acct: getAccountsByMemberIdAndExt(ext)
    BFF->>Txn: getContributionSummaryByExt(ext)
    Txn->>TxnDB: JETT / OMNI / ENV query by backend
    TxnDB-->>Txn: cyrcontrib
    Txn-->>BFF: ContributionSummary.ytdContrib
    BFF-->>Test: MobileContriSummary
```

## Related docs

- Orchestration detail: `docs/00-architecture/bff-orchestration-flow.md`
- External/on-prem: `docs/00-architecture/external-systems.md`
- Field mapping tables: `api-to-db-mapping.md`
