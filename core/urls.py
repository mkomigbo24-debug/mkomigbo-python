from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('awag/', include('awag.urls')),
    path('amuzhi/', include('amuzhi_calendar.urls')),
    path('', include('subjects.urls')), # your home
    # ... keep your other paths
]
