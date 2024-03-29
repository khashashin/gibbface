"""
WSGI config for gibbface project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

ENV = os.getenv('ENV', '')

if ENV == 'dev':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gibbface.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gibbface.settings.production")

application = get_wsgi_application()
