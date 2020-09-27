
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
AUTH_USER_MODEL = 'listanimal.CustomUser'

DEBUG = True

ALLOWED_HOSTS = []

CUSTOM_APPS=['listanimal']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
]+CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rest.middlweare.LoggerRequest'
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
    ]
}
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
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
        'log_error_request': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename':'logger/request_err.log'
        },
        'error_create_news': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename':'logger/news.log'
        },
        'error_create_advertisement': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename':'logger/advertisement.log'
        }
    },
    'loggers': {
        'rest.views': {
            'handlers': ['log_error_request'],
            'level': 'ERROR',
            'propagate': True,
        },
        'commands.createnews': {
            'handlers': ['error_create_news'],
            'level': 'ERROR',
            'propagate': True,
        },
        'commands.createanimal': {
            'handlers': ['error_create_advertisement'],
            'level': 'ERROR',
            'propagate': True,
        }
    },
}


EMAIL_USE_TLS = True
STATIC_URL = '/static/'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
}

REDOC_SETTINGS = {
   'LAZY_RENDERING': False,
}
FIXTURES_DIR = os.path.join(PROJECT_ROOT, 'Petfinder/fixtures')
FIXTURES_APPS = CUSTOM_APPS


try:
    from . local import *
except ImportError:
    pass

LOG_DIR = os.path.join(BASE_DIR,'logger')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)