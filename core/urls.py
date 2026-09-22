from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('amuzhi/', include('amuzhi_calendar.urls')), # PUBLIC - easily accessible
    path('awag/', include('africa_weekly.urls')), # PUBLIC - /awag/ -> africa_weekly app - no conflict!
    path('', include('subjects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
