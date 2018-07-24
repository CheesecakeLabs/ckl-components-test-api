import os
from os.path import dirname, join, exists, abspath

import environ

# Load operating system env variables and prepare to use them
env = environ.Env()

# .env file, should load only in development environment
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))

# Quick-start development settings - unsuitable for production
SECRET_KEY = env('DJANGO_SECRET_KEY', default='8#ubdv*jh_1u(6m4)^s^*pdo!&y_#jz)vv%5cp%8^*&%ztttxq')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', False)

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', [])

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'cklauth',
]

PROJECT_APPS = [
    'users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },

    },
]

WSGI_APPLICATION = 'app.wsgi.application'

SITE_ID = 1

# Database

DATABASES = {
    'default': env.db(),
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [{
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
}]

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

# Media files (uploads)

if DEBUG:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_ROOT = 'uploads/'
    MEDIA_URL = '/uploads/'

# Email settings

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'no-reply@localhost'
else:
    ANYMAIL = {
        'MAILGUN_API_KEY': env('MAILGUN_API_KEY', default=''),
        'MAILGUN_SENDER_DOMAIN': env('MAILGUN_DOMAIN', default=''),
    }
    EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
    DEFAULT_FROM_EMAIL = 'noreply@ckl-components-api.herokuapp.com'

# Django Rest Framework Settings

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# Authentication

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'cklauth.auth.EmailOrUsernameModelBackend',
)

CKL_REST_AUTH = {
  'LOGIN_FIELD': 'email',
  'REGISTER_FIELDS': ('email', 'first_name', 'last_name'),

  # Google authentication settings (optional)
  'GOOGLE': {
      'CLIENT_ID': env('GOOGLE_CLIENT_ID', default=''),
      'CLIENT_SECRET': env('GOOGLE_CLIENT_SECRET', default=''),
      'REDIRECT_URI': env('GOOGLE_REDIRECT_URI', default=''),
      'AUTH_FIELD_GENERATOR': None,
      'USER_INFO_MAPPING': {
          'first_name': 'given_name',
          'last_name': 'family_name',
          'email': 'email',
      },
  },

  # Facebook authentication settings (optional)
  'FACEBOOK': {
      'CLIENT_ID': env('FACEBOOK_CLIENT_ID', default=''),
      'CLIENT_SECRET': env('FACEBOOK_CLIENT_SECRET', default=''),
      'REDIRECT_URI': env('FACEBOOK_REDIRECT_URI', default=''),
      'AUTH_FIELD_GENERATOR': None,
      'USER_INFO_MAPPING': {
          'first_name': 'first_name',
          'last_name': 'last_name',
          'email': 'email',
      },
  },
}


# Logs

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
