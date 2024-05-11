from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [

    path('blog/list/', BlogListView.as_view(), name='list'),
    path('blog/create/', BlogCreateView.as_view(), name='create'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
