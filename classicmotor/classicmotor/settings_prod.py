from .settings import *

DEBUG = True

# ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'classicmotor',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'a'
    }
}


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1030481745227-akfn5cv8ckefbomdqs7igjfssnte5qpo'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '8Ca1tPqLNQnq_V9g6wChaI2m'
