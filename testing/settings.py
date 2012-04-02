import os

AUTHNET_LOGIN_ID = ''
AUTHNET_TRANSACTION_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    },
}

SECRET_KEY = 'm+qa*7_8t-=17zt_)9gi)4g%6w*v$xxkh6rwrys*bn9su+5%du'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'kvisits',
    'kvisits.tests',
    'kvisits.loghandlers.dbloghandler',
    'kvisits.uniqhandlers.dbuniqhandler',
]

LANGUAGE_CODE = 'en'

LOGIN_URL = '/accounts/login/'

MANAGERS = []

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'kvisits.middleware.KVisitsMiddleware',
]

ROOT_URLCONF = 'testing.urls'

SITE_ID = 1

TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), 'templates')]

USE_I18N = True

KVISITS_IGNORE_USER_AGENTS = [ 'test us.*' ]
KVISITS_MIN_TIME_BETWEEN_VISITS = 1
KVISITS_LOG_HANDLERS = ['kvisits.loghandlers.nologhandler.NoLogHandler', 'kvisits.loghandlers.nologhandler.NoLogHandler']
KVISITS_IGNORE_HANDLERS = ['kvisits.ignorehandlers.noignorehandler.NoIgnoreHandler', 'kvisits.ignorehandlers.noignorehandler.NoIgnoreHandler']
KVISITS_IGNORE_URLS = [ '/ignore.*' ]
