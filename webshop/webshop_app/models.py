from django.db import models
import datetime

class Kategoria(models.Model):
    nev = models.CharField(max_length=100)

    def __str__(self):
        return self.nev
    
    class Meta:
        verbose_name_plural = "kategoriák"
    
class Vasarlo(models.Model):
    vezeteknev = models.CharField(max_length=50)
    keresztnev = models.CharField(max_length=50)
    telefonszam = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.vezeteknev} {self.keresztnev}'
    
class Termek(models.Model):
    nev = models.CharField(max_length=100)
    ar = models.IntegerField(default=0, max_length=7)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, default=1)
    leiras = models.TextField(max_length=7000, default='', blank=True , null=True)
    kep = models.ImageField(upload_to='images', blank=True)

    #Leárazott dolgok
    akcios = models.BooleanField(default=False)
    akcios_ar = models.IntegerField(default=0, max_length=7)

    def __str__(self):
        return self.nev

class Megrendeles(models.Model):
    termek = models.ForeignKey(Termek, on_delete=models.CASCADE)
    vasarlo = models.ForeignKey(Vasarlo, on_delete=models.CASCADE)
    mennyiseg = models.IntegerField(default=1)
    telefonszam = models.CharField(max_length=11, default='', blank=True)
    cim = models.CharField(max_length=200, default='',blank=True)
    datum = models.DateTimeField(default=datetime.datetime.today)
    statusz = models.BooleanField(default=False)

    def __str__(self):
        return self.termek