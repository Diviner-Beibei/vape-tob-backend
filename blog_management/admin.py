from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # 添加作者字段到列表显示


admin.site.register(Blog, BlogAdmin)
