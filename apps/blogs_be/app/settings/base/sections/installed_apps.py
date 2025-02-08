DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.messages",
]

THIRD_PARTY_APPS = [
    "adminsortable2",
    "corsheaders",
    "dbbackup",
    "django_extensions",
    "rest_framework",
    "rest_framework_gis",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "drf_standardized_errors",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
]

LOCAL_APPS = [
    "api.apps.ApiConfig",
    "app.apps.AppConfig",
    "blogs.apps.BlogsConfig",
    "users.apps.UsersConfig",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
