from django.contrib import admin
from django.urls import path ,re_path
from . import views
from .views import activate  



urlpatterns = [
    path('',views.home, name='home'),
    path('product/',views.product, name='product'),
    path('bejelentkezes/',views.login_user, name='login'),
    path('kijelentkezes/',views.logout_user, name='logout'),
    path('regisztracio/',views.registrate_user, name='registration'),
    path('felhasznalo_frissites/',views.update_user, name='update_user'),
    path('jelszo_frissites/',views.update_password, name='update_password'),
    path('info_frissites/',views.update_info, name='update_info'),
    path('termek/<int:pk>/',views.product, name='product'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('kategoria/<str:foo>/',views.category, name='category'),
    path('osszes/',views.all_products, name='all_products'),
    path('kereses/',views.search, name='search'),
]