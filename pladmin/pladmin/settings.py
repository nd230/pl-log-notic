"""
Django settings for pladmin project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# 注意，在生产环境，请使用环境变量 SECRET_KEY 来配置。
if "SECRET_KEY" in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]
else:
    # 下面这个初始化项目就有的，应该仅用于本地开发
    SECRET_KEY = '+&=ul0qc_9=&0^y8bw6y5fyu3wd@v#e8w7pb)%z@hc60=lo6fy'

# 如果是生产环境，那么关闭 Debug 模式
if ("ENV" in os.environ) and ("production" == os.environ["ENV"]):
    DEBUG = False
else:
    DEBUG = True

# 就算不是生产环境，明确设置环境变量 DEBUG=False 那么也关闭 DEBUG 模式
if ("DEBUG" in os.environ) and ("False" == os.environ["DEBUG"]):
    DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'pltplconf.apps.PltplconfConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_apscheduler',
    #'pltplconf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pladmin.urls'

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

WSGI_APPLICATION = 'pladmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 20,
        }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# 模块
PL_PIPLINES = [
    'pltplconf.management.commands.Piplines.OrderSystemCommon',
    'pltplconf.management.commands.Piplines.XLogSystemQuery'
]

# es地址
ES_ADDRESS = {
    'ip': '127.0.0.1',
    'host': 'www.example.com.cn'
}

XES_ADDRESS = {
    'ip': '127.0.0.2',
    'host': 'www.example2.com.cn',
    'http_auth': 'user:password'
}

MESSAGERS_CONFIG = {
    "WxTeam": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=0000000000000000000"
}

# 日志处理
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

# 在DEBUG模式下启用大量日志输出
if DEBUG:
    LOGGING['root']['level'] = 'DEBUG'

