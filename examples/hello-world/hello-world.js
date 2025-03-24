const { Client } = require('worldlink-client');

async function main() {
    const client = new Client();
    await client.connect();

    const agentId = "hello_world_javascript";
    const manifest = {
        "name": "Hello World Agent (JavaScript)",
        "version": "1.0.0",
        "description": "A simple agent that says hello.",
        "capabilities": ["say_hello"]
    };
    await client.registerAgent(agentId, manifest);
    console.log(`JavaScript agent '${agentId}' registered.`);

    await new Promise(resolve => setTimeout(resolve, 2000)); // Give time for registration

    const topic = "greeting";
    const message = { text: "Hello from JavaScript!" };
    await client.publishMessage(topic, message, agentId);
    console.log(`JavaScript agent '${agentId}' published to topic '${topic}':`, message);

    await new Promise(resolve => setTimeout(resolve, 5000));
    await client.disconnect();
}

main();