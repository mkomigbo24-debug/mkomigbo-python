from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
POST_TYPES = [('blog','Blog'),('forum','Forum'),('thread','Thread'),('reel','Reel'),('podcast','Podcast'),('poll','Poll'),('news','News'),('market','Market'),('job','Job'),('event','Event')]
class CreatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_balance_usd = models.FloatField(default=0.0)
    total_views = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    def __str__(self): return self.user.username
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    post_type = models.CharField(max_length=20, choices=POST_TYPES, default='thread')
    subject_name = models.CharField(max_length=100, blank=True)
    is_hot_topic = models.BooleanField(default=False)
    is_monetized = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    revenue_usd = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50] + "-" + uuid.uuid4().hex[:6]
        super().save(*args, **kwargs)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        unique_together = ('post','user')