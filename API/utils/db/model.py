from peewee import Model, TextField, AutoField, ForeignKeyField
from .db_util import DB, UUIDField

SCHEMA_NAME = 'main'

class BaseModel(Model):

    class Meta:
        database = DB

class NtwUsers(BaseModel):
    id = UUIDField(primary_key=True)
    user_name = TextField(null=False, unique=True)
    passw = TextField(null=False, unique=False)

    class Meta:
        table_name = "ntw_users"
        schema = SCHEMA_NAME

class Share(BaseModel):
    from_user = ForeignKeyField(NtwUsers, to_field='id')
    to_user = ForeignKeyField(NtwUsers, to_field='id')
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