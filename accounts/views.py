from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, get_user_model,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm
from pages.views import home_view, welcome_view
from products.models import Product
# Create your views here.
User = get_user_model()

@login_required
def logout_view(request):
    logout(request)
    return redirect(welcome_view)

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect(home_view)

        if next:
            return redirect('hello')

        return redirect(login_view)
    context = {
        'form':form
    }
    return render(request,"accounts/login.html", context)

def register_view(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username,password)

        return redirect('/login')

    context = {
        'form': form
    }

    return render(request,"accounts/register.html", context)

def restaurants_view(request):
    products = Product.objects.all()

    restaurants = {}
    for product in products:
        if str(product.added_by) in restaurants.keys():
            restaurants[str(product.added_by)].append(product)
        else:
            restaurants[str(product.added_by)] = [product]

    return render(request, 'restaurant_view.html', context={'restaurants':restaurants})
