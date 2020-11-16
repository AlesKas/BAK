import psycopg2

from sys import exit
from os import getenv
from logger import initLogging

LOGGER = initLogging()

DB_name = getenv("POSTGRES_DB")
DB_host = getenv("POSTGRES_HOST")
DB_port = getenv("POSTGRES_PORT")
DB_user = getenv("DB_USER")
DB_pass = getenv("DB_PASSWD")

LOGGER.info("Starting DB check.")

try: 
    c = psycopg2.connect(host=DB_host,database=DB_name,user=DB_user,port=DB_port,password=DB_pass)
    cur = c.cursor()
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    LOGGER.info(db_version)
    c.close()
    exit(0)
except (Exception,  psycopg2.DatabaseError) as e:
    LOGGER.error(e)
    exit(-1)