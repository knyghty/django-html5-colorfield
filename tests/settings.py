DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

INSTALLED_APPS = ["tests"]

ROOT_URLCONF = "tests.urls"

SECRET_KEY = "dummy"

TEMPLATES = [
    {"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": True}
]
