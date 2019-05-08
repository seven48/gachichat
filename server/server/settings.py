""" Main project settings """


import os


# Hardcoded settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTALLED_APPS = []
ROOT_URLCONF = 'server.urls'

# Customizable settings
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1').split(',')
DEBUG = os.getenv('DEBUG') in ['True', 'true', '1']
SECRET_KEY = os.getenv('SECRET_KEY')
TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')
