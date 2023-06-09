"""
Django settings for Milostafa project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1(4iz@lhpc(klhi_89ibnmm5e2*s&0iv5xwth-c#f-)5#adv8('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EMAILBACKEND'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.Registro',
    'apps.Usuario',
    'apps.Componente',
    'rest_framework',
    'social_django',  # <--- this
    'social.apps.django_app.default',
    'pwa',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', # <--- this
]

ROOT_URLCONF = 'Milostafa.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
                'social.backends.facebook.FacebookAppOAuth2',
                'social.backends.facebook.FacebookOAuth2',
                'django.contrib.auth.backends.ModelBackend',
                'social_core.backends.facebook.FacebookOAuth2',
                'social_core.backends.github.GithubOAuth2',
                'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_LOGIN_REDIRECT_URL='/'

SOCIAL_AUTH_FACEBOOK_KEY = '1079309075844209'
SOCIAL_AUTH_FACEBOOK_SECRET = '486340cc2ccf54446af9fc6fa74cfdf6'

SOCIAL_AUTH_GITHUB_KEY = '6317965eec9a36b1e10d'
SOCIAL_AUTH_GITHUB_SECRET = '8f3234400b1c46bb57e37194849a5a0c1873f8a9'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '967816004665-duq342ssig71tstdmdjjc4dv0in00ii7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '1R_YVdVma8xPSsUC3LRLVGb9'

WSGI_APPLICATION = 'Milostafa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images')
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'static-only')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'milostafaoficial@gmail.com'
EMAIL_HOST_PASSWORD = 'grcxflbppyfljzxf'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Milostafa Team <noreply@milostafa.com>'



LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"


# PWA
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

PWA_APP_NAME = 'Milostafa'
PWA_APP_DESCRIPTION = 'Milostafa APP'
PWA_APP_THEME_COLOR = '#87EFC3'
PWA_APP_BACKGROUND_COLOR = '#fff'
PWA_APP_ICONS = [
    {
        'src': '/static/images/icons/milos.png',
        'sizes': '128x128'
    },
    {
        'src': '/static/images/icons/milos1.png',
        'sizes': '256x256'
    },
    {
        'src': '/static/images/icons/milos2.png',
        'sizes': '512x512'
    }
]
