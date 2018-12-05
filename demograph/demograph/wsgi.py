"""
WSGI config for demograph project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
try:
    sys.path.insert(0, '/var/www/demograph/code/demograph')
except:
    pass

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demograph.settings')

application = get_wsgi_application()
