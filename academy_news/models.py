from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Title'
    )
    slug = models.SlugField(
        blank=True
    )
    content = RichTextUploadingField(
        verbose_name='Content'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date created'
    )

    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title + ' - ' + str(self.date_created)
