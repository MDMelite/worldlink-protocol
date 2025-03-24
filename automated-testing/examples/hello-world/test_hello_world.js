const assert = require('assert');
const { Client } = require('worldlink-client'); // Assuming worldlink-client is installed
const helloWorld = require('../../../examples/hello-world/hello_world.js'); // Adjust path if necessary

// Mock the Client class
jest.mock('worldlink-client', () => {
    const mockClient = {
        connect: jest.fn().mockResolvedValue(),
        registerAgent: jest.fn().mockResolvedValue(),
        publishMessage: jest.fn().mockResolvedValue(),
        disconnect: jest.fn().mockResolvedValue(),
    };
    return { Client: jest.fn(() => mockClient) };
});

describe('HelloWorldAgent (JavaScript)', () => {
    let client;

    beforeEach(() => {
        // Reset the mock before each test
        Client.mockClear();
        client = new Client();
    });

    test('agent registers', async () => {
        await helloWorld.main();
        expect(client.registerAgent).toHaveBeenCalledTimes(1);
        const [agentId, manifest] = client.registerAgent.mock.calls[0];
        expect(agentId).toBe('hello_world_js');
        expect(manifest.name).toBe('Hello World Agent (JavaScript)');
    });

    test('agent publishes greeting', async () => {
        await helloWorld.main();
        expect(client.publishMessage).toHaveBeenCalledTimes(1);
        const [topic, message, senderId] = client.publishMessage.mock.calls[0];
        expect(topic).toBe('greeting');
        expect(message).toEqual({ text: 'Hello from JavaScript!' });
        expect(senderId).toBe('hello_world_js');
    });
});