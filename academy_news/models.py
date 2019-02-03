from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from utils.slugify import slugify

class News(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        blank=True,
        editable=False
    )
    tags = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Теги'
    )
    annotation = models.TextField(
        max_length=300,
        help_text='Макс. 300 символів',
        blank=False,
        verbose_name='Короткий зміст'
    )
    content = RichTextUploadingField(
        verbose_name='Зміст'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'Новини'
        verbose_name_plural = 'Новини'

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title + ' - ' + str(self.date_created)
