"""
Production Settings for Heroku
"""

import environ
import django_heroku

from website.settings.dev import *

# Activate Django-Heroku.
django_heroku.settings(locals())

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# False if not in os.environ
DEBUG = env("DEBUG")

# Raises django"s ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(", ")

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ["DATABASE_URL"] and raises ImproperlyConfigured exception if not found
    "default": env.db(),
}

# Email Configuration
SENDGRID_API_KEY = env("SENDGRID_API_KEY")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.sendgrid.net"

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_HOST_USER = "apikey"

EMAIL_HOST_PASSWORD = SENDGRID_API_KEY

CLUB_EMAIL = env("CLUB_EMAIL")