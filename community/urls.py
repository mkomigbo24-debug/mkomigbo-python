
from django.urls import path
from . import views
urlpatterns = [
    path('', views.community_home, name='community_home'),
    path('create/', views.post_create, name='community_create'),
    path('leaderboard/', views.leaderboard, name='community_leaderboard'),
    path('<slug:slug>/', views.post_detail, name='community_detail'),
    path('<slug:slug>/vote/', views.post_vote, name='community_vote'),
]
