import os 

from utils.db import *
from utils.logger import initLogging
from .base import GetRequest
from utils.db.db_util import DB
from peewee import DoesNotExist
from utils.db.model import NtwUsers

LOGGER = initLogging()

class Users(GetRequest):

    @classmethod
    def handle_get(cls):
        try:
            data = NtwUsers.select("*")
            LOGGER.info(data)
        except DoesNotExist:
            return 404
        response = {}
        for user in data:
            LOGGER.info(user.id)
            response[user.id] = {}
            for key, val in user:
                response[user.id][key] = val
        return response