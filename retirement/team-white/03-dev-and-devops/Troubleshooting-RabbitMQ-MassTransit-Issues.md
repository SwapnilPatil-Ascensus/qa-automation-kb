# Troubleshooting RabbitMQ/MassTransit Issues

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Troubleshooting-RabbitMQMassTransit-Issues-336416501.aspx) | Created: 2025-08-22 | Last modified: 2025-08-22 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

#### Issue: Message not getting picked up by consumer, command stuck in "Submitted" state

##### Fix: Consumers Must Have Unique Names Within Entire Solution

Note that all consumers must have unique names, regardless which project they are in.  We have to be mindful of porting existing consumers from Workflow API into Messaging API to ensure that every consumer receives its own unique queue and that is driven by the name of the consumer by default.  Consumers do have their own unique exchanges, which use fully qualified names based on the name of the consumer (including the namespace), but the queue names are not fully qualified, which can cause messages to be picked up incorrectly by the wrong consumer (Workflow API vs Messaging API).

When this issue occurs, there may not be any errors or indication in the logs.  However, the issue can be observed in RabbitMQ by looking for the consumers skipped message queue.

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Troubleshooting-RabbitMQMassTransit-Issues-336416501/image-2025-8-22_7-45-9.png)
