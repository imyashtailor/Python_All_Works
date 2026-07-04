from django.contrib import admin
from myapp.models import *

# Register your models here.

class displayuserdetails(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','role','age','address','phone']

admin.site.register(CustomeUser,displayuserdetails)
admin.site.register(Role)
