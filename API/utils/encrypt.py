from .logger import initLogging
from cryptography.fernet import Fernet

LOGGER = initLogging()

def encrypt_password(passwd: str) -> bytes:
    key = Fernet.generate_key()
    encryption_type = Fernet(key)
    encrypted_passwd = encryption_type.encrypt(passwd)
    LOGGER.info(encrypted_passwd)
    return encrypted_passwd