from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("signup",signup,name="signup"),
    path("home",home,name="home"),
    path("logout_user",logout_user,name="logout_user")
]