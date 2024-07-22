import uuid
import hashlib


def create_uuid():
    return uuid.uuid4().hex


def str_to_uuid(input_string, namespace=uuid.NAMESPACE_URL):
    # Generate a UUID based on the SHA-1 hash of the namespace UUID and name
    hash_value = hashlib.sha1(namespace.bytes + input_string.encode("utf-8")).digest()

    # Create a UUID using the first 16 bytes of the hash
    raw_uuid = uuid.UUID(bytes=hash_value[:16], version=5)

    # Convert the UUID to a 32-character hexadecimal string
    return raw_uuid.hex
