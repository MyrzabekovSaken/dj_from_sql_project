import django
from django.conf import settings
from django.core.management import execute_from_command_line
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def init_django():

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            'db',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        },
        DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField',
    )
    django.setup()


if __name__ == "__main__":

    init_django()
    execute_from_command_line()
