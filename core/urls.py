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
]

# Only include subjects if they exist and have urls.py
# To avoid crash, we add dynamically
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for app in ['history','culture','religion','esoterism','tradition','biafra','slavery','nigeria','africa','pogrom','uk','struggles','resistance','europe','arabs','about','people','persons','language1','lang2_app']:
    # Skip if no urls.py
    urls_path = os.path.join(BASE_DIR, app, 'urls.py')
    if os.path.exists(urls_path):
        urlpatterns.append(path(f'{app}/', include(f'{app}.urls')))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)