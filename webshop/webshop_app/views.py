from django.shortcuts import redirect, render
from .models import Termek
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.core.mail import EmailMessage  
from django.http import HttpResponse  
from django.contrib.auth import get_user_model



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
    if request.method == 'POST':  
        form = SignUpForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('email_verification.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            messages.success(request, 'Elküldtük a hitelesítő emailt , kérjük hitelesítse email címét!')
            return redirect('home')

    else:  
        form = SignUpForm()  
    return render(request, 'registration.html', {'form': form})  

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('login') 
    else:  
        return HttpResponse('Az aktivációs link érvénytelen!')  