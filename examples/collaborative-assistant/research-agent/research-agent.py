import asyncio
from worldlink_client import Client

async def main():
    client = Client()
    await client.connect()

    agent_id = "data_1"
    manifest = {
        "name": "Research Agent",
        "version": "1.0.0",
        "description": "Gathers necessary data based on the planner's requests.",
        "capabilities": ["gather_data"]
    }
    await client.register_agent(agent_id, manifest)
    print(f"Research Agent '{agent_id}' registered.")

    async def on_message(topic, payload):
        if topic == "plan_created":
            plan = payload.get("plan")
            if plan:
                research_data = {}
                for task in plan:
                    research_data[task] = f"Research data for '{task}'." # Simulated research data
                response_topic = "research_data_gathered"
                response_message = {"research_data": research_data, "original_plan": plan}
                await client.publish_message(response_topic, response_message, sender_id=agent_id)
                print(f"Research Agent '{agent_id}' gathered data for plan and published to '{response_topic}'.")

    client.subscribe("plan_created", on_message)

    await asyncio.sleep(20)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())