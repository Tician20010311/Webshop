from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webshop_app.urls')),
    path('product/', include('webshop_app.urls')),
]