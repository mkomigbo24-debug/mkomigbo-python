from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('awag/', include('africa_weekly.urls')),  # public /awag/ -> africa_weekly app
    path('amuzhi/', include('amuzhi_calendar.urls')), # public /amuzhi/
    path('', include('subjects.urls')),
]
