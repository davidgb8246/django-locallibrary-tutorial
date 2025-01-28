import os

ALLOWED_HOSTS = [ '.vercel.app' ]
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": os.environ.get('DATABASE_ENGINE', False),
        "NAME": os.environ.get('DATABASE_QUERYSTR', False),
    }
}
