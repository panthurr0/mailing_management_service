from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactsView, BlogListView, BlogCreateView, \
    BlogDetailView, BlogDeleteView, BlogUpdateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    # path('blog/activity/<int:pk>', toggle_activity, name='toggle_activity'),
]
