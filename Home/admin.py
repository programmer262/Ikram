from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class SliderAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Slider, SliderAdmin)
admin.site.register(Type)
admin.site.register(Service)
admin.site.register(Home_service)
@admin.register(home)
class homeAdmin(admin.ModelAdmin):
    list_display = ['nom']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['Last_name','First_name','Email']
@admin.register(Notre_équipe)
class Notre_équipeAdmin(admin.ModelAdmin):
    list_display = ['Nom']