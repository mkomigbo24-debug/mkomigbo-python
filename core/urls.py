from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views_auth, views_sitemap
from . import views as core_views

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
    path('awag/', include('africa_weekly.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)