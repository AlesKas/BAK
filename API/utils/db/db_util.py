import os
import peewee
import psycopg2

from playhouse.postgres_ext import PostgresqlExtDatabase
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE

DB_name = os.getenv("POSTGRES_DB")
DB_host = os.getenv("POSTGRES_HOST")
DB_port = os.getenv("POSTGRES_PORT")
DB_user = os.getenv("POSTGRES_USER")
DB_pass = os.getenv("POSTGRES_PASSWORD")

DB = peewee.PostgresqlDatabase(DB_name, user=DB_user, password=DB_pass, host=DB_host, port=DB_port, isolation_level=ISOLATION_LEVEL_SERIALIZABLE)
#conn = DB.connection()