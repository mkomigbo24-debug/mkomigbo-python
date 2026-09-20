from django.contrib import admin
from .models import AmuzhiYear, AmuzhiMonth, MarketDay, AmuzhiTide

@admin.register(AmuzhiYear)
class AmuzhiYearAdmin(admin.ModelAdmin):
    list_display = ['gregorian_year', 'igbo_year', 'is_leap', 'year_start_gregorian', 'anchor_market_day']

@admin.register(AmuzhiMonth)
class AmuzhiMonthAdmin(admin.ModelAdmin):
    list_display = ['year', 'number', 'name_igbo', 'days_in_month', 'gregorian_start']

@admin.register(MarketDay)
class MarketDayAdmin(admin.ModelAdmin):
    list_display = ['date_gregorian', 'market_day', 'igbo_day', 'month', 'moon_symbol', 'illumination']
    list_filter = ['market_day', 'month__year']
    search_fields = ['date_gregorian']

@admin.register(AmuzhiTide)
class AmuzhiTideAdmin(admin.ModelAdmin):
    list_display = ['date', 'location', 'high_tide', 'low_tide', 'height_m']