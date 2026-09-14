from django.contrib import admin
from .models import Religion, SacredText, Doctrine, Deity, EsotericTradition, Symbol

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
    list_filter = ['is_alusi', 'religion']

@admin.register(EsotericTradition)
class EsotericTraditionAdmin(admin.ModelAdmin):
    list_display = ['name', 'origin_tradition']

@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    list_display = ['name', 'tradition']
