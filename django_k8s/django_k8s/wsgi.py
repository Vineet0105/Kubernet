"""
WSGI config for django_k8s project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path
import dotenv

CUR_DIR = Path(__file__).resolve().parent
BASE_DIR = CUR_DIR.parent
ENV_FILE_PATH = BASE_DIR / '.env'

from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv(str(ENV_FILE_PATH))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_k8s.settings')

application = get_wsgi_application()
