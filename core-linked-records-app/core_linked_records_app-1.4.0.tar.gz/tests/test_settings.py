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
    "defender",
    "tz_detect",
    "menu",
    # Local apps
    "xml_utils",
    "core_main_app",
    "core_federated_search_app",
    "core_oaipmh_common_app",
    # "core_oaipmh_harvester_app",
    # "core_explore_oaipmh_app",
    "core_linked_records_app",
    "tests",
]

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

MOCK_DATABASE_NAME = "db_mock"
MOCK_DATABASE_HOST = "mongomock://localhost"
CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

CUSTOM_NAME = "mock_custom_name"

ROOT_URLCONF = "core_linked_records_app.urls"

SERVER_URI = "http://mock-cdcs.com"

database = Database(MOCK_DATABASE_HOST, MOCK_DATABASE_NAME)
database.connect()
