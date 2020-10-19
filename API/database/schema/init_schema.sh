echo "Initializing DB"

psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c "ALTER USER ${POSTGRES_USER} WITH CREATEROLE"
echo "Altered super user"
#psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f database/schema/schema.sql
#psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f database/schema/test_data.sql
#psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f database/schema/create_urers.sql

psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c "ALTER USER manager WITH PASSWORD '${POSTGRES_MANAGER_PASSWORD}'"

echo "DB initialized"