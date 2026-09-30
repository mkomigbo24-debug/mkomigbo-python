from django.db import models

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    cover = models.ImageField(upload_to='podcast/covers/', blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title

class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    audio = models.FileField(upload_to='podcast/episodes/')
    description = models.TextField()
    duration = models.CharField(max_length=20, blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
    class Meta:
        ordering = ['-published_at']
