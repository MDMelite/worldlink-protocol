# Agent Configuration

This document provides guidance on how to configure agents for the WorldLink Protocol. Agent configuration primarily involves defining the agent's manifest file (`agent.json`) and specifying communication topics.

## Agent Manifest (`agent.json`)

Each agent in the WorldLink Protocol ecosystem must have an `agent.json` file at its root directory. This file, known as the agent manifest, declares essential metadata about the agent, including its identity, capabilities, and how to interact with it.

Here is a breakdown of the key fields typically found in an `agent.json` file:

* **`agent_id` (string, required):** A unique identifier for the agent within the WorldLink Protocol network. This ID should be persistent across different runs of the agent. If not provided during registration, the bus might assign one.

* **`name` (string, required):** A human-readable name for the agent (e.g., "Weather Reporter", "Text Summarizer").

* **`version` (string, required):** The version number of the agent (e.g., "1.0.0", "0.5-beta").

* **`description` (string, optional):** A brief description of what the agent does.

* **`capabilities` (array of strings, optional):** A list of high-level functions or services that this agent can perform (e.g., `["get_weather"]`, `["summarize_text", "translate_language"]`). These capabilities can be used by other agents to discover and interact with this agent.

* **`topics` (object, optional):** Defines the communication topics that the agent will interact with. This object typically has two keys:
    * **`subscribe` (array of strings):** A list of topics that the agent will subscribe to in order to receive messages.
    * **`publish` (array of strings):** A list of topics that the agent can publish messages to.

* **`entry_point` (object, required):** Specifies how to execute the agent. The structure of this object depends on the agent's implementation language. For example:
    * **Python:**
        ```json
        "entry_point": {
            "language": "python",
            "script": "main.py"
        }
        ```
    * **JavaScript:**
        ```json
        "entry_point": {
            "language": "javascript",
            "script": "index.js"
        }
        ```
    * Other languages might have different required fields (e.g., `command` for an executable).

* **`security` (object, optional):** Contains security-related configurations, such as required permissions or authentication methods. The specific fields within this object will depend on the security mechanisms implemented in the WorldLink Protocol.

### Example `agent.json` for a Python Agent:

```json
{
  "agent_id": "weather-reporter-123",
  "name": "Weather Reporter",
  "version": "1.0.0",
  "description": "Provides current weather information for a given location.",
  "capabilities": ["get_weather"],
  "topics": {
    "subscribe": ["weather/request"],
    "publish": ["weather/report"]
  },
  "entry_point": {
    "language": "python",
    "script": "weather_agent.py"
  }
}
