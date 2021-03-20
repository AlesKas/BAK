import os
import shutil

from PIL import Image
from utils.logger import initLogging
from utils.disk_util import DISK_PATH
from flask import send_from_directory, make_response
from .base import PutRequest, GetRequest, DeleteRequest

LOGGER = initLogging()

class FilePutHandler(PutRequest):

    @classmethod
    def handle_put(cls, **kwargs):
        filePath = DISK_PATH + kwargs["user"] + kwargs["directory"]
        file = kwargs["fileName"]
        file.save(os.path.join(filePath, file.filename))
        return 200

class FileGetHandler(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        response = {}
        response["data"] = []
        currentUser = kwargs["user"]
        directory = kwargs["directory"]
        userWorkspace = DISK_PATH + currentUser + directory
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
        userWorkspace = DISK_PATH + currentUser + kwargs["directory"]
        response = make_response(send_from_directory(userWorkspace, fileName, as_attachment=True))
        response.direct_passthrough = False
        return response

class FileDeleteHandler(DeleteRequest):

    @classmethod
    def handle_delete(cls, **kwargs):
        userName = kwargs["user"]
        fileName = kwargs["fileName"]
        fullFilePath = DISK_PATH + userName + fileName
        if os.path.isdir(fullFilePath):
            shutil.rmtree(fullFilePath)
        else:
            os.remove(fullFilePath)
        return 200

class FolderHandler(PutRequest):

    @classmethod
    def handle_put(cls, **kwargs):
        dirPath = DISK_PATH + kwargs["user"] + kwargs["directory"] + kwargs["folderName"]
        os.mkdir(dirPath)
        return 200