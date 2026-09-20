from django.contrib import admin
from .models import Region, WeeklyGuide, Tide, MoonCycle, WeatherPattern

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['code','name_en','lingua_franca']
    list_filter = ['lingua_franca']
    search_fields = ['code','name_en']

@admin.register(WeeklyGuide)
class WeeklyGuideAdmin(admin.ModelAdmin):
    list_display = ['region','week_start','language','moon_phase_week']
    list_filter = ['language','region']
    
@admin.register(Tide)
class TideAdmin(admin.ModelAdmin):
    list_display = ['location','datetime','high_height_m']

@admin.register(MoonCycle)
class MoonCycleAdmin(admin.ModelAdmin):
    list_display = ['date','phase','illumination','market_day']