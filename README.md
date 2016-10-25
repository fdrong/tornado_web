# a simple demo on tornado about login and save cookie


# run
python manage.py


# celery run
celery -A app.tasks worker -l info


# with alembic
## pip install alembic
## alembic init migrate
## config alembic init
    sqlalchemy.url = postgresql://zeus:newpass@localhost/zeus

## create alter db scripts for dbs
    alembic revision --autogenerate -m "create tables"
## use alter db scripts to database
    alembic upgrade head
