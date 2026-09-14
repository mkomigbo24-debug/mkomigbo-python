from django.db import models

class CulturalPractice(models.Model):
    name = models.CharField(max_length=100)  # Kola, Masquerade
    description = models.TextField()
    significance = models.TextField()
