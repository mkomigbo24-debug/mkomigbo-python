from django.db import models
class SiteObservation(models.Model):
    page_url = models.CharField(max_length=500)
    observation = models.TextField()
    visitor_name = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(blank=True)
    is_reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.page_url[:50]} - {self.observation[:30]}"
