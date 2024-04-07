from django.shortcuts import render, redirect
from django.views import View
from .models import Students
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


class StudentListView(View):
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
        return render(request, 'student.html', {"student": student})


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if password_1 != password_2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'auth/register.html')

        try:
            user = User.objects.create_user(username=username, email=email, password=password_1, first_name=first_name, last_name=last_name)
            messages.success(request, "Registration successful. Please log in.")
            user.save()
            user.set_password(password_1)
            return redirect("login")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'auth/register.html')


class UserLoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Logged in successfully")
            return redirect("home")
        else:
            print("Invalid username or password.")
            return render(request, 'not_found_login.html')
