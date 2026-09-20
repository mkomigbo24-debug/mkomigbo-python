from django.urls import path
from . import views

urlpatterns = [
    path('', views.awag_home, name='awag_home'),
    path('region/<str:code>/', views.awag_region, name='awag_region'),
    path('tides/', views.awag_tides, name='awag_tides'),
    path('tide-table/', views.awag_tide_table, name='awag_tide_table'),
    path('farmers/', views.awag_farmers, name='awag_farmers'),
    path('weekly/', views.awag_weekly, name='awag_weekly'),
    path('coding/', views.awag_coding, name='awag_coding'),
    path('api/moon/<str:date_str>/', views.api_moon, name='api_moon'),
    path('api/wind-rain/', views.api_wind_rain, name='api_wind_rain'),
    path('api/tides/', views.api_tides, name='api_tides'),
]