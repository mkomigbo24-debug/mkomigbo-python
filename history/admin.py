from django.contrib import admin
from .models import HistoricalPeriod
@admin.register(HistoricalPeriod)
class HistoricalPeriodAdmin(admin.ModelAdmin):
    list_display = ['title', 'period']
