from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(UserPassesTestMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def test_func(self):
        return self.request.user.has_perm('blog.add_blog')


class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ('title', 'content', 'is_published', 'preview')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('blog.change_blog')


class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

    def test_func(self):
        return self.request.user.has_perm('blog.delete_blog')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()

        return self.object
