from django.contrib import admin
from .models import CreatorProfile, Post, Comment, Vote

@admin.register(CreatorProfile)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet_balance_usd', 'total_views', 'total_likes')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_type', 'views', 'likes', 'revenue_usd', 'is_hot_topic')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Comment)
admin.site.register(Vote)
