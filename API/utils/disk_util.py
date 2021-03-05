import os

DISK_PATH = "/tmp/NAS/"

def create_user_folder(userName: str):
    user_path = DISK_PATH + userName
    os.mkdir(user_path)