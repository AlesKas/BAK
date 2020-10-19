import os
import peewee
import psycopg2

from ..logger import initLogging
from playhouse.postgres_ext import PostgresqlExtDatabase
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE

LOGGER = initLogging()

DB_name = os.getenv("POSTGRES_DB")
DB_host = os.getenv("POSTGRES_HOST")
DB_port = os.getenv("POSTGRES_PORT")
DB_user = os.getenv("POSTGRES_USER")
DB_pass = os.getenv("POSTGRES_PASSWORD")

LOGGER.info(DB_name)
LOGGER.info(DB_host)
LOGGER.info(DB_port)
LOGGER.info(DB_user)
LOGGER.info(DB_pass)

DB = peewee.PostgresqlDatabase(DB_name, user=DB_user, password=DB_pass, host=DB_host, port=DB_port, isolation_level=ISOLATION_LEVEL_SERIALIZABLE)
DB.init(DB_name, user=DB_user, password=DB_pass, host=DB_host, port=DB_port)
LOGGER.info("DB inited")
#conn = DB.connection()