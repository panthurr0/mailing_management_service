from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_title = models.CharField(verbose_name='имя', max_length=100)
    category_description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_title',)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_title = models.CharField(verbose_name='Наименование', max_length=100)
    product_description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение (превью)', upload_to='catalog/', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)

    created_at = models.DateTimeField(verbose_name='Дата создания (записи в БД)', **NULLABLE, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения (записи в БД)', **NULLABLE, auto_now=True)

    def __str__(self):
        return f'{self.product_title}: {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_title',)


class Blog(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    slug = models.CharField(verbose_name='slug', max_length=150, **NULLABLE)
    content = models.TextField(verbose_name='Контент', **NULLABLE)
    preview = models.ImageField(verbose_name='Превью', upload_to='catalog/', **NULLABLE)

    created_at = models.DateTimeField(verbose_name='Дата создания (записи в БД)', **NULLABLE, auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Признак публикации', **NULLABLE, default=False)
    views = models.IntegerField(verbose_name='Количество просмотров', default=0, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
