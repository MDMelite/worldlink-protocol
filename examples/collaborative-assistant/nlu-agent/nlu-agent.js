const { Client } = require('worldlink-client');

async function main() {
    const client = new Client();
    await client.connect();

    const agentId = "nlu_1";
    const manifest = {
        "name": "NLU Agent",
        "version": "1.0.0",
        "description": "Interprets the user's query and extracts the intent.",
        "capabilities": ["extract_intent"]
    };
    await client.registerAgent(agentId, manifest);
    console.log(`NLU Agent '${agentId}' registered.`);

    client.subscribe("user_query", async (payload) => {
        const query = payload.query;
        if (query) {
            const intent = `Generate a marketing plan for an AI-powered productivity app.`; // Simplified intent extraction
            const responseTopic = "intent_extracted";
            const responseMessage = { intent: intent, originalQuery: query };
            await client.publishMessage(responseTopic, responseMessage, agentId);
            console.log(`NLU Agent '${agentId}' extracted intent: '${intent}' from query: '${query}' and published to '${responseTopic}'.`);
        }
    });

    await new Promise(resolve => setTimeout(resolve, 10000));
    await client.disconnect();
}

main();