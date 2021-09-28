from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.
def status(request):
    homes = home.objects.all()
    sliders = Slider.objects.all()
    services = Home_service.objects.all()
    context = {'homes':homes,'sliders':sliders,'services':services}
    return render(request,'home.html',context)
def services(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request,'Our services.html',context)
def serviceId(request, pk):
    service = Service.objects.get(id=pk)
    return render(request, 'Service detail.html', {'service':service})
def products(request):
    type = request.GET.get('type')
    if type == None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(type__name=type)
    types = Type.objects.all()
    context={'products':products,'types':types}
    return render(request,'products.html',context)

def productId(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'detail.html', {'product':product})
def contact(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status')
            
    context = {'form':form}
    return render(request, 'contact.html', context)

@login_required
def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request,'task.html',context)
@login_required
def taskId(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'taskd.html', {'task':task})