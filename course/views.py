from django.shortcuts import render, redirect
from django.views import View
from .models import Course, Teacher, Speciality
from django.contrib.auth.models import User


class CourseView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            courses = Course.objects.all()
            context = {
                'courses': courses,
                'search': search
            }
            return render(request, 'main/course.html', context)

        else:
            courses = Course.objects.filter(title__icontains=search)
            if courses:
                context = {
                    'courses': courses,
                    'search': search
                }
                return render(request, 'main/course.html', context)
            else:
                context = {
                    'courses': courses,
                    'search': search
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


class CourseDetailView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'course_detail.html', {'course': course})


class CourseUpdateView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'course_update.html', {'course': course})

    def post(self, request, id):
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_price = request.POST.get('price')
        new_rating = request.POST.get('rating')

        course = Course.objects.get(id=id)
        course.title = new_title
        course.description = new_description
        course.price = new_price
        course.rating = new_rating
        course.save()
        return redirect('courses')


class CourseDeleteView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('courses')


class CourseCreateView(View):
    def get(self, request):
        return render(request, 'add_course.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.POST.get('image')
        rating = request.POST.get('rating')
        course = Course(title=title, description=description, price=price, image=f"course/course/{image}", rating=rating)
        course.save()
        return redirect('courses')


class SpecialityDetailView(View):
    def get(self, request, id):
        speciality = Speciality.objects.get(id=id)
        return render(request, 'speciality_detail.html', {'speciality': speciality})


class SpecialityCreateView(View):
    def get(self, request):
        return render(request, 'create_speciality.html')

    def post(self, request):
        title = request.POST.get('title')
        image = request.POST.get('image')
        speciality = Speciality(title=title, image=f"course/speciality/{image}")
        speciality.save()
        return redirect('landing')


class SpecialityDeleteView(View):
    def get(self, request, id):
        speciality = Speciality.objects.get(id=id)
        speciality.delete()
        return redirect('landing')


class SpecialityUpdateView(View):
    def get(self, request, id):
        speciality = Speciality.objects.get(id=id)
        return render(request, 'update_speciality.html', {'speciality': speciality})

    def post(self, request, id):
        new_title = request.POST.get('title')
        new_image = request.POST.get('image')
        speciality = Speciality.objects.get(id=id)
        speciality.title = new_title
        speciality.image = new_image
        speciality.save()
        return redirect('landing')
