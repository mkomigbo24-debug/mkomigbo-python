import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from subjects.models import Subject, Page

original_21 = ['about','africa','arabs','biafra','culture','esoterism','europe','history','language1','language2','nigeria','people','persons','pogrom','religion','resistance','slavery','spirituality','struggles','tradition','uk']

print(f"BEFORE: {Subject.objects.count()} subjects")
all_slugs = list(Subject.objects.values_list('slug', flat=True))
extra = [s for s in all_slugs if s not in original_21]
print(f"Extra to convert: {extra}")

mapping = {
    'igbo-language': ('language1', 'Igbo Language'),
    'ndebe-49': ('language1', 'Ndebe 49 - 49 Glyphs'),
    'ndebe-glyphs': ('language1', 'Ndebe Glyphs H Effect'),
    'nsibidi': ('language1', 'Nsibidi - 500 Symbols MUST NOT FORGET'),
    'amuzhi-calendar': ('culture', 'Amuzhi Calendar'),
    'awag': ('africa', 'AWAG - Africa Weekly Guide'),
    'odinala': ('religion', 'Odinala'),
    'history-ndigbo': ('history', 'History Ndigbo'),
    'proverbs': ('culture', 'Ilu - Proverbs'),
    'folktales': ('culture', 'Akuko - Folktales'),
    'medicine': ('culture', 'Ogwu - Medicine'),
    'astronomy': ('culture', 'Igbo Astronomy'),
    'igbo-astronomy': ('culture', 'Igbo Astronomy'),
    'mathematics': ('culture', 'Igbo Mathematics'),
    'music': ('culture', 'Igbo Music'),
    'dance': ('culture', 'Igbo Dance'),
    'art': ('culture', 'Igbo Art'),
    'food': ('culture', 'Igbo Food'),
    'governance': ('culture', 'Igbo Governance'),
    'igbo-culture': ('culture', 'Igbo Culture Overview'),
    'culture': ('culture', 'Igbo Culture Overview'), # if duplicate
}

for extra_slug in extra:
    if extra_slug not in mapping:
        print(f"Skip {extra_slug}")
        continue
    parent_slug, page_title = mapping[extra_slug]
    try:
        extra_subj = Subject.objects.get(slug=extra_slug)
        parent = Subject.objects.get(slug=parent_slug)
        pages = list(Page.objects.filter(subject=extra_subj))
        for p in pages:
            Page.objects.update_or_create(
                subject=parent,
                slug=f"{extra_slug}-{p.slug}",
                defaults={'title': f"{page_title} - {p.title}", 'body_html': p.body_html, 'nav_order': p.nav_order}
            )
        Page.objects.update_or_create(
            subject=parent,
            slug=extra_slug,
            defaults={'title': page_title, 'body_html': f"<h1>{page_title}</h1><p>Topic preserved as page inside {parent_slug} - was subject {extra_slug}</p>", 'nav_order': 99}
        )
        print(f"Moved {extra_slug} -> {parent_slug}")
    except Exception as e:
        print(f"Error {extra_slug}: {e}")

print(f"AFTER MOVE: {Subject.objects.count()} subjects, {Page.objects.count()} pages")

# Delete extra subjects
for extra_slug in extra:
    if extra_slug in mapping:
        Subject.objects.filter(slug=extra_slug).delete()
        print(f"Deleted subject {extra_slug}")

from subjects.models import Subject, Page
print(f"FINAL: {Subject.objects.count()} subjects (should be 21), {Page.objects.count()} pages")
print(f"Remaining: {sorted(Subject.objects.values_list('slug', flat=True))}")
print(f"Nsibidi page? {Page.objects.filter(slug='nsibidi').exists()}")
