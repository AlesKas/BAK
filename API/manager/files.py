import os
import shutil
import unicodedata

from utils.db.model import Share, NtwUsers
from utils.logger import initLogging
from flask import send_from_directory, make_response
from .base import PutRequest, GetRequest, DeleteRequest
from utils.disk_util import DISK_PATH, remove_shared_file_from_db

LOGGER = initLogging()

class FilePutHandler(PutRequest):

    @classmethod
    def handle_put(cls, **kwargs):
        filePath = DISK_PATH + kwargs["user"] + kwargs["directory"]
        file = kwargs["fileName"]
        incomingFileSize = os.fstat(file.fileno()).st_size
        _, _, free = shutil.disk_usage(DISK_PATH)
        if incomingFileSize > free:
            return cls.format_exc("Internal server error", 500,"Not enough free space.") 
        savePath = filePath + str(unicodedata.normalize('NFKD', file.filename).encode('ascii', 'ignore'))[2:-1]
        file.save(savePath)
        return 200

class FileGetHandler(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        response = {}
        response["data"] = []
        currentUserName = kwargs["user"]
        directory = kwargs["directory"]
        if kwargs["toUser"]:
            currentUser = NtwUsers.get(NtwUsers.user_name == currentUserName).id
            toUser = kwargs["toUser"]
            toUser = NtwUsers.get(NtwUsers.user_name == toUser).id
            strippedDir = directory.split("/")[1]
            query = Share.select(Share.directory).distinct().where((Share.from_user == currentUser) & (Share.to_user == toUser) & (Share.file_name == strippedDir))
            sharedDir = [f for f in query]
            userWorkspace = DISK_PATH + currentUserName + sharedDir[0].directory + directory
        else:
            userWorkspace = DISK_PATH + currentUserName + directory
        for file in os.listdir(userWorkspace):
            fileResp = {}
            base = os.path.basename(file)
            fileName, fileType = os.path.splitext(base)
            fileResp["fileName"] = fileName
            if fileType == "":
                fileResp["isDir"] = True
                fileResp["fileType"] = ""
            else:
                fileResp["fileType"] = fileType[1:]
                fileResp["isDir"] = False
            response["data"].append(fileResp)

        response["data"] = sorted(response["data"], key=lambda k: k["fileType"])
        return response

class FileGetHandlerDownload(GetRequest):

    @classmethod
    def handle_get(cls, **kwargs):
        fileName = kwargs["fileName"]
        currentUserName = kwargs["user"]
        directory = kwargs["directory"]
        if kwargs["toUser"]:
            currentUser = NtwUsers.get(NtwUsers.user_name == currentUserName).id
            toUser = kwargs["toUser"]
            toUser = NtwUsers.get(NtwUsers.user_name == toUser).id
            if directory != "/":
                strippedDir = directory.split("/")[1]
                query = Share.select(Share.directory).where((Share.from_user == currentUser) & (Share.to_user == toUser) & (Share.file_name == strippedDir))
            else:
                query = Share.select(Share.directory).where((Share.from_user == currentUser) & (Share.to_user == toUser) & (Share.directory == directory))
            sharedDir = [f for f in query]
            userWorkspace = DISK_PATH + currentUserName + sharedDir[0].directory + directory
        else:
            userWorkspace = DISK_PATH + currentUserName + directory
        response = make_response(send_from_directory(userWorkspace, fileName, as_attachment=True))
        response.direct_passthrough = False
        return response

class FileDeleteHandler(DeleteRequest):

    @classmethod
    def handle_delete(cls, **kwargs):
        userName = kwargs["user"]
        from_user = NtwUsers.get(NtwUsers.user_name == userName).id
        fileName = kwargs["fileName"]
        fullFilePath = DISK_PATH + userName + fileName
        if os.path.isdir(fullFilePath):
            remove_shared_file_from_db(from_user, fullFilePath)
            shutil.rmtree(fullFilePath)
            to_del = Share.delete().where((Share.from_user == from_user) & (Share.file_name == fileName)) 
            to_del.execute()
        else:
            fileName = fileName.split("/")[-1]
            to_del = Share.delete().where((Share.from_user == from_user) & (Share.file_name == fileName)) 
            to_del.execute()
            os.remove(fullFilePath)
        return 200

class FolderHandler(PutRequest):

    @classmethod
    def handle_put(cls, **kwargs):
        dirPath = DISK_PATH + kwargs["user"] + kwargs["directory"] + kwargs["folderName"]
        os.mkdir(dirPath)
        return 200