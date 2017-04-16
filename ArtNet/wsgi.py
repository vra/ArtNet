"""
WSGI config for ArtNet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys                                                                                                                                                    
from os.path import dirname, abspath                                                                                                                    
from django.core.wsgi import get_wsgi_application                                                                                                             
PROJECT_DIR = dirname(dirname(abspath(__file__)))                                                                                                             
sys.path.insert(0, PROJECT_DIR) 

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ArtNet.settings")

application = get_wsgi_application()
