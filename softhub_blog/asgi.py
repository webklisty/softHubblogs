"""
ASGI config for softhub_blog project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'softhub_blog.settings')

application = get_asgi_application()
