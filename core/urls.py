from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views_sitemap import custom_sitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('subjects/', include('subjects.urls')),
    path('amuzhi/', include('amuzhi_calendar.urls')),
    path('awag/', include('africa_weekly.urls')),
    path('lang1/', include('lang1.urls')),
    path('community/', include('community.urls')),
    path('sitemap.xml', custom_sitemap, name='django-sitemap'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
