# Jaeger

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Jaeger-315561240.aspx) | Created: 2025-04-07 | Last modified: 2025-04-08 | Author: Max Shakirov | Last editor: Max Shakirov

---

Onboarding project is using Jaeger as a distributed tracing observability platform to collect and present data that spans multiple service call, databases, events in one cohesive way in order to trace any potential bottlenecks and understand over call structure for any given API interaction.

### Setup

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Jaeger-315561240/image-2025-4-7_15-46-21.png)

For Onboarding project, we are actively using sidecar collector in order to receive Open Telemetry data, which in turn gets pushed to Jaeger's log database and subsequently used in Jaeger UI to create a full endpoint call topology for a given API.

### Terminology

- Span - a **span**  represents a logical unit of work that has an operation name, the start time of the operation, and the duration. Spans may be nested and ordered to model causal relationships.
- Trace - a **trace**  represents the data or execution path through the system. It can be thought of as a directed acyclic graph of spans.
- Tag - key/value pair that could be attached to any activity within a span.
- Jaeger UI - web site for Jaeger trace analysis
