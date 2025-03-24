import asyncio
from worldlink_client import Client

async def main():
    client = Client()
    await client.connect()

    agent_id = "hello_world_python"
    manifest = {
        "name": "Hello World Agent (Python)",
        "version": "1.0.0",
        "description": "A simple agent that says hello.",
        "capabilities": ["say_hello"]
    }
    await client.register_agent(agent_id, manifest)
    print(f"Python agent '{agent_id}' registered.")

    await asyncio.sleep(2)  # Give time for registration

    topic = "greeting"
    message = {"text": "Hello from Python!"}
    await client.publish_message(topic, message, sender_id=agent_id)
    print(f"Python agent '{agent_id}' published to topic '{topic}': {message}")

    await asyncio.sleep(5)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())