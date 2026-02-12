from darshana_be.app.settings.dev.inherit import MIDDLEWARE

MIDDLEWARE += [
    "darshana_be.app.middleware.request_logging.request_logging_middleware",
]
