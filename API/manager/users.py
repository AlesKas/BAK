import os 

from utils.db import *
from utils.logger import initLogging
from .base import GetRequest, BaseException
from utils.db.db_util import DB
from utils.db.model import NtwUsers
from peewee import DoesNotExist

LOGGER = initLogging()

class Users(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        try:
            data = (NtwUsers.select())
        except ValueError:
            return 500
        response = {}
        for user in data:
            response[user.id] = user.user_name
        return response

class UserAuthentication(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        userName = kwargs['user_name']
        passwd = kwargs['user_passwd']
        try:
            data = NtwUsers.select().where((NtwUsers.user_name == userName) & (NtwUsers.passw == passwd)).get()
        except DoesNotExist:
            raise BaseException(f"Username or password incorrect", 404)
        return 200