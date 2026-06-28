from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)

class Passport(models.Model):
    # Foriegn key create karvi(one to one relationship mate)
    person = models.OneToOneField(Person,on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    pid = models.CharField(max_length=20)


#one to many and add forign key
class Category(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    #forieng key aapvi ahiya table na relationship mate
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="images",null=True)


    def total(self):
        return self.price*self.qty


#many to many
class Book(models.Model):
    name = models.CharField(max_length=20)

class Author(models.Model):
    book = models.ManyToManyField(Book)
    name = models.CharField(max_length=20)