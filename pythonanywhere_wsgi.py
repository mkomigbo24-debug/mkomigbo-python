import os, sys
path = '/home/mkomigbo24/mkomigbo-python'
if path not in sys.path: sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()