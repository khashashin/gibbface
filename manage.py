#!/usr/bin/env python
import os
import sys

from django.conf import settings

ENV = os.getenv('ENV', 'dev')

if __name__ == "__main__":
    if ENV == 'dev':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gibbface.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gibbface.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
