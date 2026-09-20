from django.db import models
from django.utils.translation import gettext_lazy as _
import math
from datetime import datetime, timedelta

# =========================================================================
# HYBRID LUNISOLAR - CORRECTED PER YOUR NOTE
# [STRIPPED 73 bytes]
# - 13 months in year, each 28 days = 364 days
# - To agree with Gregorian, SEVENTH month is 29 days => 365 days
# - Ọnwa Mbụ (first month) begins when new moon observed in 3rd week Feb, 28 days like others
# - Every 4th year = leap year (corresponds to Gregorian leap), February = first month made 29 days
# - Moon phase ref: 2000-01-06 18:14 UTC, synodic month 29.53058867
# =========================================================================

SYNODIC_MONTH = 29.53058867
REF_NEW_MOON = datetime(2000, 1, 6, 18, 14, 0)

class Region(models.Model):
    # For whole Africa + 2B coverage - local Lingua Franca serving
    code = models.CharField(max_length=10, unique=True) # NG, KE, ZA, EG, SN, TZ, GH, etc
    name_en = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100, blank=True)
    name_es = models.CharField(max_length=100, blank=True)
    name_pt = models.CharField(max_length=100, blank=True)
    name_sw = models.CharField(max_length=100, blank=True)
    name_ar = models.CharField(max_length=100, blank=True)
    name_ig = models.CharField(max_length=100, blank=True)
    lingua_franca = models.CharField(max_length=20, default='en', choices=[
        ('en','English'),('fr','French'),('es','Spanish'),
        ('pt','Portuguese'),('sw','Swahili'),('ar','Arabic'),('ig','Igbo')
    ])

    def __str__(self):
        return f"{self.code} - {self.name_en} ({self.lingua_franca})"

    class Meta:
        ordering = ['code']

class MoonCycle(models.Model):
    date = models.DateField(db_index=True)
    phase = models.CharField(max_length=20) # New Moon, Waxing Crescent, First Quarter, Waxing Gibbous, Full Moon, Waning Gibbous, Last Quarter, Waning Crescent
    phase_symbol = models.CharField(max_length=10, blank=True) # 🌑🌒🌓🌔🌕🌖🌗🌘
    illumination = models.IntegerField() # 0-100
    # Igbo market day linkage
    market_day = models.CharField(max_length=10, blank=True) # Eke, Orie, Afo, Nkwo
    # For farmers, fishermen
    farmers_note_en = models.TextField(blank=True)
    farmers_note_ig = models.TextField(blank=True)
    fishermen_note_en = models.TextField(blank=True)
    fishermen_note_ig = models.TextField(blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.date} {self.phase} {self.illumination}% {self.market_day}"

class WeatherPattern(models.Model):
    # Core AWAG: moon cycle, wind pattern, rainfall, tide, daily/weekly/monthly reliable forecast
    date = models.DateField(db_index=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='weather')
    # Wind
    wind_pattern = models.CharField(max_length=100, blank=True) # Harmattan, Monsoon, etc
    wind_speed_kmh = models.FloatField(default=0)
    wind_direction = models.CharField(max_length=20, blank=True) # N, NE, E, SE, S, SW, W, NW
    # Rainfall
    rainfall_mm = models.FloatField(default=0)
    rainfall_prediction = models.CharField(max_length=20, choices=[
        ('early','Early rain'),('late','Late rain'),('normal','Normal'),('heavy','Heavy'),('light','Light')
    ], default='normal')
    # Soil
    soil_condition = models.CharField(max_length=20, choices=[
        ('dry','Too dry'),('wet','Too wet'),('optimal','Optimal'),('flooded','Flooded')
    ], default='optimal')
    temperature_c = models.FloatField(default=28)
    humidity = models.FloatField(default=70)
    # Reliable forecast
    forecast_reliability = models.IntegerField(default=95) # %

    class Meta:
        ordering = ['-date']

class Tide(models.Model):
    datetime = models.DateTimeField(db_index=True)
    location = models.CharField(max_length=100, db_index=True) # Bonny, Opobo, Brass, Calabar, Lagos, Mombasa, etc
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, related_name='tides')
    high_tide_time = models.DateTimeField()
    low_tide_time = models.DateTimeField()
    high_height_m = models.FloatField()
    low_height_m = models.FloatField()
    # For fishermen, transporters - predictable
    fishing_best = models.CharField(max_length=100, blank=True) # Best fishing window
    # Multilingual advice for local people in Lingua Franca
    advice_en = models.TextField(blank=True)
    advice_fr = models.TextField(blank=True)
    advice_es = models.TextField(blank=True)
    advice_pt = models.TextField(blank=True)
    advice_sw = models.TextField(blank=True)
    advice_ar = models.TextField(blank=True)
    advice_ig = models.TextField(blank=True)

    class Meta:
        ordering = ['datetime']

class WeeklyGuide(models.Model):
    # AWAG - Africas Weekly Activities Guide - core
    # Farmers know when planting early/late rain, soil too dry/wet, harvest, sell
    # Fishermen follow moon and tide - when fishing, preserve, sell
    # Transporters know when move, predict rain pattern
    week_start = models.DateField(db_index=True)
    week_end = models.DateField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='weekly_guides')

    # Moon cycle for week
    moon_phase_week = models.CharField(max_length=50, blank=True) # New Moon week, Full Moon week etc

    # For all economic activities - predictable - multilingual for 2B
    # Farmers - reliable info whole Africa
    farmers_planting_en = models.TextField(blank=True, verbose_name="Farmers: when to start planting")
    farmers_planting_fr = models.TextField(blank=True)
    farmers_planting_es = models.TextField(blank=True)
    farmers_planting_pt = models.TextField(blank=True)
    farmers_planting_sw = models.TextField(blank=True)
    farmers_planting_ar = models.TextField(blank=True)
    farmers_planting_ig = models.TextField(blank=True, verbose_name="Ugbo: mgbe akuku")

    farmers_rain_en = models.TextField(blank=True, verbose_name="Early or late rain")
    farmers_soil_en = models.TextField(blank=True, verbose_name="Soil too dry or wet")
    farmers_harvest_en = models.TextField(blank=True, verbose_name="When to harvest")
    farmers_sell_en = models.TextField(blank=True, verbose_name="When to sell")

    # Fishermen - moon and tide
    fishermen_moon_tide_en = models.TextField(blank=True, verbose_name="Fishermen: moon and tide")
    fishermen_moon_tide_ig = models.TextField(blank=True)
    fishermen_when_fish = models.TextField(blank=True)
    fishermen_preserve = models.TextField(blank=True)
    fishermen_sell = models.TextField(blank=True)

    # Transporters - predictable economic activities
    transporters_rain_pattern = models.TextField(blank=True)
    transporters_when_move = models.TextField(blank=True)

    # Traders, artisans, hunters, traditional healers, leaders
    traders_advice = models.TextField(blank=True)
    artisans_advice = models.TextField(blank=True)
    hunters_advice = models.TextField(blank=True)
    healers_advice = models.TextField(blank=True)
    leaders_advice = models.TextField(blank=True)

    # Language for local serving
    language = models.CharField(max_length=5, default='en', choices=[
        ('en','English'),('fr','French'),('es','Spanish'),
        ('pt','Portuguese'),('sw','Swahili'),('ar','Arabic'),('ig','Igbo')
    ])

    class Meta:
        ordering = ['-week_start']
        verbose_name = "AWAG - Africas Weekly Activities Guide"
        verbose_name_plural = "AWAG - Weekly Guides"

    def __str__(self):
        return f"AWAG {self.region.code} {self.week_start} - {self.language}"

# Engine functions - Hybrid Lunisolar corrected
def moon_phase_fraction(date):
    ref = REF_NEW_MOON
    dt = datetime(date.year, date.month, date.day, 12, 0)
    days = (dt - ref).total_seconds() / 86400.0
    age = days % SYNODIC_MONTH
    if age < 0:
        age += SYNODIC_MONTH
    return age / SYNODIC_MONTH

def moon_phase_info(date):
    phase = moon_phase_fraction(date)
    illum = 0.5 * (1 - math.cos(2 * math.pi * phase))
    buckets = [
        ('🌑','New Moon'),('🌒','Waxing Crescent'),('🌓','First Quarter'),
        ('🌔','Waxing Gibbous'),('🌕','Full Moon'),('🌖','Waning Gibbous'),
        ('🌗','Last Quarter'),('🌘','Waning Crescent'),
    ]
    index = int(phase * 8)
    if index > 7:
        index = 7
    return {
        'symbol': buckets[index][0],
        'stage': buckets[index][1],
        'illum': int(round(illum * 100)),
        'phase': phase,
    }

def is_gregorian_leap_year(year):
    # Every 4th year leap - Gregorian rule
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return (year % 4 == 0)

def days_in_igbo_month(month_index, is_leap_year):
    # Your correction:
    # Each month 28 days = 364, 7th month is 29 days => 365
    # Every 4th year leap: February = first month made 29 days
    if month_index == 7:
        return 29 # Always 29 to agree with Gregorian - your note
    if month_index == 1 and is_leap_year:
        return 29 # February first month 29 days in leap year
    return 28

def igbo_year_start_new_moon(year):
    # Ọnwa Mbụ begins when new moon observed in 3rd week February
    # Approximate: Feb 15-21
    for day in range(15, 22):
        test_date = datetime(year, 2, day).date()
        info = moon_phase_info(test_date)
        if info['illum'] < 5: # Near new moon
            return test_date
    return datetime(year, 2, 18).date() # Fallback 3rd week Feb