from django.urls import path
from . import views
app_name = 'amuzhi_calendar'
urlpatterns = [
    path('', views.calendar_view, name='index'),
    path('today/', views.today_view, name='today'),
    path('<int:year>/', views.year_view, name='year'),
    path('<int:year>/<int:month>/', views.month_view, name='month'),
    path('convert/<int:day>/<int:month>/<int:year>/', views.convert_view, name='convert'),
]
