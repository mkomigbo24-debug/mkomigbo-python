from django.contrib import admin
from .models import Category, Post
admin.site.register(Category)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','author','is_published','created_at')
