from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from myapp.manager import *


# Create your models here.

class CustomeUser(AbstractUser):
    phone = models.CharField(
        max_length=15,
        unique=True
    )

    address = models.TextField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)

    USERNAME_FIELD = "phone"

    objects = CustomUserManager()

