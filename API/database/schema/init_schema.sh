#!/usr/bin/sh

echo "Initializing DB"

psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c "ALTER USER ${POSTGRES_USER} WITH CREATEROLE"
echo "Altered super user"

echo "Setting user passwords"
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c "ALTER USER manager WITH PASSWORD '${POSTGRES_MANAGER_PASSWORD}'"

echo "DB initialized"