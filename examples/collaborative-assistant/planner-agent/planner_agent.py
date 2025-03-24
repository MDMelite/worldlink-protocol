import asyncio
from worldlink_client import Client

async def main():
    client = Client()
    await client.connect()

    agent_id = "planner_1"
    manifest = {
        "name": "Planning Agent",
        "version": "1.0.0",
        "description": "Breaks down the user's request into a series of subtasks.",
        "capabilities": ["create_plan"]
    }
    await client.register_agent(agent_id, manifest)
    print(f"Planning Agent '{agent_id}' registered.")

    async def on_message(topic, payload):
        if topic == "intent_extracted":
            intent = payload.get("intent")
            if intent:
                plan = [
                    "Research target audience for AI productivity apps.",
                    "Analyze competitor marketing strategies.",
                    "Define key marketing messages and channels.",
                    "Outline a timeline and budget.",
                    "Draft the marketing plan document."
                ]
                response_topic = "plan_created"
                response_message = {"plan": plan, "original_intent": intent}
                await client.publish_message(response_topic, response_message, sender_id=agent_id)
                print(f"Planning Agent '{agent_id}' created a plan for intent: '{intent}' and published to '{response_topic}'.")

    client.subscribe("intent_extracted", on_message)

    await asyncio.sleep(15)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())