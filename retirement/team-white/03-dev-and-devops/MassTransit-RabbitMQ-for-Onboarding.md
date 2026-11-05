# MassTransit/RabbitMQ for Onboarding

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-MassTransitRabbitMQ-for-Onboarding-294978088.aspx) | Created: 2024-12-02 | Last modified: 2024-12-02 | Author: Max Shakirov | Last editor: Max Shakirov

---

### Objective

Analyze and compile a list of research goals and decisions based on MassTransit/RabbitMQ event management technologies in conjunction with Onboarding project objectives. Outline pros and cons of each approach.

### Research Goals

| **Goal** | **Description** | **Status** | **Additional Details** |
| --- | --- | --- | --- |
| Introduction to RabbitMQ | <br>Understand conceptual components of RabbitMQ broker and the way how they are connected. Research and understand following:<br>- Publishers<br>- Exchanges<br>- Queues<br>- Consumers<br>- Messages<br>- Message publish and consume process<br>- Exchange and Queue routing and binding process<br>- Exchange Types<br>- Message publish vs message send<br>- Multiple consumers per event type<br>  - Need for it<br>  - Pitfalls and considerations<br> | Completed | <br> |
| Error Handling | <br>Research and understand following:<br>- Skipped queues and error queues<br>  - Skipped and error queue handling with plugins in order to move messages back to processing<br>- Retry Policies<br>- Middleware filters<br>  - Kill switch<br>  - Circuit breaker<br>  - Rate Limiter<br>  - Concurrency Limit<br> | <br> | <br> |
| Saga Pattern | <br>Research and understand following:<br>- Understand the difference between concepts of Choreography and Orchestration in distributed transaction world<br>- Saga orchestration definitions<br>  - State management<br>  - State context<br>  - State events and their correlation<br>  - State controls<br>  - Calling consumers upon state change<br>  - Transaction monitoring and recovery<br>  - Persistence via SQL Server<br>- Routing slips<br> | <br> | <br> |
| Additional Features | <br>- Message Scheduling<br> | <br> | <br> |
| Test | <br>- Unit, Integration and End-to-end testing<br> | <br> | <br> |

### Research Decisions

| **Concept** | **Description** | **Decision** | **Additional Details** |
| --- | --- | --- | --- |
| Publishing vs Sending message | <br>Mass Transit allows for two distinct ways of working with messages and making sure that they are sent to correct exchanges and subsequently queues:<br>- Send a message to a specific queue<br>- Publish message<br>**Send a message approach**  will require that you'd need to specify a queue name that will be an address for your message - based on that queue name, Mass Transit will figure out which exchange and queue need to be used in the end.<br>- Pros<br>  - Gives a developer a better control over queue naming convention, as well as name of exchange being used and type when it's being used in Saga.<br>  - Using Send approach promotes a separation between a concept of commands and events within the application, which could be preferable under certain circumstances.<br>- Cons<br>  - Creates a dependency between sender and receiver that is explicitly defined - there is no isolation between the two.<br>  - Need to keep a track of URI addresses used for queues and message types associated with them.<br>  - No true fire and forget event propagation from sender point-of-view to Consumer.<br>  - Since queue name should always be outlined, may lead to unintended behavior when things don't get address well.<br>  - You will still need to use Publish approach within your application to handle Consumer related events in Saga.<br>**Publish a message approach**  will only require a unique datatype associated with message type in order to land in correct exchange and queue.<br>- Pros<br>  - Mass Transit will create and execute upon all infrastructure points needed for this message to land in a correct exchange, queue and finally consumer<br>    - no need to remember endpoint URIs<br>    - it's easy to see exchanges and queues created for any given publish event you are adding in RabbitMQ<br>  - Publishers and Consumers don't need to worry to match anything except message type they handle<br>  - There could be more than one consumer per type (if desired), given that they all have unique Queue name on the consumer side.<br>  - It's easier to handle multiple events that depend on single type in Mass Transit configuration.<br>- Cons<br>  - Will require Mass Transit to create more infrastructure around all event types that could be used within application - at least 3 per unit of work or more.<br>  - Consumers that need to handle certain message types need to understand if there is other consumers that already do so, so they could either choose a different queue name or a unique new message type to handle their logic....former approach is the best way to handle this scenario.<br>  - Your Saga might need to have a bit more states to handle, as well as events.<br> | Given an ease that Mass Transit has when handling messages based on type, there is hardly any reason to use Send a message approach in comparison to Publish. Publish methodology also will allow us to support a unique set of consumers per types of events that we want to handle, as well as on the Saga side for event and state management. Unless we'd learn there is a compelling reason to use Send a message methodology for Onboarding, Publishing events from both Saga and Consumers looks much more easier for a team. | <br> |
| Support multiple exchange types (see basic concepts below) |  | <br> | <br> |
| Use multiple consumers per message type |  | <br> | <br> |

### Diagrams

##### Basic Concepts

**RabbitMQ High Level Components, Definitions and Connections**

***🚧 Gliffy diagram 'RabbitMQ General Flow' replaced by image:***

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransitRabbitMQ-for-Onboarding-294978088/RabbitMQ%20General%20Flow.png)

**RabbitMQ Exchange Types: Direct Exchange**

Message propagation is orchestrated based on routing keys that's defined between queue and exchange in order to channel communication to a proper consumer.

*🚧 Gliffy diagram 'RabbitMQ Direct Exchange Copy' replaced by image:*

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransitRabbitMQ-for-Onboarding-294978088/RabbitMQ%20Direct%20Exchange%20Copy.png)

**RabbitMQ Exchange Types: Fanout Exchange**

Message propagation is not limited by any rules - every queue that's bound to selected exchange will get a message in order to communicate it down to a proper consumer.

*🚧 Gliffy diagram 'RabbitMQ Fanout Exchange' replaced by image:*

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransitRabbitMQ-for-Onboarding-294978088/RabbitMQ%20Fanout%20Exchange.png)

**RabbitMQ Exchange Types: Topic Exchange**

Message propagation is orchestrated based on routing key pattern that's defined between queue and exchange in order to channel communication to a proper consumer.

*🚧 Gliffy diagram 'RabbitMQ Topic Exchange' replaced by image:*

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransitRabbitMQ-for-Onboarding-294978088/RabbitMQ%20Topic%20Exchange.png)

**Routing Key prerequisites and Pattern Examples**

When defining Routing Keys for this type of exchange, it's necessary to incorporate words that are separated by periods as your Routing Key in order to take advantage of topic exchange.

Let's take a look at a following example to illustrate how routing works:

- Let's define Routing Keys in our imaginary application for Producers
  - order.shipping
  - order.shipping.log
  - order.payment
  - order.payment.log
- In order to route a message to ALL order specific queues, your routing key pattern will look like following
  - order.# (# is matching any amount of words that follow "order." here)
- In order to route a message to SPECIFIC (e.g. order.shipping and order.payment only) queues, your routing key pattern will look like following
  - order.* (* is matching first word that follow "order." here)

**RabbitMQ Exchange Types: Headers Exchange**

Message propagation is orchestrated based on headers (i.e. key/values pairs) which are defined between queue and exchange in order to channel communication to a proper consumer.

### *🚧 Gliffy diagram 'RabbitMQ Headers Exchange' replaced by image:*

### References and Training Material

#### Ascensus Repos

#### Online
