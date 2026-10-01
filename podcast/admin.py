from django.contrib import admin
from .models import Podcast, Episode
admin.site.register(Podcast)
@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','podcast','is_published','published_at')
