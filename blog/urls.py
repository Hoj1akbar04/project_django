from django.urls import path
from .views import BlogView, BlogDetailView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blog'),
    path('blogs/<int:blog_id>/', BlogDetailView.as_view(), name='blog-detail'),
]
