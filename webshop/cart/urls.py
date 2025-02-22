from django.urls import path
from . import views



urlpatterns = [
    path('',views.cart_summary, name='cart_summary'),
    path('hozzaadas/',views.cart_add, name='cart_add'),
    path('torles/',views.cart_delete, name='cart_delete'),
    path('frissites/',views.cart_update, name='cart_update'),
]