#!/usr/bin/bash

set -e

cmd="$@"

if [ ! -z "$POSTGRESQL_DATABASE" ]; then
  >&2 echo "Checking if PostgreSQL is up"
  if [[ $POSTGRESQL_PASSWORD == *$'\n'* ]];
    then
      POSTGRESQL_PASSWORD=${POSTGRESQL_PASSWORD%$'\n'}
      export POSTGRESQL_PASSWORD=$POSTGRESQL_PASSWORD
  fi 
  until python3 -c "import psycopg2;c=psycopg2.connect(host=\"$POSTGRESQL_HOST\",database=\"$POSTGRESQL_DATABASE\",user=\"$POSTGRESQL_USER\",port=\"$POSTGRESQL_PORT\",password=\"$POSTGRESQL_PASSWORD\");c.close()" &> /dev/null; do
    >&2 echo "PostgreSQL is unavailable - sleeping"
    sleep 1
  done
else
  >&2 echo "Skipping PostgreSQL check"
fi