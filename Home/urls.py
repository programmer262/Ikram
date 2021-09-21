from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from .models import *
urlpatterns = [
    path('',views.home,name='home'),
    path('product/<str:pk>/',views.productId,name='product'),
]
