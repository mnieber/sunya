from app.utils.env import env

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "users.User"

TERMS_VERSION = "15-08-2021"

LANDLER_PASSWORD = env("DJANGO_LANDLER_PASSWORD")
LANDLER_EMAIL = env("DJANGO_LANDLER_EMAIL")
