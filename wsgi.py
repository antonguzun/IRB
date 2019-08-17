"""
WSGI config for untitled project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import newrelic.agent


newrelic.agent.initialize("newrelic.ini")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = newrelic.agent.WSGIApplicationWrapper(get_wsgi_application())