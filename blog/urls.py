from django.urls import path
from .views import BlogView, SingleBlogView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name='blog'),
    path('blogs/detail/', SingleBlogView.as_view(), name='single-blog'),

]
