"""
Django settings for borisaelen project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
import vaulthelpers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'vaulthelpers',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'borisaelen.urls'

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
            ],
        },
    },
]

# WSGI_APPLICATION = 'borisaelen.wsgi.application'
WSGI_APPLICATION = 'borisaelen.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Decide which database to use based on the DJANG_DATABASE environment variable
if os.environ.get('DJANGO_DATABASE'):
    if os.environ.get('DJANGO_DATABASE') == 'vault':  
        #Get the database credentails from the vault
        DATABASES = {
            'default': vaulthelpers.database.get_config(),
        }
    elif os.environ.get('DJANGO_DATABASE') == 'dev':  
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
             }
        }     
    elif os.environ.get('DJANGO_DATABASE') == 'prod':  
        #Provide the connection details to your prod database in a my.cnf file
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'OPTIONS': {
                    'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                }
            }
        }
    else:
        raise ValueError('You have provided an unknown DJANGO_DATABASE value.' + os.environ.get('DJANGO_DATABASE'))
else:
    raise ValueError('DJANGO_DATABASE environment variable is not set.')

print(DATABASES)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
X_FRAME_OPTIONS = 'SAMEORIGIN'

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "menubar": True,
    "plugins": "codesample,tabfocus,advlist,autolink,lists,link,image,charmap,print,preview,anchor,searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,code,help,wordcount",
    "toolbar": "undo redo | formatselect fontselect fontsizeselect | codesample bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help",
    "codesample_languages": [
        { "text": 'Powershell', "value": 'powershell' },
        { "text": 'Batch', "value": 'batch' },
        { "text": 'HTML/XML', "value": 'markup' },
        { "text": 'JavaScript', "value": 'javascript' },
        { "text": 'CSS', "value": 'css' },
        { "text": 'JSON', "value": 'json' },
        { "text": 'YAML', "value": 'yaml' },
        { "text": 'BASH', "value": 'bash' },
        { "text": 'SHELL', "value": 'shell' },
        { "text": 'Python', "value": 'python' },
        { "text": 'Ruby', "value": 'ruby' },
        { "text": 'Java', "value": 'java' },
        { "text": 'C', "value": 'c' },
        { "text": 'C#', "value": 'csharp' },
        { "text": 'C++', "value": 'cpp' },
    ],
    'font_formats': 'sans-serif; Roboto, monospace; Roboto Mono,Arial=arial,helvetica,sans-serif; Courier New=courier new,courier,monospace; AkrutiKndPadmini=Akpdmi-n'
}

try:
    from .local_settings import *
except ImportError:
    pass
