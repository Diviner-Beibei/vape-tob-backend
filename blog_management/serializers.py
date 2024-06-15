from rest_framework import serializers
from .models import Blog
import re
import html


def get_summary(content, length=200):
    # 解码HTML实体
    content = html.unescape(content)
    # 删除HTML标签
    content = re.sub('<[^>]*>', '', content)
    # 获取前N个字符
    summary = content[:length]
    return summary


class BlogListSerializer(serializers.ModelSerializer):
    summary = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'summary', 'updated_at', 'cover_image']  # 或者列出你想要的字段，例如 ['title', 'author', 'created_at', 'updated_at']

    def get_summary(self, obj):
        return get_summary(obj.content)


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'updated_at', 'cover_image', 'author']  # 或者列出你想要的字段，例如 ['title', 'author', 'created_at', 'updated_at']

