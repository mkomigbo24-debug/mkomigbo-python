from django.urls import path
from . import views

app_name = 'amuzhi'

urlpatterns = [
    path('', views.index, name='index'),
    path('today/', views.today_view, name='today'),
    path('calculator/', views.market_calculator_view, name='calculator'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('festival/', views.festival_view, name='festival'),
    path('<int:year>/', views.year_view, name='year'),
    path('<int:year>/<int:month>/', views.month_view, name='month'),
    path('convert/<int:day>/<int:month>/<int:year>/', views.convert_view, name='convert'),
]
