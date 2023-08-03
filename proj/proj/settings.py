"""
Django settings for proj project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path


MYSQL_ROOT_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")

RABBITMQ_DEFAULT_USER = os.environ.get("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.environ.get("RABBITMQ_DEFAULT_PASS")

REDIS_HOST = os.environ.get("REDIS_HOST")
MYSQL_HOST = os.environ.get("MYSQL_HOST")
RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST")


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fjs%1*6jl#rgunox-mrb#$d&hu0(1f0u&=7u6_w$i37*+il$9$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'bilibili',
    'youtube'
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

ROOT_URLCONF = 'proj.urls'

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

WSGI_APPLICATION = 'proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    # default  用于存储与django关联的表数据
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangotemplate',
        'HOST': MYSQL_HOST,
        'PORT': 3306,
        'USER': "root",
        'PASSWORD': MYSQL_ROOT_PASSWORD
    },
    'bilibili': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bilibili',
        'HOST': MYSQL_HOST,
        'PORT': 3306,
        'USER': "root",
        'PASSWORD': MYSQL_ROOT_PASSWORD
    },
    'youtube': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'youtube',
        'HOST': MYSQL_HOST,
        'PORT': 3306,
        'USER': "root",
        'PASSWORD': MYSQL_ROOT_PASSWORD
    },
}

DATABASE_ROUTERS = ['proj.database_apps_router.DatabaseAppsRouter']

DATABASE_APPS_MAPPING = {
    "bilibili": "bilibili",
    "youtube": "youtube",
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer', ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'MAX_LIMIT': 20
}


# 解决请求跨域问题配置

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    ['http://127.0.0.1:8080', 'http://localhost:8080']
    # ['http://localhost:*']
)

# CORS_ORIGIN_REGEX_WHITELIST = [ # 可跨域白名单设置
#    "http://192.168.1.112:8080", # 前段请求的IP地址
# ]
CORS_ALLOW_METHODS = ("DELETE", "GET", "OPTIONS",
                      "PATCH", "POST", "PUT")  # 配置允许的请求方式
CORS_ALLOW_HEADERS = (
    "access-control-allow-origin",
    "accept", "accept-encoding", "authorization", "content-type",
    "dnt", "origin", "user-agent", "x-csrftoken", "x-requested-with")  # 配置允许的请求头
