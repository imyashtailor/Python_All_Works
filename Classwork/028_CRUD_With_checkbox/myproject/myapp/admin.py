from django.contrib import admin
from myapp.models import *

# Register your models here.

class displaystudents(admin.ModelAdmin):
    list_display = ['id','name','email','password','gender','lang','country','address']

admin.site.register(Student,displaystudents)