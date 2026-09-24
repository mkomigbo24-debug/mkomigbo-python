# core/views_sitemap.py - CUSTOM SITEMAP - NO TEMPLATE NEEDED - 200 OK GUARANTEED
from django.http import HttpResponse

def custom_sitemap(request):
    from core.sitemap import sitemaps
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    base = "https://mkomigbo24user.pythonanywhere.com"
    
    # Static - 4 URLs
    for path in ['/', '/amuzhi/', '/awag/', '/subjects/']:
        xml.append(f"<url><loc>{base}{path}</loc><priority>0.9</priority></url>")
    
    # Subjects - 121 pages from DB
    try:
        from subjects.models import Page
        for p in Page.objects.filter(is_published=True)[:200]:
            try:
                loc = f"{base}/subjects/{p.subject.slug}/{p.slug}/"
                xml.append(f"<url><loc>{loc}</loc><priority>0.8</priority></url>")
            except:
                pass
    except Exception as e:
        xml.append(f"<!-- error {e} -->")
    
    xml.append("</urlset>")
    return HttpResponse("\n".join(xml), content_type="application/xml")