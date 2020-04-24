from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from django.core.files.storage import FileSystemStorage
from .models import Product
from events.models import Event
from .forms import ProductForm

app_name='products'

# Create your views here.
def product_edit_view(request, id):
    obj = get_object_or_404(Product,id=id)
    img_name = obj.image
    fs = FileSystemStorage()
    obj_dict = model_to_dict(obj)
    obj_dict['image'] = fs.open(img_name)
    print(obj_dict)
    form = ProductForm(request.POST or None,initial=obj_dict)
    form.title = obj.title
    form.description = obj.description
    form.price = obj.price
    form.image = fs.url(img_name)
    form.added_by = obj.added_by
    form.sold_at = obj.sold_at

    # if request.method == 'POST' and form.is_valid:

        # # obj = form.save(commit=False)
        # obj.save()

    context = {
        'action': 'Edit',
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_create_view(request, event_id=None):

    form = ProductForm()

    if event_id != None:
        event_obj = get_object_or_404(Event,id=event_id)
        ##Help - for some reason this initial value is not setting
        form = ProductForm(initial={'sold_at':event_obj})

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid() and request.user.is_restaurant:
            obj = form.cleaned_data

            img = request.FILES['image']
            obj['added_by'] = request.user
            obj['image'] = img.name

            fs = FileSystemStorage()
            fs.save(img.name,img)

            Product.objects.create(**obj)

            return redirect('/products')
        else:
            print(form.errors)

    context = {
        'action': 'Create',
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_list_view(request, *args, **kwargs):
    products = Product.objects.all()

    products_list = []
    for product in products:
        if product.added_by == request.user:
            products_list.append(product)

    return render(request, 'products/product_list.html', context={'products':products_list})

'''
def product_list_view(request, *args, **kwargs):
    products = Product.objects.all()

    context = {
        'products':products
    }

    return render(request, "products/product_list.html", context)
'''

def product_delete(request, id):
    product = get_object_or_404(Product,id=id)

    # if request.method == 'POST':
    if request.user == product.added_by:
        product.delete()

    return redirect('/products')

def daily_deal_view(request):
    products = Product.objects.all()
    products_list = []
    for product in products:
        if product.daily_deal == True:
            products_list.append(product)

    return render(request, 'products/product_list.html', context={'products':products_list})
