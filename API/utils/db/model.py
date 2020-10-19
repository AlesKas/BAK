from peewee import Model, TextField, DateTimeField, DecimalField, ForeignKeyField, BooleanField, IntegerField, AutoField, UUIDField, CharField
from .db_util import DB

class BaseModel(Model):

    class MetaData:
        database = DB

class NtwUsers(BaseModel):
    id = IntegerField()
    userName = TextField(null=False, unique=True)
    passw = TextField(null=False, unique=True)

    class Meta:
        table_name = "ntw_users"