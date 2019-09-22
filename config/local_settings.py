import os

#settings.pyからコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hb+^xma=y!wd&21m!@e++62qqg#v7_kjs1et3%nh%@pdc&ewc%'

#settings.pyからコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True #ローカル環境でDebugできるようになる

