from django.urls import path
from . import views

app_name = 'amuzhi_calendar'

urlpatterns = [
    path('', views.calendar_view, name='index'),
    path('today/', views.today_view, name='today'),
    path('convert/<int:day>/<int:month>/<int:year>/', views.convert_view, name='convert'),
]
