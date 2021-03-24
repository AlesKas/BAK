import os

from .db.model import Share
from .logger import initLogging

LOGGER = initLogging()
DISK_PATH = "/tmp/NAS/"

def create_user_folder(userName: str):
    user_path = DISK_PATH + userName
    os.mkdir(user_path)

def remove_shared_file_from_db(fromUser: str, startDir: str):
    for fileName in os.listdir(startDir):
        to_del = Share.delete().where((Share.from_user == fromUser) & (Share.file_name == fileName)) 
        to_del.execute()
        newPath = startDir + "/" + fileName
        if os.path.isdir(newPath):
            remove_shared_file_from_db(fromUser, newPath)