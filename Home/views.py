from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
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