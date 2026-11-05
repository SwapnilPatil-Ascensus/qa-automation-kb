# 03 - Workflows and diagrams

Sources: Team White Architecture / Messaging Command Sagas / OTP / PAS pages **[Doc]**, plus what the QA app showed **[Seen]**. Items marked **[Guess]** are inferred.

## 1. System landscape

```mermaid
flowchart TB
    subgraph Users
        ADV[Advisor / Agent]
        SPN[Plan Sponsor<br/>business owner]
        OPS[Ascensus ops<br/>installation coordinators]
    end
    subgraph Front[Experience layer - Unqork no-code]
        EAPP[eapp - Advisor flow]
        SIGN[Sponsor sign-in / flow]
        DASH[Partner dashboard + DCA]
        SALESP[Sales Portal - welcome email]
        SIM[Partner-site simulator]
    end
    GW[Kong API gateway + SecureAuth]
    subgraph MT[Middle tier - Team White]
        OAPI[Onboarding.Api]
        SAPI[Sales.Api]
        MSG[Onboarding.Messaging.Api<br/>MassTransit + RabbitMQ sagas]
        SETUP[Onboarding.Setup.Plan API<br/>steps 1-5 - Archers]
    end
    subgraph Back[Back-end systems]
        ARK[(ARK / Sybase<br/>recordkeeping)]
        PAS[PAS<br/>plan document generation]
        CLIFF[Cliff EDMS]
        CHORUS[Chorus workflow]
        SF[Salesforce CRM]
        DS[DocuSign]
        SQL[(Msvc_Onboarding<br/>SQL Server)]
        EMAIL[Email / OTP<br/>SecureAuth + notifications]
    end
    ADV --> EAPP --> GW
    SPN --> SIGN --> GW
    OPS --> DASH
    SALESP --> SAPI
    SIM -. simulates partner purchase .-> OAPI
    GW --> OAPI --> MSG
    MSG --> SETUP --> ARK
    SETUP --> PAS
    MSG --> CLIFF
    MSG --> CHORUS
    MSG --> SF
    MSG --> DS
    OAPI --> SQL
    OAPI --> EMAIL
    DASH --> SQL
```

## 2. Group 1 advisor-to-live flow (Individual(k))

```mermaid
sequenceDiagram
    autonumber
    actor ADV as Advisor
    participant UQ as Unqork eapp
    participant API as Onboarding.Api (via Kong)
    participant SAGA as Saga / Messaging
    participant ARK as ARK (Setup Plan API)
    participant PAS as PAS
    participant DS as DocuSign
    participant OPS as Cliff + Chorus + Salesforce
    actor SPN as Sponsor
    ADV->>UQ: Open partner link (style + product)
    UQ->>ADV: Landing: fees, FAQs, CRD or name+email
    ADV->>UQ: Get started
    UQ->>API: Create onboarding (advisor, offering key)
    UQ->>ADV: Firm Information (business, dealer)
    ADV->>UQ: Plan Details (client, transfer?, funds, defaults)
    UQ->>API: Save plan design data
    API->>SAGA: InitializePlanDesign
    SAGA->>ARK: Step 1 create plan id
    SAGA->>ARK: Steps 2-4 init system, defaults, establish plan
    SAGA->>PAS: Step 5 InitializePlanAdoptionDocuments
    PAS-->>SAGA: Plan document package
    SAGA->>OPS: File docs to Cliff, create Chorus item, sync Salesforce
    UQ->>ADV: Confirmation
    SAGA->>SPN: Email: sponsor to review and sign
    SPN->>DS: E-sign plan documents
    DS-->>SAGA: Signed
    SAGA->>OPS: Final comms, plan ready (about 5 business days)
```

## 3. Saga states (Messaging Command Sagas) [Doc]

```mermaid
stateDiagram-v2
    [*] --> InitializePlanDesign
    InitializePlanDesign --> SavePlanDesignData
    SavePlanDesignData --> CreatePlanInArk
    CreatePlanInArk --> InitializePlanEstablishment
    InitializePlanEstablishment --> InitializeRKSystem
    InitializeRKSystem --> InitializeRKPlanDefaults
    InitializeRKPlanDefaults --> EstablishPlan
    EstablishPlan --> InitializePlanInPAS
    InitializePlanInPAS --> ComplianceCheckFailed: compliance fails (final)
    InitializePlanInPAS --> InitializePlanDocuments
    InitializePlanDocuments --> GeneratePASDocuments
    GeneratePASDocuments --> VerifyDocumentStatus
    VerifyDocumentStatus --> ProcessPASDocumentsData
    ProcessPASDocumentsData --> UpdatePASDocumentsStatus
    UpdatePASDocumentsStatus --> InitiatePlanInstallation
    InitiatePlanInstallation --> InitiatePlanTransfer: transfer plan
    InitiatePlanInstallation --> InitiateStartupPlan: startup plan
    InitiatePlanTransfer --> [*]: docs to Cliff, Chorus item, prior-plan docs
    InitiateStartupPlan --> [*]: assign installation coordinator
    ComplianceCheckFailed --> [*]
```

Every step has a `...Submitted` pending state and a `...Failed` state. `VerifyPlanDocumentsStatusTimedOut` is a distinct failure for slow PAS. Troubleshooting uses the **Plan Setup Dashboard** (`.../onboarding/setup/plan/PlanSetup/PlanCreationStatus` on DEV/QA/PRO hosts; QA only for us).

## 4. BAML (Merrill Edge) entry flow [Seen + Doc]

```mermaid
sequenceDiagram
    actor U as Business owner
    participant ME as Merrill Edge site
    participant OP as Onboarding Portal (secure-qa)
    participant API as Onboarding.Api
    participant UQ as Unqork sign-in landing (baml style)
    participant OTP as SecureAuth OTP
    U->>ME: Customize plan (Individual(k) or Group)
    ME->>OP: /onboarding/portal/baml/initialize?plandesigntype=ik|group
    OP->>API: create onboarding (returns onboardingId)
    OP->>UQ: redirect ?onboardingId=...&userRole=Primary&planDesignType=IK|Group
    U->>UQ: First/last name, business email, phone for secure login
    UQ->>OTP: send one-time passcode (sms, phone or email)
    OTP-->>U: code
    U->>UQ: validate code, continue onboarding
```

Endpoints **[Doc]**: `POST /security/{onboardingId}/otps` (send, 201) and `POST /security/{onboardingId}/otps/validate`; 400 for unknown onboarding id, missing OTP account, or blocked account.

## 5. ShareBuilder purchase flow [Seen simulator + Doc]

```mermaid
sequenceDiagram
    actor U as Business owner
    participant SB as ShareBuilder 401k site
    participant API as Onboarding.Api
    participant UQ as Unqork (sponsor flow)
    U->>SB: Buy plan (pick SoloK Plus: loans or multiple owners)
    SB->>API: Purchase payload (contact, EIN, business, plan type, transfer?, bank, model, fees, discounts)
    API-->>SB: Redirect URL to Unqork
    SB->>U: Redirect
    U->>UQ: Complete sponsor-side onboarding
```
In QA, the **Purchase Site Simulator** (`/app/partner-site`) replaces the real ShareBuilder call.

## 6. Onboarding status model [Guess, from dashboard + issue titles]

```mermaid
stateDiagram-v2
    [*] --> Started: advisor/sponsor starts
    Started --> InProgress: saved first page
    InProgress --> FollowUp: hardstop / duplicate EIN / sponsor history
    FollowUp --> InProgress: resolved (Resolve Hardstop)
    InProgress --> Completed: documents signed and plan established
    InProgress --> Expired: reminder / last-chance emails, no action
    Expired --> InProgress: Reactivate / Extend
    InProgress --> Cancelled: Cancel
    Completed --> [*]
    Cancelled --> [*]
```
Evidence: dashboard tabs "Follow up", "Individual(k)"; columns PLAN, START DATE, TIME, SPONSOR, DUPLICATE EIN; Team White release items for "Cancel/Extend/Reactivate", "Resolve Hardstop", "Sponsor History", "Expiration emails".

## 7. QA information flow (what to check where)

```mermaid
flowchart LR
    UI[Unqork UI in QA] --> A[Plan Setup Dashboard<br/>step status]
    UI --> B[(Msvc_Onboarding / Msvc_Onboarding_Ark)]
    A --> C[(ARK QA / Sybase tables<br/>RULES.. PRFUND, PRDEFELECT ...)]
    A --> D[PAS documents -> Cliff QA]
    B --> E[Chorus QA work item]
    B --> F[Salesforce]
    UI --> G[LogRocket session replay<br/>SmallBusinessOnboarding QA]
```

Next: [04 Page-by-page walkthrough](04-page-by-page-walkthrough.md)
