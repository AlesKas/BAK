from .base import GetRequest
from utils.encrypt import encrypt_password

class Encryption(GetRequest):
    @classmethod
    def handle_get(cls):
        return 200