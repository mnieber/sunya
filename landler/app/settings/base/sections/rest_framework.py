REST_FRAMEWORK = {
    # "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "api.openapi.AutoSchemaWithErrorResponses",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    # "PAGE_SIZE": 1000,
}


SPECTACULAR_SETTINGS = {
    "TITLE": "Landler API",
    "DESCRIPTION": "Landler REST API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_SPLIT_REQUEST": True,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "ENUM_NAME_OVERRIDES": {},
}
