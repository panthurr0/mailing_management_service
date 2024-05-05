from django.contrib import admin

from catalog.models import Category, Product, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_title', 'product_description',)


@admin.register(Version)
class ProductVersion(admin.ModelAdmin):
    list_display = ('version_number', 'version_title', 'product', 'is_active')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
