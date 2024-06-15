from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from urllib.parse import urljoin
import re


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(verbose_name='content')
    author = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='blog_covers/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Django服务器的地址
        base_url = 'http://localhost:8000'
        # 使用正则表达式找到所有的<img>标签
        img_tags = re.findall('<img [^>]*src="([^"]*)"[^>]*>', self.content)
        for img_tag in img_tags:
            # 将相对URL转换为完整的URL
            full_url = urljoin(base_url, img_tag)
            # 在content中替换相对URL为完整的URL
            self.content = self.content.replace(img_tag, full_url)
        super().save(*args, **kwargs)
