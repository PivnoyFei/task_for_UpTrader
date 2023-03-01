from django.db import models


class Menu(models.Model):
    title = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField('Слаг', unique=True, db_index=True)
    parent = models.ForeignKey(
        'Menu',
        null=True,
        blank=True,
        default=None,
        related_name='children',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta(object):
        ordering = ('-created', )
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self) -> str:
        return self.title
