from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url

SECRET_KEY = os.getenv('SECRET_KEY', '')

DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('GIBBFACE_DB_NAME', 'gibbface_db'),
        'USER': os.getenv('GIBBFACE_DB_USER', 'gibbfaceadmin'),
        'PASSWORD': os.getenv('GIBBFACE_DB_PASS', ''),
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['localhost', 'gibbface.iet-gibb.ch', '86.118.65.69']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

try:
    from .local import *
except ImportError:
    pass
