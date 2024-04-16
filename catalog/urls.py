from django.urls import path
from catalog.views import home, contacts, product_info
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product_info, name='product_info')
]
