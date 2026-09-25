from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views_sitemap
from . import views_auth  # ADD THIS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', views_auth.signup, name='signup'),  # ADD THIS - Before auth.urls
    path('accounts/', include('django.contrib.auth.urls')),
    path('subjects/', include('subjects.urls')),
    path('amuzhi/', include('amuzhi.urls')),
    path('awag/', include('awag.urls')),
    path('lang1/', include('lang1.urls')),
    path('community/', include('community.urls')),
    path('sitemap.xml', views_sitemap.sitemap_view, name='django-sitemap'),
    path('', views_sitemap.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    