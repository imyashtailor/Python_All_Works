from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST
        uname = data.get('username')
        password = data.get('password')

        user = authenticate(username=uname,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"index.html",{'error':'Invalid Credentails'})

    if request.user.is_authenticated:
        return redirect("home")
    return render(request,"index.html")

def signup(request):
    if request.method == 'POST':
        data = request.POST
        fname = data.get('firstname')
        lname = data.get('lastname')
        email = data.get('email')
        uname = data.get('username')
        password = data.get('password')

        User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=password)
        return render(request,"signup.html",{'msg':'User Registration Successfully!...'})
    return render(request,"signup.html")

@login_required(login_url="index")
def home(request):
    return render(request,"home.html")

def logout_user(request):
    logout(request)
    return redirect("index")