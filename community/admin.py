from django.contrib import admin
from .models import Post, Comment, Vote, CreatorProfile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','post_type','author','views','likes','revenue_usd','created_at')
    list_filter = ('post_type','is_hot_topic')
    search_fields = ('title','body')

@admin.register(CreatorProfile)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('id','user','wallet_balance_usd','total_views','total_likes')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','post','author','created_at')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('id','post','user','created_at')
