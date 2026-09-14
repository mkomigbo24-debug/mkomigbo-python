from django.contrib import admin
from .models import PresentAlphabet, MissingPhoneme
@admin.register(PresentAlphabet)
class PresentAdmin(admin.ModelAdmin):
    list_display = ('symbol','ipa','category','is_dropped')
    list_filter = ('category','is_dropped')
@admin.register(MissingPhoneme)
class MissingAdmin(admin.ModelAdmin):
    list_display = ('symbol','category','ipa')
    list_filter = ('category',)
