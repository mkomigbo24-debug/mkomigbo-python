
from django.contrib import admin
from .models import CreatorProfile, Post, Comment, Vote
@admin.register(CreatorProfile)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ['user','wallet_balance_usd','total_views','is_verified']
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','post_type','subject_name','views','likes','revenue_usd','is_hot_topic','created_at']
    list_filter = ['post_type','is_hot_topic']
admin.site.register(Comment)
admin.site.register(Vote)
