"""
WSGI config for softhub_blog project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'softhub_blog.settings')

application = get_wsgi_application()
