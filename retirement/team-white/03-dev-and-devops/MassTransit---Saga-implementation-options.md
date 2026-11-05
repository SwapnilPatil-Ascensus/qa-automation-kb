# MassTransit - Saga implementation options

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-MassTransit---Saga-implementation-options-294988196.aspx) | Created: 2024-12-13 | Last modified: 2024-12-27 | Author: Diego Emanuel Travieso | Last editor: Diego Emanuel Travieso

---

### Fault handling

In MassTransit Sagas we will have Saga Activities (commands) that will be executed by publishing an event that will request for it, let's say the Saga needs to create a Plan. When the moment comes, a behavior in the Saga State Machine will Publish an event (e.g. CreatePlanRequested).

In the behavior that makes such request, the state machine will be set to a specific state (e.g. PlanCreationRequested) and will probably remain in that state until the Activity is finished.

Saga StateMachine code:

Event(() =>  PlanCreated , x => x.CorrelateBy((instance, context) =>     instance.CorrelationId == context.Message.CorrelationId)); Event(() =>  PlanCreationFaulted, x => x.CorrelateBy((instance, context) =>     instance.CorrelationId == context.Message.Message.CorrelationId)); ... Initially(     When(EventPreviousToCreatePlan)         .PublishAsync(x => x.Init<CreatePlanRequested>(new 		{     		x.Saga.CorrelationId 		}))         .TransitionTo(PlanCreationRequested)); ... public Event<CreatePlanCompleted> PlanCreated { get; } public Event<Fault<CreatePlanCompleted>> PlanCreationFaulted { get; }

There will be a Consumer listening to that particular event (CreatePlanRequested) that will perform the Saga Activity and in case the activity completes successfully it will Publish back an event informing that the task was completed (e.g. CreatePlanCompleted).

public class CreatePlanConsumer :     IConsumer<CreatePlanRequested> {     public async Task Consume(ConsumeContext<CreatePlanRequested> context)     {         // Do stuff to create the plan 		// Set the new PlanId in the message         await context.Publish<CreatePlanCompleted>(context.Message);     } }

The Saga State Machine will have a behavior listening to that event to change its own state and move forward with the next Activity in the Orchestration.

During(PlanCreationRequested,     When(PlanCreated)         .Then(context =>         {             context.Saga.PlanId = context.Message.PlanId;         }) 		.PublishAsync(x => x.Init<EventForNextActivity>(new 		{     		x.Saga.CorrelationId,     		x.Saga.PlanId 		}))         .TransitionTo(PlanCreated) );

In case something goes wrong when performing the CreatePlan Activity, the Consumer will throw an exception that will result in publishing an event informing the failure that will be grabbed by the Saga State Machine (public Event<Fault<CreatePlanCompleted>> PlanCreationFaulted { get; } )

public class CreatePlanConsumer :     IConsumer<CreatePlanRequested> {     public async Task Consume(ConsumeContext<CreatePlanRequested> context)     { 		try 		{         	// Do stuff to create the plan 			// Set the new PlanId in the message         	await context.Publish<CreatePlanCompleted>(context.Message); 		} 		catch (Exception e) 		{ 		    throw new Exception("Unable to create plan", e); 		}     } }

The Saga State Machine will have a behavior listening to that event to handle it. Now, depending on the nature of the Activity the State Machine could change the State to an Aborted status Compensating all needed to abort the Saga.

During(PlanCreationRequested,     When(CreatePlanCompleted)         .Then(context =>         {             context.Saga.PlanId = context.Message.PlanId;         }) 		.PublishAsync(x => x.Init<EventForNextActivity>(new 		{     		x.Saga.CorrelationId,     		x.Saga.PlanId 		}))         .TransitionTo(PlanCreated) ); DuringAny(When(PlanCreationFaulted)     .Then(context =>     {         Console.WriteLine("PlanCreation faulted");     }) 	.TransitionTo(OnboardingSagaPlanCreationStuck));

If the faulted activity could be amended by retrying, the behavior of the State Machine can initiate a retry procedure and set the State to a specific value indicating that that particular Activity is on a retry process (e.g.WaitingToRetryPlanCreation).

Schedule(() => RetryDelayExpired, saga => saga.ScheduleRetryToken, x => {     x.Received = r =>     {         r.CorrelateById(context => context.Message.CorrelationId);         r.ConfigureConsumeTopology = false;     }; }); ... During(WaitingToRetryPlanCreation,     When(RetryDelayExpired.Received)         .Then(context => context.Saga.RetryAttempt++)        //increase the counter         .PublishAsync(x => x.Init<CreatePlanRequested>(new     // Retry processing         {             x.Saga.CorrelationId         }))         .TransitionTo(PlanCreationRequested)); const int retryCount = 5; var retryDelay = TimeSpan.FromSeconds(10); WhenEnter(OnboardingSagaPlanCreationStuck, x => x     .If(context => context.Saga.RetryAttempt < retryCount,         retry => retry             .Schedule(RetryDelayExpired, context => new RetryDelayExpired(context.Saga.CorrelationId), _ => retryDelay)             .TransitionTo(WaitingToRetryPlanCreation)     ) ); ... public Schedule<RegistrationState, RetryDelayExpired> RetryDelayExpired { get; }

**Note** : For simplicity's sake, in these code samples the Saga StateMachine behavior is executing the Saga Activities by simply doing a publish of an event. In a well implemented State Machine the activities could be implemented with their own class (implementing the IStateMachineActivity interface).

*🚧 Gliffy diagram 'StateMachineWithFaultHandling' replaced by image:*

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransit---Saga-implementation-options-294988196/StateMachineWithFaultHandling.png)

### Routing Slips

In **MassTransit** a **Routing Slip**  is a sequence of steps, an **Itinerary** , that can be changing dynamically and is expected to be executed successfully in all its steps or none at all. Meaning that if a step in the **Routing Slip**  process fails all the previous steps have to be **Compensated** (i.e. returned back to the state things were before the **Routing Slip**  started). This is a similar concept to a **Transaction** in a relational database, if at any point of a DB transaction a step fails, all that was done up until that point is rolled back. The idea of the **Routing Slip**  is to do the same but while consuming and executed different resources, a **Distributed Transaction** .

A whole **Routing Slip**  could be associated to one single **Saga Activity** , and then the **Routing Slip**  will be composed by several **Routing Slip Activities** .

While the **Saga State Machine Activities**  implement **IStateMachineActivity** , the **Routing Slip Activities**  implement **IActivity** , which in turn implements **IExecuteActivity<TArguments>**  and **ICompensateActivity<TLog>** . **IExecute** will request for the Execute method, that will be called to execute the Activity. The **ICompensateActivity** will request for the **Compensate** method, which will be called if an **Activity** executed after, in the same **Routing Slip** , fails.

Another key difference to highlight about **Routing Slips**  is that instead of an **Orchestration** , where all the steps are defined and executed in a central controller, **Routing Slips**  are executed in a **Choreography** , where the list of the activities is not managed from a central orchestrator, but handled dynamically through the process. The information of the **Routing Slip Activities**  is passed over from one **Activity** to the next in the **Routing Slip** , and each **Activity** owns the **Routing Slip**  and is able to change the **Activities** within it.

To give an example, let's consider the case we used above and say that the creation of a Plan consists of several steps that have to be executed in order and if one of those steps fail, the whole plan creation has to be rolled back. For that, our CreatePlanConsumer could user a Routing Slip:

public class CreatePlanConsumer :     IConsumer<CreatePlanRequested> {     public async Task Consume(ConsumeContext<CreatePlanRequested> context)     {         var routingSlip = CreateRoutingSlip(context); 		await context.Execute(routingSlip).ConfigureAwait(false);         // Set the new PlanId in the message         await context.Publish<CreatePlanCompleted>(context.Message);     }     RoutingSlip CreateRoutingSlip(ConsumeContext<ProcessRegistration> context) 	{     	var builder = new RoutingSlipBuilder(NewId.NextGuid());     	builder.SetVariables(new     	{         	context.Message.PlanType,         	context.Message.PlaDetails     	});     	if (!string.IsNullOrWhiteSpace(context.Message.PlanType))     	{         	builder.AddActivity("PlanTypeVerification", _provider.GetExecuteEndpoint<PlanTypeVerificationActivity, PlanTypeVerificationArguments>(),             new             {                 EventType = "Road",             });         	builder.AddSubscription(context.SourceAddress, RoutingSlipEvents.ActivityFaulted, RoutingSlipEventContents.None, "PlanTypeVerification",             	x => x.Send<PlanTypeVerificationFailed>(new { context.Message.CorrelationId }));     	}     	builder.AddActivity("SaveToARK1", _provider.GetExecuteEndpoint<SaveToARK1Activity, SaveToArk1Arguments>(),         new         {             context.Message.PlanType,             context.Message.PlaDetails         }); 	    builder.AddActivity("SaveToARK2", _provider.GetExecuteEndpoint<SaveToARK2Activity, SaveToArk2Arguments>(),         new         { 			context.Message.PlanId,             context.Message.PlanType,             context.Message.PlaDetails         });     	     	builder.AddSubscription(context.SourceAddress, RoutingSlipEvents.ActivityFaulted, RoutingSlipEventContents.None, "SaveToARK2",         	x => x.Send<PlanCreationFaulted>(new { context.Message.CorrelationId }));     	builder.AddSubscription(context.SourceAddress, RoutingSlipEvents.Completed,         	x => x.Send<CreatePlanCompleted>(new { context.Message.CorrelationId }));     	return builder.Build(); 	} } public class PlanTypeVerificationActivity :     IExecuteActivity<PlanTypeVerificationArguments> {     readonly ILogger< PlanTypeVerificationActivity> _logger;     public LicenseVerificationActivity(ILogger<PlanTypeVerificationActivity> logger)     {         _logger = logger;     }     public async Task<ExecutionResult> Execute(ExecuteContext<PlanTypeVerificationArguments> context)     {         var arguments = context.Arguments;         var planType = arguments.PlanType;         _logger.LogInformation("Verifying plan type: {PlanType}",  planType); 		DateTime? expirationDate = DateTime.Today + TimeSpan.FromDays(90);         return context.CompletedWithVariables(new { ExpirationDate = expirationDate });     } } public class SaveToARK1Activity :     IActivity<SaveToARK1Arguments, SaveToARK1Log> {     readonly ILogger<SaveToARK1Activity> _logger;     readonly IEndpointAddressProvider _provider;     public SaveToARK1Activity(ILogger<SaveToARK1Activity> logger, IEndpointAddressProvider provider)     {         _logger = logger;         _provider = provider;     }     public async Task<ExecutionResult> Execute(ExecuteContext<SaveToARK1Arguments> context)     {         // Do the work to save data to ARK (step 1)                 if (arguments.PlanType == "peculiar")         {             return context.ReviseItinerary(log, variables, x =>             {                 x.AddActivitiesFromSourceItinerary();                 x.AddActivity("NewActivity", _provider.GetExecuteEndpoint<NewActivity, NewArguments>());             });         }         return context.CompletedWithVariables(new         {             planId,             arguments.PlanType         }, variables);     }     public async Task<CompensationResult> Compensate(CompensateContext<SaveToARK1Log> context)     {         //To all needed to rollback what was done in the Execute method of this activity         return context.Compensated();     } }

In the sample above PlanTypeVerificationActivity is an Activity that does not need a Compensation, so it just implements IExecuteActivity:

public class PlanTypeVerificationActivity :     IExecuteActivity<PlanTypeVerificationArguments> {     readonly ILogger<PlanTypeVerificationActivity> _logger;     public LicenseVerificationActivity(ILogger<PlanTypeVerificationActivity> logger)     {         _logger = logger;     }     public async Task<ExecutionResult> Execute(ExecuteContext<PlanTypeVerificationArguments> context)     {         var arguments = context.Arguments;         var planType = arguments.PlanType;         _logger.LogInformation("Verifying plan type: {PlanType}",  planType); 		DateTime? expirationDate = DateTime.Today + TimeSpan.FromDays(90);         return context.CompletedWithVariables(new { ExpirationDate = expirationDate });     } } public class SaveToARK1Activity :     IActivity<SaveToARK1Arguments, SaveToARK1Log> {     readonly ILogger<SaveToARK1Activity> _logger;     readonly IEndpointAddressProvider _provider;     public SaveToARK1Activity(ILogger<SaveToARK1Activity> logger, IEndpointAddressProvider provider)     {         _logger = logger;         _provider = provider;     }     public async Task<ExecutionResult> Execute(ExecuteContext<SaveToARK1Arguments> context)     {         // Do the work to save data to ARK (step 1)                 if (arguments.PlanType == "peculiar")         {             return context.ReviseItinerary(log, variables, x =>             {                 x.AddActivitiesFromSourceItinerary();                 x.AddActivity("NewActivity", _provider.GetExecuteEndpoint<NewActivity, NewArguments>());             });         }         return context.CompletedWithVariables(new         {             planId,             arguments.PlanType         }, variables);     }     public async Task<CompensationResult> Compensate(CompensateContext<SaveToARK1Log> context)     {         //To all needed to rollback what was done in the Execute method of this activity         return context.Compensated();     } }

And SaveToArk1Activity does need a Compensation, in case something goes wrong after it is completed, so it implements IActivity interface:

public class SaveToARK1Activity :     IActivity<SaveToARK1Arguments, SaveToARK1Log> {     readonly ILogger<SaveToARK1Activity> _logger;     readonly IEndpointAddressProvider _provider;     public SaveToARK1Activity(ILogger<SaveToARK1Activity> logger, IEndpointAddressProvider provider)     {         _logger = logger;         _provider = provider;     }     public async Task<ExecutionResult> Execute(ExecuteContext<SaveToARK1Arguments> context)     {         // Do the work to save data to ARK (step 1)                 if (arguments.PlanType == "peculiar")         {             return context.ReviseItinerary(log, variables, x =>             {                 x.AddActivitiesFromSourceItinerary();                 x.AddActivity("NewActivity", _provider.GetExecuteEndpoint<NewActivity, NewArguments>());             });         }         return context.CompletedWithVariables(new         {             planId,             arguments.PlanType         }, variables);     }     public async Task<CompensationResult> Compensate(CompensateContext<SaveToARK1Log> context)     {         //Do all needed to rollback what was done in the Execute method of this activity         return context.Compensated();     } }

Activities in a Routing Slip do Send to specific exchanges when the next Activity is called.

Routing Slip Activities have a CompensationLog which contains all the information needed to Compensate (rollback) all that was processed by that Activity if needed.

Routing Slip Activities can throw different types of Exception depending on the pupose (RoutingSlipException, TransientException, LongTransientException).

services.AddMassTransit(x => {     x.AddConfigureEndpointsCallback((_, _, cfg) =>     {         cfg.UseDelayedRedelivery(r =>         {             r.Handle<LongTransientException>();             r.Interval(500, 1000);         }); 	    cfg.UseMessageRetry(r => 		{     		r.Handle<TransientException>();     		r.Interval(25, 50); 		}); ...

### POC

A PoC was created to take a look at how things are actually implemented under the hood in RabbitMQ and with the exception handling.

This PoC consists of a console application running a worker that will accept a PlanType (string) that when entered will publish an event that will start a Saga.

The Saga has 2 activities: VerifyPlan and ProcessPlan.

VerifyPlan is a simple activity that given the PlanType provided is "fail" it will throw an exception that will be caught by MassTransit, sent to its corresponding error queue and ALSO sent to the State Machine queue as a Fault<VerifyPlanRequested> message, then handled by the Saga State Machine.

ProcessPlan is a Saga Activity that builds a Routing Slip which in turn, contains 3 Activities:

- VerifyPlanType: It is an execute only activity. If the PlanType is empty it will throw and exception and the whole Routing Slip will be aborted.
- SavePlanToArk: It is an execute/compensate activity. This activity will be responsible of getting the PlanId back to the Routing Slip and the Saga. If the PlanType is "noplanid" it will leave the PlanId empty.
- SavePptToArk: It is an execute/compensate activity. In case the PlanId is empty it will fail the activity, and fail the whole Routing Slip.

Observations:

- When running a "happy path" it can be seen that all the activities are executed the corresponding order.
- When PlanType is set to "fail", VerifyPlan Saga Activity throws an exception. MassTransit as a result of that exception publishes a message in verify-plan_error queue and it also publishes a Fault<VerifyPlanRequested> message in plan_state queue, that is in turn picked up by the Saga State Machine handling that specific fault.
- When PlanType is set to an empty value, the first Activity in the ProcessPlan Routing Slip (VerifyPlanType) will fail, faulting the whole Routing Slip, Publishing the ProcessPlanFailed event, that is then handled by the Saga State Machine.
- When PlanType is set to "NoPlanId", the second Activity in the ProcessPlan Routing Slip (SavePlanToArk) will leave the PlanId empty. This will lead to the last Activity in the Routing Slip (SavePptToArk) to fail. The while Routing Slip Fails and the previous Activities (in this case just SavePlanToArk) will run its own Compensation. Then the Routing Slip publishes ProcessPlanFailed and the Saga State Machine handles it.

With the setup mentioned above the following was observed in RabbitMQ

Queues

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransit---Saga-implementation-options-294988196/image-2024-12-24_16-11-7.png)

Relevant Exchanges

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransit---Saga-implementation-options-294988196/image-2024-12-24_16-12-20.png)![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransit---Saga-implementation-options-294988196/image-2024-12-24_16-13-2.png)

The exception handling framework was included in the POC in a couple of places with different approaches to allow the exceptions in the Saga Activities and in the Routing Slip to reach the Saga State Machine through RabbitMQ.

In VerifyPlanConsumer

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransit---Saga-implementation-options-294988196/image-2024-12-27_17-7-39.png)

The exception thrown by ManagerExceptionHandler.HandleException(ex) results in a Fault<T> message in the SagaStateMachine queue, where it's handled.

In SavePptToArkActivity, a specific approach was used in order to keep the contents of the original exception at Manager level and send it back to the Orchestrator.

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-MassTransit---Saga-implementation-options-294988196/image-2024-12-27_17-12-51.png)

Note that with the current exception framework, if the original exception is sent directly to the ManagerExceptionHandler.HandleException method, the original message will be lost.

The code of this POC lives in [Repo](https://tfs.ascensus.com/tfs/PSG/Sandbox/_git/MassTransitPOC)
