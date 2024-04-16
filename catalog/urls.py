from django.urls import path
from catalog.views import home, contacts, product_info, index
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', product_info, name='product_info')
]
