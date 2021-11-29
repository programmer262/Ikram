from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from .models import *
urlpatterns = [
    path('',views.status,name="status"),
    path('services/',views.services,name="service"),
    path('services/<str:pk>/',views.serviceId,name='service'),
    path('contact/',views.contact,name='contact'),
]
