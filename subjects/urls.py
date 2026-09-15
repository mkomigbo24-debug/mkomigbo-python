# subjects/urls.py - FINAL - Keep this
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('subjects/<slug:slug>/', views.subject_detail, name='subject_detail'),
    path('subjects/<slug:subject_slug>/<slug:page_slug>/', views.page_detail, name='page_detail'),
]
