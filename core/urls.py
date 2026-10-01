from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views_auth, views_sitemap
from . import views as core_views
from django.views.generic import TemplateView, RedirectView

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
    path('blog/', include('blog.urls')),
    path('podcast/', include('podcast.urls')),
    path('awag/', include('africa_weekly.urls')),
    path('amuzhi/', include('amuzhi_calendar.urls')),
    path('ndebe/', RedirectView.as_view(url='/subjects/language1/', permanent=False)),
    path('odinala/', RedirectView.as_view(url='/subjects/spirituality/', permanent=False)),
    path('lang1/', RedirectView.as_view(url='/subjects/language1/', permanent=False)),
    path('lang2/', RedirectView.as_view(url='/subjects/language2/', permanent=False)),
    path('language2/', RedirectView.as_view(url='/subjects/language2/', permanent=False)),
    path('history/', RedirectView.as_view(url='/subjects/history/', permanent=False)),
    path('religion/', RedirectView.as_view(url='/subjects/religion/', permanent=False)),
    path('culture/', RedirectView.as_view(url='/subjects/culture/', permanent=False)),
    path('language1/', RedirectView.as_view(url='/subjects/language1/', permanent=False)),
    path('biafra/', RedirectView.as_view(url='/subjects/biafra/', permanent=False)),
    path('slavery/', RedirectView.as_view(url='/subjects/slavery/', permanent=False)),
    path('nigeria/', RedirectView.as_view(url='/subjects/nigeria/', permanent=False)),
    path('africa/', RedirectView.as_view(url='/subjects/africa/', permanent=False)),
    path('tradition/', RedirectView.as_view(url='/subjects/tradition/', permanent=False)),
    path('esoterism/', RedirectView.as_view(url='/subjects/esoterism/', permanent=False)),
    path('about/', RedirectView.as_view(url='/subjects/about/', permanent=False)),
    path('spirituality/', RedirectView.as_view(url='/subjects/spirituality/', permanent=False)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
