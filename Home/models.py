from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    thumbnail = models.ImageField(upload_to='Product/principal')
    thumbnail1 = models.ImageField(upload_to='Product/secondary',blank=True, null=True)
    thumbnail2 = models.ImageField(upload_to='Product/secondary',blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL,blank=True, null=True)
    if (type=='Beat making'):
        audio = models.FileField()
    else:
        audio = models.FileField(blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    posted=models.DateField (auto_now_add=True)
    def __str__(self):
        return self.name
    