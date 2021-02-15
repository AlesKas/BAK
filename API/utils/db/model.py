from peewee import Model, TextField, DateTimeField, DecimalField, ForeignKeyField, BooleanField, IntegerField, AutoField, UUIDField, CharField
from .db_util import DB

SCHEMA_NAME = 'main'

class BaseModel(Model):

    class MetaData:
        database = DB

class NtwUsers(BaseModel):
    id = AutoField()
    user_name = TextField(null=False, unique=True)
    passw = TextField(null=False, unique=True)

    class Meta:
        table_name = "ntw_users"
        database = DB
        schema = SCHEMA_NAME

class NtwSalt(BaseModel):
    salt = TextField(null=False)

    class Meta:
        table_name = "ntw_salt"
        primary_key = False
        database = DB

DB.create_tables([NtwUsers])