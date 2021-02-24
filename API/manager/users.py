import json
import peewee

from utils.logger import initLogging
from .base import GetRequest, PutRequest, BaseException
from utils.db.model import NtwUsers
from peewee import DoesNotExist, IntegrityError

LOGGER = initLogging()

class Users(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        try:
            data = (NtwUsers.select())
        except ValueError:
            raise Exception
        response = {}
        response["data"] = []
        for user in data:
            response["data"].append(user.user_name)
        return response

class UserAuthentication(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        userName = kwargs['user_name']
        passwd = kwargs['user_passwd']
        try:
            NtwUsers.select().where((NtwUsers.user_name == userName) & (NtwUsers.passw == passwd)).get()
        except DoesNotExist:
            return cls.format_exc("Username or password incorrect", 404)
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
            return
        except peewee.IntegrityError:
            return cls.format_exc(f"Username is already taken", 409)
        except Exception as exc:
            return cls.format_exc(f"Unhandeled error: {exc}", 500)
        LOGGER.info(password)
        LOGGER.info(user_name)
        return