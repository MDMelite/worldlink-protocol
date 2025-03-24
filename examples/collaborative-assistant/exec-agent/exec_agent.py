import asyncio
from worldlink_client import Client

async def main():
    client = Client()
    await client.connect()

    agent_id = "exec_1"
    manifest = {
        "name": "Execution Agent",
        "version": "1.0.0",
        "description": "Executes the subtasks and formats the final output.",
        "capabilities": ["execute_plan"]
    }
    await client.register_agent(agent_id, manifest)
    print(f"Execution Agent '{agent_id}' registered.")

    async def on_message(topic, payload):
        if topic == "research_data_gathered":
            research_data = payload.get("research_data")
            if research_data:
                marketing_plan = "## Marketing Plan for AI-Powered Productivity App\n\n"
                for task, data in research_data.items():
                    marketing_plan += f"### {task}\n{data}\n\n"
                response_topic = "marketing_plan_generated"
                response_message = {"marketing_plan": marketing_plan}
                await client.publish_message(response_topic, response_message, sender_id=agent_id)
                print(f"Execution Agent '{agent_id}' generated marketing plan and published to '{response_topic}'.")

    client.subscribe("research_data_gathered", on_message)

    await asyncio.sleep(25)
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())