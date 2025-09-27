"""
ASGI config for fashion_store project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fashion_store.settings')

application = get_asgi_application()
