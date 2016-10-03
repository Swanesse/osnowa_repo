"""
Django settings for osnowa project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '33sitzn^tp-ewjs&-v#9pjtq_hxf6cgxb5!is*t7caw*4+pj(1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    #Tutaj w django/contrib/auth/models.py jest model reprezentujący użytkownika - zarządzający użytkownikami
    #username - 30 znaków lub mniej (litery, cyfry, podkreślenia)
    #first_name - Opcjonalne, 30 znaków lub mniej.
    #last_name - Opcjonalne, 30 znaków lub mniej.
    #email - Opcjonalne, adres email
    #password - Wymagane, hasz i metadane hasła. Szczegóły dalej.
    #is_staff - Boolean. Czy użytkownik ma dostęp do panelu admina
    #is_active - Boolean. Czy użytkownik może się zalogować, czy konto jest aktywne.
    #is_superuser - Boolean. Określa czy użytkownik jest adminem. Admin ma wszystkie uprawnienia bez ich jawnego przypisania.
    #last_login - datetime, przechowuje datę ostatniego logowania
    #date_joined -- przechowuje datę rejestracji     
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'osnowa_app'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'osnowa.urls'

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

WSGI_APPLICATION = 'osnowa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# ścieżka w adresie po której będziemy się odwoływać do plików statycznych (standardowo /static/)
STATIC_URL = '/static/'
#ścieżka do katalogu w którym będą przechowywane wszystkie pliki statyczne. Nie powinniśmy umieszczać tutaj żadnych plików.
STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

#lista katalogów w naszymi plikami statycznymi nie przynależącymi do żadnej konkretnej aplikacji (ogólnostronowymi)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LOGIN_REDIRECT_URL = '/'
