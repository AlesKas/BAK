import json

from utils.logger import initLogging
from .base import GetRequest, PutRequest, BaseException
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
            NtwUsers.select().where((NtwUsers.user_name == userName) & (NtwUsers.passw == passwd)).get()
        except DoesNotExist:
            raise BaseException(f"Username or password incorrect", 404)
        return 200

class CreateUser(PutRequest):
    
    @classmethod
    def handle_put(cls, **kwargs):
        data = str(kwargs).replace("\'", "\"")
        data = json.loads(data)
        data = data['body']
        password = data['password']
        user_name = data['userName']
        user_id = NtwUsers.select()
        user_id = user_id.count()
        try:
            NtwUsers.create(id= user_id+1,user_name=user_name, passw=password)
            return 200
        except Exception as exc:
            return 500, exc
        LOGGER.info(password)
        LOGGER.info(user_name)
        return 200