from django.urls import path
from .views import BlogListView, BlogDetailView


app_name = "blog_management"


urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]
