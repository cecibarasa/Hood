"""
ASGI config for Hood project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from some_asgi_library import AmazingMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hood.settings')

application = get_asgi_application()

application = AmazingMiddleware(application)
