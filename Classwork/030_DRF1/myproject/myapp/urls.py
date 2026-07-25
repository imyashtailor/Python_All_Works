from django.urls import path
from myapp.views import *

urlpatterns = [
    path("list_student",list_student,name="list_student"),
    path("create_student",create_student,name="create_student"),
    path("delete_student/<id>",delete_student,name="delete_student"),
    path("update_student/<id>",update_student,name="update_student"),
    path("patch_student/<id>",patch_student,name="patch_student")
]