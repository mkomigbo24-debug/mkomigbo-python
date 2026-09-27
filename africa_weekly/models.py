from django.db import models
class Region(models.Model):
 code=models.CharField(max_length=30,unique=True)
 name=models.CharField(max_length=100)
 country=models.CharField(max_length=100)
 zone=models.CharField(max_length=100)
 zone_code=models.CharField(max_length=20)
 wind=models.CharField(max_length=200)
 rain=models.CharField(max_length=200)
 tide_port=models.CharField(max_length=200)
 lingua=models.CharField(max_length=10,default='en')
 element=models.CharField(max_length=50)
 activity=models.CharField(max_length=200)
 def __str__(self): return self.code
