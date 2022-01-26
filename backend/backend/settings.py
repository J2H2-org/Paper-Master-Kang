"""
Django settings for backend project.

Generated by 'backend-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '$yx3jf3y@r)%g+479&f*&(8o9@%quk#zwf57i0w^*)y9_vx9ka'
SECRET_KEY = os.getenv('SECRET_KEY', 'foo')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv('DEBUG', 1))

if os.getenv('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(' ')
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'chatphone.apps.ChatphoneConfig',
    'corsheaders',
    # 'drf_yasg', #TODO: 이거 도커에서 실행할 때 모듈을 못찾음 (로컬에서 runserver로 실행하면 실행됨)
    'djongo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# TODO DB설정 해야됨

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propogate': False,
                }
            },
        },
        'NAME': 'cp_items',
        'CLIENT': {
            'host': 'mongo',
            # 'host': 'localhost',
            # 'port': 9017,
            'username': 'root',
            'password': "temppw",
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'backend.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'backend.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'backend.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'backend.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CORS realted settings

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOW_METHODS = ['DELETE','GET','OPTIONS','PATCH','POST','PUT']

CORS_ORIGIN_WHITELIST = ['http://localhost:8000',
                         'http://localhost:8081',
                         'http://localhost:9017',
                         'http://localhost:80',
                         'http://localhost']

CORS_ALLOW_CREDENTIALS = True

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
