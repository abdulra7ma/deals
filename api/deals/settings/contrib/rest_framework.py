from ..environment import env

from datetime import timedelta


REST_FRAMEWORK = {
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_RENDERER_CLASSES": env.tuple(
        "CORE_DEFAULT_RENDERER_CLASSES",
        default=("rest_framework.renderers.JSONRenderer",),
    ),
    "PAGE_SIZE": 100,
}

SIMPLE_JWT = {
    "USER_ID_FIELD": "uuid",
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=5),
}
