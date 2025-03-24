# Deployment Guide for WorldLink Protocol

This guide provides instructions on how to deploy and run the WorldLink Protocol components, focusing on the Python-based reference implementation of the WorldLink Bus.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

* Python 3.7 or higher
* pip (Python package installer)
* Node.js 14 or higher (if you intend to run the JavaScript Hello World agent)

## Step 1: Running the WorldLink Bus (Python Reference Implementation)

The reference implementation of the WorldLink Bus is a Python-based HTTP microservice. Here's how to set it up and run:

1.  **Navigate to the Bus Directory:** Open your terminal and navigate to the directory where the `bus_server.py` script (or similar entrypoint for your bus implementation) is located. This might be a `bus/` directory in your repository.

    ```bash
    cd bus/
    ```

2.  **Install Dependencies:** The bus depends on a lightweight HTTP server library. You will need to install either Flask or FastAPI (and optionally uvicorn if using FastAPI).

    * **Using Flask:**

        ```bash
        pip install Flask
        ```

    * **Using FastAPI (and uvicorn):**

        ```bash
        pip install fastapi uvicorn
        ```

3.  **Run the Bus:** Execute the `bus_server.py` script using the Python interpreter:

    ```bash
    python bus_server.py
    ```

    Refer to the specific instructions or documentation for your WorldLink Bus implementation for the exact command if `bus_server.py` is not the correct entry point.

4.  **Agent Manifest Files:** The bus loads agent manifest files (`agent.json`) when agents register. Ensure these files are accessible to the bus.

5.  **Configuration:** The bus might have some configuration options, such as the port it listens on or logging settings. These might be configured through a `.env` file in the bus directory or as inline variables within the `bus_server.py` script. Check your bus implementation for specific configuration details. The default port is likely to be `8080`.

6.  **Verify the Bus is Running:** You should see output in the terminal indicating that the WorldLink Bus has started successfully and is listening for HTTP requests, likely on `http://localhost:8080` by default.

## Step 2: Deploying and Running Agents

Once the WorldLink Bus is running, you can deploy and run your agents.

1.  **Navigate to the Agent Directory:** Open a new terminal window (or tab) for each agent you want to run. Navigate to the directory containing the agent's code. For example, for the Hello World agent:

    ```bash
    cd examples/hello-world/
    ```

2.  **Run the Agent:** Execute the command to start the agent.

    * **For Python:** Ensure you have the `worldlink-client` library installed (if it's a separate dependency). Then run:

        ```bash
        python hello_world.py
        ```

    * **For JavaScript:** Ensure you have installed the dependencies (e.g., `worldlink-client`) using `npm install`. Then run:

        ```bash
        node hello_world.js
        ```

3.  **Agent Configuration:** Ensure that the agent's code specifies the correct address of the WorldLink Bus. For the Python reference implementation, this will likely be an HTTP address like `http://localhost:8080`. For WebSocket implementations (if you have any agents using that), it might be `ws://localhost:8080`.

4.  **Verify Agent Connection:** You should see output in the agent's terminal indicating that it has connected to the WorldLink Bus and registered itself.

## Next Steps

This guide covered the basic deployment of the Python reference implementation of the WorldLink Bus and running agents. More advanced deployment scenarios might involve:

* **Containerization:** Using tools like Docker to package the bus and agents for easier deployment and management.
* **Cloud Platforms:** Deploying the WorldLink Bus and agents on cloud infrastructure.
* **Advanced Configuration:** Exploring more complex configuration options for the bus and agents.
* **Security Considerations:** Implementing security measures for your WorldLink Protocol deployment.
* **Monitoring and Logging:** Setting up systems to monitor the health and performance of the deployed components.

Please create this file in the `deployment/` directory. After you have done so, we can proceed to the next item on our QA checklist.