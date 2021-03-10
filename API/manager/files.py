import os
import connexion

from utils.logger import initLogging
from utils.disk_util import DISK_PATH
from flask import send_from_directory, make_response
from .base import PutRequest, GetRequest, DeleteRequest

LOGGER = initLogging()

class FilePutHandler(PutRequest):

    @classmethod
    def handle_put(cls, **kwargs):
        filePath = DISK_PATH + kwargs["user"]
        file = kwargs["fileName"]
        file.save(os.path.join(filePath, file.filename))
        return 200

class FileGetHandler(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        response = {}
        response["data"] = []
        currentUser = kwargs["user"]
        userWorkspace = DISK_PATH + currentUser
        for file in os.listdir(userWorkspace):
            fileResp = {}
            base = os.path.basename(file)
            fileName, fileType = os.path.splitext(base)
            fileResp["fileName"] = fileName
            if fileType == "":
                fileResp["fileType"] = ""
            else:
                fileResp["fileType"] = fileType[1:]
            response["data"].append(fileResp)

        response["data"] = sorted(response["data"], key=lambda k: k["fileType"])
        return response

class FileGetHandlerDownload(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        fileName = kwargs["fileName"]
        currentUser = kwargs["user"]
        userWorkspace = DISK_PATH + currentUser + "/"
        response = make_response(send_from_directory(userWorkspace, fileName, as_attachment=True))
        response.direct_passthrough = False
        return response

class FileDeleteHandler(DeleteRequest):

    @classmethod
    def handle_delete(cls, **kwargs):
        LOGGER.info("DELETE")