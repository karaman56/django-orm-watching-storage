import os
from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

DATABASES = {
    'default': {
        'ENGINE': env("DB_ENGINE"),
        'HOST': env("DB_HOST"),
        'PORT': env.int("DB_PORT"),
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
    }
}

SECRET_KEY = env("SECRET_KEY", default='REPLACE_ME')

ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

INSTALLED_APPS = ['datacenter']













