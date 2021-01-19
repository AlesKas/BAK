import json

from utils.logger import initLogging
from .base import GetRequest, BaseException
from utils.db.model import NtwSalt
from peewee import DoesNotExist

LOGGER = initLogging()

class Salt(GetRequest):
    
    @classmethod
    def handle_get(cls, **kwargs):
        salt = NtwSalt.get().salt
        response = {}
        response['salt'] = salt
        return response