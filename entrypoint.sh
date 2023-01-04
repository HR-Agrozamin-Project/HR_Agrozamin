#!/bin/bash


if [ "$DATABASE" = "HR_Agrozamin" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

sleep 10

echo "Apply database migrations"
python manage.py migrate

echo "collectstatic"
python manage.py collectstatic

echo "initadmin"
python create_admin.py

echo "Starting server"
python manage.py runserver --insecure 0.0.0.0:8000

exec "$@"