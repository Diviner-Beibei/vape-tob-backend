from rest_framework.pagination import PageNumberPagination
from rest_framework import  generics
from .models import Blog
from .serializers import BlogSerializer, BlogListSerializer


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    pagination_class = PageNumberPagination
    http_method_names = ['get']


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    http_method_names = ['get']