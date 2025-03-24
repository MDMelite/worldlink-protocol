Please generate a markdown file named agent-manifest-reference.md in the docs/ directory with the following content and formatting:

Start with a level 1 heading: Agent Manifest Reference

Then add this paragraph: The agent manifest is a JSON file (`agent.json`) that provides essential information about an agent to the WorldLink Protocol bus. It declares the agent's identity, capabilities, security context, and other important metadata necessary for the bus and other agents to understand and interact with it.

Next, add a level 2 heading: Sample `agent.json`

Then add a code block containing:
{
  "agent_id": "my_unique_agent_id",
  "name": "My Intelligent Agent",
  "version": "1.0.0",
  "description": "A brief description of what this agent does.",
  "author": "Your Name or Organization",
  "contact": "your.email@example.com",
  "capabilities": [
    "intent_recognition",
    "data_retrieval",
    "task_execution"
  ],
  "trust_level": "community",
  "permissions": {
    "network": ["read", "write"],
    "storage": ["read"],
    "external_apis": ["weatherapi.com"]
  },
  "sandbox_mode": true,
  "entry_point": "main.py:run",
  "client_library": "python"
}

Next, add a level 2 heading: Field Descriptions

Then add a level 3 heading: `agent_id`

Followed by this paragraph: **Data Type:** String. **Purpose:** A globally unique identifier for the agent within the WorldLink Protocol network. This ID is crucial for the bus to correctly register and route messages to the agent. **Recommendation:** Use a UUID or a namespaced identifier to ensure uniqueness. This field is **required**.

Next, add a level 3 heading: `name`

Followed by this paragraph: **Data Type:** String. **Purpose:** A human-readable name for the agent, intended for display in logs, monitoring tools, or user interfaces. **Recommendation:** Choose a name that clearly and concisely describes the agent's function. This field is **recommended**.

Next, add a level 3 heading: `version`

Followed by this paragraph: **Data Type:** String. **Purpose:** The version of the agent's software. This allows for tracking updates and managing compatibility within the protocol ecosystem. **Recommendation:** Follow semantic versioning (e.g., "1.0.0"). This field is **recommended**.

Next, add a level 3 heading: `description`

Followed by this paragraph: **Data Type:** String. **Purpose:** A brief textual description of the agent's functionality, its main purpose, and any key features. This helps in understanding the role of the agent in the overall system. **Recommendation:** Keep it concise and informative. This field is **recommended**.

Next, add a level 3 heading: `author`

Followed by this paragraph: **Data Type:** String. **Purpose:** The name of the individual or organization responsible for developing and maintaining the agent. This is useful for attribution and contact purposes. This field is **optional**.

Next, add a level 3 heading: `contact`

Followed by this paragraph: **Data Type:** String. **Purpose:** An email address or other contact method for the agent's author or support team. This allows for reporting issues or making inquiries. This field is **optional**.

Next, add a level 3 heading: `capabilities`

Followed by this paragraph: **Data Type:** Array of Strings. **Purpose:** A list of the high-level functionalities or skills that the agent possesses. These capabilities can be used by other agents or the bus for service discovery and task delegation. **Recommendation:** Use a consistent and well-defined vocabulary of capabilities within your WorldLink network. Example: `["intent_recognition", "data_retrieval", "task_execution"]`. This field is **recommended**.

Next, add a level 3 heading: `trust_level`

Followed by this paragraph: **Data Type:** String. **Purpose:** Indicates the level of trust associated with the agent within the protocol. This can influence how other agents interact with it and what permissions are granted. **Recommendation:** Define a clear hierarchy or set of trust levels (e.g., "official", "verified", "community", "untrusted"). This field is **optional**.

Next, add a level 3 heading: `permissions`

Followed by this paragraph: **Data Type:** Object. **Purpose:** Defines the specific permissions granted to the agent, outlining what resources (e.g., network, storage, external APIs) it can access and what actions it can perform. The structure of this object can be tailored to the security requirements of your protocol.

Next, add a level 4 heading: `network`

Followed by this paragraph: **Data Type:** Array of Strings. **Purpose:** Specifies the allowed network operations for the agent (e.g., `["read"]`, `["write"]`, `["connect"]`).

Next, add a level 4 heading: `storage`

Followed by this paragraph: **Data Type:** Array of Strings. **Purpose:** Specifies the allowed storage operations (e.g., `["read"]`, `["write"]`, `["delete"]`).

Next, add a level 4 heading: `external_apis`

Followed by this paragraph: **Data Type:** Array of Strings. **Purpose:** A list of specific external API domains or services that the agent is permitted to access. This helps in controlling external dependencies and potential security risks. Example: `["weatherapi.com", "maps.googleapis.com"]`.

Next, add a level 3 heading: `sandbox_mode`

Followed by this paragraph: **Data Type:** Boolean. **Purpose:** A security flag indicating whether the agent should be run in a restricted or sandboxed environment to limit its access to system resources and prevent potential harm. **Recommendation:** Set to `true` for agents from untrusted sources or those performing sensitive operations. This field is **optional**.

Next, add a level 3 heading: `entry_point`

Followed by this paragraph: **Data Type:** String. **Purpose:** Specifies how to execute the agent's code. The format typically includes the main file or module and the function or class to be instantiated (e.g., `"main.py:run"`, `"com.example.MyAgent"`). This field is **required**.

Next, add a level 3 heading: `client_library`

Followed by this paragraph: **Data Type:** String. **Purpose:** Identifies the client library or SDK used to build the agent. This can be useful for the bus or other management tools to understand the agent's runtime environment. Example: `"python"`, `"javascript"`, `"java"`. This field is **required**.

Next, add a level 2 heading: Optional Fields

Followed by this paragraph: The following are some additional optional fields that you might consider including in your agent manifest:

Next, add a level 3 heading: `bus_address`

Followed by this paragraph: **Data Type:** String. **Purpose:** The specific address and port of the WorldLink Protocol bus that this agent should connect to. While often configured separately, it can be included in the manifest for static deployments.

Next, add a level 3 heading: `security_policy`

Followed by this paragraph: **Data Type:** String. **Purpose:** A reference to a specific security policy document or configuration that should be applied to this agent.

Next, add a level 3 heading: `dependencies`

Followed by this paragraph: **Data Type:** Array of Strings. **Purpose:** A list of external software packages or services that the agent relies on. This can be helpful for deployment and dependency management.

Next, add a level 3 heading: `topics`

Followed by this paragraph: **Data Type:** Object. **Purpose:** Defines the topics that the agent intends to subscribe to and/or publish to. This can provide a declarative way to understand the agent's communication patterns. The structure of this object can be further defined based on your needs.

Next, add a level 2 heading: Best Practices

Followed by this paragraph: Here are some recommended best practices for creating agent manifest files:

Then add an unordered list with the following items:
* Ensure the `agent_id` is globally unique and follows a consistent naming convention.
* Provide a clear and informative `description` to help others understand the agent's role.
* Accurately list all the agent's `capabilities` to facilitate proper discovery and interaction within the network.
* Define the `permissions` as precisely as possible, adhering to the principle of least privilege to enhance security.
* Use a well-defined and documented set of values for `trust_level` if you are using this field.
* Keep the manifest file synchronized with the agent's actual configuration and capabilities.
* Consider using a schema validation tool to ensure your `agent.json` file is correctly formatted.

This provides a more comprehensive reference for the agent manifest file. Please update the `docs/agent-manifest-reference.md` file with this content.