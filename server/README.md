# Gachichat Backend 

* <a href="#environment-variables">Environment variables</a>
* <a href="#api">API</a>
* * <a href="#users">Users</a>
* * * <a href="#post-userscreate">create</a>
* * * <a href="#get-usersgetme">getMe</a>
* * <a href="#rooms">Rooms</a>
* * * <a href="#post-roomscreate">create</a>
* * * <a href="#get-roomsinfo">info</a>
* * <a href="#messages">Messages</a>
* * * <a href="#post-messagessend">send</a>
* * * <a href="#get-messagesget">get</a>
* <a href="#installation">Installation</a>

# Environment variables

You can customize the application using environment variables

<table>
    <tr>
        <th>Variable</th>
        <th>Description</th>
        <th>Default value</th>
    </tr>
    <td colspan="3" align="center">Django settings</td>
    <tr>
        <td>ALLOWED_HOSTS</td>
        <td>Comma separated values of hosts for django setting ALLOWED_HOSTS. <a href="https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts">Django docs</a></td>
        <td>127.0.0.1,localhost</td>
    </tr>
    <tr>
        <td>DEBUG</td>
        <td><a href="https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-DEBUG">Django docs</a></td>
        <td>False</td>
    </tr>
    <tr>
        <td>TIME_ZONE</td>
        <td><a href="https://docs.djangoproject.com/en/2.2/ref/settings/#time-zone">Django docs</a>
        <td>UTC</td>
    </tr>
    <td colspan="3" align="center">Database settings</td>
    <tr>
        <td>DATABASE_ENGINE</td>
        <td>Django database engine that will used for ORM</td>
        <td>django.db.backends.postgresql_psycopg2</td>
    </tr>
    <tr>
        <td>DATABASE_NAME</td>
        <td>Your database name</td>
        <td>gachichat</td>
    </tr>
    <tr>
        <td>DATABASE_HOST</td>
        <td>Your database host name</td>
        <td>127.0.0.1</td>
    </tr>
    <tr>
        <td>DATABASE_PORT</td>
        <td>DB port</td>
        <td>5432</td>
    </tr>
    <tr>
        <td>DATABASE_USER</td>
        <td>Username for DB auth</td>
        <td>postgres</td>
    </tr>
    <tr>
        <td>DATABASE_PASSWORD</td>
        <td>Password for DB auth</td>
        <td></td>
    </tr>
    <td colspan="3" align="center">Other settings</td>
    <tr>
        <td>SECRET_KEY</td>
        <td>Secret key for hashing and encoding</td>
        <td></td>
    </tr>
    <tr>
        <td>USER_TOKEN_EXPIRING</td>
        <td>Count of seconds for JSON Web Token lifetime</td>
        <td>604800</td>
    </tr>
</table>

# API

## Users

### POST `/users/create`

Create new user for chosen room

__JSON POST Data:__

room_id - Numeric value for id of the room for registration

password [optional] - Password for the room. If password is setted

__Response:__
```
{
    id: 26,
    token: 'yourAPItoken'
    first_name: 'maria'
    last_name: 'hart'
    created: 1557492563
    expired_in: 1558097363
}
```

### GET `/users/getMe`

Get information of user

__Headers:__
```
{
    Authorization: 'yourAPItoken'
}
```

__Response:__
```
{
    id: 26
    first_name: 'maria'
    last_name: 'hart'
    created: 1557492563
}
```

## Rooms

### POST `/rooms/create`

Create random named room and user for this room

__JSON POST Data:__

password [optional] - Password for creating room. If you set it, your room will be private.

name [optional] - Name of the creating room. Default is random words.

description [optional] - Description of the creating room.

__Response:__
```
{
    user: {
        id: 26,
        token: 'yourAPItoken'
        first_name: 'maria'
        last_name: 'hart'
        created: 1557492563
        expired_in: 1558097363
    }
    room: {
        id: 10
        name: 'Soap_Laptop'
        description: ''
        link: ''
        created: 1557492563
        password: 'qwerty12+'
    }
}
```

## GET `/rooms/info`

Get information of room

__Headers:__
```
{
    Authorization: 'yourAPItoken'
}
```

__Response:__
```
{
    id: 10
    name: 'Soap_Laptop'
    description: ''
    link: ''
    created: 1557492563
}
```

## Messages

### POST `/messages/send`

Send message to room

__Headers:__
```
{
    Authorization: 'yourAPItoken'
}
```

__Response:__
```
{
    id: 19
    text: 'Hello. This is text of message'
    created: 1557615906
    user: {
        id: 26,
        first_name: 'maria'
        last_name: 'hart'
        created: 1557492563
    }
}
```

### GET `/messages/get`

Getting all or filtered messages

__Headers:__
```
{
    Authorization: 'yourAPItoken'
}
```

__GET arguments:__

offset [optional] - count of messages for offset

count [optional] - numeric value of count messages in response

__Response:__
```
[
    {
        id: 19
        text: 'Hello. This is text of message'
        created: 1557615906
        user: {
            id: 26,
            first_name: 'maria'
            last_name: 'hart'
            created: 1557492563
        }
    }
]
```


# Installation

It's very easy. Follow the instructions:

## Python and dependencies

1. Install the Python interpreter using the batch manager of your operating system.
2. Create virtual environment
```
$ virtualenv venv -p python3 --no-site-packages
Running virtualenv with interpreter /bin/python3
...
done
```
3. Enter to virtual environment
```
$ source venv/bin/activate
```
4. Install all dependencies using pip
```
(venv) $ pip install -r requirements.txt
Collecting...
...
Successfully installed...
```

## PostgreSQL

1. Install PostgreSQL using your package manager of your OS
2. Run it like a daemon
```
$ systemctl start postgresql.service
```
3. Open PostgreSQL console
```
$ sudo -u postgres psql postgres
```
4. Create database
```
# create database gachichat owner postgres
```
5. That is all. Just log out from postgres user by pressing `CTRL + D`

__If you have difficulties with postgresql consult your operating system documentation__

## Migrations

After the previous two steps you need to enter again the virtual environment (step 3 in python) and apply all migrations
```
(venv) $ python manage.py migrate
```

## Fin

That's all. You awesome. Just run
```
(venv) $ python manage.py runserver
```
And have fun!
