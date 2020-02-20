from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
DEV = DEBUG

INSTALLED_APPS += ('debug_toolbar',)

{% if cookiecutter.postgres == "y" or cookiecutter.postgres == "Y" %}
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': '',
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	}
}
{% else %}
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': '{{ cookiecutter.project_name }}.db',
	}
}
{% endif %}

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

SECRET_KEY = 'devel'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 2

AUTH_PASSWORD_VALIDATORS = []

INTERNAL_IPS = ("127.0.0.1",)
