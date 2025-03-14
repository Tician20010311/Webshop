from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    felhasznalo = models.OneToOneField(User, on_delete=models.CASCADE)
    modositas_datuma = models.DateTimeField(User , auto_now=True)
    telefon = models.CharField(max_length=11, blank=True)
    cim1 = models.CharField(max_length=100, blank=True)
    cim2 = models.CharField(max_length=100, blank=True)
    iranyitoszam = models.CharField(max_length=4, blank=True)
    varos = models.CharField(max_length=50, blank=True)
    megye = models.CharField(max_length=50, blank=True)
    regikosar = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.felhasznalo.username
    
#Alap felhasználó létrehozása regisztrációkor
def create_profile(sender, instance,created , **kwargs):
    if created:
        user_profile = Profile.objects.create(felhasznalo=instance)
        user_profile.save

post_save.connect(create_profile, sender=User)

class Kategoria(models.Model):
    nev = models.CharField(max_length=100)

    def __str__(self):
        return self.nev
    
    class Meta:
        verbose_name_plural = "kategoriak"

class Termek(models.Model):
    nev = models.CharField(max_length=100)
    ar = models.IntegerField(default=0)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, default=1)
    leiras = models.TextField(max_length=7000, default='', blank=True , null=True)
    kep = models.ImageField(upload_to='images', blank=True)

    #Leárazott dolgok
    akcios = models.BooleanField(default=False)
    akcios_ar = models.IntegerField(default=0)

    def __str__(self):
        return self.nev
    
class Vasarlo(models.Model):
    vezeteknev = models.CharField(max_length=50)
    keresztnev = models.CharField(max_length=50)
    telefonszam = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.vezeteknev} {self.keresztnev}'
    


class Megrendeles(models.Model):
    termek = models.ForeignKey(Termek, on_delete=models.CASCADE)
    vasarlo = models.ForeignKey(Vasarlo, on_delete=models.CASCADE)
    mennyiseg = models.IntegerField(default=1)
    telefonszam = models.CharField(max_length=12, default='', blank=True)
    cim = models.CharField(max_length=200, default='',blank=True)
    datum = models.DateTimeField(default=datetime.datetime.today)
    statusz = models.BooleanField(default=False)

    def __str__(self):
        return self.termek