from .base import PutRequest, GetRequest

class FilePutHandler(PutRequest):

    @classmethod
    def handle_put(cls, **kwargs):
        return 200

class FileGetHandler(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        return 200