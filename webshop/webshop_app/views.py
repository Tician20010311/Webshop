from django.shortcuts import render
from .models import Termek
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, "product_details.html")

def gamer_pc(request):
    products = Termek.objects.all()
    return render(request, "gamer_pc.html", {'products': products})

def login_user(request):
    return render(request, "login.html", {})

def logout_user(request):
    return render(request, "logout.html", {})

def registrate_user(request):
    return render(request, "registration.html", {})