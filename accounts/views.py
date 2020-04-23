from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, get_user_model,login,logout
from .forms import UserLoginForm, UserRegisterForm
# Create your views here.
User = get_user_model()

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request,user)

        if next:
            return redirect(next)

        
        return redirect('/')
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


