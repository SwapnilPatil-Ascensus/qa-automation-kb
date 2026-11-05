# Architecture

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Architecture-294981599.aspx) | Created: 2024-12-05 | Last modified: 2024-12-17 | Author: Max Shakirov | Last editor: Max Shakirov

---

### IK Workflow Group 1

| <br>*🚧 Displaying source code of HTML macro instead of rendering it*<br>*🚧 Nested Code Block macro 1️⃣ moved below*<br> |
| --- |

*🚧 Nested Code Block macro 1️⃣ moved here:*

<iframe width="100%" height="1200" src="https://miro.com/app/board/uXjVMIMg1Yo=/?moveToWidget=3458764610469529081&cot=14" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

### Infrastructure Setup

| <br>*🚧 Displaying source code of HTML macro instead of rendering it*<br>*🚧 Nested Code Block macro 2️⃣ moved below*<br> |
| --- |

*🚧 Nested Code Block macro 2️⃣ moved here:*

<iframe width="100%" height="1200" src="https://miro.com/app/board/uXjVMIMg1Yo=/?moveToWidget=3458764610012864773&cot=14" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

### High Level

High level diagram depicts layers of interaction that wrap around a full onboarding process for a plan. Although below diagram contains a lot of details already, all of the pieces are still subject to change.

- Please note that diagram is divided into 4 distinct logical sections:
  - Sales - this section is aimed to explain a set of interactions that happen before the plan is created through sales process.
  - Plan Initiation - this particular section explains part of the process when sales process is completed and plan goes into its initiation phase.
  - Plan Design - this section depicts set of interactions needed to design various aspects of plan, e.g. building up plan rules, adding funds etc.
  - Plan Completion and Activation - this is a final step in the process that explains processes taking place when a plan is already designed, documents signed etc.
- Quick guide how to look a diagram efficiently:
  - The overall process flow happens from left to right across all horizontal sections, i.e. Sales → Plan Initiation → Plan Design → Plan Completion and Activation.
  - Everything that's above the API layer is either WEB experience or other systems within Asensus that TAP into API layer that team will build.
    - Here, important pieces are those that depicted in **green** - this is Unqork experience that Axo will be helping Team White to build.
      - For Sales it's IK Sales Portal box
      - For Plan Initiation, Design, Completion and Activation it's Unqork (Plan Design) box
    - Please note DCA integration into Unqork - we will be integrating DCA with the Dashboard in Unqork (more on this detail later)
  - API layer explains all isolated API features that Team White will build and potentially support.
    - Sales.API - Sales portal related data exchange
    - Branding.API - a placeholder for all matters related to branding. Whether this will be API or not is still a suspended question. At least intend here is to provide CSS/Styling capabilities to Onboarding experience when it comes to our branded products.
    - Onbording.API - Onboarding portal related data/document exchange
  - Items beneath each API layer explain various steps, data models and systems we will be using in our Integration work on the backend - they are kind of self-explanatory, with only exception of Saga/Orchestration and Onbording.API, these are explained below.
    - Onboarding.API will be a main service that Unqork Web experience will access  (via secure Kong gateway) in order to support plan onboarding from the beginning and all the way down.
      - Onboarding.API won't be doing any "work" it-self, it's a passthrough point for data that's coming in and out. Here we will define all contracts and data models needed to interact with Unqork, or any other WEB experience going forward, and this is where we will pass all requests to our new Orchestrator/Saga to fulfill.
      - Plan Onboarding Workflow, Orchestration, Saga box represents a point in processing when we need to execute multiple transactions within the application based on variety of services that we plan to use. Saga (i.e. Workflow or Orchestration) is nothing but a sequence of events that could be controlled and acted upon as a whole, both when things are successful or not. Sagas, just like any multistep action could succeed, fail, or paused across the whole process.

| <br>*🚧 Displaying source code of HTML macro instead of rendering it*<br>*🚧 Nested Code Block macro 3️⃣ moved below*<br> |
| --- |

*🚧 Nested Code Block macro 3️⃣ moved here:*

<iframe width="100%" height="1200" src="https://miro.com/app/board/uXjVMIMg1Yo=/?moveToWidget=3458764608417604508&cot=14" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>

### IK Proposed Architecture

| <br>*🚧 Displaying source code of HTML macro instead of rendering it*<br>*🚧 Nested Code Block macro 4️⃣ moved below*<br> |
| --- |

*🚧 Nested Code Block macro 4️⃣ moved here:*

<iframe width="100%" height="1200" src="https://miro.com/app/board/uXjVMIMg1Yo=/?moveToWidget=3458764603341945815&cot=14" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>
