import asyncio
from worldlink_client import Client

async def main():
    client = Client()
    await client.connect()

    agent_id = "compliance_1"
    manifest = {
        "name": "Compliance Agent",
        "version": "1.0.0",
        "description": "Performs a quality assurance check on the output.",
        "capabilities": ["check_quality"]
    }
    await client.register_agent(agent_id, manifest)
    print(f"Compliance Agent '{agent_id}' registered.")

    async def on_message(topic, payload):
        if topic == "marketing_plan_generated":
            marketing_plan = payload.get("marketing_plan")
            if marketing_plan:
                quality_check_result = "Marketing plan looks good." # Simplified quality check
                response_topic = "marketing_plan_reviewed"
                response_message = {"quality_check": quality_check_result, "marketing_plan": marketing_plan}
                await client.publish_message(response_topic, response_message, sender_id=agent_id)
                print(f"Compliance Agent '{agent_id}' reviewed marketing plan and published result to '{response_topic}'.")

    client.subscribe("marketing_plan_generated", on_message)

    await asyncio.sleep(30)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())