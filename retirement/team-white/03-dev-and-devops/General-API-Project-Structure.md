# General API Project Structure

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-General-API-Project-Structure-294985047.aspx) | Created: 2024-12-10 | Last modified: 2025-02-15 | Author: Max Shakirov | Last editor: Franklin Zabala

---

### Objective

This is a simple guideline for a project structure that DEVs agreed to follow. Keep in mind that structure of the project is an evolving concept, hence not everything below will make sense for any given service.

### Folder structure for a single service

- **Build**
  - Service build specific scripts for CI/CD
- **Deploy**
  - Service deploy specific scripts for CI/CD
- **Source**
  - **[ServiceName].Api**
    - Entry point for a service application
    - Contains endpoint definitions
    - Will have DI configuration responsibilities for it-self and have means to configure DI for all child projects by calling those child project DI container methods.
    - Will be responsible for request filtering, response caching etc., or any other middleware.
  - **[ServiceName].Api.Contract**
    - Contains definitions for request and response objects at the service level
  - **[ServiceName].Api.Domain**  (Following IDesign architecture approach for its folders and contains all necessary code to configure domain specific DI injections for clients calling into this)
    - **Manager**
      - Contains class definitions to group certain business rules into a logical set of operations within the domain
    - **Engine**
      - Contains class definitions to implement business rules within the application
    - **ResourceAccess**
      - Contains class definitions to access data outside of this project (i.e. Sybase, SQL, Rest, SOAP etc)
  - **[ServiceName].Api.Domain.Contract**
    - Contains definitions for request and response objects in and out of domain level
  - **[ServiceName].Workflow**
    - Entry point for a service that will have endpoints configured specifically to work in context of message broker and Saga(s)
    - Contains all definitions for MassTransit/RabbitMQ configuration, including DI container
    - Contains Saga state machine and Saga context definitions
    - Could contain events or they could be offset to a different project (see payroll)
    - Could contain consumers or they could be offset to a different project (see payroll)
    - Could contain business logic for consumers or that could be offset to a different project (see payroll)
- **Test** (Self-explanatory)
  - **[ServiceName].Api.UnitTest**
  - **[ServiceName].Api.AutomationTest**
