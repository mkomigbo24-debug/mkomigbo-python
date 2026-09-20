from django.db import models
import math
from datetime import datetime, timedelta, date

# =========================================================================
# AMUZHI IGBO CALENDAR - CORRECTED PER YOUR NOTE (Renamed amujz → Amuzhi)
# [STRIPPED 73 bytes]
# - 13 months, each 28 days = 364 days
# - 7th month is 29 days to agree with Gregorian => 365 days
# - Ọnwa Mbụ (first month) begins new moon observed 3rd week February, 28 days
# - Every 4th year = leap year (Gregorian leap), February = Ọnwa Mbụ made 29 days => 366
# - Hybrid Lunisolar: Gregorian only reference overlay
# - Moon ref: 2000-01-06 18:14 UTC, synodic 29.53058867
# - Market days: Eke, Orie, Afo, Nkwo - 4-day week Izu
# - With tides upgrade (Bonny, Opobo, Brass, Calabar, Lagos, etc)
# =========================================================================

SYNODIC_MONTH = 29.53058867
REF_NEW_MOON = datetime(2000, 1, 6, 18, 14, 0)

# Month registry - from PHP IgboCalendarYear.php
MONTH_REGISTRY = {
    1: {'name': 'Ọnwa Mbụ', 'gloss': 'First Moon', 'theme': 'New beginnings'},
    2: {'name': 'Ọnwa Abụọ', 'gloss': 'Second Moon', 'theme': 'Stability'},
    3: {'name': 'Ọnwa Ife Eke', 'gloss': 'Light of Eke', 'theme': 'Awakening'},
    4: {'name': 'Ọnwa Anọ', 'gloss': 'Fourth Moon', 'theme': 'Growth'},
    5: {'name': 'Ọnwa Agwụ', 'gloss': 'Moon of Agwụ', 'theme': 'Spiritual insight'},
    6: {'name': 'Ọnwa Ifejiọkụ', 'gloss': 'Yam Deity Moon', 'theme': 'Agriculture'},
    7: {'name': 'Ọnwa Alọm Chi', 'gloss': 'Personal Spirit', 'theme': 'Reflection - 29 days to agree Gregorian'},
    8: {'name': 'Ọnwa Ilo Mmụọ', 'gloss': 'Spirits Retreat', 'theme': 'Cleansing'},
    9: {'name': 'Ọnwa Ana', 'gloss': 'Earth Moon', 'theme': 'Grounding'},
    10: {'name': 'Ọnwa Okike', 'gloss': 'Creation', 'theme': 'Renewal'},
    11: {'name': 'Ọnwa Ajana', 'gloss': 'Harvest Cleansing', 'theme': 'Harvest'},
    12: {'name': 'Ọnwa Ede Ajana', 'gloss': 'End of Ajana', 'theme': 'Completion'},
    13: {'name': 'Ọnwa Ụzọ Alụsị', 'gloss': 'Path of Deities', 'theme': 'Transition'},
}

MARKET_CYCLE = ['Eke', 'Orie', 'Afo', 'Nkwo']

def moon_phase_fraction(d):
    if isinstance(d, datetime):
        dt = d
    else:
        dt = datetime(d.year, d.month, d.day, 12, 0)
    days = (dt - REF_NEW_MOON).total_seconds() / 86400.0
    age = days % SYNODIC_MONTH
    if age < 0:
        age += SYNODIC_MONTH
    return age / SYNODIC_MONTH

def moon_phase_info(d):
    phase = moon_phase_fraction(d)
    illum = 0.5 * (1 - math.cos(2 * math.pi * phase))
    buckets = [
        ('🌑','New Moon'),('🌒','Waxing Crescent'),('🌓','First Quarter'),
        ('🌔','Waxing Gibbous'),('🌕','Full Moon'),('🌖','Waning Gibbous'),
        ('🌗','Last Quarter'),('🌘','Waning Crescent'),
    ]
    idx = int(phase * 8)
    if idx > 7:
        idx = 7
    return {'symbol': buckets[idx][0], 'stage': buckets[idx][1], 'illum': int(round(illum*100)), 'phase': phase}

def is_gregorian_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return (year % 4 == 0)

def days_in_igbo_month(month_index, is_leap):
    # YOUR CORRECTION:
    # 7th month always 29 days to agree Gregorian (364+1=365)
    # Every 4th year leap: February = Ọnwa Mbụ (1st month) made 29 days (365+1=366)
    if month_index == 7:
        return 29
    if month_index == 1 and is_leap:
        return 29
    return 28

def igbo_year_start_new_moon(greg_year):
    # Ọnwa Mbụ begins new moon observed 3rd week February
    for day in range(15, 22):
        try:
            test_date = date(greg_year, 2, day)
            info = moon_phase_info(test_date)
            if info['illum'] < 10: # Near new moon
                return test_date
        except:
            continue
    return date(greg_year, 2, 18) # Fallback 3rd week Feb

class AmuzhiYear(models.Model):
    gregorian_year = models.IntegerField(unique=True)
    igbo_year = models.IntegerField() # Nri calendar
    is_leap = models.BooleanField(default=False) # Every 4th year Gregorian leap
    year_start_gregorian = models.DateField() # Observed new moon 3rd week Feb
    anchor_market_day = models.CharField(max_length=10, default='Afo') # Eke Orie Afo Nkwo
    reference_chart_id = models.IntegerField(default=1) # 112 charts Silver Eze 0001-8064

    def save(self, *args, **kwargs):
        if not self.is_leap:
            self.is_leap = is_gregorian_leap_year(self.gregorian_year)
        if not self.year_start_gregorian:
            self.year_start_gregorian = igbo_year_start_new_moon(self.gregorian_year)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.gregorian_year} = Igbo {self.igbo_year} {'Leap 366' if self.is_leap else '365'} - Start {self.year_start_gregorian}"

    class Meta:
        ordering = ['gregorian_year']

class AmuzhiMonth(models.Model):
    year = models.ForeignKey(AmuzhiYear, on_delete=models.CASCADE, related_name='months')
    number = models.IntegerField() # 1-13
    name_igbo = models.CharField(max_length=50)
    gloss = models.CharField(max_length=50, blank=True)
    theme = models.CharField(max_length=50, blank=True)
    days_in_month = models.IntegerField(default=28)
    gregorian_start = models.DateField()
    gregorian_end = models.DateField()

    def __str__(self):
        return f"{self.year.gregorian_year} {self.name_igbo} ({self.days_in_month} days) {self.gregorian_start} - {self.gregorian_end}"

    class Meta:
        ordering = ['year', 'number']
        unique_together = ['year', 'number']

class MarketDay(models.Model):
    MARKET_CHOICES = [('EKE','Eke'),('ORIE','Orie'),('AFO','Afo'),('NKWO','Nkwo')]
    date_gregorian = models.DateField(unique=True, db_index=True)
    market_day = models.CharField(max_length=10, choices=MARKET_CHOICES, db_index=True)
    igbo_day = models.IntegerField() # 1-28/29
    month = models.ForeignKey(AmuzhiMonth, on_delete=models.CASCADE, related_name='days')
    weekday = models.CharField(max_length=20, blank=True) # Monday etc Gregorian ref
    moon_symbol = models.CharField(max_length=10, blank=True) # 🌑 etc
    moon_stage = models.CharField(max_length=30, blank=True)
    illumination = models.IntegerField(default=0)
    # Tides upgrade - you wanted tides to Amuzhi
    high_tide = models.TimeField(null=True, blank=True)
    low_tide = models.TimeField(null=True, blank=True)
    tide_height_m = models.FloatField(null=True, blank=True)
    tide_location = models.CharField(max_length=100, default="Bonny", blank=True)
    tide_advice = models.TextField(blank=True) # How tide affects market
    is_today = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date_gregorian} {self.market_day} {self.moon_symbol} {self.month.name_igbo} Day {self.igbo_day}"

    class Meta:
        ordering = ['date_gregorian']

class AmuzhiTide(models.Model):
    # Tides to Amuzhi - your upgrade for fishermen
    date = models.DateField(db_index=True)
    market_day = models.ForeignKey(MarketDay, on_delete=models.CASCADE, null=True, blank=True, related_name='tides')
    location = models.CharField(max_length=100, db_index=True) # Bonny, Opobo, Brass, Calabar, Lagos, Mombasa
    high_tide = models.TimeField()
    low_tide = models.TimeField()
    height_m = models.FloatField()
    fishing_window = models.CharField(max_length=100, blank=True)
    market_effect = models.TextField(blank=True)

    class Meta:
        ordering = ['date']