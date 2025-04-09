#!/bin/sh

if [ "$WAIT_FOR_DB" = "true" ]
then
    until python manage.py check --database default 2>/dev/null; do
        echo "Waiting for database..."
        sleep 3
    done
fi

python manage.py migrate --noinput

exec "$@"