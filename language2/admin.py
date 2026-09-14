from django.contrib import admin
from .models import Tone, GrammarRule, Dialect, Sentence

@admin.register(Tone)
class ToneAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'tone_type', 'example1', 'example2']
    list_filter = ['tone_type']

@admin.register(GrammarRule)
class GrammarRuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category']

@admin.register(Dialect)
class DialectAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ['igbo', 'translation']
