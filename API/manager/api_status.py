from .base import GetRequest

class ApiStatus(GetRequest):

    @classmethod
    def handle_get(cls):
        return 200