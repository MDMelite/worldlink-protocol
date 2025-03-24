# Glossary

This glossary defines key terms used within the WorldLink Protocol documentation.

* **Agent:** An autonomous software entity capable of perceiving its environment, acting upon that environment using actuators, and operating autonomously to achieve its objectives.
* **Agent Certificate:** A digital certificate that verifies the identity and potentially the capabilities and trust level of an agent within the WorldLink Protocol. Issued by a Certificate Authority (potentially the Bus Arbiter or a designated service).
* **Bus:** The central communication channel in the WorldLink Protocol that facilitates the exchange of messages (packets) between agents.
* **Bus Arbiter:** A core component (logical or physical) of the WorldLink Protocol responsible for managing the communication bus, including agent registration, message routing, and potentially enforcing security policies.
* **Capability:** A high-level function or service that an agent can perform (e.g., "text summarization," "weather retrieval," "image generation"). Agents declare their capabilities in their manifest.
* **Module:** A self-contained unit of functionality within an agent or the broader WorldLink Protocol ecosystem. Can refer to UI modules, NLU modules, etc.
* **Packet:** A unit of data transmitted over the WorldLink Protocol bus between agents. Contains a payload and metadata such as source and destination agent identifiers.
* **Packet Lifecycle:** The journey of a message as it travels through the WorldLink Protocol, from its creation by a sending agent to its receipt and processing by a destination agent. This includes stages like creation, routing, arbitration, delivery, and response.
* **Sandbox Mode:** A restricted execution environment for agents, designed to limit their access to system resources and prevent malicious behavior. Agents running in sandbox mode typically have limited permissions.
* **Software Development Kit (SDK):** A collection of tools, libraries, documentation, code samples, and processes that allow developers to create software applications for a specific platform or environment (in this case, for building WorldLink Protocol agents).
* **Topic:** A logical channel or subject to which agents can publish messages and subscribe to receive messages of interest. The WorldLink bus uses topics to route messages between agents.
* **WorldLink Protocol:** The standardized set of specifications, guidelines, and protocols that enable communication and collaboration between intelligent agents across a decentralized network.