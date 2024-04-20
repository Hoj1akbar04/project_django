from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from blog.models import Blog
from .forms import UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.views.generic import TemplateView
from course.models import Course, Speciality, Teacher


class LandingView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        courses = Course.objects.all()
        teachers = Teacher.objects.all()
        blogs = Blog.objects.all()
        context = {
            'specialities': specialities,
            'courses': courses,
            'teachers': teachers,
            'blogs': blogs,
            'active': {
                "home": "active",
                "about": None,
                "contact": None,
                "course": None,
                "blog": None,
                "teacher": None,
            }
        }
        return render(request, 'main/index.html', context)


class TermsOfServiceView(TemplateView):
    template_name = 'terms_of_service.html'


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

        if password_1 == password_2:
            user_check = User.objects.filter(username=username, password=password_1)
            if user_check:
                return render(request, "auth/register.html")
            else:
                user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password_1)
                user.save()
                return redirect("login")
        else:
            return render(request, "auth/register.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "auth/login.html", context)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("university")

        else:
            form = UserLoginForm()
            context = {
                "form": form
            }
            return render(request, "auth/login.html", context)


class ForgetPasswordView(View):
    def get(self, request):
        return render(request, 'forget_password.html')

    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            reset_password_link = reverse('reset-password', kwargs={'uidb64': str(user.id)})
            # reset_password_link foydalanuvchiga email orqali yuboriladi
            return render(request, 'reset_password.html')
        else:
            return render(request, 'forget_password.html')


class ResetPasswordView(View):
    def get(self, request, uidb64):
        return render(request, 'reset_password.html', {'uidb64': uidb64})

    def post(self, request, uidb64):
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if new_password1 == new_password2:
            user_id = int(uidb64)
            user = User.objects.get(id=user_id)
            user.set_password(new_password1)
            user.save()

            return redirect('login')
        else:
            return redirect('reset_password', uidb64=uidb64)


class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("university")



