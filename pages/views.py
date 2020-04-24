from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from products.models import Product
# Create your views here.

def home_view(request, *args, **kwargs):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "home.html", context)

def welcome_view(request):
    return render(request,"welcome.html",{})
