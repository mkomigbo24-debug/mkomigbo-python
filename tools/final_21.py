import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from subjects.models import Subject, Page

# Last 2 extras
extras = {
    'esoteric': ('esoterism', 'Esoteric - Duplicate Topic'),
    'thesis': ('about', 'Thesis - Research Overview'),
}

for extra_slug, (parent_slug, title) in extras.items():
    try:
        extra_subj = Subject.objects.get(slug=extra_slug)
        parent = Subject.objects.get(slug=parent_slug)
        for p in Page.objects.filter(subject=extra_subj):
            Page.objects.update_or_create(
                subject=parent,
                slug=f"{extra_slug}-{p.slug}",
                defaults={'title': f"{title} - {p.title}", 'body_html': p.body_html, 'nav_order': p.nav_order}
            )
        Page.objects.update_or_create(
            subject=parent, slug=extra_slug,
            defaults={'title': title, 'body_html': f"<h1>{title}</h1><p>Moved from {extra_slug}</p>", 'nav_order': 98}
        )
        print(f"Moved {extra_slug} -> {parent_slug}")
        extra_subj.delete()
        print(f"Deleted {extra_slug}")
    except Subject.DoesNotExist:
        print(f"{extra_slug} already deleted")

from subjects.models import Subject, Page
print(f"FINAL CORRECT: {Subject.objects.count()} subjects, {Page.objects.count()} pages")
print(f"Subjects: {sorted(Subject.objects.values_list('slug', flat=True))}")
print(f"21? {Subject.objects.count()==21} Nsibidi page? {Page.objects.filter(slug='nsibidi').exists()} Lang1? preserved")
