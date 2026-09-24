from django.contrib.sitemaps import Sitemap
from subjects.models import Page
from django.urls import reverse

class StaticSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    def items(self):
        return ['home', 'amuzhi', 'awag']
    def location(self, item):
        return reverse(item) if item != 'home' else '/'

class SubjectSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    def items(self):
        return Page.objects.all()
    def lastmod(self, obj):
        return obj.updated_at if hasattr(obj, 'updated_at') else None

sitemaps = {
    'static': StaticSitemap,
    'subjects': SubjectSitemap,
}
