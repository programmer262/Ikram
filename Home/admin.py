from django.contrib import admin
from .models import *

admin.site.register(Type)
admin.site.register(Service)
admin.site.register(Slider)
admin.site.register(Home_service)
@admin.register(home)
class homeAdmin(admin.ModelAdmin):
    list_display = ['nom']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','type','posted']
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['Last_name','First_name','Email']
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['Last_name','First_name','email']
