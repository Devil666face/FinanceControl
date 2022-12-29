import os
from config.settings import STATIC_ROOT, MEDIA_ROOT
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT, prefix='static/')
application.add_files(root=MEDIA_ROOT, prefix="media/")