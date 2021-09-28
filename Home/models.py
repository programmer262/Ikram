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
    description = models.TextField()
class Product(models.Model):
    thumbnail = models.ImageField(upload_to='Product/principal')
    thumbnail1 = models.ImageField(upload_to='Product/secondary',blank=True, null=True)
    thumbnail2 = models.ImageField(upload_to='Product/secondary',blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL,blank=True, null=True)
    if (type=='Beat making'):
        audio = models.FileField(upload_to="Audio")
    else:
        audio = models.FileField(upload_to="Audio",blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    posted=models.DateField (auto_now_add=True)
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
    mqs = models.TextField(blank=True, null=True)
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
class Task(models.Model):
    id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    First_name = models.CharField( max_length=50)
    Last_name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    Type = models.ForeignKey(Type,on_delete=models.CASCADE)
    task = models.TextField()



