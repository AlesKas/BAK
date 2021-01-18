import hashlib
from .logger import initLogging


def encrypt_string(input: str) -> bytes:
    has = hashlib.sha256(input.encode('utf-8')).hexdigest()
    return has

def decrypt_string(input: str) -> str:
    pass