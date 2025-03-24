# client-libraries/python/bus_client.py

import json

class Packet:
    def __init__(self, to, action, payload=None, sender=None, response_to=None):
        self.to = to
        self.action = action
        self.payload = payload or {}
        self.sender = sender
        self.response_to = response_to

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Packet(**data)

class BusClient:
    def __init__(self, bus_address="localhost:8080"):
        self.bus_address = bus_address
        self.handlers = {}

    def connect(self):
        print(f"Connecting to bus at: {self.bus_address}")
        # In a real implementation, this would establish a connection.
        pass

    def disconnect(self):
        print("Disconnecting from bus.")
        # In a real implementation, this would close the connection.
        pass

    def register_handler(self, action, handler_function):
        self.handlers[action] = handler_function

    def send(self, packet):
        print(f"Sending packet: {packet.to_json()} to {self.bus_address}")
        # In a real implementation, this would send the packet over the bus.
        pass

    def receive(self):
        # In a real implementation, this would listen for incoming packets.
        pass

    def spin_forever(self):
        # In a real implementation, this would keep the client running and listening for events.
        try:
            while True:
                # Simulate receiving a packet
                # For demonstration purposes, we'll just pass.
                pass
        except KeyboardInterrupt:
            print("Agent shutting down...")
            self.disconnect()

    def _handle_incoming_packet(self, json_str):
        packet = Packet.from_json(json_str)
        if packet.action in self.handlers:
            response = self.handlers[packet.action](packet.payload)
            if response:
                response_packet = Packet(
                    to=packet.sender,
                    response_to=packet.id, # Assuming a packet ID exists in a real scenario
                    payload=response
                )
                self.send(response_packet)
        else:
            print(f"No handler registered for action: {packet.action}")

if __name__ == "__main__":
    # Example usage
    client = BusClient()
    client.connect()

    def handle_greeting(payload):
        name = payload.get("name", "Guest")
        return {"message": f"Hello {name} from the Python agent!"}

    client.register_handler("greet", handle_greeting)

    example_packet = Packet(to="another_agent", action="greet", payload={"name": "Developer"})
    client.send(example_packet)

    client.spin_forever()