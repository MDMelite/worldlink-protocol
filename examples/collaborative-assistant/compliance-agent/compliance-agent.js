const { Client } = require('worldlink-client');

async function main() {
    const client = new Client();
    await client.connect();

    const agentId = "compliance_1";
    const manifest = {
        "name": "Compliance Agent",
        "version": "1.0.0",
        "description": "Performs a quality assurance check on the output.",
        "capabilities": ["check_quality"]
    };
    await client.registerAgent(agentId, manifest);
    console.log(`Compliance Agent '${agentId}' registered.`);

    client.subscribe("marketing_plan_generated", async (payload) => {
        const marketingPlan = payload.marketingPlan;
        if (marketingPlan) {
            const qualityCheckResult = "Marketing plan looks good."; // Simplified quality check
            const responseTopic = "marketing_plan_reviewed";
            const responseMessage = { qualityCheck: qualityCheckResult, marketingPlan: marketingPlan };
            await client.publishMessage(responseTopic, responseMessage, agentId);
            console.log(`Compliance Agent '${agentId}' reviewed marketing plan and published result to '${responseTopic}'.`);
        }
    });

    await new Promise(resolve => setTimeout(resolve, 30000));
    await client.disconnect();
}

main();