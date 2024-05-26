from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactsView, CategoryListView
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
