from django.shortcuts import render, redirect
from django.views import View
from .models import Course, Teacher, Speciality
from django.contrib.auth.models import User


class CourseView(View):
    def get(self, request):
        search = request.GET.get('search')
        specialities = Speciality.objects.all()
        if not search:
            courses = Course.objects.filter(status='pb')
            context = {
                'courses': courses,
                'search': search,
                'specialities': specialities,
                'active': {
                    "home": None,
                    "about": None,
                    "contact": None,
                    "course": "active",
                    "blog": None,
                    "teacher": None,
                }
            }
            return render(request, 'main/course.html', context)

        else:
            courses = Course.objects.filter(title__icontains=search, status='pb')
            if courses:
                context = {
                    'courses': courses,
                    'search': search,
                    'specialities': specialities,
                    'active': {
                        "home": None,
                        "about": None,
                        "contact": None,
                        "course": "active",
                        "blog": None,
                        "teacher": None,
                    }
                }
                return render(request, 'main/course.html', context)
            else:
                context = {
                    'courses': courses,
                    'search': search,
                    'specialities': specialities,
                    'active': {
                        "home": None,
                        "about": None,
                        "contact": None,
                        "course": "active",
                        "blog": None,
                        "teacher": None,
                    }
                }
                return render(request, 'main/course.html', context)


class TeacherView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        specialities = Speciality.objects.all()
        context = {
            'teachers': teachers,
            'specialities': specialities,
            'active': {
                "home": None,
                "about": None,
                "contact": None,
                "course": None,
                "blog": None,
                "teacher": "active",
            }
        }
        return render(request, 'main/teacher.html', context)


class AboutView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        context = {
            'specialities': specialities,
            'active': {
                "home": None,
                "about": "active",
                "contact": None,
                "course": None,
                "blog": None,
                "teacher": None,
            }
        }
        return render(request, 'main/about.html', context)


class ContactView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        context = {
            'specialities': specialities,
            'active': {
                "home": None,
                "about": None,
                "contact": "active",
                "course": None,
                "blog": None,
                "teacher": None,
            }
        }
        return render(request, 'main/contact.html', context)


class CourseDetailView(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        specialities = Speciality.objects.all()
        context = {
            'course': course,
            'specialities': specialities,
        }
        return render(request, 'course_detail.html', context)


class CourseUpdateView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        specialities = Speciality.objects.all()
        context = {
            'course': course,
            'specialities': specialities,
        }
        return render(request, 'course_update.html', context)

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
        specialities = Speciality.objects.all()
        context = {
            'specialities': specialities,
            'speciality': speciality,
        }
        return render(request, 'speciality_detail.html', context)


class SpecialityCreateView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        context = {
            'specialities': specialities,
        }
        return render(request, 'create_speciality.html',context)

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
        specialities = Speciality.objects.all()

        context = {
            'specialities': specialities,
            'speciality': speciality
        }
        return render(request, 'update_speciality.html', context)

    def post(self, request, id):
        new_title = request.POST.get('title')
        new_image = request.POST.get('image')
        speciality = Speciality.objects.get(id=id)
        speciality.title = new_title
        speciality.image = new_image
        speciality.save()
        return redirect('landing')
