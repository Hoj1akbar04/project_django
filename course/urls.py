from django.urls import path
from .views import CourseView, TeacherView, AboutView, ContactView, CourseDetailView, CourseUpdateView, CourseDeleteView, CourseCreateView, SpecialityCreateView, SpecialityDeleteView, SpecialityUpdateView, SpecialityDetailView

urlpatterns = [
    path('course/', CourseView.as_view(), name='courses'),
    path('teacher/', TeacherView.as_view(), name='teachers'),
    path('about/', AboutView.as_view(), name='about'),
    path('connect/', ContactView.as_view(), name='contact'),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/update/<int:id>/', CourseUpdateView.as_view(), name='course-update'),
    path('course/delete/<int:id>/', CourseDeleteView.as_view(), name='course-delete'),
    path('course/create/<slug:slug>/', CourseCreateView.as_view(), name='create-course'),
    path('speciality/<int:id>/', SpecialityDetailView.as_view(), name='speciality-detail'),
    path('speciality/create/', SpecialityCreateView.as_view(), name='create-speciality'),
    path('speciality/update/<int:id>/',SpecialityUpdateView.as_view(), name='update-speciality'),
    path('speciality/delete/<int:id>',SpecialityDeleteView.as_view(), name='delete-speciality'),
]