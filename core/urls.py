from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views_auth, views_sitemap
from . import views as core_views
from django.views.generic import TemplateView
import os

urlpatterns = [
    path('', core_views.landing, name='landing'),
    path('home/', core_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/signup/', views_auth.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('community/', include('community.urls')),
    path('sitemap.xml', views_sitemap.custom_sitemap, name='sitemap_xml'),
    path('observation/add/', core_views.add_observation, name='observation_add'),
    path('subjects/', include('subjects.urls')),
    path('amuzhi/', include('amuzhi_calendar.urls')),
    path('awag/', include('africa_weekly.urls')),  # Your remote uses africa_weekly folder
    path('ndebe/', TemplateView.as_view(template_name='ndebe_viewer.html'), name='ndebe'),
    path('odinala/', TemplateView.as_view(template_name='odinala_viewer.html'), name='odinala'),
    path('lang1/', TemplateView.as_view(template_name='lang1_viewer.html'), name='lang1'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)