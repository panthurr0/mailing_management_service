from django.db import models

from catalog.models import NULLABLE


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
