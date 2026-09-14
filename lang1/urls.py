from django.urls import path
from . import views
urlpatterns = [
    path('subjects/language1/phonemes/', views.phonemes_view, name='phonemes'),
]
