# WorldLink Protocol Bus API Reference

This document provides a detailed reference for the WorldLink Protocol bus API, which allows agents to interact with the central communication hub.

## Overview

The WorldLink Protocol bus facilitates communication between agents by providing a mechanism for registration, message publishing, and topic-based subscription. Agents interact with the bus using a defined set of API calls. While the specific implementation details might vary, the fundamental concepts remain consistent.

## API Endpoints

Agents communicate with the bus via a specific address (e.g., `localhost:8080`). The API primarily involves the following operations:

### Registering an Agent

Agents must register with the bus to participate in the WorldLink network. This typically involves sending a request with the agent's ID and other metadata defined in the `agent.json` manifest.

#### Endpoint

`/register`

#### Method

POST

#### Request Body (Example JSON)

```json
{
  "agent_id": "my_agent",
  "manifest": {
    "name": "My Agent",
    "version": "1.0.0",
    "capabilities": ["example"]
  }
}
```

#### Response (Example JSON - Success)

```json
{
  "status": "success",
  "message": "Agent registered successfully."
}
```

### Unregistering an Agent

Agents can unregister from the bus when they are no longer active.

#### Endpoint

`/unregister`

#### Method

POST

#### Request Body (Example JSON)

```json
{
  "agent_id": "my_agent"
}
```

#### Response (Example JSON - Success)

```json
{
  "status": "success",
  "message": "Agent unregistered successfully."
}
```

### Publishing a Message

Agents publish messages to specific topics. The bus then routes these messages to all subscribed agents.

#### Endpoint

`/publish`

#### Method

POST

#### Request Body (Example JSON)

```json
{
  "topic": "example.topic",
  "payload": {
    "data": "This is a message payload."
  },
  "sender_id": "my_agent"
}
```

#### Response (Example JSON - Success)

```json
{
  "status": "success",
  "message": "Message published."
}
```

### Subscribing to a Topic

Agents can subscribe to one or more topics to receive relevant messages.

#### Endpoint

`/subscribe`

#### Method

POST

#### Request Body (Example JSON)

```json
{
  "agent_id": "my_agent",
  "topic": "example.topic"
}
```

#### Response (Example JSON - Success)

```json
{
  "status": "success",
  "message": "Subscribed to topic 'example.topic'."
}
```

### Unsubscribing from a Topic

Agents can unsubscribe from topics they no longer wish to receive messages from.

#### Endpoint

`/unsubscribe`

#### Method

POST

#### Request Body (Example JSON)

```json
{
  "agent_id": "my_agent",
  "topic": "example.topic"
}
```

#### Response (Example JSON - Success)

```json
{
  "status": "success",
  "message": "Unsubscribed from topic 'example.topic'."
}
```

## Authentication and Authorization

Interactions with the bus API may require authentication and authorization. The specific mechanisms used will depend on the implementation of the WorldLink Protocol. This might involve API keys, tokens, or other security measures.

## Error Handling

The bus API will typically return error responses in case of issues, such as invalid requests, unauthorized access, or internal server errors. Error responses will usually include a status code and a descriptive message.

## Further Details

This document provides a high-level overview of the WorldLink Protocol bus API. For more detailed information on specific implementations, message formats, and security configurations, please refer to the implementation-specific documentation.