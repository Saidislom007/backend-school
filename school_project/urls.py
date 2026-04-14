from django.contrib import admin
from django.urls import path, include, re_path # re_path qo'shildi
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve # serve import qilindi
from api.views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', include('api.urls')),
]

# Production (Railway) da statik va media fayllarni ko'rsatish uchun
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
else:
    # Lokal rivojlanish jarayonida
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)