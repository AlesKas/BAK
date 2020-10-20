import os
import peewee
import psycopg2

from ..logger import initLogging
from playhouse.postgres_ext import PostgresqlExtDatabase

LOGGER = initLogging()

DB_name = os.getenv("POSTGRES_DB")
DB_host = os.getenv("POSTGRES_HOST")
DB_port = os.getenv("POSTGRES_PORT")
DB_user = os.getenv("DB_USER")
DB_pass = os.getenv("DB_PASSWD")

LOGGER.info(DB_name)
LOGGER.info(DB_host)
LOGGER.info(DB_port)
LOGGER.info(DB_user)
LOGGER.info(DB_pass)

DB = PostgresqlExtDatabase(DB_name, user=DB_user, password=DB_pass, host=DB_host, port=DB_port)
LOGGER.info("DB inited")