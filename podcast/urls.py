from django.urls import path
from . import views
urlpatterns=[
 path('', views.podcast_list, name='podcast_list'),
 path('<slug:podcast_slug>/', views.episode_list, name='episode_list'),
 path('<slug:podcast_slug>/<slug:episode_slug>/', views.episode_detail, name='episode_detail'),
]
