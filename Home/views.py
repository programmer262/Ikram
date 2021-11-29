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
    teams = Notre_équipe.objects.all()
    context = {'homes':homes,'sliders':sliders,'services':services,'teams':teams}
    return render(request,'home.html',context)
def services(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request,'Our services.html',context)
def serviceId(request, pk):
    service = Service.objects.get(id=pk)
    return render(request, 'Service detail.html', {'service':service})


def contact(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status')
            
    context = {'form':form}
    return render(request, 'contact.html', context)

