from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('amuzhi/', include('amuzhi_calendar.urls')), # PUBLIC - easily accessible
    path('awag/', include('africa_weekly.urls')), # PUBLIC - /awag/ -> africa_weekly app - no conflict!
    path('', include('subjects.urls')),
]
