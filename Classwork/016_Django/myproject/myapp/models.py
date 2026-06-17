from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    age = models.IntegerField()


class Product(models.Model):
    P_name = models.CharField(max_length=20)
    P_price = models.IntegerField()
    P_Description = models.CharField(max_length=50)
    P_brand = models.CharField(max_length=20,null=True)
    P_quantity = models.IntegerField(max_length=10,default=10)