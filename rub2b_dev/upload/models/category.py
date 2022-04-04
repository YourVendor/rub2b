from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=90,
                             help_text='Наименование до 90 символов',
                             verbose_name='Наименование')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        app_label = 'upload'

    def __str__(self):
        return self.title
