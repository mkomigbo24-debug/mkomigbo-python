from django.db import models

class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    nav_order = models.IntegerField()
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, default='active')
    
    class Meta:
        ordering = ['nav_order']
    
    def __str__(self):
        return f"{self.nav_order}. {self.name}"

class Page(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='pages')
    slug = models.SlugField()  # intro, overview, etc
    title = models.CharField(max_length=200)
    body_html = models.TextField()
    nav_order = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ['subject', 'slug']
        ordering = ['nav_order']
    
    def __str__(self):
        return f"{self.subject.slug}/{self.slug} - {self.title}"