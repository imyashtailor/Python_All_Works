from django.contrib import admin
from myapp.models import *

# Register your models here.

admin.site.register(Product)

class displaylocation(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Country,displaylocation)
admin.site.register(State)
admin.site.register(City)