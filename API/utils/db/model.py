from peewee import Model, TextField, DateTimeField, DecimalField, ForeignKeyField, BooleanField, IntegerField, AutoField, UUIDField, CharField
from .db_util import DB

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

class Salt(BaseModel):
    salt = TextField(null=False)

    class Meta:
        table_name = "salt"
        database = DB

DB.create_tables([NtwUsers])