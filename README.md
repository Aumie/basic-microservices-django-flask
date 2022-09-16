# basic-microservices-django-flask

##### for migration, if wanna delete old migrations folder

## Django

```sh
python manage.py makemigrations;python manage.py migrate;
```

## Flask

```sh
flask db init; flask db stamp head; flask db migrate; flask db upgrade;
```

## docker-compose

```sh
docker-compose up
```

## cli inside a container

```sh
docker-compose exec <container-name> sh
```
