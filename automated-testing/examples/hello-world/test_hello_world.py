import unittest
from unittest.mock import MagicMock
import asyncio
from examples.hello_world.hello_world import main  # Assuming your hello_world.py is in examples/hello_world/

class TestHelloWorldAgent(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        # Mock the worldlink_client to avoid actual bus interaction
        self.mock_client = MagicMock()
        self.mock_client.connect = MagicMock(return_value=asyncio.Future())
        self.mock_client.connect().set_result(None)
        self.mock_client.register_agent = MagicMock(return_value=asyncio.Future())
        self.mock_client.register_agent().set_result(None)
        self.mock_client.publish_message = MagicMock(return_value=asyncio.Future())
        self.mock_client.publish_message().set_result(None)
        self.mock_client.disconnect = MagicMock(return_value=asyncio.Future())
        self.mock_client.disconnect().set_result(None)

        # Patch the Client class in your module with the mock
        from examples.hello_world import hello_world
        hello_world.Client = MagicMock(return_value=self.mock_client)

    async def test_agent_registers(self):
        await main()
        self.mock_client.register_agent.assert_called_once()
        args, _ = self.mock_client.register_agent.call_args
        self.assertEqual(args[0], "hello_world_python")
        self.assertEqual(args[1]["name"], "Hello World Agent (Python)")

    async def test_agent_publishes_greeting(self):
        await main()
        # Check if publish_message was called with the correct topic and message
        expected_topic = "greeting"
        expected_message = {"text": "Hello from Python!"}
        published = False
        for call in self.mock_client.publish_message.mock_calls:
            args, _ = call
            if args[0] == expected_topic and args[1] == expected_message:
                published = True
                break
        self.assertTrue(published, f"Message not published to '{expected_topic}' with content: {expected_message}")

if __name__ == '__main__':
    unittest.main()