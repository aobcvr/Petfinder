
import os
from . local import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AUTH_USER_MODEL = 'listanimal.CustomUser'

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'listanimal',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'django_db_logger'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rest.views.LoggerRequest'
]

ROOT_URLCONF = 'petfinder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'petfinder.wsgi.application'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ]
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'photos',
        'USER': 'postgres',
        'PASSWORD': 'qazwsx1861',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CELERY_BROKER_URL='redis://localhost:6379'

CELERY_ACCEPT_CONTENT=['json']
CELERY_TASK_SERIALIZER='json'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'log_news': {
            'level': 'ERROR',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler',
        },
        'log_animal': {
            'level': 'ERROR',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler',
        },
        'log_rest': {
            'level': 'ERROR',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler',
        },
    },
    'loggers': {
        'commands.createnews': {
            'handlers': ['log_news'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
    'loggers': {
        'commands.createanimal': {
            'handlers': ['log_animal'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
    'loggers': {
        'rest.views': {
            'handlers': ['log_rest'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
#EMAIL_HOSTE=EMAIL_HOST
#EMAIL_HOST_USER=EMAIL_HOST_USER
#EMAIL_HOST_PASSWORD=EMAIL_HOST_PASSWORD
#EMAIL_PORT = EMAIL_PORT
#SECRET_KEY = SECRET_KEY
EMAIL_USE_TLS = True
STATIC_URL = '/static/'