from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views_auth
from . import views_sitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', views_auth.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('community/', include('community.urls')),
    path('sitemap.xml', views_sitemap.custom_sitemap, name='sitemap_xml'),
    path('', include('subjects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
