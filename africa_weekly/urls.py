from django.urls import path
from . import views
app_name = 'africa_weekly'
urlpatterns = [
    path('', views.weekly_guide, name='index'),
    path('week/<int:year>/<int:week>/', views.week_view, name='week'),
    path('today/', views.today_guide, name='today'),
]
