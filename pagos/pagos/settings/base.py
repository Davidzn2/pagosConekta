import os
from unipath import Path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR =Path(__file__).ancestor(3)
SECRET_KEY = 'pa40iz9v98tcl(k_jkq85y19%3fiz*3&4r_n*=^ca7(48rx5&r'

DJANGO_APPS = (
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

	)
LOCAL_APPS = (
	'apps.main',
	)

THIRD_PARTY_APPS = (

    )
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pagos.urls'

WSGI_APPLICATION = 'pagos.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
