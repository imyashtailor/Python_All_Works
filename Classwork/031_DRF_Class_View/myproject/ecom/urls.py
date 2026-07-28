from django.urls import path
from ecom.views import *

urlpatterns = [
    path("categories",CategoryAPI.as_view()),
    path("categories/<id>",CategoryAPIById.as_view()),
    path("products",ProductAPI.as_view())
]