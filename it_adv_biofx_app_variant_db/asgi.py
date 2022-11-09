"""
ASGI config for it_adv_biofx_app_variant_db project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_adv_biofx_app_variant_db.settings')

application = get_asgi_application()
