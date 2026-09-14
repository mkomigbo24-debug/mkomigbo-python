from django.contrib import admin
from .models import EsotericTradition, Symbol

@admin.register(EsotericTradition)
class EsotericTraditionAdmin(admin.ModelAdmin):
    list_display = ['name', 'origin_tradition']

@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    list_display = ['name', 'tradition']
