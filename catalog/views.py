from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

        return redirect('/contacts/')
# def home(request):
#     context = {
#         'title': 'Products',
#         'object_list': Product.objects.all(),
#     }
#     return render(request, 'catalog/product_list.html', context=context)


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     return render(request, 'catalog/contacts.html')

# def product_info(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product,
#         'title': 'About product',
#     }
#
#     return render(request, 'catalog/product_detail.html', context=context)
