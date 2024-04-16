from django.shortcuts import render
from django.views import View
from .models import Course, Teacher, Speciality


class CourseView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        courses = Course.objects.all()
        context = {
            'specialities': specialities,
            'courses': courses
        }
        return render(request, 'main/course.html', context)


class TeacherView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            'teachers': teachers
        }
        return render(request, 'main/teacher.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'main/about.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'main/contact.html')
