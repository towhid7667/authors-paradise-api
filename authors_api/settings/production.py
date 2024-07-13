from .base import *  # noqa
from .base import env

ADMINS = [("Towhid", "towhidulhq@gmail.com")]

CSRF_TRUSTED_ORIGINS = ["https://ec2-52-65-200-31.ap-southeast-2.compute.amazonaws.com"]

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["ec2-52-65-200-31.ap-southeast-2.compute.amazonaws.com"])

ADMIN_URL = env("DJANGO_ADMIN_URL")

DATABASES = {"default": env.db("DATABASE_URL")}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # Fixed typo here

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 518400

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # Updated storage class

DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL", default="Authors Paradise Support <towhidulhq@gmail.com>")

SITE_NAME = "Authors Paradise"

SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Authors Paradise]")

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_HOST_USER = "postmaster@sandboxf27a65eb1bb142a7b55ac997dda8dea7.mailgun.org"
EMAIL_HOST_PASSWORD = env("SMTP_MAILGUN_PASSWORD")

EMAIL_PORT = 587
EMAIL_USE_TLS = True
DOMAIN = env("DOMAIN")

# Logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True
        },
        "django.security.DisallowedHost": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True
        }
    }
}

