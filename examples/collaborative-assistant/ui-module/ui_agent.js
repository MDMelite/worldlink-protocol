const { Client } = require('worldlink-client');

async function main() {
    const client = new Client();
    await client.connect();

    const agentId = "ui_1";
    const manifest = {
        "name": "UI Agent",
        "version": "1.0.0",
        "description": "Captures the user's query.",
        "capabilities": ["capture_query"]
    };
    await client.registerAgent(agentId, manifest);
    console.log(`UI Agent '${agentId}' registered.`);

    await new Promise(resolve => setTimeout(resolve, 2000));

    const userQuery = "Can you generate a marketing plan for my AI-powered productivity app?";
    const topic = "user_query";
    const message = { query: userQuery };
    await client.publishMessage(topic, message, agentId);
    console.log(`UI Agent '${agentId}' published user query: '${userQuery}' to topic '${topic}'.`);

    await new Promise(resolve => setTimeout(resolve, 5000));
    await client.disconnect();
}

main();