FROM postgres

ENV POSTGRES_USER 'db_admin'
ENV POSTGRES_PASSWORD 'admin_pwd'
ENV POSTGRES_DB 'ntw_database'
ENV POSTGRES_MANAGER_PASSWORD 'manager_pwd'

COPY database/schema/*.sql              /docker-entrypoint-initdb.d/
COPY database/schema/init_schema.sh     /docker-entrypoint-initdb.d/