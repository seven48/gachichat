""" Main project settings """


import os


# Hardcoded settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTALLED_APPS = [
    'users',
    'rooms'
]
ROOT_URLCONF = 'server.urls'

# Customizable settings
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_NAME', 'gachichat'),
        'HOST': os.getenv('POSTGRES_HOST', '127.0.0.1'),
        'PORT': int(os.getenv('POSTGRES_PORT', '5432')),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD')
    }
}
DEBUG = os.getenv('DEBUG') in ['True', 'true', '1']
SECRET_KEY = os.getenv('SECRET_KEY')
TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')
USER_TOKEN_EXPIRING = int(os.getenv('USER_TOKEN_EXPIRING', '604800'))
