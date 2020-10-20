#!/usr/bin/sh

set -e
  
until python3 -c "import psycopg2;c=psycopg2.connect(host=\"$POSTGRES_HOST\",database=\"$POSTGRES_DB\",user=\"$DB_USER\",port=\"$POSTGRES_PORT\",password=\"$DB_PASSWD\");c.close()" &> /dev/null; do
    echo "Waiting for database to initialize"
    sleep 2;
done

echo "Database intialized, running $1"

if [[ ! -z "$1" ]]; then
    if ([ "$1" == "manager" ] && [ ${DEBUG} == "false" ]); then 
        exec python3.8 -m manager.main
    fi
    if ([ "$1" == "manager" ] && [ ${DEBUG} == "true" ]); then
        echo "Running debug mode"
        exec python3 -m ptvsd --host 0.0.0.0 --port 5678 --wait -m flask run --no-reload --no-debugger --host 0.0.0.0 --port 8000
    fi
fi

echo "Command not found"
exit -1