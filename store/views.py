from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def about(request):
    return render(request, "about.html", {})

def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,("you are logged in"))
            return redirect('home')
        else:
            messages.success(request,("there was an error pls try again later"))
            return redirect('home')
    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request,("you have been logged out"))
    return redirect('home')