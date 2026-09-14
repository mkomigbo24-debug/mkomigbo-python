from django.contrib import admin
from .models import PresentAlphabet, MissingPhoneme

@admin.register(PresentAlphabet)
class PresentAlphabetAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'ipa', 'category', 'is_dropped']
    list_filter = ['category', 'is_dropped']

@admin.register(MissingPhoneme)
class MissingPhonemeAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'ipa', 'category']
    list_filter = ['category']
