# Collaborative Assistant Example

This document provides a complete example of how multiple agents collaborate over the WorldLink Protocol to fulfill a user request.

## Scenario

A user asks:  
**"Can you generate a marketing plan for my AI-powered productivity app?"**

## Agents Involved

1. **UI Agent (ui-1)** – Captures the user query.
2. **Language Understanding Agent (nlu-1)** – Interprets the query and extracts intent.
3. **Planning Agent (planner-1)** – Breaks down the request into subtasks.
4. **Research Agent (data-1)** – Gathers relevant market and competitor data.
5. **Execution Agent (exec-1)** – Formats and assembles the final document.
6. **Compliance Agent (compliance-1)** – Performs a final QA check to ensure the document meets required standards.

## Packet Flow

1. **UI Agent → Bus:**  
   Sends packet with user query.

2. **NLU Agent:**  
   Extracts task: `"generate_marketing_plan"`  
   Sends interpreted query to Planning Agent.

3. **Planning Agent:**  
   Breaks task into:
   - Market research
   - Competitor analysis
   - Target audience definition
   - Channel strategy
   - Budget outline  
   Sends `data_request` packet to Research Agent.

4. **Research Agent:**  
   Returns structured insights from relevant databases.

5. **Planning Agent:**  
   Sends structured subplan to Execution Agent.

6. **Execution Agent:**  
   Generates final document and returns it to UI Agent.

7. **Compliance Agent (optional):**  
   Reviews and signs off.

## Example Packet (Simplified)

```json
{
  "source": "planner-1",
  "destination": "exec-1",
  "type": "execution_command",
  "payload": {
    "task": "assemble_marketing_plan",
    "inputs": {
      "audience": "Tech-savvy professionals",
      "channels": ["Email", "LinkedIn", "YouTube"],
      "budget": "$5,000/month"
    }
  }
}
