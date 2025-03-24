import asyncio
from worldlink_client import Client

async def main():
    client = Client()
    await client.connect()

    agent_id = "ui_1"
    manifest = {
        "name": "UI Agent",
        "version": "1.0.0",
        "description": "Captures the user's query.",
        "capabilities": ["capture_query"]
    }
    await client.register_agent(agent_id, manifest)
    print(f"UI Agent '{agent_id}' registered.")

    await asyncio.sleep(2)

    user_query = "Can you generate a marketing plan for my AI-powered productivity app?"
    topic = "user_query"
    message = {"query": user_query}
    await client.publish_message(topic, message, sender_id=agent_id)
    print(f"UI Agent '{agent_id}' published user query: '{user_query}' to topic '{topic}'.")

    await asyncio.sleep(5)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())