from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(verbose_name='content')
    author = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
