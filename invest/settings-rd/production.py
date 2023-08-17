from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = config('DEBUG', cast=bool)


#ALLOWED_HOSTS = []
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=list)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT', cast=int)
    }
}