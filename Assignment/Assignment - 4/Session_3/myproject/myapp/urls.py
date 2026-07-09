from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("home1",home1,name="home1"),
    path("explore",explore,name="explore")
]