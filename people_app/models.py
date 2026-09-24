from django.db import models

class PeopleAppPage(models.Model):
    slug = models.SlugField(unique=True, max_length=200)
    title = models.CharField(max_length=500)
    content = models.TextField()
    php_file = models.CharField(max_length=500, blank=True)
    order = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'slug']
        verbose_name = "PeopleApp Page"
        verbose_name_plural = "PeopleApp Pages"

    def __str__(self):
        return f"{self.order:03d} - {self.title} ({self.slug})"
