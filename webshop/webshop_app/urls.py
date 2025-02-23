from django.contrib import admin
from django.urls import path
from . import views
from .views import activate  



urlpatterns = [
    path('',views.home, name='home'),
    path('product/',views.product, name='product'),
    path('bejelentkezes/',views.login_user, name='login'),
    path('kijelentkezes/',views.logout_user, name='logout'),
    path('regisztracio/',views.registrate_user, name='registration'),
    path('termek/<int:pk>/',views.product, name='product'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  activate, name='activate'),  
    path('kategoria/<str:foo>/',views.category, name='category'),
    path('kategoria_summary/',views.category_summary, name='category_summary'),
]