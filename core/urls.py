from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lang1/', include('lang1.urls')),  # advanced 49 phonemes
    path('', include('subjects.urls')),  # 21 subjects
]