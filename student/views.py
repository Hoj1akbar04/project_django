from django.shortcuts import render, redirect
from django.views import View
from .models import Students
from django.contrib.auth.mixins import LoginRequiredMixin


class StudentListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            students = Students.objects.all()
            context = {
                'students': students
            }
            return render(request, 'student.html', context)

        else:
            students = Students.objects.filter(first_name__icontains=search)
            if not students:
                return render(request, 'not_found_user.html')
            else:
                context = {
                    'students': students,
                    'search': search
                }
                return render(request, 'student.html', context)


class UserDetailView(View):
    def get(self, request, id):
        student = Students.objects.get(id=id)
        return render(request, 'student_details.html', {"student": student})

