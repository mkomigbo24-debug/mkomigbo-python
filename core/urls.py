from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subjects/', include('subjects.urls')),
    path('amuzhi/', include('amuzhi_calendar.urls')),
    path('awag/', include('africa_weekly.urls')),
    path('lang1/', include('lang1.urls')),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    if hasattr(settings, 'MEDIA_URL'):
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)