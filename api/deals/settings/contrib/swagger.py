from ..environment import env

SWAGGER_SETTINGS = {
    "DEFAULT_API_URL": env.str(
        "CORE_BASE_API_URL", default="https://example.com"
    ),
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
}
