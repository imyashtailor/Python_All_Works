from django.urls import path
from profileapp.views import *

urlpatterns = [
    path("",create_profile,name="create_profile"),
    path("profiles",profile_list,name="profile_list")
]