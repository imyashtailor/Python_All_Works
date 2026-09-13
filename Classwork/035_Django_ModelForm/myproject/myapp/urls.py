from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("update",update_std,name="update"),
    path("delete",delete_std,name="delete")
]