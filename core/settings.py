from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-mkomigbo-thesis-2026-change-in-prod'
DEBUG = True
ALLOWED_HOSTS = ['*']

# FIXED: NO language2 conflict! All 21 subjects SAFE names!
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Core
    'core',
    'subjects',
    'lang1',
    'lang2_app',  # FIXED: was language2 → CONFLICTS!
    'amuzhi_calendar',  # PUBLIC /amuzhi/ - 3-day full + pitch dark - KEEP!
    'africa_weekly',    # PUBLIC /awag/
    # 21 subjects from PHP
    'history',
    'culture',
    'religion',
    'esoterism',
    'tradition',
    'biafra',
    'slavery',
    'nigeria',
    'africa_app',
    'pogrom',
    'uk_diaspora',
    'struggles',
    'resistance',
    'europe',
    'arabs',
    'about_app',
    'people_app',
    'persons',
    'language1_app',
    'uk',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates', BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French - Français'),
    ('es', 'Spanish - Español'),
    ('pt', 'Portuguese - Português'),
    ('sw', 'Swahili - Kiswahili'),
    ('ar', 'Arabic - العربية'),
    ('ig', 'Igbo - Igbo'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'https://mkomigbo24debug.pythonanywhere.com',
    'https://mkomigbo24user.pythonanywhere.com',
]
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False