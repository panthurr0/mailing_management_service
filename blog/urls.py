from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [

    path('blog_list/', BlogListView.as_view(), name='list'),
    path('blog_create/', BlogCreateView.as_view(), name='create'),
    path('blog_view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('blog_edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
