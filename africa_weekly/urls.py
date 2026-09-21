from django.urls import path
from . import views
app_name = 'africa_weekly'
urlpatterns = [
    path('', views.weekly_guide, name='index'),
    path('tides/', views.tides_view, name='tides'),
    path('farming/', views.farming_view, name='farming'),
    path('regions/', views.regions_view, name='regions'),
    path('week/<int:year>/<int:week>/', views.week_view, name='week'),
    path('today/', views.today_guide, name='today'),
]
