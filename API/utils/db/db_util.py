import uuid

from  os import getenv
from ..logger import initLogging
from playhouse.postgres_ext import PostgresqlExtDatabase
from peewee import Field

LOGGER = initLogging()

DB_name = getenv("POSTGRES_DB")
DB_host = getenv("POSTGRES_HOST")
DB_port = getenv("POSTGRES_PORT")
DB_user = getenv("DB_USER")
DB_pass = getenv("DB_PASSWD")

class UUIDField(Field):
    field_type = 'uuid'

    def db_value(self, value):
        return value.hex

    def python_value(self, value):
        return uuid.UUID(value)

DB = PostgresqlExtDatabase(DB_name, user=DB_user, password=DB_pass, host=DB_host, port=DB_port, field_types={'uuid': 'uuid'})
LOGGER.info("DB inited")