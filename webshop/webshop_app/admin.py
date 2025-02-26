from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin  # Eredeti UserAdmin importálása
from .models import Kategoria, Vasarlo, Termek, Megrendeles, Profile

admin.site.register(Kategoria)
admin.site.register(Vasarlo)
admin.site.register(Termek)
admin.site.register(Megrendeles)
admin.site.register(Profile)

# Profil adatokat a UserAdmin osztályhoz adni
# Mix profile info and user info
class ProfileInline(admin.StackedInline):
	model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)
