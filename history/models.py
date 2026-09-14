from django.db import models

class HistoricalPeriod(models.Model):
    name = models.CharField(max_length=100)  # Igbo-Ukwu 9th century, Atlantic Trade
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20, blank=True)
    overview = models.TextField()
    thesis_argument = models.TextField(blank=True)
