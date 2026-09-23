from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # PUBLIC - Amuzhi - 3-day Full + Pitch Dark - DONE 200 OK
    path('amuzhi/', include('amuzhi_calendar.urls')),
    # PUBLIC - AWAG
    path('awag/', include('africa_weekly.urls')),
    # Subjects hub
    path('subjects/', include('subjects.urls')),
    # 20 subjects - SAFE names
    path('history/', include('history.urls')),
    path('culture/', include('culture.urls')),
    path('language1/', include('language1_app.urls')),
    path('lang2/', include('lang2_app.urls')),
    path('language2/', include('lang2_app.urls')),
    path('religion/', include('religion.urls')),
    path('esoterism/', include('esoterism.urls')),
    path('tradition/', include('tradition.urls')),
    path('biafra/', include('biafra.urls')),
    path('slavery/', include('slavery.urls')),
    path('nigeria/', include('nigeria.urls')),
    path('africa/', include('africa_app.urls')),
    path('pogrom/', include('pogrom.urls')),
    path('uk/', include('uk_diaspora.urls')),
    path('uk-diaspora/', include('uk_diaspora.urls')),
    path('struggles/', include('struggles.urls')),
    path('resistance/', include('resistance.urls')),
    path('europe/', include('europe.urls')),
    path('arabs/', include('arabs.urls')),
    path('about/', include('about_app.urls')),
    path('people/', include('people_app.urls')),
    path('persons/', include('persons.urls')),
    path('lang1/', include('lang1.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)