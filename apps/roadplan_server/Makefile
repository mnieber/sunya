#
# Postgres
#

create-db:
	PGPASSWORD=${POSTGRES_PASSWORD} psql -h ${POSTGRES_HOST} -d postgres -U postgres -c "CREATE USER ${DJANGO_DATABASE_USER} WITH CREATEDB PASSWORD '${DJANGO_DATABASE_PASSWORD}';" || true
	PGPASSWORD=${DJANGO_DATABASE_PASSWORD} psql -h ${POSTGRES_HOST} -d postgres -U ${DJANGO_DATABASE_USER} -c "CREATE DATABASE ${DJANGO_DATABASE_NAME};" || true
	PGPASSWORD=${POSTGRES_PASSWORD} psql -h ${POSTGRES_HOST} -d postgres -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE ${DJANGO_DATABASE_NAME} TO ${DJANGO_DATABASE_USER};"

pgcli:
	pgcli `python src/manage.py sqldsn --quiet --style=uri`

#
# Python
#

pip-compile:
	uv pip compile --upgrade requirements.in requirements.editable -o requirements.txt
	sed -i 's/jaraco-classes==/jaraco.classes==/g' requirements.txt
#
# Django
#

collect-static:
	python src/manage.py collectstatic --link

create-superuser:
	python src/manage.py createsuperuser --noinput || true

dump-db:
	mkdir -p /app/dumps && python src/manage.py dbbackup

make-migrations-users:
	python src/manage.py makemigrations users

migrate:
	python src/manage.py migrate

run-server:
	python src/manage.py runserver 0.0.0.0:8003

generateschema:
	python src/manage.py spectacular --file api/openapi-schema.yml --validate

#
# Stack
#

init-dev: \
	create-db \
	make-migrations-users \
	migrate \
	collect-static \
	create-superuser
