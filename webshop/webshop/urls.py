from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webshop_app.urls')),
    path('product/', include('webshop_app.urls')),
    path('gamer_pc/', include('webshop_app.urls')),
    path('bejelentkezes/', include('webshop_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)