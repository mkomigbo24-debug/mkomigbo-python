from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subjects/', include('subjects.urls')),
    path('amuzhi/', include('amuzhi_calendar.urls')),
    path('awag/', include('africa_weekly.urls')),  # <-- ADD THIS! FIX 404!
    path('lang1/', include('lang1.urls')),
    path('', views.home, name='home'),
]
