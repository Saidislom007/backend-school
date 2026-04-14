import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_project.settings')

application = get_wsgi_application()
# Statik fayllarni xizmat qilish uchun WhiteNoise ulaymiz
application = WhiteNoise(application, root='/app/staticfiles')