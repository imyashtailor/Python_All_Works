from django.db import models

# Create your models here.

class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Restaurant(models.Model):
    cuisine = models.ForeignKey(Cuisine,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    rating = models.FloatField()
