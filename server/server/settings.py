""" Main project settings """


import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'SECRET_KEY'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = []
ROOT_URLCONF = 'server.urls'
TIME_ZONE = 'UTC'
