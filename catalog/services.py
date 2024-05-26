from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cached_category():
    """
    Получает данные по категориям из кэша
    """
    if settings.CACHE_ENABLED:
        key = f'category_list'
        category_list = cache.get(key)
        if category_list is None:  # если кэша нет, получает данные из бд
            category_list = Category.objects.all()
            cache.set(key, category_list)
            return category_list
    else:  # если кэш выключен, получает данные из бд
        category_list = Category.objects.all()

    return category_list
