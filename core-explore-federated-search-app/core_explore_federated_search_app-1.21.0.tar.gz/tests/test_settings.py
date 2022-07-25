from core_main_app.utils.databases.mongoengine_database import Database

SECRET_KEY = "fake-key"

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    # Extra apps
    "oauth2_provider",
    "defender",
    "tz_detect",
    "menu",
    # Local apps
    "core_main_app",
    "tests",
]

# SERVER URI
SERVER_URI = "http://example.com"

# IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

MIDDLEWARE = (
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "tz_detect.middleware.TimezoneMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core_main_app.utils.custom_context_processors.domain_context_processor",  # Needed by any curator app
                "django.template.context_processors.i18n",
            ],
        },
    },
]

STATIC_URL = "/static/"
ROOT_URLCONF = "tests.urls"
CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

MOCK_DATABASE_NAME = "db_mock"
MOCK_DATABASE_HOST = "mongomock://localhost"

DATA_SORTING_FIELDS = ["+title"]

CUSTOM_NAME = "Curator"

database = Database(MOCK_DATABASE_HOST, MOCK_DATABASE_NAME)
database.connect()
