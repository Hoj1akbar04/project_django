from django.shortcuts import render
from django.views import View

from course.models import Speciality
from .models import Blog, Comment
from course import models


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        specialities = Speciality.objects.all()
        context = {
            'blogs': blogs,
            'specialities': specialities,
        }
        return render(request, 'main/blog.html', context)


class SingleBlogView(View):
    def get(self, request):
        comments = Comment.objects.all()
        specialities = Speciality.objects.all()
        context = {
            'comments': comments,
            'specialities': specialities,
        }
        return render(request, 'main/single.html', context)
