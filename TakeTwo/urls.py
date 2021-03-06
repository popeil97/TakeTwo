"""TakeTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from pages.views import home_view, welcome_view
from products.views import product_edit_view, product_create_view, product_list_view, product_delete, daily_deal_view
from accounts.views import login_view, register_view, logout_view, restaurants_view
from cart.views import add_to_cart, cart_list_view, delete_cart_item,checkout
from events.views import event_list_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('', welcome_view, name='welcome'),
    path('products/<int:id>', product_edit_view, name='product'),
    path('products/delete/<int:id>', product_delete, name='delete'),
    path('products/', product_list_view, name='product_list'),
    path('products/create/', product_create_view, name='create'),
    path('products/create/<int:event_id>', product_create_view, name='create'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('restaurants/', restaurants_view, name='restaurant_view'),
    path('register/', register_view, name='register'),
    path('cart/<int:prod_id>', add_to_cart, name='add_to_cart'),
    path('cart/', cart_list_view, name='view_cart'),
    path('cart_remove/<int:prod_id>', delete_cart_item, name='remove_from_cart'),
    path('cart/checkout', checkout, name='checkout'),
    path('events/', event_list_view, name='event_view'),
    path('deals/', daily_deal_view, name='daily_deals')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
