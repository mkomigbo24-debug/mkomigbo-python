from django.contrib.sitemaps import Sitemap

class StaticSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    def items(self):
        return ['/', '/amuzhi/', '/awag/', '/subjects/']
    def location(self, item):
        return item

class SubjectSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    def items(self):
        try:
            from subjects.models import Page
            return Page.objects.filter(is_published=True)[:200]
        except:
            return []
    def location(self, obj):
        try:
            return f"/subjects/{obj.subject.slug}/{obj.slug}/"
        except:
            return "/subjects/"

sitemaps = {
    'static': StaticSitemap,
    'subjects': SubjectSitemap,
}