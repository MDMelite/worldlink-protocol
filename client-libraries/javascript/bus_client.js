// client-libraries/javascript/bus_client.js

class Packet {
    constructor(to, action, payload = null, sender = null, responseTo = null) {
      this.to = to;
      this.action = action;
      this.payload = payload || {};
      this.sender = sender;
      this.responseTo = responseTo;
    }
  
    toJson() {
      return JSON.stringify(this);
    }
  
    static fromJson(jsonStr) {
      const data = JSON.parse(jsonStr);
      return new Packet(data.to, data.action, data.payload, data.sender, data.responseTo);
    }
  }
  
  class BusClient {
    constructor(busAddress = "localhost:8080") {
      this.busAddress = busAddress;
      this.handlers = {};
    }
  
    connect() {
      console.log(`Connecting to bus at: ${this.busAddress}`);
      // In a real implementation, this would establish a connection.
    }
  
    disconnect() {
      console.log("Disconnecting from bus.");
      // In a real implementation, this would close the connection.
    }
  
    registerHandler(action, handlerFunction) {
      this.handlers[action] = handlerFunction;
    }
  
    send(packet) {
      console.log(`Sending packet: ${packet.toJson()} to ${this.busAddress}`);
      // In a real implementation, this would send the packet over the bus.
    }
  
    receive() {
      // In a real implementation, this would listen for incoming packets.
    }
  
    spinForever() {
      // In a real implementation, this would keep the client running and listening for events.
      console.log("JavaScript Agent is running...");
      // For demonstration purposes, we'll simulate a shutdown after a short delay.
      setTimeout(() => {
        this.disconnect();
      }, 5000);
    }
  
    _handleIncomingPacket(jsonStr) {
      const packet = Packet.fromJson(jsonStr);
      if (packet.action in this.handlers) {
        const response = this.handlers[packet.action](packet.payload);
        if (response) {
          const responsePacket = new Packet(
            packet.sender,
            "response", // Assuming a generic 'response' action for simplicity
            response,
            null,
            packet.id // Assuming a packet ID exists in a real scenario
          );
          this.send(responsePacket);
        }
      } else {
        console.log(`No handler registered for action: ${packet.action}`);
      }
    }
  }
  
  // Example usage (can be uncommented for testing later)
  /*
  const client = new BusClient();
  client.connect();
  
  function handleGreeting(payload) {
    const name = payload.name || "Guest";
    return { message: `Hello ${name} from the JavaScript agent!` };
  }
  
  client.registerHandler("greet", handleGreeting);
  
  const examplePacket = new Packet("another_agent", "greet", { name: "Developer" });
  client.send(examplePacket);
  
  client.spinForever();
  */