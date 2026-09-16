from django.urls import path
from . import views

urlpatterns = [
    path('phonemes/', views.phonemes_view, name='lang1_phonemes'),
]

