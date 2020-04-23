from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from django.core.files.storage import FileSystemStorage
from .models import Product
from .forms import ProductForm 

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

    # if request.method == 'POST' and form.is_valid:
        
        # # obj = form.save(commit=False)
        # obj.save()

    context = {
        'action': 'Edit',
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_create_view(request, *args, **kwargs):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST) 
        
        if form.is_valid():
            obj = form.cleaned_data
            print(obj)
            img = request.FILES['image']
            print(request.FILES['image'])
            obj['image'] = img.name
            fs = FileSystemStorage()
            fs.save(img.name,img)
            Product.objects.create(**obj)
            print(img.name)
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

    context = {
        'products':products
    }

    return render(request, "products/product_list.html", context)

def product_delete(request, id):
    product = get_object_or_404(Product,id=id)

    # if request.method == 'POST':
    product.delete()

    return redirect('/products')