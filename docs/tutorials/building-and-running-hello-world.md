# Building and Running the Hello World Agent

This tutorial will guide you through the process of building and running the "Hello, World!" agent example provided in the WorldLink Protocol repository. We will cover both the Python and JavaScript versions.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

* Python 3.7 or higher
* Node.js 14 or higher

## Running the Python Hello World Agent

1.  **Navigate to the Example Directory:** Open your terminal and navigate to the `examples/hello-world/` directory in your local copy of the WorldLink Protocol repository.

    ```bash
    cd examples/hello-world/
    ```

2.  **Examine the Code:** Open the `hello_world.py` file to see the code for the Python Hello World agent. It typically performs the following actions:
    * Connects to the WorldLink bus.
    * Registers itself with a specific agent ID and manifest.
    * Publishes a greeting message to a designated topic.
    * Disconnects from the bus.

3.  **Run the Agent:** Execute the Python script using the following command:

    ```bash
    python hello_world.py
    ```

    This will run the Hello World agent, and you should see output indicating that it has connected, registered, published a message, and disconnected.

## Running the JavaScript Hello World Agent

1.  **Navigate to the Example Directory:** Open your terminal and navigate to the `examples/hello-world/` directory in your local copy of the WorldLink Protocol repository.

    ```bash
    cd examples/hello-world/
    ```

2.  **Examine the Code:** Open the `hello_world.js` file to see the code for the JavaScript Hello World agent. Similar to the Python version, it typically:
    * Connects to the WorldLink bus.
    * Registers itself with an agent ID and manifest.
    * Publishes a greeting message to a topic.
    * Disconnects from the bus.

    You might need to install the `worldlink-client` dependency if you haven't already. You can do this by running:

    ```bash
    npm install worldlink-client
    ```

3.  **Run the Agent:** Execute the JavaScript file using Node.js with the following command:

    ```bash
    node hello_world.js
    ```

    This will run the Hello World agent, and you should see output indicating its actions.

## What to Expect

When you run either the Python or JavaScript Hello World agent, it will attempt to connect to a WorldLink bus (you might need a bus instance running for it to connect successfully in a real environment). The agent will then register itself and publish a simple greeting message. This example demonstrates the basic steps an agent takes to interact with the WorldLink Protocol.

This is a foundational tutorial. More advanced tutorials will cover other common use cases and features of the WorldLink Protocol in detail.