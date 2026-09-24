
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

POST_TYPES = [
    ('blog', 'Blog - Long form'),
    ('forum', 'Forum - Debate'),
    ('thread', 'Thread - Hot take'),
    ('reel', 'Reel - 60s video'),
    ('podcast', 'Podcast - Audio'),
]

class CreatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    wallet_balance_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_views = models.IntegerField(default=0)
    stripe_account_id = models.CharField(max_length=100, blank=True)
    wise_email = models.EmailField(blank=True)
    is_verified = models.BooleanField(default=False)
    def __str__(self): return f"{self.user.username} - ${self.wallet_balance_usd}"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    post_type = models.CharField(max_length=10, choices=POST_TYPES, default='blog')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_hot_topic = models.BooleanField(default=False)
    is_monetized = models.BooleanField(default=True)
    revenue_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:40] or "post"
            self.slug = f"{base}-{Post.objects.count()+1}"
        super().save(*args, **kwargs)
    def __str__(self): return self.title
    class Meta: ordering = ['-created_at']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=1)
    class Meta: unique_together = ('post','user')
