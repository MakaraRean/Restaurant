from django.shortcuts import render
from django.template import context

from myrestaurant.models import Product

# Create your views here.

def test(request):
    return render(request,'test.html')

def home(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request,'home.html',context)