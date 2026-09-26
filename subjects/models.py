"""
subjects/models.py - Main hub for 20 subjects, 137 pages
PHP MySQL -> Python PostgreSQL - UPDATE NO OVERWRITE
Keeps amuzhi_calendar untouched!
"""
from django.db import models

class Subject(models.Model):
    SUBJECT_CHOICES = [
        ('history', 'History - 6 pages'),
        ('culture', 'Culture - 5 pages'),
        ('language1', 'Language 1 - 5 pages'),
        ('lang2_app', 'Language 2 - 5 pages - SAFE'),
        ('religion', 'Religion - 15 pages - thesis'),
        ('esoterism', 'Esoterism - 7 pages'),
        ('tradition', 'Tradition - 5 pages'),
        ('biafra', 'Biafra - 5 pages'),
        ('slavery', 'Slavery - 5 pages'),
        ('nigeria', 'Nigeria - 5 pages'),
        ('africa', 'Africa - 5 pages'),
        ('pogrom', 'Pogrom - 5 pages'),
        ('uk', 'UK - 5 pages'),
        ('struggles', 'Struggles - 5 pages'),
        ('resistance', 'Resistance - 5 pages'),
        ('europe', 'Europe - 5 pages'),
        ('arabs', 'Arabs - 5 pages'),
        ('about', 'About - 5 pages'),
        ('people', 'People - 5 pages'),
        ('persons', 'Persons - 5 pages'),
        ('spirituality', 'Igbo Spirituality - 7 pages - EKE ORIE AFO NKWO'),
    ]
    slug = models.SlugField(unique=True, choices=SUBJECT_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    page_count = models.IntegerField(default=5)
    order = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.page_count} pages)"

class Page(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='pages')
    slug = models.SlugField(unique=True, help_text="e.g., history-s01")
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500, blank=True)
    content = models.TextField(help_text="Full HTML from PHP - as is")
    content_enhanced = models.TextField(blank=True)
    sources = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['subject', 'order']

    def __str__(self):
        return f"{self.subject.slug} - {self.slug} - {self.title[:50]}"