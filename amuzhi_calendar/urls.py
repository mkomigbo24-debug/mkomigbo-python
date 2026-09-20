from django.urls import path
from. import views

urlpatterns = [
    path('', views.amuzhi_home, name='amuzhi_home'),
    path('search/', views.amuzhi_search, name='amuzhi_search'),
    path('today/', views.amuzhi_today, name='amuzhi_today'),
    path('<int:year>/', views.amuzhi_year, name='amuzhi_year'),
]