# Gachichat Docker

## Setup

You can set up the project using environment variables in `.env` file

[All list of environment variables](/server/README.md#environment-variables)

Example of using `.env` file:
```
SECRET_KEY=putYourSecretKeyHere
ALLOWED_HOSTS=0.0.0.0,myhost.com
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=database.sqlite3
```

[Here](https://dotenv-linter.readthedocs.io/en/latest/#usage) you can see the dotenv linter and some of rules for dotenv file compilation

## Run

Just install docker and run
```
$ docker-compose up
```
in this directory
