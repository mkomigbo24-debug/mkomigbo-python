from django.contrib import admin
from .models import CulturalPractice
@admin.register(CulturalPractice)
class CulturalPracticeAdmin(admin.ModelAdmin):
    list_display = ['__str__']
