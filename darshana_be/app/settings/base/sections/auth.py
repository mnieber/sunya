from datetime import timedelta

from app.utils.env import env

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=int(env("ACCESS_TOKEN_LIFETIME", "8"))),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=int(env("REFRESH_TOKEN_LIFETIME", "36"))),
}

AUTH_USER_MODEL = "users.User"

TERMS_VERSION = "15-08-2021"

DARSHANA_PASSWORD = env("DJANGO_DARSHANA_PASSWORD")
DARSHANA_EMAIL = env("DJANGO_DARSHANA_EMAIL")
