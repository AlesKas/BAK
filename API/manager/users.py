import json

from utils.db.model import NtwUsers
from utils.logger import initLogging
from utils.disk_util import create_user_folder
from peewee import DoesNotExist, IntegrityError
from .base import GetRequest, PostRequest, BaseException

LOGGER = initLogging()

class Users(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        currentUser = kwargs['user']
        try:
            data = (NtwUsers.select().where(NtwUsers.user_name != currentUser))
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

class CreateUser(PostRequest):
    
    @classmethod
    def handle_post(cls, **kwargs):
        data = str(kwargs).replace("\'", "\"")
        data = json.loads(data)
        data = data['body']
        password = data['password']
        user_name = data['userName']
        try:
            NtwUsers.create(user_name=user_name, passw=password)
            create_user_folder(user_name)
            return
        except IntegrityError:
            return cls.format_exc(f"Username is already taken", 409)
        except Exception as exc:
            return cls.format_exc(f"Unhandeled error: {exc}", 500)
        LOGGER.info(password)
        LOGGER.info(user_name)
        return