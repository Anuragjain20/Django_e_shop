import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from decouple import config
SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}