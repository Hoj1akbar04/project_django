from django.shortcuts import render
from django.views import View
from .models import Blog


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs
        }
        return render(request, 'main/blog.html', context)


class BlogDetailView(View):
    def get(self, request, post_id):
        blog = Blog.objects.get(id=post_id)
        return render(request, 'single.html', {'blog': blog})