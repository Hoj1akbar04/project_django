from django.shortcuts import render
from django.views import View
from .models import Blog, Comment


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs
        }
        return render(request, 'main/blog.html', context)


class SingleBlogView(View):
    def get(self, request):
        comments = Comment.objects.all()
        return render(request, 'main/single.html', {'comments': comments})
