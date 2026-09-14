from django.db import models
from religion.models import Religion

class EsotericTradition(models.Model):
    name = models.CharField(max_length=100)
    origin_tradition = models.CharField(max_length=100)
    parent_religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    inner_teaching = models.TextField()
    outer_teaching = models.TextField(blank=True)
    methods = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Symbol(models.Model):
    name = models.CharField(max_length=100)
    tradition = models.ForeignKey(EsotericTradition, on_delete=models.CASCADE, related_name='symbols', null=True, blank=True)
    meaning = models.TextField()
    esoteric_meaning = models.TextField(blank=True)
    def __str__(self):
        return self.name
