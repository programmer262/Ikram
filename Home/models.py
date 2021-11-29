from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Slider(models.Model):
    name = models.CharField(max_length=100 )
    image = models.ImageField( upload_to='sliders/')
    def __str__(self):
        return self.name
class Service(models.Model):
    thumbnail = models.ImageField(upload_to='Services')
    name =models.CharField(max_length=200)
    Type = models.ForeignKey(Type, on_delete=models.SET_NULL,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    posted=models.DateField (auto_now_add=True)
    def __str__(self):
        return self.name
class home(models.Model):
    nom = models.CharField(max_length=50)
    slider = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nom


from django.db import models

# Create your models here.

class Contact(models.Model):  
    First_name = models.CharField(max_length=300)
    Last_name= models.CharField(max_length=300)
    Tel = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100)
    Message = models.TextField(null=False,blank=False)
    def __str__(self):
        return self.Last_name
class Home_service(models.Model):
    thumbnail = models.ImageField(upload_to='home/Services')
    name =models.CharField(max_length=200)
    url =models.URLField()
    Type = models.ForeignKey(Type, on_delete=models.SET_NULL,blank=True, null=True)
    def __str__(self):
        return self.name
class Notre_équipe(models.Model):
    Nom = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='team/photos')
    Fonctionnement = models.TextField()


