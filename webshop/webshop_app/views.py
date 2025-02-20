from django.shortcuts import redirect, render
from .models import Termek
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


def home(request):
    return render(request, 'home.html')

def product(request,pk):
    product = Termek.objects.get(id=pk)
    return render(request, "product_details.html",{'product':product})

def gamer_pc(request):
    products = Termek.objects.all()
    return render(request, "gamer_pc.html", {'products': products})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Sikeres bejelentkezés!")
            return redirect('home')
        else:
            messages.error(request, "Sikertelen bejelentkezés!")
            return redirect('login')
    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "Sikeres kijelentkezés!")
    return redirect('home')

def registrate_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, "Sikeres regisztráció!")
            return redirect('home')
        else:
            messages.error(request, "Sikertelen regisztráció!")
            return redirect('registration')
    else:
        return render(request, "registration.html", {'form': form})