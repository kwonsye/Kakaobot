"""
WSGI config for bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys

sys.path.append("/home/ubuntu/Django/bot")
#sys.path.append('/home/ubuntu/Django/bot')
sys.path.append("/home/ubuntu/Django/myvenv/lib/python3.5/site-packages")

from django.core.wsgi import get_wsgi_application
#path='/home/ubuntu/Django/bot'
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
	sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE']='bot.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bot.settings")

application = get_wsgi_application()
