from django.urls import path
from catalog.views import home, contacts, product_info, products
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product_info, name='product_info')
]
