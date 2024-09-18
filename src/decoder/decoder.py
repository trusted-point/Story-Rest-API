import base64
from protobuf.src.cosmospy_protobuf.cosmos.crypto.ed25519.keys_pb2 import PubKey as Ed25519PubKey
from protobuf.src.cosmospy_protobuf.cosmos.crypto.secp256k1.keys_pb2 import PubKey as Secp256k1PubKey
from google.protobuf.any_pb2 import Any

def decode_consensus_pubkey(any_pubkey: Any) -> str:
    """
    Decode a public key from its serialized form based on the `type_url` and return it as a Base64-encoded string.

    Args:
        any_pubkey (Any): The serialized public key in protobuf Any format.
        
    Returns:
        str: The Base64-encoded public key.

    Raises:
        ValueError: If the `type_url` is unknown or the public key cannot be deserialized.
    """
    if any_pubkey.type_url == "/cosmos.crypto.ed25519.PubKey":
        pubkey = Ed25519PubKey()
        pubkey.ParseFromString(any_pubkey.value)
        pubkey_bytes = pubkey.key
        return base64.b64encode(pubkey_bytes).decode('utf-8')
    
    elif any_pubkey.type_url == "/cosmos.crypto.secp256k1.PubKey":
        pubkey = Secp256k1PubKey()
        pubkey.ParseFromString(any_pubkey.value)
        pubkey_bytes = pubkey.key
        return base64.b64encode(pubkey_bytes).decode('utf-8')
    
    else:
        raise ValueError(f"Unknown consensus pubkey type: {any_pubkey.type_url}")