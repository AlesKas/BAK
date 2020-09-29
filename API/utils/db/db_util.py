import os
import peewee

DB_name = os.getenv("POSTGRES_DB")
DB_host = os.getenv("POSTGRES_HOST")
DB_port = os.getenv("POSTGRES_PORT")
DB_user = os.getenv("POSTGRES_USER")
DB_pass = os.getenv("POSTGRES_PASSWORD")

posgres_sql = peewee.PostgresqlDatabase(DB_name, user=DB_user, password=DB_pass, host=DB_host, port=DB_port)