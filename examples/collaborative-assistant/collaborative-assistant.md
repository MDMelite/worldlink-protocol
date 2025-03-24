# Collaborative Assistant Example

This example demonstrates a simple collaborative assistant workflow where different agents work together to fulfill a user request. The scenario involves a user asking for the current weather.

## Flow

1.  **UI Module (`ui-module/`):**
    * **Receiving Input:** The `ui-module` is responsible for capturing user input. This could be through a text interface or a graphical user interface.
    * **Example:** The user types: "What's the weather like in Calgary?"
    * The `ui-module` might format this input into a standard packet and send it to the `nlu-agent`.

    ```json
    {
      "to": "nlu_agent",
      "action": "parse_query",
      "payload": {
        "user_query": "What's the weather like in Calgary?"
      }
    }
    ```

2.  **NLU Agent (`nlu-agent/`):**
    * **Parsing:** The `nlu-agent` (Natural Language Understanding agent) receives the user query and parses it to understand the intent and extract relevant information (entities).
    * **Example:** The `nlu-agent` analyzes the query and determines the intent is to get the weather and the location is "Calgary".
    * It then sends a packet to the `planner-agent` with the parsed information.

    ```json
    {
      "to": "planner_agent",
      "action": "get_weather",
      "payload": {
        "location": "Calgary"
      }
    }
    ```

3.  **Planner Agent (`planner-agent/`):**
    * **Dispatching Subtasks:** The `planner-agent` receives the request and determines the necessary steps to fulfill it. For a weather query, it might need to call an external weather API.
    * **Example:** The `planner-agent` decides to use an `exec-agent` that has the capability to fetch weather data. It sends a task to the `exec-agent`.

    ```json
    {
      "to": "exec_agent",
      "action": "fetch_weather",
      "payload": {
        "city": "Calgary"
      }
    }
    ```

4.  **Exec Agent (`exec-agent/`):**
    * **Formatting and Returning a Result:** The `exec-agent` receives the task, performs the action (e.g., calls a weather API - this would be a placeholder for now), and formats the result.
    * **Example:** The `exec-agent` (hypothetically) retrieves weather data for Calgary.
    * It then sends the formatted result back to the `ui-module` (or potentially through the `planner-agent`). For simplicity, we'll send it directly back to the `ui-module` in this example.

    ```json
    {
      "to": "ui_module",
      "action": "display_weather",
      "payload": {
        "location": "Calgary",
        "temperature": "15°C",
        "conditions": "Sunny"
      }
    }
    ```

5.  **UI Module (Continued):**
    * The `ui-module` receives the result and displays it to the user.
    * **Example:** The UI shows: "The weather in Calgary is 15°C and sunny."

This example illustrates a basic interaction flow between the different agents in the collaborative assistant. Each agent has a specific role, and they communicate through well-defined packets.

This concludes Phase 2 of the assignment. Please let me know when you have created this file and pasted the content. We can then move on to Phase 3: SDK & Tooling Scaffold.