from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'   # 或者列出你想要的字段，例如 ['title', 'author', 'created_at', 'updated_at']