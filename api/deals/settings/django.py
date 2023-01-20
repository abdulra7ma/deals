from pathlib import Path

from .environment import env


BASE_DIR = Path(__file__).resolve().parent.parent


def rel(*path):
    return BASE_DIR.joinpath(*path)


DEBUG = env.bool("CORE_DEBUG", default=False)

print(DEBUG)

INTERNAL_IPS = env.list("CORE_INTERNAL_IPS", default=[])

ALLOWED_HOSTS = env.list("CORE_ALLOWED_HOSTS", default=[])

SECRET_KEY = env.str("CORE_SECRET_KEY")

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "django_extensions",
    "django_filters",
    "drf_yasg",
    "rest_framework",
    "rest_framework_simplejwt",
    # First-party apps
    "deals.apps.common",
    "deals.apps.accounts",
    "deals.apps.processor",
] + env.list("CORE_DEV_INSTALLED_APPS", default=[])

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
] + env.list("CORE_DEV_MIDDLEWARE", default=[])

ROOT_URLCONF = "deals.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [rel("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "deals.wsgi.application"

DATABASES = {
    "default": env.db(
        "CORE_DATABASE_URL",
        default="psql://postgres:awesome_password_1@database:5432/deals_db",
    ),
}

AUTH_USER_MODEL = "accounts.UserAccount"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "CORE_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)
SECURE_HSTS_SECONDS = env.int(
    "CORE_SECURE_HSTS_SECONDS", default=31536000
)  # 1 year

SESSION_COOKIE_HTTPONLY = env.bool(
    "CORE_SESSION_COOKIE_HTTPONLY", default=True
)
SESSION_COOKIE_SECURE = env.bool("CORE_SESSION_COOKIE_SECURE", default=True)
SESSION_COOKIE_NAME = "s"

CSRF_COOKIE_SECURE = env.bool("CORE_CSRF_COOKIE_SECURE", default=True)
CSRF_COOKIE_NAME = "c"

X_FRAME_OPTIONS = env.str("CORE_X_FRAME_OPTIONS", default="SAMEORIGIN")

LANGUAGE_CODE = "en-us"

TIME_ZONE = env.str("CORE_TIME_ZONE", default="UTC")

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [rel("..", "..", "api", "locale")]

STATIC_URL = env.str("CORE_STATIC_URL", default="static/")
STATIC_ROOT = env.str(
    "CORE_STATIC_ROOT", default=rel("..", "..", "public", "static")
)

MEDIA_URL = env.str("CORE_MEDIA_URL", default="media/")
MEDIA_ROOT = env.str("CORE_MEDIA_ROOT", rel("..", "..", "public", "media"))

# EMAIL_BACKEND = env.str(
#     "CORE_EMAIL_BACKEND",
#     default="django.core.mail.backends.smtp.EmailBackend",
# )

# if (
#     EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend"
# ):  # pragma: no cover
#     EMAIL_HOST = env.str("CORE_EMAIL_HOST")
#     EMAIL_PORT = env.str("CORE_EMAIL_PORT")
#     EMAIL_HOST_USER = env.str("CORE_EMAIL_HOST_USER")
#     EMAIL_HOST_PASSWORD = env.str("CORE_EMAIL_HOST_PASSWORD")
#     EMAIL_USE_TLS = env.bool("CORE_EMAIL_USE_TLS", default=True)

SITE_ID = env.int("CORE_SITE_ID", default=1)

USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

USER_ID_FIELD = "uuid"

REDIS_HOST = env.str("CORE_REDIS_HOST", default="localhost")  # or the host of your redis server
REDIS_PORT = env.int("CORE_REDIS_PORT", default=6379)   # or the port of your redis server
REDIS_DB = env.int("CORE_REDIS_DB", default=0)  # or the db number you want to use

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
