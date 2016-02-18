# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': ''
    }
}

#Fill the SMTP details below
EMAIL_HOST = ""
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
