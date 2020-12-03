import os 

from utils.db import *
from utils.logger import initLogging
from .base import GetRequest
from utils.db.db_util import DB
from peewee import DoesNotExist
from utils.db.model import NtwUsers
from utils.db.database_handler import DatabasePoolConnection

LOGGER = initLogging()

class Users(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        try:
            data = (NtwUsers.select())
        except DoesNotExist:
            return 404
        response = {}
        for user in data:
            response[user.id] = user.user_name
        return response

class UserDetail(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        user_id = kwargs['user_id']
        LOGGER.info(user_id)
        try:
            data = NtwUsers.select().where(NtwUsers.id == user_id).get()
        except DoesNotExist:
            return 404
        response = {}
        response[user_id] = data.user_name
        return response