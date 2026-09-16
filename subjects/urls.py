# subjects/urls.py - FINAL - 49 phonemes + H effect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('subjects/<slug:slug>/', views.subject_detail, name='subject_detail'),
    path('subjects/<slug:subject_slug>/<slug:page_slug>/', views.page_detail, name='page_detail'),
    # Ndebe 49 - specific routes FIRST before <slug>
    path('scripts/ndebe-49/', views.ndebe_49, name='ndebe_49'),
    path('ndebe/glyphs/', views.ndebe_glyphs, name='ndebe_glyphs'),  # H effect - hover 49 glyphs visual
    path('scripts/<slug:slug>/', views.script_detail, name='script_detail'),
]
