from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-mkomigbo-thesis-2026-change-in-production'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'django.contrib.sites','django.contrib.sitemaps',
    'community','core','subjects','lang1','language1','amuzhi_calendar','africa_weekly',
    'history','culture','religion','esoterism','tradition','biafra','slavery','nigeria',
    'africa','pogrom','uk','struggles','resistance','europe','arabs','about','people','persons',
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
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'core' / 'templates', BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'core.context_processors.site_branding',
    ]},
}]
WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3'}}
AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CSRF_TRUSTED_ORIGINS = ['https://mkomigbo24user.pythonanywhere.com','https://mkomigbo.com','https://nkomigbo.com']
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SITE_ID = 1
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/community/'
LOGOUT_REDIRECT_URL = '/community/'
SITE_NAME = "Nkomigbo"
OLD_NAME = "Mkomigbo"
SITE_TAGLINE = "Nko mi Igbo - Meditation on Igbo"