import os
import json

from utils.db.model import Share, NtwUsers
from utils.logger import initLogging
from utils.disk_util import DISK_PATH
from .base import GetRequest, PostRequest

LOGGER = initLogging()

class ListSharedFiles(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        response = {}
        response["data"] = []
        toUser = kwargs["user"]
        toUser = NtwUsers.get(NtwUsers.user_name == toUser).id
        query = Share.select().where(Share.to_user == toUser)
        for item in query:
            fileResp = {}
            workspace = DISK_PATH + item.from_user.user_name + "/"
            file = workspace + item.file_name
            base = os.path.basename(file)
            fileName, fileType = os.path.splitext(base)
            fileResp["fileName"] = fileName
            fileResp["fromUser"] = item.from_user.user_name
            if fileType == "":
                fileResp["fileType"] = ""
                fileResp["isDir"] = True
            else:
                fileResp["fileType"] = fileType[1:]
                fileResp["isDir"] = False
            response["data"].append(fileResp)
        response["data"] = sorted(response["data"], key=lambda k: k["fileType"])
        return response


class ListSharedUsers(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        toUser = kwargs["user"]
        response = {}
        response["data"] = []
        toUser = NtwUsers.get(NtwUsers.user_name == toUser).id
        query = Share.select().distinct().where(Share.to_user == toUser)
        for user in query:
            sharedUser = NtwUsers.get(NtwUsers.id == user.from_user)
            if sharedUser.user_name not in response["data"]:
                response["data"].append(sharedUser.user_name)
        return response


class ShareFile(PostRequest):

    @classmethod
    def handle_post(cls, **kwargs):
        fromUser = kwargs["user"]
        toUser = kwargs["toUser"]
        sharedDir = kwargs["directory"]
        fileName = kwargs["fileName"]
        fromUser = NtwUsers.get(NtwUsers.user_name == fromUser).id
        toUser = NtwUsers.get(NtwUsers.user_name == toUser).id
        Share.create(from_user=fromUser, to_user=toUser, directory=sharedDir, file_name=fileName)