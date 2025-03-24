# Tooling - Certificate Generator

This document outlines the purpose and conceptual usage of a tool designed to generate Agent Certificates within the WorldLink Protocol. Agent Certificates are crucial for establishing trust and verifying the identity of agents participating in the protocol.

## Purpose of Agent Certificates

Agent Certificates serve several key purposes within the WorldLink Protocol:

* **Identity Verification:** They provide a cryptographically verifiable way to identify an agent.
* **Authentication:** They allow the Bus Arbiter and other agents to authenticate the identity of a connecting agent.
* **Authorization:** Certificates can contain information about an agent's capabilities and trust level, which can be used to determine what actions the agent is authorized to perform.
* **Secure Communication:** Certificates can be used to establish secure, encrypted communication channels between agents.

## Conceptual Usage

While the actual implementation of the certificate generation tool may vary, the general process would likely involve the following steps:

1.  **Prerequisites:** Ensure you have the necessary software installed, such as Python and potentially cryptographic libraries.
2.  **Running the Tool:** Execute the certificate generation script. This might be done via a command-line interface.
3.  **Providing Agent Information:** The tool would likely prompt you to provide essential information about the agent for which the certificate is being generated. This would typically include:
    * **Agent ID:** A unique identifier for the agent.
    * **Public Key:** The public key associated with the agent's private key. This is crucial for cryptographic operations.
    * **Validity Period:** The duration for which the certificate will be valid (e.g., in days or years).
    * **Optional Metadata:** Depending on the implementation, you might be able to include other metadata such as the agent's capabilities or trust level.
4.  **Certificate Authority (CA) Interaction:** In a real-world scenario, the tool would likely communicate with a designated Certificate Authority (potentially the Bus Arbiter or a separate service). The CA would sign the certificate, verifying its authenticity.
5.  **Output:** The tool would generate the Agent Certificate, typically in a standard format such as X.509. This certificate file would then need to be securely stored and used by the agent for identification and authentication.

## Placeholder Script (Conceptual - Not Executable)

```python
# tools/certgen/generate_certificate.py (Conceptual)

import datetime
import uuid

class AgentCertificate:
    def __init__(self, agent_id, public_key, expiry_date, serial_number, signature):
        self.agent_id = agent_id
        self.public_key = public_key
        self.expiry_date = expiry_date
        self.serial_number = serial_number
        self.signature = signature

    def __str__(self):
        return f"Agent ID: {self.agent_id}\nSerial: {self.serial_number}\nPublic Key: {self.public_key[:20]}...\nExpires: {self.expiry_date}\nSignature: {self.signature[:30]}..."

def issue_certificate(agent_id, public_key, ca_private_key, validity_days=365):
    today = datetime.date.today()
    expiry = today + datetime.timedelta(days=validity_days)
    serial = uuid.uuid4()
    # In a real system, the CA would use its private key to sign the certificate data
    signature_data = f"{agent_id}-{public_key}-{expiry}-{serial}"
    signature = _sign_data(signature_data, ca_private_key)
    certificate = AgentCertificate(agent_id, public_key, expiry, serial, signature)
    return certificate

def _sign_data(data, private_key):
    # This is a placeholder for a real cryptographic signing function
    return "SIGNED_" + str(uuid.uuid4()) + "_WITH_" + private_key[:10] + "..."

if __name__ == "__main__":
    # Example usage (conceptual)
    ca_private_key = "MOCK_CA_PRIVATE_KEY_" + str(uuid.uuid4()) # In a real system, this would be securely managed
    agent_id = "example_agent"
    public_key = "MOCK_PUBLIC_KEY_FOR_" + agent_id + "_" + str(uuid.uuid4())
    certificate = issue_certificate(agent_id, public_key, ca_private_key)
    print("--- Mock Agent Certificate Issued ---")
    print(certificate)