from django.contrib import admin
from .models import Room, Message

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user','room']
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','id']