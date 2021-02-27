import os

DISK_PARH = "/tmp/NAS/"

def create_user_folder(userName: str):
    user_path = DISK_PARH + userName
    os.mkdir(user_path)