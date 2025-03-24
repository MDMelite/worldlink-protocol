const { Client } = require('worldlink-client');

async function main() {
    const client = new Client();
    await client.connect();

    const agentId = "exec_1";
    const manifest = {
        "name": "Execution Agent",
        "version": "1.0.0",
        "description": "Executes the subtasks and formats the final output.",
        "capabilities": ["execute_plan"]
    };
    await client.registerAgent(agentId, manifest);
    console.log(`Execution Agent '${agentId}' registered.`);

    client.subscribe("research_data_gathered", async (payload) => {
        const researchData = payload.researchData;
        if (researchData) {
            let marketingPlan = "## Marketing Plan for AI-Powered Productivity App\n\n";
            for (const task in researchData) {
                marketingPlan += `### ${task}\n${researchData[task]}\n\n`;
            }
            const responseTopic = "marketing_plan_generated";
            const responseMessage = { marketingPlan: marketingPlan };
            await client.publishMessage(responseTopic, responseMessage, agentId);
            console.log(`Execution Agent '${agentId}' generated marketing plan and published to '${responseTopic}'.`);
        }
    });

    await new Promise(resolve => setTimeout(resolve, 25000));
    await client.disconnect();
}

main();