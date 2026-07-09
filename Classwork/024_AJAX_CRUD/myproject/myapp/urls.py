from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("display",display_student,name="display"),
    path("delete",delete_student,name="delete"),
    path("retrive",retrive_student,name="retrive"),
    path("update",update_student,name="update")
]