import os
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE', default='django.db.backends.postgresql'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
    }
}

SECRET_KEY = env('SECRET_KEY', default='apollo84')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['.localhost', '127.0.0.1'])

DEBUG = env.bool('DEBUG', default=False)

INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
