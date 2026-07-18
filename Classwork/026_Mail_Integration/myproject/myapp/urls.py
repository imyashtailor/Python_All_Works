from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("mail",mail_send,name="mail"),
    path("mailhtml",mail_html,name="mailhtml"),
    path("attach",mail_attach,name="attach")
]