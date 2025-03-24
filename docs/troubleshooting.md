# Troubleshooting WorldLink Protocol

This document provides guidance on common issues that you might encounter while setting up or using the WorldLink Protocol and offers potential solutions or steps to resolve them.

## Setup and Installation Issues

### Python or Node.js Not Installed

**Problem:** The WorldLink client library requires either Python 3.7+ or Node.js 14+. If these are not installed, you will encounter errors during installation or when running agents. **Solution:** Ensure that you have the correct versions of Python or Node.js installed on your system. Refer to their official websites for installation instructions: [Download Python](https://www.python.org/downloads/) and [Download Node.js](https://nodejs.org/en/download/).

### Client Library Installation Errors

**Problem:** Errors might occur during the installation of the `worldlink-client` library using pip (for Python) or npm (for Node.js). **Solution:**
* **For Python:** Make sure you have pip installed and up-to-date. Try upgrading pip: `pip install --upgrade pip`. Then, try installing the client library again: `pip install worldlink-client`. Check your Python environment and ensure there are no conflicting packages.
* **For JavaScript (Node.js):** Ensure you have npm installed and that your Node.js version meets the requirements. Try clearing the npm cache: `npm cache clean --force` and then reinstalling the client library: `npm install worldlink-client`.

## Connection to the Bus

### Unable to Connect to `localhost:8080`

**Problem:** Agents might fail to connect to the WorldLink Protocol bus, often resulting in a "connection refused" error. The default address is usually `localhost:8080`. **Solution:**
* **Verify Bus is Running:** Ensure that the WorldLink Protocol bus server is running and accessible on the specified address and port.
* **Check Address and Port:** Double-check the bus address and port configured in your agent code. If the bus is running on a different address or port, update your agent's connection settings accordingly.
* **Firewall Issues:** A firewall on your system or network might be blocking the connection. Ensure that the necessary ports (typically 8080) are open for communication.

## Agent Registration Issues

### Agent ID Already Registered

**Problem:** When trying to register an agent, you might receive an error indicating that the `agent_id` is already in use. **Solution:** Each agent in the WorldLink network must have a unique `agent_id`. Choose a different, unique ID for the agent that is failing to register.

### Missing Agent Manifest

**Problem:** The bus might require an `agent.json` manifest file for registration. If this file is missing or not accessible, registration might fail. **Solution:** Ensure that an `agent.json` file exists in the same directory as your agent script (or in a location where the bus can access it) and that it contains valid JSON with the necessary information. Refer to the [Agent Manifest Reference](agent-manifest-reference.md) for the required fields.

## Message Publishing and Subscription Issues

### Messages Not Being Received

**Problem:** An agent might publish a message, but the intended recipient (another subscribed agent) does not receive it. **Solution:**
* **Verify Topic:** Ensure that the publisher and subscriber agents are using the exact same topic string (case-sensitive).
* **Check Subscription:** Confirm that the recipient agent has successfully subscribed to the correct topic. Check the agent's logs for subscription confirmation.
* **Bus Connectivity:** Verify that both agents are still connected to the WorldLink Protocol bus.
* **Message Filtering:** The bus or subscribing agents might have filtering mechanisms in place. Ensure that the message payload meets any filtering criteria.

### Errors During Publishing

**Problem:** An error might occur when an agent attempts to publish a message. **Solution:** Check the agent's logs for any error messages from the client library or the bus. Common issues include invalid topic names or malformed message payloads.

## General Debugging Tips

### Enable Logging

Most WorldLink client libraries provide options to enable detailed logging. This can be invaluable for diagnosing issues. Refer to the documentation of your specific client library for instructions on how to enable logging.

### Use Monitoring Tools

If available, use monitoring tools for the WorldLink Protocol bus to inspect agent registrations, active topics, and message flow. This can help identify if messages are being routed correctly.

### Check Agent Manifest Configuration

Ensure that the `agent.json` manifest file is correctly configured, especially the `agent_id`, `capabilities`, and `permissions`. Incorrect configurations can lead to unexpected behavior.

## Network Issues

### Firewall Blocking Connections

**Problem:** Firewalls can prevent agents from connecting to the bus or communicating with each other. **Solution:** Configure your firewall to allow traffic on the port used by the WorldLink Protocol bus (default is 8080) and any other ports used for inter-agent communication if applicable.

### DNS Resolution Issues

**Problem:** If you are using hostnames instead of IP addresses for the bus or other services, DNS resolution issues might prevent connections. **Solution:** Ensure that your system can correctly resolve the hostnames. Try using IP addresses directly to rule out DNS problems.

## Version Incompatibility

**Problem:** Using incompatible versions of the WorldLink Protocol bus and the client libraries can lead to errors and unexpected behavior. **Solution:** Ensure that you are using compatible versions of the bus and the client libraries. Refer to the release notes or compatibility documentation for the specific versions you are using.

## Contacting Support

If you encounter issues that you cannot resolve using this troubleshooting guide, please refer to the project's support channels (e.g., forums, mailing lists, issue trackers) for assistance. Provide detailed information about the problem you are facing, including any error messages or logs.