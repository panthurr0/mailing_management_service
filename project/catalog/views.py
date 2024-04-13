from django.shortcuts import render
from catalog.models import items


def home(request):
    return render(request, 'main/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'main/contacts.html')


def product(request, pk):
    context = {
        'object': Model.objects.get(pk=pk),
    }

    return render(request, 'main/products.html')
