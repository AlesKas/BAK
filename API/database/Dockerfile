FROM postgres

ENV POSTGRES_USER 'db_admin'
ENV POSTGRES_PASSWORD 'admin_pwd'
ENV POSTGRES_DB 'ntw_database'

COPY database/schema/schema.sql /docker-entrypoint-initdb.d/
