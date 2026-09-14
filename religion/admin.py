from django.contrib import admin
from .models import Religion, SacredText, Doctrine, Deity

@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'origin']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SacredText)
class SacredTextAdmin(admin.ModelAdmin):
    list_display = ['title', 'religion', 'language_original']

@admin.register(Doctrine)
class DoctrineAdmin(admin.ModelAdmin):
    list_display = ['title', 'religion']

@admin.register(Deity)
class DeityAdmin(admin.ModelAdmin):
    list_display = ['name', 'religion', 'role', 'is_alusi']
