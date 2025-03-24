import asyncio
from worldlink_client import Client

async def main():
    client = Client()
    await client.connect()

    agent_id = "nlu_1"
    manifest = {
        "name": "NLU Agent",
        "version": "1.0.0",
        "description": "Interprets the user's query and extracts the intent.",
        "capabilities": ["extract_intent"]
    }
    await client.register_agent(agent_id, manifest)
    print(f"NLU Agent '{agent_id}' registered.")

    async def on_message(topic, payload):
        if topic == "user_query":
            query = payload.get("query")
            if query:
                intent = f"Generate a marketing plan for an AI-powered productivity app." # Simplified intent extraction
                response_topic = "intent_extracted"
                response_message = {"intent": intent, "original_query": query}
                await client.publish_message(response_topic, response_message, sender_id=agent_id)
                print(f"NLU Agent '{agent_id}' extracted intent: '{intent}' from query: '{query}' and published to '{response_topic}'.")

    client.subscribe("user_query", on_message)

    await asyncio.sleep(10)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())