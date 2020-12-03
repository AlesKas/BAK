from  os import getenv
from ..logger import initLogging
from playhouse.postgres_ext import PostgresqlExtDatabase, PostgresqlDatabase

LOGGER = initLogging()

DB_name = getenv("POSTGRES_DB")
DB_host = getenv("POSTGRES_HOST")
DB_port = getenv("POSTGRES_PORT")
DB_user = getenv("DB_USER")
DB_pass = getenv("DB_PASSWD")

DB = PostgresqlExtDatabase(DB_name, user=DB_user, password=DB_pass, host=DB_host, port=DB_port)
LOGGER.info("DB inited")