# Quick Start Guide: Your First WorldLink Agent

Welcome to the WorldLink Protocol! This guide will walk you through the steps to create a simple agent and register it with the bus to send and receive messages.

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python:** Version 3.7 or higher (if you plan to use the Python SDK) - [Download Python](https://www.python.org/downloads/)
* **Node.js:** Version 14 or higher (if you plan to use the JavaScript SDK) - [Download Node.js](https://nodejs.org/en/download/)
* **pip:** Python package installer (should come with Python 3)
* **npm:** Node.js package manager (should come with Node.js)

You will also need a running instance of the WorldLink Protocol bus. If you don't have one set up, please refer to the documentation on setting up the bus.

## Install the WorldLink Client Library

Choose the SDK you want to use and install the client library:

### For Python:

```
pip install worldlink-client
```

### For JavaScript (Node.js):

```
npm install worldlink-client
```

## Create Your First Agent

Let's create a basic agent that can register with the bus, subscribe to a topic, and publish a message.

### For Python:

Create a file named `hello_agent.py`:

```python
from worldlink_client import BusClient
import time

def on_message(topic, payload):
    print(f"Received message on topic '{topic}': {payload}")

# Initialize the BusClient and connect to the WorldLink Protocol bus
bus = BusClient()
bus.connect("localhost:8080") # Replace with your Bus address if different

# Define a handler for messages received on the 'greeting' topic
@bus.subscribe("greeting")
def handle_greeting(payload):
    on_message("greeting", payload)

# Function to send a greeting message to a specific agent
def send_greeting(recipient_agent_id):
    bus.publish(f"agent.{recipient_agent_id}.greet", {"message": "Hello from my first WorldLink agent!"})

if __name__ == "__main__":
    # Define a unique identifier for your agent
    agent_id = "my_hello_agent"
    # Register the agent with the WorldLink Protocol bus
    bus.register_agent(agent_id)
    print(f"Agent '{agent_id}' registered.")

    # Example: Send a greeting to another agent (replace 'target_agent_id' with an actual agent ID)
    # target_agent_id = "another_agent"
    # send_greeting(target_agent_id)

    # Keep the agent running to receive messages
    try:
        while True:
            time.sleep(0.1) # Small delay to prevent busy-waiting
    except KeyboardInterrupt:
        print("Agent shutting down.")
    finally:
        bus.disconnect()
```

### For JavaScript (Node.js):

Create a file named `hello_agent.js`:

```javascript
const { BusClient } = require('worldlink-client');

// Initialize the BusClient and connect to the WorldLink Protocol bus
const bus = new BusClient();
bus.connect('localhost:8080'); // Replace with your Bus address if different

// Subscribe to the 'greeting' topic and define a message handler
bus.subscribe('greeting', (payload) => {
    console.log(`Received message on topic 'greeting': ${JSON.stringify(payload)}`);
});

// Function to send a greeting message to a specific agent
function sendGreeting(recipientAgentId) {
    bus.publish(`agent.${recipientAgentId}.greet`, { message: 'Hello from my first WorldLink agent!' });
}

const agentId = 'my_hello_agent';
// Register the agent with the WorldLink Protocol bus
bus.registerAgent(agentId);
console.log(`Agent '${agentId}' registered.`);

// Example: Send a greeting to another agent (replace 'targetAgentId' with an actual agent ID)
// const targetAgentId = 'another_agent';
// sendGreeting(targetAgentId);

// Keep the agent running
console.log('Agent is running...');
```

## Run Your Agent

Open a terminal and navigate to the directory where you saved your agent file (`hello_agent.py` or `hello_agent.js`).

### For Python:

```
python hello_agent.py
```

### For JavaScript (Node.js):

```
node hello_agent.js
```

You should see output indicating that your agent has registered with the bus.

## Sending and Receiving Messages

In the example code, there's a commented-out section that shows how to send a greeting to another agent. To see this in action, you would need to:

1. Run at least two instances of WorldLink agents (either two instances of the `hello_agent` or one instance of `hello_agent` and another agent). Make sure each agent has a unique `agent_id`.
2. Uncomment and modify the `target_agent_id` in one of the agent scripts to the `agent_id` of the other running agent.
3. Run the modified agent script.

You should then see the greeting message being printed in the terminal of the recipient agent. This demonstrates the basic publish/subscribe mechanism of the WorldLink Protocol. Agents can subscribe to specific topics to receive messages and publish messages to topics to send information to other interested agents.

## Next Steps

Congratulations! You've created and run your first WorldLink agent. This is just the beginning. Explore the rest of the documentation to learn about more advanced features of the WorldLink Protocol, such as different packet formats, security considerations, and building more complex collaborative agents.