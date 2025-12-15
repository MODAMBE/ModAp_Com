<<<<<<< HEAD
"""
WSGI config for ModApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModApp.settings')
=======
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModApp.settings")
>>>>>>> 2a352f9 (Premier commit du projet ModApp)

application = get_wsgi_application()
