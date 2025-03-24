const { Client } = require('worldlink-client');

async function main() {
    const client = new Client();
    await client.connect();

    const agentId = "planner_1";
    const manifest = {
        "name": "Planning Agent",
        "version": "1.0.0",
        "description": "Breaks down the user's request into a series of subtasks.",
        "capabilities": ["create_plan"]
    };
    await client.registerAgent(agentId, manifest);
    console.log(`Planning Agent '${agentId}' registered.`);

    client.subscribe("intent_extracted", async (payload) => {
        const intent = payload.intent;
        if (intent) {
            const plan = [
                "Research target audience for AI productivity apps.",
                "Analyze competitor marketing strategies.",
                "Define key marketing messages and channels.",
                "Outline a timeline and budget.",
                "Draft the marketing plan document."
            ];
            const responseTopic = "plan_created";
            const responseMessage = { plan: plan, originalIntent: intent };
            await client.publishMessage(responseTopic, responseMessage, agentId);
            console.log(`Planning Agent '${agentId}' created a plan for intent: '${intent}' and published to '${responseTopic}'.`);
        }
    });

    await new Promise(resolve => setTimeout(resolve, 15000));
    await client.disconnect();
}

main();