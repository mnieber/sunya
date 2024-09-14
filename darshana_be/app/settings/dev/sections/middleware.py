from app.settings.dev.inherit import MIDDLEWARE

MIDDLEWARE += [
    "app.middleware.request_logging.request_logging_middleware",
]
