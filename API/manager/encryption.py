from .base import GetRequest
from utils.encrypt import encrypt_password

class Encryption(GetRequest):
    @classmethod
    def handle_get(cls, **kwargs):
        passwd = kwargs['string_arg']
        passwd = encrypt_password(passwd)
        return str(passwd), 200