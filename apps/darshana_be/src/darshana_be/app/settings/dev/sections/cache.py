from darshana_be.app.settings.dev.inherit import CACHES

CACHES["default"] = {
    "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
}
