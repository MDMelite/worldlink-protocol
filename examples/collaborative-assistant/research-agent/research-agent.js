const { Client } = require('worldlink-client');

async function main() {
    const client = new Client();
    await client.connect();

    const agentId = "data_1";
    const manifest = {
        "name": "Research Agent",
        "version": "1.0.0",
        "description": "Gathers necessary data based on the planner's requests.",
        "capabilities": ["gather_data"]
    };
    await client.registerAgent(agentId, manifest);
    console.log(`Research Agent '${agentId}' registered.`);

    client.subscribe("plan_created", async (payload) => {
        const plan = payload.plan;
        if (plan) {
            const researchData = {};
            for (const task of plan) {
                researchData[task] = `Research data for '${task}'.`; // Simulated research data
            }
            const responseTopic = "research_data_gathered";
            const responseMessage = { researchData: researchData, originalPlan: plan };
            await client.publishMessage(responseTopic, responseMessage, agentId);
            console.log(`Research Agent '${agentId}' gathered data for plan and published to '${responseTopic}'.`);
        }
    });

    await new Promise(resolve => setTimeout(resolve, 20000));
    await client.disconnect();
}

main();