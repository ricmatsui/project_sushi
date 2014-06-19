"""
Django settings for project_sushi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '&q(pxkzx)z(u5lb0hcy@pwm=am)c0&12$lz02i_pca3)%e8x3*')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', True))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Management

ADMINS = (('Project Sushi Admin', os.environ.get('ADMIN_EMAIL', 'admin@example.com')),)
SERVER_EMAIL = os.environ.get('SERVER_EMAIL', 'server@example.com')

# Email

EMAIL_FROM = SERVER_EMAIL
if DEBUG:
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'debug_toolbar',
    'pipeline',
    'core',
    'projects',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project_sushi.urls'

WSGI_APPLICATION = 'project_sushi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project_sushi',
        'USER': 'project_sushi',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', '123456'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Pipeline

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_COMPILERS = (
  'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'bootstrap/less/bootstrap.less',
        ),
        'output_filename': 'bootstrap/css/bootstrap.css',
    },
    'projects': {
        'source_filenames': (
            'projects/less/projects.less',
        ),
        'output_filename': 'projects/css/projects.css',
    }
}

PIPELINE_JS = {
    'bootstrap': {
        'source_filenames': (
            'bootstrap/js/affix.js',
            'bootstrap/js/alert.js',
            'bootstrap/js/button.js',
            'bootstrap/js/carousel.js',
            'bootstrap/js/collapse.js',
            'bootstrap/js/dropdown.js',
            'bootstrap/js/modal.js',
            'bootstrap/js/scrollspy.js',
            'bootstrap/js/tab.js',
            'bootstrap/js/tooltip.js',
            'bootstrap/js/transition.js',
            'bootstrap/js/popover.js',
        ),
        'output_filename': 'bootstrap/js/bootstrap.js',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
