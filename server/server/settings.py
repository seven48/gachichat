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
ALLOWED_HOSTS = (
    os.getenv('ALLOWED_HOSTS') or '127.0.0.1,localhost'
).split(',')
DATABASES = {
    'default': {
        'ENGINE': os.getenv(
            'DATABASE_ENGINE',
            'django.db.backends.postgresql_psycopg2'
        ),
        'NAME': os.getenv('DATABASE_NAME') or 'gachichat',
        'HOST': os.getenv('DATABASE_HOST') or '127.0.0.1',
        'PORT': int(os.getenv('DATABASE_PORT') or '5432'),
        'USER': os.getenv('DATABASE_USER') or 'postgres',
        'PASSWORD': os.getenv('DATABASE_PASSWORD')
    }
}
DEBUG = os.getenv('DEBUG') in ['True', 'true', '1']
SECRET_KEY = os.getenv('SECRET_KEY')
TIME_ZONE = os.getenv('TIME_ZONE') or 'UTC'
USER_TOKEN_EXPIRING = int(os.getenv('USER_TOKEN_EXPIRING') or '604800')
