from peewee import Model, TextField, AutoField
from .db_util import DB

SCHEMA_NAME = 'main'

class BaseModel(Model):

    class Meta:
        database = DB

class NtwUsers(BaseModel):
    id = AutoField()
    user_name = TextField(null=False, unique=True)
    passw = TextField(null=False, unique=False)

    class Meta:
        table_name = "ntw_users"
        schema = SCHEMA_NAME

class Share(BaseModel):
    from_user = TextField(null=False)
    to_user = TextField(null=False)
    directory = TextField(null=False)
    file_name = TextField()

    class Meta:
        table_name = "share"
        schema = SCHEMA_NAME
        primary_key = False

class NtwSalt(BaseModel):
    salt = TextField(null=False)

    class Meta:
        table_name = "ntw_salt"
        primary_key = False