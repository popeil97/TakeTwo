from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model,login,logout
from .models import CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_to_cart(request,prod_id):
    item = CartItem(
        username = request.user.username,
        productID = prod_id
    )

    item.save()

    return redirect('/home')

@login_required
def cart_list_view(request):
    cart = CartItem.objects.filter(username=request.user.username)
    prod_ids = [item.productID for item in cart]
    products = Product.objects.in_bulk(prod_ids)
    total = 0
    for key,prod in products.items():
        total += prod.price
    context = {
        'products':products,
        'total': total
    }

    print(products)
    return render(request,'cart/cart_list_view.html', context)

def delete_cart_item(request, prod_id):
    print("in delete from cart")
    cart_item = CartItem.objects.filter(username=request.user.username, productID=prod_id)

    cart_item.delete()

    return redirect('/cart')

def checkout(request):
    CartItem.objects.filter(username=request.user.username).delete()

    return redirect('/home')
