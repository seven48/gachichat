# Gachichat Backend 

* <a href="#environment-variables">Environment variables</a>
* <a href="#api">API</a>
* * <a href="#users">Users</a>
* * * <a href="#post-userscreate">create</a>
* * * <a href="#get-usersgetme">getMe</a>

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
        <td>POSTGRES_NAME</td>
        <td>PostgreSQL database name</td>
        <td>gachichat</td>
    </tr>
    <tr>
        <td>POSTGRES_HOST</td>
        <td>PostgreSQL host name</td>
        <td>127.0.0.1</td>
    </tr>
    <tr>
        <td>POSTGRES_PORT</td>
        <td>PostgreSQL port</td>
        <td>5432</td>
    </tr>
    <tr>
        <td>POSTGRES_USER</td>
        <td>Username for PostgreSQL auth</td>
        <td>postgres</td>
    </tr>
    <tr>
        <td>POSTGRES_PASSWORD</td>
        <td>Password for PostgreSQL auth</td>
        <td></td>
    </tr>
    <td colspan="3" align="center">Other settings</td>
    <tr>
        <td>USER_TOKEN_EXPIRING</td>
        <td>Count of seconds for JSON Web Token lifetime</td>
        <td>604800</td>
    </tr>
</table>

# API

## Users

### POST `/users/create`

Create new user instance

Response:
```
{
    token: 'yourAPItoken'
    first_name: 'maria'
    last_name: 'hart'
    created: 1557444096
    expired_in: 1558048896
}
```

### GET `/users/getMe`

Get information of user

Headers:
```
{
    Authorization: 'yourAPItoken'
}
```

Response:
```
{
    first_name: 'maria'
    last_name: 'hart'
}
```
