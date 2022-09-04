from .base import *


DEBUG = bool(os.environ.get("DEBUG", False))
ALLOWED_HOSTS = ['.herokuapp.com', 'naturaloil-app.heroku.com', 'locashost', '127.0.0.1']


DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'd5885c3hs576ul',
        "USER": 'voghwvllacickq',
        "PASSWORD": '899e3110f40b37c2be304999aaaaa5d182fe02fad48f4aee23926fa958ef5229',
        "HOST": 'ec2-34-225-159-178.compute-1.amazonaws.com',
        "PORT": '5432',

    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]