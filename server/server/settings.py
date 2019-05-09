""" Main project settings """


import os


# Hardcoded settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTALLED_APPS = []
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv('MONGODB_NAME', 'gachichat'),
        'HOST': os.getenv('MONGODB_HOST', 'localhost'),
        'PORT': int(os.getenv('MONGODB_PORT', '27017')),
        'USER': os.getenv('MONGODB_USER'),
        'PASSWORD': os.getenv('MONGODB_PASSWORD')
    }
}
ROOT_URLCONF = 'server.urls'

# Customizable settings
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1').split(',')
DEBUG = os.getenv('DEBUG') in ['True', 'true', '1']
SECRET_KEY = os.getenv('SECRET_KEY')
TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')
