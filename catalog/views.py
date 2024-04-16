from django.shortcuts import render
from catalog.models import Product
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'main/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'main/contacts.html')


def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product,
        'title': 'About product',
    }

    return render(request, 'main/product_info.html', context=context)


def products(request):
    context = {
        'title': 'Products',
        'object_list': Product.objects.all(),
    }
    return render(request, 'main/products.html', context=context)
