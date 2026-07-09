from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def home1(request):
    return render(request,"home.html")

def explore(request):
    return render(request,"explore.html")
