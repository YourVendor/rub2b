from django.db import models

from upload.models.category import Category


class Product(models.Model):
    title = models.CharField(max_length=90,
                             help_text='Наименование до 90 символов',
                             verbose_name='Наименование')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория продукта')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        app_label = 'upload'

    def __str__(self):
        return self.title
