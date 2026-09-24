# subjects/urls.py
from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
    path('', views.subject_list, name='list'),  # /subjects/ - 21 subjects, 121 pages
    path('<slug:subject_slug>/', views.subject_detail, name='detail'),  # /subjects/history/
    path('<slug:subject_slug>/<slug:page_slug>/', views.page_detail, name='page'),  # /subjects/history/history-intro/
]