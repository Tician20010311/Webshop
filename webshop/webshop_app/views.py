from django.shortcuts import redirect, render
from .models import Termek , Kategoria , Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm , UpdateUserForm , ChangePasswordForm , UserInfoForm , SearchForm
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.core.mail import EmailMessage  
from django.http import HttpResponse  
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import json
from cart.cart import Cart



def search(request):
    form = SearchForm(request.GET or None)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            results = Termek.objects.filter(nev__icontains=query)

    return render(request, 'search_results.html', {'results': results, 'form': form})



def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        kategoria = Kategoria.objects.get(nev = foo)
        products = Termek.objects.filter(kategoria = kategoria)
        return render(request, 'category.html', {'products': products , 'category': kategoria })
    except:
        messages.success(request, "A kategória nem létezik.")
        return redirect('home')




def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(felhasznalo__id=request.user.id)

        form = UserInfoForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()

            messages.success(request, "A felhasználói adatok frissítve lettek!")
            return redirect('home')
        return render(request, "update_info.html", {'user_form':form})
    else:
        messages.success(request, "Be kell jelentkezzen a felhasználói adatok frissítéséhez!")
        return redirect('home')




def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "A felhasználó frissítve lett!")
			return redirect('home')
		return render(request, "update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "Be kell jelentkezzen a felhasználó frissítéséhez!")
		return redirect('home')




def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method  == 'POST':
			form = ChangePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "A jelszó frissítve...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "update_password.html", {'form':form})
	else:
		messages.success(request, "Be kell jelentkeznie a jelszó frissítéséhez!")
		return redirect('home')




def home(request):
    return render(request, 'home.html')




def product(request,pk):
    product = Termek.objects.get(id=pk)
    return render(request, "product_details.html",{'product':product}) 




def all_pc(request):
    products = Termek.objects.all()
    return render(request, "all_pc.html", {'products': products})




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            current_user = Profile.objects.get(felhasznalo__id=request.user.id)
            saved_cart = current_user.regikosar
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                     cart.db_add(product=key, quantity=value)

 
            messages.success(request, "Sikeres bejelentkezés! Kérjük adja meg a hiányzó adatokat!")
            return redirect('update_info')
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
            mail_subject = 'Az aktivációs link elküldve!'  
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
        messages.success(request,'Üdvözöljük ! Sikeres aktiváció! Most már bejelentkezhet.')
        return redirect('login') 
    else:  
        return HttpResponse('Az aktivációs link érvénytelen!')  




def all_products(request):
    products = Termek.objects.all()
    return render(request, 'all_products.html', {"products":products})

