import os
import json

from utils.db.model import Share
from utils.logger import initLogging
from utils.disk_util import DISK_PATH
from .base import GetRequest, PutRequest

LOGGER = initLogging()

class ListSharedFiles(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        response = {}
        response["data"] = []
        user = kwargs["user"]
        query = Share.select().where(Share.to_user == user)
        for item in query:
            fileResp = {}
            file = DISK_PATH + item.from_user + "/" + item.file_name
            base = os.path.basename(file)
            fileName, fileType = os.path.splitext(base)
            fileResp["fileName"] = fileName
            fileResp["fromUser"] = item.from_user
            if fileType == "":
                fileResp["fileType"] = ""
            else:
                fileResp["fileType"] = fileType[1:]
            response["data"].append(fileResp)
        response["data"] = sorted(response["data"], key=lambda k: k["fileType"])
        return response


#TODO: List shared files from specifis user in specific directory.

class ShareFile(PutRequest):

    @classmethod
    def handle_put(cls, **kwargs):
        fromUser = kwargs["user"]
        toUser = kwargs["toUser"]
        sharedDir = kwargs["directory"]
        fileName = kwargs["fileName"]

        # if os.path.isdir(DISK_PATH + fromUser + sharedDir + fileName):
        #     sharedDir += fileName
        #     Share.create(from_user=fromUser, to_user=toUser, directory=sharedDir, file_name=None)
        # else:
        Share.create(from_user=fromUser, to_user=toUser, directory=sharedDir, file_name=fileName)