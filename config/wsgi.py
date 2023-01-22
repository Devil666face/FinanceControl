import os
import socket
from config.settings import (
    STATIC_ROOT, 
    MEDIA_ROOT,
    DEBUG,
)
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
host = socket.gethostbyname(socket.gethostname())
print(f'Server start on http://{host}')
application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT, prefix='static/')
application.add_files(root=MEDIA_ROOT, prefix="media/")
if not DEBUG:
    from sys import platform
    if platform == "linux" or platform == "linux2":
        os.system('ifconfig|grep inet')
    elif platform == "win32":
        os.system('ipconfig|findstr IPv4')
        os.system(f'start http://{host}')